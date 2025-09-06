import pytest
from gemcontent import (
    CompanyInfo, GenerationRequest, GenerationResponse, 
    GenerationStatus, Publication, Image, SubscriptionStatus,
    StatisticsOverview
)


class TestCompanyInfo:
    def test_company_info_creation(self):
        """Test CompanyInfo creation with all fields"""
        company = CompanyInfo(
            name="Test Company",
            description="Test description",
            industry="Technology",
            target_audience="Developers",
            content_preferences={
                "length": "medium",
                "style": "educational",
                "include_examples": True,
                "include_statistics": True,
                "include_images": True
            },
            tone="professional"
        )

        assert company.name == "Test Company"
        assert company.description == "Test description"
        assert company.industry == "Technology"
        assert company.target_audience == "Developers"
        assert company.content_preferences["length"] == "medium"
        assert company.tone == "professional"

    def test_company_info_to_dict(self):
        """Test CompanyInfo to_dict method"""
        company = CompanyInfo(
            name="Test Company",
            description="Test description"
        )

        result = company.to_dict()

        assert result["name"] == "Test Company"
        assert result["description"] == "Test description"
        assert "industry" not in result  # None values should be excluded

    def test_company_info_to_dict_with_none(self):
        """Test CompanyInfo to_dict with None values"""
        company = CompanyInfo()

        result = company.to_dict()

        assert result == {}


class TestGenerationRequest:
    def test_generation_request_creation(self):
        """Test GenerationRequest creation"""
        company_info = CompanyInfo(name="Test Company")
        request = GenerationRequest(
            prompt="Write about AI",
            company_info=company_info,
            keywords=["AI", "business", "automation"]
        )

        assert request.prompt == "Write about AI"
        assert request.company_info.name == "Test Company"
        assert request.keywords == ["AI", "business", "automation"]

    def test_generation_request_to_dict(self):
        """Test GenerationRequest to_dict method"""
        company_info = CompanyInfo(name="Test Company")
        request = GenerationRequest(
            prompt="Write about AI",
            company_info=company_info,
            keywords=["AI", "business"]
        )

        result = request.to_dict()

        assert result["prompt"] == "Write about AI"
        assert result["company_info"]["name"] == "Test Company"
        assert result["keywords"] == ["AI", "business"]

    def test_generation_request_to_dict_no_optional(self):
        """Test GenerationRequest to_dict without optional fields"""
        request = GenerationRequest(prompt="Write about AI")

        result = request.to_dict()

        assert result["prompt"] == "Write about AI"
        assert "company_info" not in result
        assert "keywords" not in result


class TestGenerationResponse:
    def test_generation_response_creation(self):
        """Test GenerationResponse creation"""
        response = GenerationResponse(
            success=True,
            data={
                "publicationId": "pub_123",
                "sessionId": "sess_456"
            },
            message="Generation started"
        )

        assert response.success is True
        assert response.data["publicationId"] == "pub_123"
        assert response.data["sessionId"] == "sess_456"
        assert response.message == "Generation started"

    def test_generation_response_properties(self):
        """Test GenerationResponse properties"""
        response = GenerationResponse(
            success=True,
            data={
                "publicationId": "pub_123",
                "sessionId": "sess_456"
            }
        )

        assert response.publication_id == "pub_123"
        assert response.session_id == "sess_456"

    def test_generation_response_properties_none(self):
        """Test GenerationResponse properties with None data"""
        response = GenerationResponse(success=False)

        assert response.publication_id is None
        assert response.session_id is None


class TestGenerationStatus:
    def test_generation_status_creation(self):
        """Test GenerationStatus creation"""
        status = GenerationStatus(
            success=True,
            data={
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "completed",
                "content": "Generated content",
                "blogTopic": "AI in Business"
            }
        )

        assert status.success is True
        assert status.data["publicationId"] == "pub_123"
        assert status.data["status"] == "completed"

    def test_generation_status_properties(self):
        """Test GenerationStatus properties"""
        status = GenerationStatus(
            success=True,
            data={
                "status": "completed",
                "content": "Generated content",
                "blogTopic": "AI in Business"
            }
        )

        assert status.status == "completed"
        assert status.content == "Generated content"
        assert status.blog_topic == "AI in Business"
        assert status.is_completed is True
        assert status.is_failed is False

    def test_generation_status_failed(self):
        """Test GenerationStatus with failed status"""
        status = GenerationStatus(
            success=True,
            data={"status": "failed"}
        )

        assert status.is_completed is False
        assert status.is_failed is True


