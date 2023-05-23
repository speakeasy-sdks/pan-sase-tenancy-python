# tenancy_group

### Available Operations

* [create](#create) - Create a tenant service group
* [delete](#delete) - Delete a tenant service group
* [get](#get) - Get a tenant service group
* [list](#list) - List all tenant service groups
* [list_ancestors](#list_ancestors) - List tenant service group ancestors
* [list_children](#list_children) - List tenant service group children
* [update](#update) - Update a tenant service group

## create

Create a tenant service group.
The service account used to authenticate this request
is granted `msp_superuser` access to the new tenant
service group.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations, shared

s = sase_tenancy.SaseTenancy()

req = shared.TenantServiceGroupCreate(
    display_name='Example TSG',
    parent_id='1378242802',
    support_contact='user@example.com',
    vertical=shared.TenantServiceGroupCreateVertical.HIGH_TECH,
)

res = s.tenancy_group.create(req, operations.PostTenancyV1TenantServiceGroupsSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.tenant_service_group is not None:
    # handle response
```

## delete

Delete a tenant service group. If the TSG ID supplied
in this API's path does not match the TSG ID contained in
the access token used to authenticate this request, this
request will fail.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy()

req = operations.DeleteTenancyV1TenantServiceGroupsTsgIDRequest(
    tsg_id='1378242802',
)

res = s.tenancy_group.delete(req, operations.DeleteTenancyV1TenantServiceGroupsTsgIDSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.tenant_service_group is not None:
    # handle response
```

## get

Get a tenant service group by TSG ID.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy()

req = operations.GetTenancyV1TenantServiceGroupsTsgIDRequest(
    tsg_id='1378242802',
)

res = s.tenancy_group.get(req, operations.GetTenancyV1TenantServiceGroupsTsgIDSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.tenant_service_group is not None:
    # handle response
```

## list

Get a list of all the tenant service groups
that are available to the service account used to
authenticate this request.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy()

req = operations.GetTenancyV1TenantServiceGroupsRequest(
    hierarchy=False,
)

res = s.tenancy_group.list(req, operations.GetTenancyV1TenantServiceGroupsSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.get_tenancy_v1_tenant_service_groups_200_application_json_object is not None:
    # handle response
```

## list_ancestors

List the ancestor tenants of the tenant service group
specified in this request. If the TSG ID supplied
in this API's path does not match the TSG ID contained in
the access token used to authenticate this request, this
request will fail.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy()

req = operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsRequest(
    fields_='corrupti',
    include_self=False,
    sort=operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSort.DESC,
    tsg_id='1378242802',
)

res = s.tenancy_group.list_ancestors(req, operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_ancestors_200_application_json_object is not None:
    # handle response
```

## list_children

List the child tenants of the tenant service group
specified in this request. If the TSG ID supplied
in this API's path does not match the TSG ID contained in
the access token used to authenticate this request, this
request will fail.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy()

req = operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenRequest(
    hierarchy=False,
    include_self=False,
    tsg_id='1378242802',
)

res = s.tenancy_group.list_children(req, operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_children_200_application_json_object is not None:
    # handle response
```

## update

Update a tenant service group. If the TSG ID supplied 
in this API's path does not match the TSG ID contained in
the access token used to authenticate this request, this 
request will fail.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations, shared

s = sase_tenancy.SaseTenancy()

req = operations.PutTenancyV1TenantServiceGroupsTsgIDRequest(
    tenant_service_group_update=shared.TenantServiceGroupUpdate(
        display_name='Example TSG',
        support_contact='user@example.com',
        vertical=shared.TenantServiceGroupUpdateVertical.HIGH_TECH,
    ),
    tsg_id='1378242802',
)

res = s.tenancy_group.update(req, operations.PutTenancyV1TenantServiceGroupsTsgIDSecurity(
    bearer="YOUR_BEARER_TOKEN_HERE",
))

if res.tenant_service_group is not None:
    # handle response
```
