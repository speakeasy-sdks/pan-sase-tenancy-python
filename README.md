# sase-tenancy

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/pan-sase-tenancy-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
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
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [tenancy_group](docs/tenancygroup/README.md)

* [create](docs/tenancygroup/README.md#create) - Create a tenant service group
* [delete](docs/tenancygroup/README.md#delete) - Delete a tenant service group
* [get](docs/tenancygroup/README.md#get) - Get a tenant service group
* [list](docs/tenancygroup/README.md#list) - List all tenant service groups
* [list_ancestors](docs/tenancygroup/README.md#list_ancestors) - List tenant service group ancestors
* [list_children](docs/tenancygroup/README.md#list_children) - List tenant service group children
* [update](docs/tenancygroup/README.md#update) - Update a tenant service group
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