class TestPublication:
    def test_publication_from_dict(self):
        """Test Publication creation from dictionary"""
        data = {
            "id": "pub_123",
            "title": "Test Publication",
            "content": "Test content",
            "type": "blog",
            "status": "published",
            "contentLength": 100,
            "imagesCount": 2,
            "createdAt": "2024-01-01T00:00:00Z",
            "updatedAt": "2024-01-01T00:00:00Z",
            "metaTitle": "Test Meta Title",
            "metaDescription": "Test meta description",
            "companyName": "Test Company",
            "topic": "AI",
            "qualityScore": 8.5,
            "generationTimeSeconds": 30,
            "publishedAt": "2024-01-01T01:00:00Z"
        }

        publication = Publication.from_dict(data)

        assert publication.id == "pub_123"
        assert publication.title == "Test Publication"
        assert publication.content == "Test content"
        assert publication.type == "blog"
        assert publication.status == "published"
        assert publication.content_length == 100
        assert publication.images_count == 2
        assert publication.meta_title == "Test Meta Title"
        assert publication.company_name == "Test Company"
        assert publication.topic == "AI"
        assert publication.quality_score == 8.5
        assert publication.generation_time_seconds == 30


class TestImage:
    def test_image_from_dict(self):
        """Test Image creation from dictionary"""
        data = {
            "id": "img_123",
            "filename": "test.jpg",
            "originalName": "original.jpg",
            "mimeType": "image/jpeg",
            "size": 1024,
            "url": "https://example.com/test.jpg",
            "createdAt": "2024-01-01T00:00:00Z",
            "prompt": "A beautiful landscape",
            "tags": ["landscape", "nature"],
            "publicationId": "pub_123"
        }

        image = Image.from_dict(data)

        assert image.id == "img_123"
        assert image.filename == "test.jpg"
        assert image.original_name == "original.jpg"
        assert image.mime_type == "image/jpeg"
        assert image.size == 1024
        assert image.url == "https://example.com/test.jpg"
        assert image.prompt == "A beautiful landscape"
        assert image.tags == ["landscape", "nature"]
        assert image.publication_id == "pub_123"


class TestSubscriptionStatus:
    def test_subscription_status_properties(self):
        """Test SubscriptionStatus properties"""
        status = SubscriptionStatus(
            success=True,
            data={
                "subscription": {
                    "planName": "Pro",
                    "postsRemaining": 75
                }
            }
        )

        assert status.subscription["planName"] == "Pro"
        assert status.plan_name == "Pro"
        assert status.posts_remaining == 75

    def test_subscription_status_properties_none(self):
        """Test SubscriptionStatus properties with None data"""
        status = SubscriptionStatus(success=False)

        assert status.subscription is None
        assert status.plan_name is None
        assert status.posts_remaining is None


class TestStatisticsOverview:
    def test_statistics_overview_properties(self):
        """Test StatisticsOverview properties"""
        overview = StatisticsOverview(
            success=True,
            data={
                "publications": {"total": 10, "published": 8},
                "images": {"totalImages": 25, "totalSize": 1024000},
                "apiKeys": {"totalKeys": 3, "activeKeys": 2},
                "userLimits": {"postsUsed": 25, "postsRemaining": 75}
            }
        )

        assert overview.publications["total"] == 10
        assert overview.images["totalImages"] == 25
        assert overview.api_keys["totalKeys"] == 3
        assert overview.user_limits["postsUsed"] == 25

    def test_statistics_overview_properties_none(self):
        """Test StatisticsOverview properties with None data"""
        overview = StatisticsOverview(success=False)

        assert overview.publications is None
        assert overview.images is None
        assert overview.api_keys is None
        assert overview.user_limits is None 