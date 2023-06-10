"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from sase_tenancy import utils
from typing import Optional

class TenantServiceGroupVertical(str, Enum):
    r"""A token that identifies the business vertical supported by the SASE
    products managed by this TSG.
    """
    HIGH_TECH = 'High Tech'
    EDUCATION = 'Education'
    MANUFACTURING = 'Manufacturing'
    HOSPITALITY = 'Hospitality'
    PROFESSIONAL_AND_LEGAL_SERVICES = 'Professional & Legal Services'
    WHOLESALE_AND_RETAIL = 'Wholesale & Retail'
    FINANCE = 'Finance'
    TELECOMMUNICATIONS = 'Telecommunications'
    STATE_AND_LOCAL_GOVERNMENT = 'State & Local Government'
    TRANSPORTATION_AND_LOGISTICS = 'Transportation & Logistics'
    FEDERAL_GOVERNMENT = 'Federal Government'
    MEDIA_AND_ENTERTAINMENT = 'Media & Entertainment'
    NONCLASSIFIABLE_ESTABLISHMENTS = 'Nonclassifiable Establishments'
    HEALTHCARE = 'Healthcare'
    UTILITIES_AND_ENERGY = 'Utilities & Energy'
    INSURANCE = 'Insurance'
    AGRICULTURE = 'Agriculture'
    PHARMA_AND_LIFE_SCIENCES = 'Pharma & Life Sciences'
    CONSTRUCTION = 'Construction'
    AEROSPACE_AND_DEFENSE = 'Aerospace & Defense'
    REAL_ESTATE = 'Real Estate'
    RESTAURANT_FOOD_INDUSTRY = 'Restaurant/Food Industry'
    OTHER = 'Other'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TenantServiceGroup:
    r"""Successful response."""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The tenant service group's ID."""
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    r"""The tenant service group's display name."""
    parent_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parent_id'), 'exclude': lambda f: f is None }})
    r"""The TSG ID for this tenant service group's parent."""
    support_contact: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('support_contact'), 'exclude': lambda f: f is None }})
    r"""The email address of the person or organization that should
    be contacted for support of this TSG.
    """
    vertical: Optional[TenantServiceGroupVertical] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vertical'), 'exclude': lambda f: f is None }})
    r"""A token that identifies the business vertical supported by the SASE
    products managed by this TSG.
    """
    

