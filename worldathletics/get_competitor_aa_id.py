# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import Optional

from pydantic import Field

from .base_model import BaseModel


class GetCompetitorAAId(BaseModel):
    get_competitor_aa_id: Optional[int] = Field(alias="getCompetitorAAId")
