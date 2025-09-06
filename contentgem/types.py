"""
Type definitions for ContentGem Python SDK
"""

from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ContentPreferences:
    """Content generation preferences"""
    length: Optional[str] = None  # short, medium, long
    style: Optional[str] = None  # educational, promotional, technical, etc.
    include_examples: Optional[bool] = None
    include_statistics: Optional[bool] = None
    include_images: Optional[bool] = None
    include_custom_templates: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        for field_name, value in self.__dict__.items():
            if value is not None:
                result[field_name] = value
        return result


@dataclass
class Service:
    """Company service"""
    name: str
    description: str


@dataclass
class Expertise:
    """Company expertise area"""
    area: str
    description: str
    years_of_experience: Optional[int] = None


@dataclass
class Value:
    """Company value"""
    value: str
    description: str


@dataclass
class SocialMedia:
    """Company social media links"""
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
    facebook: Optional[str] = None
    instagram: Optional[str] = None


@dataclass
class CompanyInfo:
    """Company information for content generation"""
    name: Optional[str] = None
    description: Optional[str] = None
    industry: Optional[str] = None
    target_audience: Optional[str] = None
    website: Optional[str] = None
    services: Optional[List[Service]] = None
    expertise: Optional[List[Expertise]] = None
    values: Optional[List[Value]] = None
    mission: Optional[str] = None
    vision: Optional[str] = None
    social_media: Optional[SocialMedia] = None
    content_preferences: Optional[ContentPreferences] = None
    tone: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {}
        for field_name, value in self.__dict__.items():
            if value is not None:
                if field_name == "services" and value:
                    result["services"] = [s.__dict__ for s in value]
                elif field_name == "expertise" and value:
                    result["expertise"] = [e.__dict__ for e in value]
                elif field_name == "values" and value:
                    result["values"] = [v.__dict__ for v in value]
                elif field_name == "social_media" and value:
                    result["social_media"] = value.__dict__
                elif field_name == "content_preferences" and value:
                    result["content_preferences"] = value.to_dict()
                else:
                    result[field_name] = value
        return result


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
class BulkGenerationRequest:
    """Request for bulk content generation"""
    prompts: List[str]
    company_info: Optional[CompanyInfo] = None
    common_settings: Optional[Dict[str, Any]] = None
    keywords: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        result = {"prompts": self.prompts}
        if self.company_info:
            result["company_info"] = self.company_info.to_dict()
        if self.common_settings:
            result["common_settings"] = self.common_settings
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
class BulkGenerationResponse:
    """Response from bulk generation request"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def total_prompts(self) -> Optional[int]:
        """Get total prompts count"""
        return self.data.get("totalPrompts") if self.data else None

    @property
    def success_count(self) -> Optional[int]:
        """Get success count"""
        return self.data.get("successCount") if self.data else None

    @property
    def error_count(self) -> Optional[int]:
        """Get error count"""
        return self.data.get("errorCount") if self.data else None

    @property
    def publications(self) -> Optional[List[Dict[str, Any]]]:
        """Get publications list"""
        return self.data.get("publications") if self.data else None


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
    def step_name(self) -> Optional[str]:
        """Get current step name"""
        return self.data.get("stepName") if self.data else None

    @property
    def metadata(self) -> Optional[Dict[str, Any]]:
        """Get generation metadata"""
        return self.data.get("metadata") if self.data else None

    @property
    def is_completed(self) -> bool:
        """Check if generation is completed"""
        return self.status == "completed"

    @property
    def is_failed(self) -> bool:
        """Check if generation failed"""
        return self.status == "failed"

    @property
    def is_generating(self) -> bool:
        """Check if generation is in progress"""
        return self.status == "generating"


@dataclass
class BulkGenerationStatus:
    """Status of bulk generation"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def bulk_session_id(self) -> Optional[str]:
        """Get bulk session ID"""
        return self.data.get("bulkSessionId") if self.data else None

    @property
    def status(self) -> Optional[str]:
        """Get bulk generation status"""
        return self.data.get("status") if self.data else None

    @property
    def total_publications(self) -> Optional[int]:
        """Get total publications count"""
        return self.data.get("totalPublications") if self.data else None

    @property
    def completed_publications(self) -> Optional[int]:
        """Get completed publications count"""
        return self.data.get("completedPublications") if self.data else None

    @property
    def failed_publications(self) -> Optional[int]:
        """Get failed publications count"""
        return self.data.get("failedPublications") if self.data else None

    @property
    def publications(self) -> Optional[List[Dict[str, Any]]]:
        """Get publications list with status"""
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
class PublicationImage:
    """Publication image model"""
    id: str
    url: str
    alt: Optional[str] = None
    filename: Optional[str] = None
    prompt: Optional[str] = None
    section_title: Optional[str] = None
    is_main_image: Optional[bool] = None
    created_at: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PublicationImage":
        """Create PublicationImage from dictionary"""
        return cls(
            id=data["id"],
            url=data["url"],
            alt=data.get("alt"),
            filename=data.get("filename"),
            prompt=data.get("prompt"),
            section_title=data.get("sectionTitle"),
            is_main_image=data.get("isMainImage"),
            created_at=data.get("createdAt"),
        )


