# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCISCompetitorResDate(BaseModel):
    get_cis_competitor_res_date: Optional[
        "GetCISCompetitorResDateGetCisCompetitorResDate"
    ] = Field(alias="getCISCompetitorResDate")


class GetCISCompetitorResDateGetCisCompetitorResDate(BaseModel):
    parameters: Optional["GetCISCompetitorResDateGetCisCompetitorResDateParameters"]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    with_remark: Optional[bool] = Field(alias="withRemark")
    results_by_date: Optional[
        List[Optional["GetCISCompetitorResDateGetCisCompetitorResDateResultsByDate"]]
    ] = Field(alias="resultsByDate")


class GetCISCompetitorResDateGetCisCompetitorResDateParameters(BaseModel):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetCISCompetitorResDateGetCisCompetitorResDateResultsByDate(BaseModel):
    date: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    country: Optional[str]
    category: Optional[str]
    race: Optional[str]
    place: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    result_score: Optional[int] = Field(alias="resultScore")
    remark: Optional[str]


GetCISCompetitorResDate.model_rebuild()
GetCISCompetitorResDateGetCisCompetitorResDate.model_rebuild()