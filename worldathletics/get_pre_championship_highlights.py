# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetPreChampionshipHighlights(BaseModel):
    get_pre_championship_highlights: Optional[
        "GetPreChampionshipHighlightsGetPreChampionshipHighlights"
    ] = Field(alias="getPreChampionshipHighlights")


class GetPreChampionshipHighlightsGetPreChampionshipHighlights(BaseModel):
    events: Optional[
        List[Optional["GetPreChampionshipHighlightsGetPreChampionshipHighlightsEvents"]]
    ]


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEvents(BaseModel):
    discipline: Optional[str]
    ranking_leaders: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeaders"
            ]
        ]
    ] = Field(alias="rankingLeaders")
    reigning_champions: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampions"
            ]
        ]
    ] = Field(alias="reigningChampions")
    sex: Optional[str]
    world_leaders: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeaders"
            ]
        ]
    ] = Field(alias="worldLeaders")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeaders(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampions(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeaders(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    team_members: Optional[
        List[
            Optional[
                "GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembersTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


class GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembersTeamMembers(
    BaseModel
):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


GetPreChampionshipHighlights.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlights.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEvents.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeaders.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembers.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsRankingLeadersTeamMembersTeamMembers.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampions.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembers.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsReigningChampionsTeamMembersTeamMembers.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeaders.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembers.model_rebuild()
GetPreChampionshipHighlightsGetPreChampionshipHighlightsEventsWorldLeadersTeamMembersTeamMembers.model_rebuild()
