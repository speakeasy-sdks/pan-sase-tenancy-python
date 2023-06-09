"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import tenant_service_group as shared_tenant_service_group
from ..shared import tenant_service_group_update as shared_tenant_service_group_update
from typing import Optional


@dataclasses.dataclass
class PutTenancyV1TenantServiceGroupsTsgIDSecurity:
    
    bearer: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class PutTenancyV1TenantServiceGroupsTsgIDRequest:
    
    tenant_service_group_update: shared_tenant_service_group_update.TenantServiceGroupUpdate = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    tsg_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'tsg_id', 'style': 'simple', 'explode': False }})
    r"""A unique identifier for the tenant service group."""
    

@dataclasses.dataclass
class PutTenancyV1TenantServiceGroupsTsgIDResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    tenant_service_group: Optional[shared_tenant_service_group.TenantServiceGroup] = dataclasses.field(default=None)
    r"""Successful response."""
    