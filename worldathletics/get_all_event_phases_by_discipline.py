# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAllEventPhasesByDiscipline(BaseModel):
    get_all_event_phases_by_discipline: Optional[
        List[Optional["GetAllEventPhasesByDisciplineGetAllEventPhasesByDiscipline"]]
    ] = Field(alias="getAllEventPhasesByDiscipline")


class GetAllEventPhasesByDisciplineGetAllEventPhasesByDiscipline(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    phase_code: Optional[str] = Field(alias="phaseCode")
    phase_name: Optional[str] = Field(alias="phaseName")
    event_i_d: Optional[int] = Field(alias="eventID")
    phase_date_and_time: Optional[Any] = Field(alias="phaseDateAndTime")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    discipline: Optional[
        "GetAllEventPhasesByDisciplineGetAllEventPhasesByDisciplineDiscipline"
    ]
    is_startlist_published: Optional[bool] = Field(alias="isStartlistPublished")
    is_result_published: Optional[bool] = Field(alias="isResultPublished")
    is_phase_summary_published: Optional[bool] = Field(alias="isPhaseSummaryPublished")
    is_team_standing_published: Optional[bool] = Field(alias="isTeamStandingPublished")
    combined_discipline_order: Optional[int] = Field(alias="combinedDisciplineOrder")
    phase_order: Optional[int] = Field(alias="phaseOrder")
    phase_session_name: Optional[str] = Field(alias="phaseSessionName")
    phase_session_order: Optional[int] = Field(alias="phaseSessionOrder")
    status: Optional[int]
    has_time: Optional[bool] = Field(alias="hasTime")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    primary_phase_order: Optional[int] = Field(alias="primaryPhaseOrder")
    is_points_published: Optional[bool] = Field(alias="isPointsPublished")
    phase_name_url_slug: Optional[str] = Field(alias="phaseNameUrlSlug")
    sex_name_url_slug: Optional[str] = Field(alias="sexNameUrlSlug")
    unit_name: Optional[str] = Field(alias="unitName")
    unit_type_name: Optional[str] = Field(alias="unitTypeName")


class GetAllEventPhasesByDisciplineGetAllEventPhasesByDisciplineDiscipline(BaseModel):
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    id: Optional[str] = Field(alias="_id")
    name: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    type_name: Optional[str] = Field(alias="typeName")
    type_order: Optional[int] = Field(alias="typeOrder")
    order: Optional[int]
    is_track: Optional[bool] = Field(alias="isTrack")
    is_field: Optional[bool] = Field(alias="isField")
    is_road: Optional[bool] = Field(alias="isRoad")
    is_combined: Optional[bool] = Field(alias="isCombined")
    is_walk: Optional[bool] = Field(alias="isWalk")
    is_indoor: Optional[bool] = Field(alias="isIndoor")
    is_reaction: Optional[bool] = Field(alias="isReaction")
    is_outdoor: Optional[bool] = Field(alias="isOutdoor")
    is_wind: Optional[bool] = Field(alias="isWind")
    is_relay: Optional[bool] = Field(alias="isRelay")
    is_valid_i_a_a_f: Optional[bool] = Field(alias="isValidIAAF")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")


GetAllEventPhasesByDiscipline.update_forward_refs()
GetAllEventPhasesByDisciplineGetAllEventPhasesByDiscipline.update_forward_refs()
GetAllEventPhasesByDisciplineGetAllEventPhasesByDisciplineDiscipline.update_forward_refs()