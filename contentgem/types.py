"""
Type definitions for ContentGem Python SDK
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from datetime import datetime


@dataclass
class CompanyInfo:
    """Company information for content generation"""
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    target_audience: Optional[str] = None
    content_preferences: Optional[Dict[str, Any]] = None
    tone: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        for field, value in self.__dict__.items():
            if value is not None:
                result[field] = value
        return result


@dataclass
class BulkGenerationRequest:
    """Request for bulk content generation"""
    prompts: List[str]
    company_info: Optional[CompanyInfo] = None
    common_settings: Optional[Dict[str, Any]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"prompts": self.prompts}
        if self.company_info:
            result["company_info"] = self.company_info.to_dict()
        if self.common_settings:
            result["common_settings"] = self.common_settings
        return result


@dataclass
class BulkGenerationResponse:
    """Response from bulk generation request"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def bulk_session_id(self) -> Optional[str]:
        """Get bulk session ID from response"""
        return self.data.get("bulk_session_id") if self.data else None

    @property
    def total_prompts(self) -> Optional[int]:
        """Get total number of prompts"""
        return self.data.get("total_prompts") if self.data else None


@dataclass
class BulkGenerationStatus:
    """Status of bulk content generation"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def status(self) -> Optional[str]:
        """Get bulk generation status"""
        return self.data.get("status") if self.data else None

    @property
    def completed_prompts(self) -> Optional[int]:
        """Get number of completed prompts"""
        return self.data.get("completed_prompts") if self.data else None

    @property
    def failed_prompts(self) -> Optional[int]:
        """Get number of failed prompts"""
        return self.data.get("failed_prompts") if self.data else None

    @property
    def publications(self) -> Optional[List[Dict[str, Any]]]:
        """Get publications list"""
        return self.data.get("publications") if self.data else None

    @property
    def is_completed(self) -> bool:
        """Check if bulk generation is completed"""
        return self.status == "completed"

    @property
    def is_failed(self) -> bool:
        """Check if bulk generation failed"""
        return self.status == "failed"


@dataclass
class CompanyData:
    """Company data structure"""
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None
    contact_email: Optional[str] = None
    contact_phone: Optional[str] = None
    address: Optional[str] = None
    social_media: Optional[Dict[str, str]] = None
    logo_url: Optional[str] = None
    founded_year: Optional[int] = None
    employee_count: Optional[str] = None
    revenue: Optional[str] = None
    target_audience: Optional[str] = None
    services: Optional[List[str]] = None
    keywords: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        for field, value in self.__dict__.items():
            if value is not None:
                result[field] = value
        return result


@dataclass
class CompanyResponse:
    """Response from company operations"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def company(self) -> Optional[CompanyData]:
        """Get company data"""
        if self.data and "company" in self.data:
            company_dict = self.data["company"]
            return CompanyData(**company_dict)
        return None


@dataclass
class CompanyParsingRequest:
    """Request for company website parsing"""
    website_url: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {"website_url": self.website_url}


@dataclass
class CompanyParsingResponse:
    """Response from company parsing request"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def parsing_session_id(self) -> Optional[str]:
        """Get parsing session ID"""
        return self.data.get("parsing_session_id") if self.data else None


@dataclass
class CompanyParsingStatus:
    """Status of company parsing"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def status(self) -> Optional[str]:
        """Get parsing status"""
        return self.data.get("status") if self.data else None

    @property
    def progress(self) -> Optional[int]:
        """Get parsing progress"""
        return self.data.get("progress") if self.data else None

    @property
    def extracted_data(self) -> Optional[CompanyData]:
        """Get extracted company data"""
        if self.data and "extracted_data" in self.data:
            extracted_dict = self.data["extracted_data"]
            return CompanyData(**extracted_dict)
        return None


@dataclass
class GenerationRequest:
    """Request for content generation"""
    prompt: str
    company_info: Optional[CompanyInfo] = None
    keywords: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"prompt": self.prompt}
        if self.company_info:
            result["company_info"] = self.company_info.to_dict()
        if self.keywords:
            result["keywords"] = self.keywords
        return result


