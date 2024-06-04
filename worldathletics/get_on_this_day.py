# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetOnThisDay(BaseModel):
    get_on_this_day: Optional["GetOnThisDayGetOnThisDay"] = Field(alias="getOnThisDay")


class GetOnThisDayGetOnThisDay(BaseModel):
    module_title: Optional[str] = Field(alias="moduleTitle")
    module_subtitle: Optional[str] = Field(alias="moduleSubtitle")
    results: Optional[List[Optional["GetOnThisDayGetOnThisDayResults"]]]


class GetOnThisDayGetOnThisDayResults(BaseModel):
    id: Optional[int]
    category: Optional[str]
    title: Optional[str]
    body: Optional[str]
    competitor_id: Optional[int] = Field(alias="competitorId")


GetOnThisDay.update_forward_refs()
GetOnThisDayGetOnThisDay.update_forward_refs()
GetOnThisDayGetOnThisDayResults.update_forward_refs()
