"""
Deserialize responses whose models were @object examples or undefined in canvas-lms.

The fixtures in ``fixtures/return_models/`` were captured as a seeded account
admin from a seeded Canvas (``--media-objects`` and ``--rubric-locations``):

- ``media_objects.json``: ``GET /api/v1/courses/:id/media_objects?exclude[]=sources``
  (dev has no Kaltura, so listing media sources fails there)
- ``media_tracks.json``: ``GET /api/v1/media_objects/:id/media_tracks`` with every ``include[]``
- ``registration_history.json``: ``GET /api/v1/accounts/:id/lti_registrations/:id/history``
- ``used_locations.json``: ``GET /api/v1/courses/:id/rubrics/:id/used_locations``

If one of these models loses a field, or the operations go back to untyped
responses, these assertions fail.
"""

import json
import pathlib
from datetime import datetime

import pytest

from canvas_lms_python_client.models import (
    LtiDeployment,
    LtiRegistrationHistoryEntry,
    MediaObject,
    MediaObjectMediaSourcesInner,
    MediaObjectMediaTracksInner,
    MediaTrack,
    RubricUsedLocation,
    RubricUsedLocationAssignmentsInner,
    User,
)

FIXTURES = pathlib.Path(__file__).parent / "fixtures" / "return_models"


def _load(name):
    return json.loads((FIXTURES / f"{name}.json").read_text())


def _parse_datetime(value):
    return None if value is None else datetime.fromisoformat(value)


MEDIA_OBJECTS = _load("media_objects")
MEDIA_TRACKS = _load("media_tracks")
HISTORY = _load("registration_history")
USED_LOCATIONS = _load("used_locations")

# Kaltura flavor from the canvas-lms MediaObject docs; dev can't produce one
MEDIA_SOURCE = {
    "height": "240",
    "width": "336",
    "content_type": "video/mp4",
    "containerFormat": "isom",
    "url": "https://canvas.example.com/media_objects/m-1/redirect?bitrate=382",
    "bitrate": "382",
    "size": "204",
    "isOriginal": "0",
    "fileExt": "mp4",
    "src": "https://canvas.example.com/media_objects/m-1/redirect?bitrate=382",
    "label": "0 kbps",
}


def test_fixtures_have_data():
    assert MEDIA_OBJECTS and MEDIA_OBJECTS[0]["media_tracks"]
    assert MEDIA_TRACKS and HISTORY and USED_LOCATIONS
    assert all(entry["created_by"] == "Instructure" for entry in HISTORY)


@pytest.mark.parametrize("item", MEDIA_OBJECTS, ids=lambda item: item["media_id"])
def test_media_object_keeps_canvas_fields(item):
    media_object = MediaObject.from_dict(item)

    assert media_object.media_id == item["media_id"]
    assert media_object.media_type == item["media_type"]
    assert media_object.title == item["title"]
    assert media_object.can_add_captions is item["can_add_captions"]
    assert media_object.embedded_iframe_url == item["embedded_iframe_url"]
    assert media_object.created_at == _parse_datetime(item["created_at"])
    assert media_object.viewer_restrictions == item["viewer_restrictions"]
    for track, raw in zip(media_object.media_tracks, item["media_tracks"], strict=True):
        assert isinstance(track, MediaObjectMediaTracksInner)
        assert (track.id, track.kind, track.locale, track.url) == (raw["id"], raw["kind"], raw["locale"], raw["url"])
        assert track.asr is raw["asr"]
        assert track.created_at == _parse_datetime(raw["created_at"])


def test_media_object_media_sources_are_typed():
    media_object = MediaObject.from_dict({**MEDIA_OBJECTS[0], "media_sources": [MEDIA_SOURCE]})

    (source,) = media_object.media_sources
    assert isinstance(source, MediaObjectMediaSourcesInner)
    assert source.to_dict() == MEDIA_SOURCE


@pytest.mark.parametrize("item", MEDIA_TRACKS, ids=lambda item: f"track-{item['id']}")
def test_media_track_keeps_canvas_fields(item):
    track = MediaTrack.from_dict(item)

    assert (track.id, track.locale, track.kind) == (item["id"], item["locale"], item["kind"])
    assert track.media_object_id == item["media_object_id"]
    assert track.user_id == item["user_id"]
    assert track.content == item["content"]
    assert track.webvtt_content == item["webvtt_content"]
    assert track.created_at == _parse_datetime(item["created_at"])


@pytest.mark.parametrize("item", HISTORY, ids=lambda item: f"entry-{item['id']}")
def test_registration_history_entry_keeps_canvas_fields(item):
    entry = LtiRegistrationHistoryEntry.from_dict(item)

    assert entry.id == item["id"]
    assert entry.lti_registration_id == item["lti_registration_id"]
    assert entry.update_type == item["update_type"]
    assert entry.diff == item["diff"]
    assert entry.created_by.actual_instance == "Instructure"
    for deployment, raw in zip(entry.new_controls_by_deployment, item["new_controls_by_deployment"], strict=True):
        assert isinstance(deployment, LtiDeployment)
        assert deployment.id == raw["id"]


def test_registration_history_entry_created_by_a_user():
    # Live data only has "Instructure"; a non-site-admin editor is a user object
    user = {"id": 392, "name": "Seeded Admin 2", "sortable_name": "2, Seeded Admin", "short_name": "Seeded Admin 2"}
    entry = LtiRegistrationHistoryEntry.from_dict({**HISTORY[0], "created_by": user})

    assert isinstance(entry.created_by.actual_instance, User)
    assert entry.created_by.actual_instance.id == 392


@pytest.mark.parametrize("item", USED_LOCATIONS, ids=lambda item: f"course-{item['id']}")
def test_rubric_used_location_keeps_canvas_fields(item):
    location = RubricUsedLocation.from_dict(item)

    assert (location.id, location.name) == (item["id"], item["name"])
    assert location.concluded is item["concluded?"]
    assert location.to_dict()["concluded?"] is item["concluded?"]
    for assignment, raw in zip(location.assignments, item["assignments"], strict=True):
        assert isinstance(assignment, RubricUsedLocationAssignmentsInner)
        assert (assignment.id, assignment.title) == (raw["id"], raw["title"])
