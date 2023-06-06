# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetPlacingTableDetails(BaseModel):
    get_placing_table_details: Optional[
        List[Optional["GetPlacingTableDetailsGetPlacingTableDetails"]]
    ] = Field(alias="getPlacingTableDetails")


class GetPlacingTableDetailsGetPlacingTableDetails(BaseModel):
    id: int
    placing_table_id: int = Field(alias="placingTableId")
    competitor_id: Optional[int] = Field(alias="competitorId")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    sex_code: Optional[str] = Field(alias="sexCode")
    placing_date: Optional[Any] = Field(alias="placingDate")
    details_order: Optional[int] = Field(alias="detailsOrder")
    event_id: Optional[int] = Field(alias="eventId")
    type_id: Optional[int] = Field(alias="typeId")
    type_name: Optional[str] = Field(alias="typeName")
    type_abbreviation: Optional[str] = Field(alias="typeAbbreviation")
    result_mark: Optional[str] = Field(alias="resultMark")
    placing_points: Optional[str] = Field(alias="placingPoints")
    result_id: Optional[int] = Field(alias="resultId")
    phase_id: Optional[int] = Field(alias="phaseId")
    country_code: Optional[str] = Field(alias="countryCode")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    event_store_id: Optional[str] = Field(alias="eventStoreId")


GetPlacingTableDetails.update_forward_refs()
GetPlacingTableDetailsGetPlacingTableDetails.update_forward_refs()