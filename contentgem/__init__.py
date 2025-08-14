"""
ContentGem Python SDK

Official Python SDK for the ContentGem API.
"""

from .client import ContentGemClient
from .types import (
    CompanyInfo,
    GenerationRequest,
    GenerationResponse,
    GenerationStatus,
    Publication,
    Image,
    SubscriptionStatus,
    StatisticsOverview,
)

__version__ = "1.0.0"
__author__ = "ContentGem Team"
__email__ = "support@contentgem.com"

__all__ = [
    "ContentGemClient",
    "CompanyInfo",
    "GenerationRequest",
    "GenerationResponse",
    "GenerationStatus",
    "Publication",
    "Image",
    "SubscriptionStatus",
    "StatisticsOverview",
] 