@dataclass
class GenerationMetadata:
    """Generation metadata"""
    model: Optional[str] = None
    tokens: Optional[int] = None
    generation_time: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GenerationMetadata":
        """Create GenerationMetadata from dictionary"""
        return cls(
            model=data.get("model"),
            tokens=data.get("tokens"),
            generation_time=data.get("generationTime"),
        )


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
    user_id: Optional[str] = None
    session_id: Optional[str] = None
    marketing_id: Optional[str] = None
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    generation_type: Optional[str] = None
    company_name: Optional[str] = None
    company_description: Optional[str] = None
    company_industry: Optional[str] = None
    company_target_audience: Optional[str] = None
    initial_prompt: Optional[str] = None
    topic: Optional[str] = None
    structure: Optional[Dict[str, Any]] = None
    images: Optional[List[PublicationImage]] = None
    quality_score: Optional[float] = None
    generation_metadata: Optional[GenerationMetadata] = None
    generation_time_seconds: Optional[int] = None
    published_at: Optional[str] = None
    main_image_url: Optional[str] = None
    image_url: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Publication":
        """Create Publication from dictionary"""
        images = None
        if data.get("images"):
            images = [PublicationImage.from_dict(img) for img in data["images"]]
        
        generation_metadata = None
        if data.get("generationMetadata"):
            generation_metadata = GenerationMetadata.from_dict(data["generationMetadata"])
        
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
            user_id=data.get("userId"),
            session_id=data.get("sessionId"),
            marketing_id=data.get("marketingId"),
            meta_title=data.get("metaTitle"),
            meta_description=data.get("metaDescription"),
            generation_type=data.get("generationType"),
            company_name=data.get("companyName"),
            company_description=data.get("companyDescription"),
            company_industry=data.get("companyIndustry"),
            company_target_audience=data.get("companyTargetAudience"),
            initial_prompt=data.get("initialPrompt"),
            topic=data.get("topic"),
            structure=data.get("structure"),
            images=images,
            quality_score=data.get("qualityScore"),
            generation_metadata=generation_metadata,
            generation_time_seconds=data.get("generationTimeSeconds"),
            published_at=data.get("publishedAt"),
            main_image_url=data.get("mainImageUrl"),
            image_url=data.get("imageUrl"),
        )


@dataclass
class ImageDimensions:
    """Image dimensions"""
    width: int
    height: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImageDimensions":
        """Create ImageDimensions from dictionary"""
        return cls(
            width=data["width"],
            height=data["height"],
        )


@dataclass
class Image:
    """Image model"""
    id: str
    filename: str
    original_name: str
    public_url: str
    created_at: str
    prompt: Optional[str] = None
    section_title: Optional[str] = None
    file_size: Optional[int] = None
    dimensions: Optional[ImageDimensions] = None
    tags: Optional[List[str]] = None
    publication_id: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Image":
        """Create Image from dictionary"""
        dimensions = None
        if data.get("dimensions"):
            dimensions = ImageDimensions.from_dict(data["dimensions"])
        
        return cls(
            id=data["id"],
            filename=data["filename"],
            original_name=data["originalName"],
            public_url=data["publicUrl"],
            created_at=data["createdAt"],
            prompt=data.get("prompt"),
            section_title=data.get("sectionTitle"),
            file_size=data.get("fileSize"),
            dimensions=dimensions,
            tags=data.get("tags"),
            publication_id=data.get("publicationId"),
        )


@dataclass
class Plan:
    """Subscription plan model"""
    name: str
    slug: str
    price: float
    currency: str
    interval: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Plan":
        """Create Plan from dictionary"""
        return cls(
            name=data["name"],
            slug=data["slug"],
            price=data["price"],
            currency=data["currency"],
            interval=data["interval"],
        )


