# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class PreviousMedalists(BaseModel):
    previous_medalists: Optional[
        List[Optional["PreviousMedalistsPreviousMedalists"]]
    ] = Field(alias="previousMedalists")


class PreviousMedalistsPreviousMedalists(BaseModel):
    id: Optional[int]
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    medal_table_id: Optional[int] = Field(alias="medalTableId")
    type_id: Optional[int] = Field(alias="typeId")
    result_mark: Optional[str] = Field(alias="resultMark")
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    name: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")


PreviousMedalists.update_forward_refs()
PreviousMedalistsPreviousMedalists.update_forward_refs()
