# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAthleteRepresentativeTopList(BaseModel):
    get_athlete_representative_top_list: Optional[
        "GetAthleteRepresentativeTopListGetAthleteRepresentativeTopList"
    ] = Field(alias="getAthleteRepresentativeTopList")


class GetAthleteRepresentativeTopListGetAthleteRepresentativeTopList(BaseModel):
    genders: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListGenders"
            ]
        ]
    ]
    events: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListEvents"
            ]
        ]
    ]
    toplist: Optional[
        "GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListToplist"
    ]
    event_types: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListEventTypes"
            ]
        ]
    ] = Field(alias="eventTypes")


class GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListGenders(BaseModel):
    gender: Optional[str]
    gender_code: Optional[str] = Field(alias="genderCode")
    selected_gender: Optional[bool] = Field(alias="selectedGender")


class GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListEvents(BaseModel):
    event: Optional[str]
    event_id: Optional[int] = Field(alias="eventId")
    gender_code: Optional[str] = Field(alias="genderCode")
    event_type_id: Optional[int] = Field(alias="eventTypeId")
    selected_event: Optional[bool] = Field(alias="selectedEvent")


class GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListToplist(BaseModel):
    event: Optional[str]
    toplist_date: Optional[str] = Field(alias="toplistDate")
    athletes: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListToplistAthletes"
            ]
        ]
    ]


class GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListToplistAthletes(
    BaseModel
):
    rank: Optional[int]
    result: Optional[str]
    country: Optional[str]
    last_name: Optional[str] = Field(alias="lastName")
    athlete_id: Optional[int] = Field(alias="athleteId")
    birthdate: Optional[str]
    first_name: Optional[str] = Field(alias="firstName")
    result_date: Optional[str] = Field(alias="resultDate")
    athlete_name: Optional[str] = Field(alias="athleteName")
    country_code: Optional[str] = Field(alias="countryCode")
    result_venue: Optional[str] = Field(alias="resultVenue")
    representative_name: Optional[str] = Field(alias="representativeName")
    representative_type_id: Optional[int] = Field(alias="representativeTypeId")
    representative_last_name: Optional[str] = Field(alias="representativeLastName")
    athlete_representative_id: Optional[int] = Field(alias="athleteRepresentativeId")
    representative_first_name: Optional[str] = Field(alias="representativeFirstName")


class GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListEventTypes(
    BaseModel
):
    event_type: Optional[str] = Field(alias="eventType")
    event_type_id: Optional[int] = Field(alias="eventTypeId")
    selected_event_type: Optional[bool] = Field(alias="selectedEventType")


GetAthleteRepresentativeTopList.update_forward_refs()
GetAthleteRepresentativeTopListGetAthleteRepresentativeTopList.update_forward_refs()
GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListGenders.update_forward_refs()
GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListEvents.update_forward_refs()
GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListToplist.update_forward_refs()
GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListToplistAthletes.update_forward_refs()
GetAthleteRepresentativeTopListGetAthleteRepresentativeTopListEventTypes.update_forward_refs()