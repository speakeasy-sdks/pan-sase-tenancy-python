"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from . import utils
from sase_tenancy.models import operations, shared
from typing import Optional

class TenancyGroup:
    _client: requests_http.Session
    _security_client: requests_http.Session
    _server_url: str
    _language: str
    _sdk_version: str
    _gen_version: str

    def __init__(self, client: requests_http.Session, security_client: requests_http.Session, server_url: str, language: str, sdk_version: str, gen_version: str) -> None:
        self._client = client
        self._security_client = security_client
        self._server_url = server_url
        self._language = language
        self._sdk_version = sdk_version
        self._gen_version = gen_version
        
    
    def create(self, request: shared.TenantServiceGroupCreate, security: operations.PostTenancyV1TenantServiceGroupsSecurity) -> operations.PostTenancyV1TenantServiceGroupsResponse:
        r"""Create a tenant service group
        Create a tenant service group.
        The service account used to authenticate this request
        is granted `msp_superuser` access to the new tenant
        service group.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/tenancy/v1/tenant_service_groups'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostTenancyV1TenantServiceGroupsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TenantServiceGroup])
                res.tenant_service_group = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            pass

        return res

    
    def delete(self, request: operations.DeleteTenancyV1TenantServiceGroupsTsgIDRequest, security: operations.DeleteTenancyV1TenantServiceGroupsTsgIDSecurity) -> operations.DeleteTenancyV1TenantServiceGroupsTsgIDResponse:
        r"""Delete a tenant service group
        Delete a tenant service group. If the TSG ID supplied
        in this API's path does not match the TSG ID contained in
        the access token used to authenticate this request, this
        request will fail.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.DeleteTenancyV1TenantServiceGroupsTsgIDRequest, base_url, '/tenancy/v1/tenant_service_groups/{tsg_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteTenancyV1TenantServiceGroupsTsgIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TenantServiceGroup])
                res.tenant_service_group = out
        elif http_res.status_code in [401, 403, 404, 500]:
            pass

        return res

    
    def get(self, request: operations.GetTenancyV1TenantServiceGroupsTsgIDRequest, security: operations.GetTenancyV1TenantServiceGroupsTsgIDSecurity) -> operations.GetTenancyV1TenantServiceGroupsTsgIDResponse:
        r"""Get a tenant service group
        Get a tenant service group by TSG ID.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.GetTenancyV1TenantServiceGroupsTsgIDRequest, base_url, '/tenancy/v1/tenant_service_groups/{tsg_id}', request)
        headers = {}
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTenancyV1TenantServiceGroupsTsgIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TenantServiceGroup])
                res.tenant_service_group = out
        elif http_res.status_code in [401, 403, 404, 500]:
            pass

        return res

    
    def list(self, request: operations.GetTenancyV1TenantServiceGroupsRequest, security: operations.GetTenancyV1TenantServiceGroupsSecurity) -> operations.GetTenancyV1TenantServiceGroupsResponse:
        r"""List all tenant service groups
        Get a list of all the tenant service groups
        that are available to the service account used to
        authenticate this request.
        """
        base_url = self._server_url
        
        url = base_url.removesuffix('/') + '/tenancy/v1/tenant_service_groups'
        headers = {}
        query_params = utils.get_query_params(operations.GetTenancyV1TenantServiceGroupsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetTenancyV1TenantServiceGroupsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetTenancyV1TenantServiceGroups200ApplicationJSON])
                res.get_tenancy_v1_tenant_service_groups_200_application_json_object = out
        elif http_res.status_code in [401, 403, 404, 500]:
            pass

        return res

    
    def list_ancestors(self, request: operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsRequest, security: operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSecurity) -> operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsResponse:
        r"""List tenant service group ancestors
        List the ancestor tenants of the tenant service group
        specified in this request. If the TSG ID supplied
        in this API's path does not match the TSG ID contained in
        the access token used to authenticate this request, this
        request will fail.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsRequest, base_url, '/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_ancestors', request)
        headers = {}
        query_params = utils.get_query_params(operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestors200ApplicationJSON])
                res.post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_ancestors_200_application_json_object = out
        elif http_res.status_code in [401, 403, 404, 500]:
            pass

        return res

    
    def list_children(self, request: operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenRequest, security: operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenSecurity) -> operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenResponse:
        r"""List tenant service group children
        List the child tenants of the tenant service group
        specified in this request. If the TSG ID supplied
        in this API's path does not match the TSG ID contained in
        the access token used to authenticate this request, this
        request will fail.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenRequest, base_url, '/tenancy/v1/tenant_service_groups/{tsg_id}/operations/list_children', request)
        headers = {}
        query_params = utils.get_query_params(operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('POST', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildren200ApplicationJSON])
                res.post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_children_200_application_json_object = out
        elif http_res.status_code in [401, 403, 404, 500]:
            pass

        return res

    
    def update(self, request: operations.PutTenancyV1TenantServiceGroupsTsgIDRequest, security: operations.PutTenancyV1TenantServiceGroupsTsgIDSecurity) -> operations.PutTenancyV1TenantServiceGroupsTsgIDResponse:
        r"""Update a tenant service group
        Update a tenant service group. If the TSG ID supplied 
        in this API's path does not match the TSG ID contained in
        the access token used to authenticate this request, this 
        request will fail.
        """
        base_url = self._server_url
        
        url = utils.generate_url(operations.PutTenancyV1TenantServiceGroupsTsgIDRequest, base_url, '/tenancy/v1/tenant_service_groups/{tsg_id}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "tenant_service_group_update", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self._language} {self._sdk_version} {self._gen_version}'
        
        client = utils.configure_security_client(self._client, security)
        
        http_res = client.request('PUT', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.PutTenancyV1TenantServiceGroupsTsgIDResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.TenantServiceGroup])
                res.tenant_service_group = out
        elif http_res.status_code in [401, 403, 404, 500]:
            pass

        return res

    