@dataclass
class GenerationResponse:
    """Response from content generation request"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def publication_id(self) -> Optional[str]:
        """Get publication ID from response"""
        return self.data.get("publicationId") if self.data else None

    @property
    def session_id(self) -> Optional[str]:
        """Get session ID from response"""
        return self.data.get("sessionId") if self.data else None


@dataclass
class GenerationStatus:
    """Status of content generation"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def status(self) -> Optional[str]:
        """Get generation status"""
        return self.data.get("status") if self.data else None

    @property
    def content(self) -> Optional[str]:
        """Get generated content"""
        return self.data.get("content") if self.data else None

    @property
    def blog_topic(self) -> Optional[str]:
        """Get blog topic"""
        return self.data.get("blogTopic") if self.data else None

    @property
    def is_completed(self) -> bool:
        """Check if generation is completed"""
        return self.status == "completed"

    @property
    def is_failed(self) -> bool:
        """Check if generation failed"""
        return self.status == "failed"


@dataclass
class Publication:
    """Publication model"""
    id: str
    title: str
    content: str
    type: str
    status: str
    content_length: int
    images_count: int
    created_at: str
    updated_at: str
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    company_name: Optional[str] = None
    company_description: Optional[str] = None
    company_industry: Optional[str] = None
    company_target_audience: Optional[str] = None
    topic: Optional[str] = None
    structure: Optional[Dict[str, Any]] = None
    images: Optional[List[Dict[str, Any]]] = None
    quality_score: Optional[float] = None
    generation_time_seconds: Optional[int] = None
    published_at: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Publication":
        """Create Publication from dictionary"""
        return cls(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            type=data["type"],
            status=data["status"],
            content_length=data["contentLength"],
            images_count=data["imagesCount"],
            created_at=data["createdAt"],
            updated_at=data["updatedAt"],
            meta_title=data.get("metaTitle"),
            meta_description=data.get("metaDescription"),
            company_name=data.get("companyName"),
            company_description=data.get("companyDescription"),
            company_industry=data.get("companyIndustry"),
            company_target_audience=data.get("companyTargetAudience"),
            topic=data.get("topic"),
            structure=data.get("structure"),
            images=data.get("images"),
            quality_score=data.get("qualityScore"),
            generation_time_seconds=data.get("generationTimeSeconds"),
            published_at=data.get("publishedAt"),
        )


@dataclass
class Image:
    """Image model"""
    id: str
    filename: str
    original_name: str
    mime_type: str
    size: int
    url: str
    created_at: str
    prompt: Optional[str] = None
    tags: Optional[List[str]] = None
    publication_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Image":
        """Create Image from dictionary"""
        return cls(
            id=data["id"],
            filename=data["filename"],
            original_name=data["originalName"],
            mime_type=data["mimeType"],
            size=data["size"],
            url=data["url"],
            created_at=data["createdAt"],
            prompt=data.get("prompt"),
            tags=data.get("tags"),
            publication_id=data.get("publicationId"),
        )


@dataclass
class SubscriptionStatus:
    """Subscription status model"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def subscription(self) -> Optional[Dict[str, Any]]:
        """Get subscription data"""
        return self.data.get("subscription") if self.data else None

    @property
    def plan_name(self) -> Optional[str]:
        """Get plan name"""
        sub = self.subscription
        return sub.get("planName") if sub else None

    @property
    def posts_remaining(self) -> Optional[int]:
        """Get remaining posts"""
        sub = self.subscription
        return sub.get("postsRemaining") if sub else None


@dataclass
class StatisticsOverview:
    """Statistics overview model"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def publications(self) -> Optional[Dict[str, int]]:
        """Get publications statistics"""
        return self.data.get("publications") if self.data else None

    @property
    def images(self) -> Optional[Dict[str, Any]]:
        """Get images statistics"""
        return self.data.get("images") if self.data else None

    @property
    def api_keys(self) -> Optional[Dict[str, Any]]:
        """Get API keys statistics"""
        return self.data.get("apiKeys") if self.data else None

    @property
    def user_limits(self) -> Optional[Dict[str, Any]]:
        """Get user limits"""
        return self.data.get("userLimits") if self.data else None


# Response types
PublicationsResponse = Dict[str, Any]
ImagesResponse = Dict[str, Any]
ApiResponse = Dict[str, Any] 