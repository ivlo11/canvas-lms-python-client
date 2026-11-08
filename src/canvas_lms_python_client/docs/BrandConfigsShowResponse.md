# BrandConfigsShowResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ic_brand_discovery_custom_message** | **str** |  | [optional] 
**ic_brand_login_content_bgd_color** | **str** |  | [optional] 
**ic_brand_login_content_border_color** | **str** |  | [optional] 
**ic_brand_login_content_inner_bgd** | **str** |  | [optional] 
**ic_brand_login_content_inner_body_bgd** | **str** |  | [optional] 
**ic_brand_login_content_inner_body_border** | **str** |  | [optional] 
**ic_brand_login_content_inner_border** | **str** |  | [optional] 
**ic_brand_login_content_label_text_color** | **str** |  | [optional] 
**ic_brand_login_content_password_text_color** | **str** |  | [optional] 
**ic_brand_login_body_bgd_color** | **str** |  | [optional] 
**ic_brand_login_body_bgd_image** | **str** |  | [optional] 
**ic_brand_login_body_bgd_shadow_color** | **str** |  | [optional] 
**ic_brand_login_custom_message** | **str** |  | [optional] 
**ic_brand_login_footer_link_color** | **str** |  | [optional] 
**ic_brand_login_footer_link_color_hover** | **str** |  | [optional] 
**ic_brand_login_instructure_logo** | **str** |  | [optional] 
**ic_brand_login_logo** | **str** |  | [optional] 
**ic_brand_registration_custom_message** | **str** |  | [optional] 
**ic_brand_registration_parent_custom_message** | **str** |  | [optional] 
**ic_brand_apple_touch_icon** | **str** |  | [optional] 
**ic_brand_button__primary_bgd** | **str** |  | [optional] 
**ic_brand_button__primary_bgd_darkened_15** | **str** |  | [optional] 
**ic_brand_button__primary_bgd_darkened_5** | **str** |  | [optional] 
**ic_brand_button__primary_text** | **str** |  | [optional] 
**ic_brand_button__secondary_bgd** | **str** |  | [optional] 
**ic_brand_button__secondary_bgd_darkened_15** | **str** |  | [optional] 
**ic_brand_button__secondary_bgd_darkened_5** | **str** |  | [optional] 
**ic_brand_button__secondary_text** | **str** |  | [optional] 
**ic_brand_favicon** | **str** |  | [optional] 
**ic_brand_font_color_dark** | **str** |  | [optional] 
**ic_brand_font_color_dark_lightened_15** | **str** |  | [optional] 
**ic_brand_font_color_dark_lightened_28** | **str** |  | [optional] 
**ic_brand_global_nav_avatar_border** | **str** |  | [optional] 
**ic_brand_global_nav_bgd** | **str** |  | [optional] 
**ic_brand_global_nav_ic_icon_svg_fill** | **str** |  | [optional] 
**ic_brand_global_nav_ic_icon_svg_fill__active** | **str** |  | [optional] 
**ic_brand_global_nav_logo_bgd** | **str** |  | [optional] 
**ic_brand_global_nav_menu_item__badge_bgd** | **str** |  | [optional] 
**ic_brand_global_nav_menu_item__badge_bgd__active** | **str** |  | [optional] 
**ic_brand_global_nav_menu_item__badge_text** | **str** |  | [optional] 
**ic_brand_global_nav_menu_item__badge_text__active** | **str** |  | [optional] 
**ic_brand_global_nav_menu_item__text_color** | **str** |  | [optional] 
**ic_brand_global_nav_menu_item__text_color__active** | **str** |  | [optional] 
**ic_brand_header_image** | **str** |  | [optional] 
**ic_brand_mobile_global_nav_logo** | **str** |  | [optional] 
**ic_brand_msapplication_tile_color** | **str** |  | [optional] 
**ic_brand_msapplication_tile_square** | **str** |  | [optional] 
**ic_brand_msapplication_tile_wide** | **str** |  | [optional] 
**ic_brand_primary** | **str** |  | [optional] 
**ic_brand_primary_darkened_10** | **str** |  | [optional] 
**ic_brand_primary_darkened_15** | **str** |  | [optional] 
**ic_brand_primary_darkened_5** | **str** |  | [optional] 
**ic_brand_primary_lightened_10** | **str** |  | [optional] 
**ic_brand_primary_lightened_15** | **str** |  | [optional] 
**ic_brand_primary_lightened_5** | **str** |  | [optional] 
**ic_brand_right_sidebar_logo** | **str** |  | [optional] 
**ic_brand_watermark** | **str** |  | [optional] 
**ic_brand_watermark_opacity** | **str** |  | [optional] 
**ic_link_color** | **str** |  | [optional] 
**ic_link_color_darkened_10** | **str** |  | [optional] 
**ic_link_color_lightened_10** | **str** |  | [optional] 

## Example

```python
from canvas_lms_python_client.models.brand_configs_show_response import BrandConfigsShowResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrandConfigsShowResponse from a JSON string
brand_configs_show_response_instance = BrandConfigsShowResponse.from_json(json)
# print the JSON string representation of the object
print(BrandConfigsShowResponse.to_json())

# convert the object into a dict
brand_configs_show_response_dict = brand_configs_show_response_instance.to_dict()
# create an instance of BrandConfigsShowResponse from a dict
brand_configs_show_response_from_dict = BrandConfigsShowResponse.from_dict(brand_configs_show_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


