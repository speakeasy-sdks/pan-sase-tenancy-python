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
from sase_tenancy.models import shared

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)

req = shared.TenantServiceGroupCreate(
    display_name='Example TSG',
    parent_id='1378242802',
    support_contact='user@example.com',
    vertical=shared.TenantServiceGroupCreateVertical.HIGH_TECH,
)

res = s.tenancy_group.create(req)

if res.tenant_service_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [shared.TenantServiceGroupCreate](../../models/shared/tenantservicegroupcreate.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.PostTenancyV1TenantServiceGroupsResponse](../../models/operations/posttenancyv1tenantservicegroupsresponse.md)**


## delete

Delete a tenant service group. If the TSG ID supplied
in this API's path does not match the TSG ID contained in
the access token used to authenticate this request, this
request will fail.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)


res = s.tenancy_group.delete('1378242802')

if res.tenant_service_group is not None:
    # handle response
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `tsg_id`                                           | *str*                                              | :heavy_check_mark:                                 | A unique identifier for the tenant service group.<br/> | 1378242802                                         |


### Response

**[operations.DeleteTenancyV1TenantServiceGroupsTsgIDResponse](../../models/operations/deletetenancyv1tenantservicegroupstsgidresponse.md)**


## get

Get a tenant service group by TSG ID.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)


res = s.tenancy_group.get('1378242802')

if res.tenant_service_group is not None:
    # handle response
```

### Parameters

| Parameter                                          | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `tsg_id`                                           | *str*                                              | :heavy_check_mark:                                 | A unique identifier for the tenant service group.<br/> | 1378242802                                         |


### Response

**[operations.GetTenancyV1TenantServiceGroupsTsgIDResponse](../../models/operations/gettenancyv1tenantservicegroupstsgidresponse.md)**


## list

Get a list of all the tenant service groups
that are available to the service account used to
authenticate this request.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)


res = s.tenancy_group.list(False)

if res.get_tenancy_v1_tenant_service_groups_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hierarchy`                                                                                                                                                                                                                                     | *Optional[bool]*                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                              | Indicates whether the response structure lists groups in<br/>their hierarchy, or as an array of TSGs without regard to<br/>hierarchy. Default is false (don't show hierarchy).<br/><br/>If false, the order of the TSGs in the result array is not<br/>guaranteed.<br/> |


### Response

**[operations.GetTenancyV1TenantServiceGroupsResponse](../../models/operations/gettenancyv1tenantservicegroupsresponse.md)**


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

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)


res = s.tenancy_group.list_ancestors('1378242802', 'corrupti', False, operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSort.DESC)

if res.post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_ancestors_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                                            | Type                                                                                                                                                                                 | Required                                                                                                                                                                             | Description                                                                                                                                                                          | Example                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `tsg_id`                                                                                                                                                                             | *str*                                                                                                                                                                                | :heavy_check_mark:                                                                                                                                                                   | A unique identifier for the tenant service group.<br/>                                                                                                                               | 1378242802                                                                                                                                                                           |
| `fields_`                                                                                                                                                                            | *Optional[str]*                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                   | Provide a comma-separated list of fields you want returned.<br/>                                                                                                                     |                                                                                                                                                                                      |
| `include_self`                                                                                                                                                                       | *Optional[bool]*                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                   | Indicates if the TSG used to generate this hierarchy is<br/>included in the resulting TSG list. `true` to include<br/>self. Default is `false`.<br/>                                 |                                                                                                                                                                                      |
| `sort`                                                                                                                                                                               | [Optional[operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsSort]](../../models/operations/posttenancyv1tenantservicegroupstsgidoperationslistancestorssort.md) | :heavy_minus_sign:                                                                                                                                                                   | Identifies the response structure's sort order:<br/><br/>* `asc` : From root to leaf.<br/>* `desc` : From leaf to root.<br/>                                                         |                                                                                                                                                                                      |


### Response

**[operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListAncestorsResponse](../../models/operations/posttenancyv1tenantservicegroupstsgidoperationslistancestorsresponse.md)**


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

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)


res = s.tenancy_group.list_children('1378242802', False, False)

if res.post_tenancy_v1_tenant_service_groups_tsg_id_operations_list_children_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                                                         | Type                                                                                                                                                              | Required                                                                                                                                                          | Description                                                                                                                                                       | Example                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tsg_id`                                                                                                                                                          | *str*                                                                                                                                                             | :heavy_check_mark:                                                                                                                                                | A unique identifier for the tenant service group.<br/>                                                                                                            | 1378242802                                                                                                                                                        |
| `hierarchy`                                                                                                                                                       | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | If `true`, return the entire descendent hierarchy.<br/>If `false`, return only the immediate children of the<br/>TSG identified in this call's path. Default is<br/>`false`.<br/> |                                                                                                                                                                   |
| `include_self`                                                                                                                                                    | *Optional[bool]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                | Indicates if the TSG used to generate this hierarchy is<br/>included in the resulting TSG list. `true` to include<br/>self. Default is `false`.<br/>              |                                                                                                                                                                   |


### Response

**[operations.PostTenancyV1TenantServiceGroupsTsgIDOperationsListChildrenResponse](../../models/operations/posttenancyv1tenantservicegroupstsgidoperationslistchildrenresponse.md)**


## update

Update a tenant service group. If the TSG ID supplied 
in this API's path does not match the TSG ID contained in
the access token used to authenticate this request, this 
request will fail.


### Example Usage

```python
import sase_tenancy
from sase_tenancy.models import operations, shared

s = sase_tenancy.SaseTenancy(
    security=shared.Security(
        bearer="",
    ),
)


res = s.tenancy_group.update(shared.TenantServiceGroupUpdate(
    display_name='Example TSG',
    support_contact='user@example.com',
    vertical=shared.TenantServiceGroupUpdateVertical.HIGH_TECH,
), '1378242802')

if res.tenant_service_group is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        | Example                                                                            |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `tenant_service_group_update`                                                      | [shared.TenantServiceGroupUpdate](../../models/shared/tenantservicegroupupdate.md) | :heavy_check_mark:                                                                 | N/A                                                                                |                                                                                    |
| `tsg_id`                                                                           | *str*                                                                              | :heavy_check_mark:                                                                 | A unique identifier for the tenant service group.<br/>                             | 1378242802                                                                         |


### Response

**[operations.PutTenancyV1TenantServiceGroupsTsgIDResponse](../../models/operations/puttenancyv1tenantservicegroupstsgidresponse.md)**

