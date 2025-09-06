"""
GemContent Python SDK

Official Python SDK for the GemContent API.
"""

from .client import GemContentClient
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
__author__ = "GemContent Team"
__email__ = "support@gemcontent.com"

__all__ = [
    "GemContentClient",
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