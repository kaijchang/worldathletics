# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRecentResults(BaseModel):
    get_recent_results: Optional["GetRecentResultsGetRecentResults"] = Field(
        alias="getRecentResults"
    )


class GetRecentResultsGetRecentResults(BaseModel):
    module_title: Optional[str] = Field(alias="moduleTitle")
    module_subtitle: Optional[str] = Field(alias="moduleSubtitle")
    results: Optional[List[Optional["GetRecentResultsGetRecentResultsResults"]]]


class GetRecentResultsGetRecentResultsResults(BaseModel):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    name: Optional[str]
    venue: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    event: Optional["GetRecentResultsGetRecentResultsResultsEvent"]


class GetRecentResultsGetRecentResultsResultsEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    circuits: Optional[
        List[Optional["GetRecentResultsGetRecentResultsResultsEventCircuits"]]
    ]
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    page: Optional["GetRecentResultsGetRecentResultsResultsEventPage"]
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetRecentResultsGetRecentResultsResultsEventCircuits(BaseModel):
    updated_on: Optional[Any] = Field(alias="UpdatedOn")
    hash: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    circuit_name: Optional[str] = Field(alias="circuitName")
    season: Optional[int]
    circuit_order: Optional[int] = Field(alias="circuitOrder")
    circuit_type_name: Optional[str] = Field(alias="circuitTypeName")


class GetRecentResultsGetRecentResultsResultsEventPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    site_id: Optional[str] = Field(alias="siteId")
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")


GetRecentResults.update_forward_refs()
GetRecentResultsGetRecentResults.update_forward_refs()
GetRecentResultsGetRecentResultsResults.update_forward_refs()
GetRecentResultsGetRecentResultsResultsEvent.update_forward_refs()
GetRecentResultsGetRecentResultsResultsEventCircuits.update_forward_refs()
GetRecentResultsGetRecentResultsResultsEventPage.update_forward_refs()
