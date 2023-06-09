"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import tenant_service_group as shared_tenant_service_group
from dataclasses_json import Undefined, dataclass_json
from sase_tenancy import utils
from typing import Optional


@dataclasses.dataclass
class GetTenancyV1TenantServiceGroupsSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class GetTenancyV1TenantServiceGroupsRequest:
    
    hierarchy: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'hierarchy', 'style': 'form', 'explode': True }})
    r"""Indicates whether the response structure lists groups in
    their hierarchy, or as an array of TSGs without regard to
    hierarchy. Default is false (don't show hierarchy).
    
    If false, the order of the TSGs in the result array is not
    guaranteed.
    """
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetTenancyV1TenantServiceGroups200ApplicationJSON:
    r"""Successful response."""
    
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""Total count of the items"""
    items: list[shared_tenant_service_group.TenantServiceGroup] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    

@dataclasses.dataclass
class GetTenancyV1TenantServiceGroupsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_tenancy_v1_tenant_service_groups_200_application_json_object: Optional[GetTenancyV1TenantServiceGroups200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    