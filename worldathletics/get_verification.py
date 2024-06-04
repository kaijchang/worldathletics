# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetVerification(BaseModel):
    get_verification: Optional[List[Optional["GetVerificationGetVerification"]]] = (
        Field(alias="getVerification")
    )


class GetVerificationGetVerification(BaseModel):
    confirmation_code: Optional[str] = Field(alias="confirmationCode")
    username: Optional[str]


GetVerification.update_forward_refs()
GetVerificationGetVerification.update_forward_refs()
