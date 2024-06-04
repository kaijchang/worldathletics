# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRankingScoreCalculation(BaseModel):
    get_ranking_score_calculation: Optional[
        "GetRankingScoreCalculationGetRankingScoreCalculation"
    ] = Field(alias="getRankingScoreCalculation")


class GetRankingScoreCalculationGetRankingScoreCalculation(BaseModel):
    rank_date: Optional[str] = Field(alias="rankDate")
    event_group: Optional[str] = Field(alias="eventGroup")
    male: Optional[bool]
    athlete: Optional[str]
    athlete_url_slug: Optional[str] = Field(alias="athleteUrlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    country_full_name: Optional[str] = Field(alias="countryFullName")
    place: Optional[int]
    with_wind: Optional[bool] = Field(alias="withWind")
    with_drop: Optional[bool] = Field(alias="withDrop")
    with_world_record: Optional[bool] = Field(alias="withWorldRecord")
    with_month_correction: Optional[bool] = Field(alias="withMonthCorrection")
    average_performance_score: Optional[int] = Field(alias="averagePerformanceScore")
    ranking_score: Optional[int] = Field(alias="rankingScore")
    results: Optional[
        List[Optional["GetRankingScoreCalculationGetRankingScoreCalculationResults"]]
    ]


class GetRankingScoreCalculationGetRankingScoreCalculationResults(BaseModel):
    date: Optional[str]
    competition: Optional[str]
    country: Optional[str]
    category: Optional[str]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    indoor: Optional[bool]
    discipline: Optional[str]
    race: Optional[str]
    place: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    drop: Optional[str]
    result_score: Optional[int] = Field(alias="resultScore")
    world_record: Optional[int] = Field(alias="worldRecord")
    placing_score: Optional[int] = Field(alias="placingScore")
    performance_score: Optional[int] = Field(alias="performanceScore")
    month_correction_applied: Optional[bool] = Field(alias="monthCorrectionApplied")


GetRankingScoreCalculation.update_forward_refs()
GetRankingScoreCalculationGetRankingScoreCalculation.update_forward_refs()
GetRankingScoreCalculationGetRankingScoreCalculationResults.update_forward_refs()
