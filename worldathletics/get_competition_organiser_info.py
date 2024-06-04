# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCompetitionOrganiserInfo(BaseModel):
    get_competition_organiser_info: Optional[
        "GetCompetitionOrganiserInfoGetCompetitionOrganiserInfo"
    ] = Field(alias="getCompetitionOrganiserInfo")


class GetCompetitionOrganiserInfoGetCompetitionOrganiserInfo(BaseModel):
    units: Optional[
        List[Optional["GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoUnits"]]
    ]
    prize_money: Optional[
        List[
            Optional["GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoPrizeMoney"]
        ]
    ] = Field(alias="prizeMoney")
    website_url: Optional[str] = Field(alias="websiteUrl")
    results_page_url: Optional[str] = Field(alias="resultsPageUrl")
    live_streaming_url: Optional[str] = Field(alias="liveStreamingUrl")
    additional_info: Optional[str] = Field(alias="additionalInfo")
    contact_persons: Optional[
        List[
            Optional[
                "GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoContactPersons"
            ]
        ]
    ] = Field(alias="contactPersons")


class GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoUnits(BaseModel):
    events: Optional[List[Optional[str]]]
    gender: Optional[str]


class GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoPrizeMoney(BaseModel):
    gender: Optional[str]
    prizes: Optional[List[Optional[str]]]


class GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoContactPersons(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str] = Field(alias="phoneNumber")
    title: Optional[str]


GetCompetitionOrganiserInfo.update_forward_refs()
GetCompetitionOrganiserInfoGetCompetitionOrganiserInfo.update_forward_refs()
GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoUnits.update_forward_refs()
GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoPrizeMoney.update_forward_refs()
GetCompetitionOrganiserInfoGetCompetitionOrganiserInfoContactPersons.update_forward_refs()
