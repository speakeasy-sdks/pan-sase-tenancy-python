"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import tenant_service_group as shared_tenant_service_group
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sase_tenancy import utils
from typing import Optional


@dataclasses.dataclass
class PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    
class PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSort(str, Enum):
    r"""Identifies the response structure's sort order:
    
    * `asc` : From root to leaf.
    * `desc` : From leaf to root.
    """
    ASC = 'asc'
    DESC = 'desc'


@dataclasses.dataclass
class PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsRequest:
    
    tsg_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tsg_id', 'style': 'simple', 'explode': False }})
    r"""A unique identifier for the tenant service group."""
    fields_: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'fields', 'style': 'form', 'explode': True }})
    r"""Provide a comma-separated list of fields you want returned."""
    include_self: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'include_self', 'style': 'form', 'explode': True }})
    r"""Indicates if the TSG used to generate this hierarchy is
    included in the resulting TSG list. `true` to include
    self. Default is `false`.
    """
    sort: Optional[PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSort] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sort', 'style': 'form', 'explode': True }})
    r"""Identifies the response structure's sort order:
    
    * `asc` : From root to leaf.
    * `desc` : From leaf to root.
    """
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestors200ApplicationJSON:
    r"""Successful response."""
    
    count: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('count') }})
    r"""Total count of the items"""
    items: list[shared_tenant_service_group.TenantServiceGroup] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items') }})
    

@dataclasses.dataclass
class PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_ancestors_200_application_json_object: Optional[PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestors200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successful response."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    