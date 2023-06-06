# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRecordsByCategory(BaseModel):
    get_records_by_category: Optional[
        List[Optional["GetRecordsByCategoryGetRecordsByCategory"]]
    ] = Field(alias="getRecordsByCategory")


class GetRecordsByCategoryGetRecordsByCategory(BaseModel):
    progression_list_id: Optional[int] = Field(alias="progressionListId")
    category: Optional[str]
    performance: Optional[str]
    equal: Optional[bool]
    pending: Optional[bool]
    set_indoor: Optional[bool] = Field(alias="setIndoor")
    women_only: Optional[bool] = Field(alias="womenOnly")
    mixed: Optional[bool]
    yard: Optional[bool]
    wind: Optional[str]
    competitor: Optional["GetRecordsByCategoryGetRecordsByCategoryCompetitor"]
    country: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    legend: Optional[str]
    discipline: Optional[str]
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")


class GetRecordsByCategoryGetRecordsByCategoryCompetitor(BaseModel):
    name: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")


GetRecordsByCategory.update_forward_refs()
GetRecordsByCategoryGetRecordsByCategory.update_forward_refs()
GetRecordsByCategoryGetRecordsByCategoryCompetitor.update_forward_refs()