@dataclass
class Usage:
    """Usage statistics"""
    posts_used: int
    posts_remaining: int
    posts_per_month: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Usage":
        """Create Usage from dictionary"""
        return cls(
            posts_used=data["postsUsed"],
            posts_remaining=data["postsRemaining"],
            posts_per_month=data["postsPerMonth"],
        )


@dataclass
class SubscriptionStatus:
    """Subscription status model"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def plan(self) -> Optional[Plan]:
        """Get plan data"""
        if self.data and self.data.get("plan"):
            return Plan.from_dict(self.data["plan"])
        return None

    @property
    def usage(self) -> Optional[Usage]:
        """Get usage data"""
        if self.data and self.data.get("usage"):
            return Usage.from_dict(self.data["usage"])
        return None

    @property
    def status(self) -> Optional[str]:
        """Get subscription status"""
        return self.data.get("status") if self.data else None

    @property
    def next_billing_date(self) -> Optional[str]:
        """Get next billing date"""
        return self.data.get("nextBillingDate") if self.data else None


@dataclass
class PlanFeature:
    """Plan feature"""
    publications: int
    images: int
    ai_generation: bool
    image_generation: bool
    custom_templates: bool
    priority_support: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PlanFeature":
        """Create PlanFeature from dictionary"""
        return cls(
            publications=data["publications"],
            images=data["images"],
            ai_generation=data["aiGeneration"],
            image_generation=data["imageGeneration"],
            custom_templates=data["customTemplates"],
            priority_support=data["prioritySupport"],
        )


@dataclass
class SubscriptionPlan:
    """Subscription plan with features"""
    id: str
    name: str
    price: float
    currency: str
    interval: str
    features: PlanFeature

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SubscriptionPlan":
        """Create SubscriptionPlan from dictionary"""
        return cls(
            id=data["id"],
            name=data["name"],
            price=data["price"],
            currency=data["currency"],
            interval=data["interval"],
            features=PlanFeature.from_dict(data["features"]),
        )


@dataclass
class SubscriptionLimits:
    """Subscription limits"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def current_plan(self) -> Optional[str]:
        """Get current plan slug"""
        return self.data.get("currentPlan") if self.data else None

    @property
    def limits(self) -> Optional[Dict[str, Any]]:
        """Get limits data"""
        return self.data.get("limits") if self.data else None

    @property
    def features(self) -> Optional[Dict[str, Any]]:
        """Get features data"""
        return self.data.get("features") if self.data else None


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


@dataclass
class Pagination:
    """Pagination information"""
    current_page: int
    total_pages: int
    total_items: int
    items_per_page: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Pagination":
        """Create Pagination from dictionary"""
        return cls(
            current_page=data["currentPage"],
            total_pages=data["totalPages"],
            total_items=data["totalItems"],
            items_per_page=data["itemsPerPage"],
        )


@dataclass
class PublicationsResponse:
    """Publications list response"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def publications(self) -> Optional[List[Publication]]:
        """Get publications list"""
        if self.data and self.data.get("publications"):
            return [Publication.from_dict(pub) for pub in self.data["publications"]]
        return None

    @property
    def pagination(self) -> Optional[Pagination]:
        """Get pagination info"""
        if self.data and self.data.get("pagination"):
            return Pagination.from_dict(self.data["pagination"])
        return None

    @property
    def stats(self) -> Optional[Dict[str, int]]:
        """Get statistics"""
        return self.data.get("stats") if self.data else None

    @property
    def user_limits(self) -> Optional[Dict[str, Any]]:
        """Get user limits"""
        return self.data.get("userLimits") if self.data else None


@dataclass
class ImagesResponse:
    """Images list response"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def images(self) -> Optional[List[Image]]:
        """Get images list"""
        if self.data and self.data.get("images"):
            return [Image.from_dict(img) for img in self.data["images"]]
        return None

    @property
    def pagination(self) -> Optional[Pagination]:
        """Get pagination info"""
        if self.data and self.data.get("pagination"):
            return Pagination.from_dict(self.data["pagination"])
        return None

    @property
    def stats(self) -> Optional[Dict[str, Any]]:
        """Get statistics"""
        return self.data.get("stats") if self.data else None


# Generic response type
ApiResponse = Dict[str, Any] 