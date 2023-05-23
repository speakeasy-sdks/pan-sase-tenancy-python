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