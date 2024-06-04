# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLiveCombinedSummaryDetails(BaseModel):
    get_live_combined_summary_details: Optional[
        List[Optional["GetLiveCombinedSummaryDetailsGetLiveCombinedSummaryDetails"]]
    ] = Field(alias="getLiveCombinedSummaryDetails")


class GetLiveCombinedSummaryDetailsGetLiveCombinedSummaryDetails(BaseModel):
    id: Optional[str]
    phase_id: int = Field(alias="phaseId")
    competition_id: Optional[int] = Field(alias="competitionId")
    overall_rank: Optional[int] = Field(alias="overallRank")
    bib: Optional[str]
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_birth_date: Optional[str] = Field(alias="competitorBirthDate")
    result_mark: Optional[str] = Field(alias="resultMark")
    record: Optional[str]
    details_disc_order: Optional[int] = Field(alias="detailsDiscOrder")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_mark: Optional[str] = Field(alias="disciplineMark")
    detail_wind: Optional[str] = Field(alias="detailWind")
    overall_points: Optional[int] = Field(alias="overallPoints")
    overall_order: Optional[int] = Field(alias="overallOrder")
    detail_combined_rank: Optional[str] = Field(alias="detailCombinedRank")
    discipline_rank: Optional[str] = Field(alias="disciplineRank")
    discipline_points: Optional[str] = Field(alias="disciplinePoints")
    update_on: Optional[str] = Field(alias="updateOn")
    combined_type: Optional[str] = Field(alias="combinedType")
    event_store_id: Optional[str] = Field(alias="eventStoreId")


GetLiveCombinedSummaryDetails.update_forward_refs()
GetLiveCombinedSummaryDetailsGetLiveCombinedSummaryDetails.update_forward_refs()
