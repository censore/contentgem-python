"""
ContentGem Python SDK

Official Python SDK for the ContentGem API.
"""

from .client import ContentGemClient
from .types import (
    CompanyInfo,
    ContentPreferences,
    Service,
    Expertise,
    Value,
    SocialMedia,
    GenerationRequest,
    BulkGenerationRequest,
    GenerationResponse,
    BulkGenerationResponse,
    GenerationStatus,
    BulkGenerationStatus,
    Publication,
    PublicationImage,
    GenerationMetadata,
    Image,
    ImageDimensions,
    SubscriptionStatus,
    Plan,
    Usage,
    PlanFeature,
    SubscriptionPlan,
    SubscriptionLimits,
    StatisticsOverview,
    Pagination,
    PublicationsResponse,
    ImagesResponse,
    ApiResponse,
)

__version__ = "1.2.0"
__author__ = "ContentGem Team"
__email__ = "support@contentgem.com"

__all__ = [
    "ContentGemClient",
    "CompanyInfo",
    "ContentPreferences",
    "Service",
    "Expertise",
    "Value",
    "SocialMedia",
    "GenerationRequest",
    "BulkGenerationRequest",
    "GenerationResponse",
    "BulkGenerationResponse",
    "GenerationStatus",
    "BulkGenerationStatus",
    "Publication",
    "PublicationImage",
    "GenerationMetadata",
    "Image",
    "ImageDimensions",
    "SubscriptionStatus",
    "Plan",
    "Usage",
    "PlanFeature",
    "SubscriptionPlan",
    "SubscriptionLimits",
    "StatisticsOverview",
    "Pagination",
    "PublicationsResponse",
    "ImagesResponse",
    "ApiResponse",
] 