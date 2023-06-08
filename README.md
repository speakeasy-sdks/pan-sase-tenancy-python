<div align="center">
    <img src="https://github.com/speakeasy-sdks/pan-sase-tenancy-ts/assets/6267663/e0205c2a-fa61-4b1f-aaa0-599896e022da" width="300">
    <h1>SASE Tenancy Python SDK</h1>
   <p>Containers used to build your tenant hierachy.</p>
   <a href="https://pan.dev/category/sase/api/tenancy/tenant-service-group/"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=000&style=for-the-badge" /></a>
   <a href="https://github.com/speakeasy-sdks/pan-sase-tenancy-python/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/pan-sase-tenancy-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>

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
