# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetMedals(BaseModel):
    get_medals: Optional[List[Optional["GetMedalsGetMedals"]]] = Field(
        alias="getMedals"
    )


class GetMedalsGetMedals(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    event_id: Optional[int] = Field(alias="eventId")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    country_code: Optional[str] = Field(alias="countryCode")
    medal_rank: Optional[str] = Field(alias="medalRank")
    silver: Optional[int]
    gold: Optional[int]
    bronze: Optional[int]
    total: Optional[int]
    event_medal_table_order: Optional[int] = Field(alias="eventMedalTableOrder")
    country: Optional["GetMedalsGetMedalsCountry"]
    event_sub_category_code: Optional[str] = Field(alias="eventSubCategoryCode")


class GetMedalsGetMedalsCountry(BaseModel):
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    id: Optional[str] = Field(alias="_id")
    country_name: Optional[str] = Field(alias="countryName")
    country_order: Optional[int] = Field(alias="countryOrder")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    area_order: Optional[int] = Field(alias="areaOrder")
    is_valid: Optional[bool] = Field(alias="isValid")
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    country_name_url_slug: Optional[str] = Field(alias="countryNameUrlSlug")


GetMedals.update_forward_refs()
GetMedalsGetMedals.update_forward_refs()
GetMedalsGetMedalsCountry.update_forward_refs()
