import pytest
import responses
from unittest.mock import patch, Mock
from gemcontent import GemContentClient, CompanyInfo, GenerationRequest


class TestContentGemClient:
    @pytest.fixture
    def client(self):
        return ContentGemClient(
            api_key="cg_test_api_key_123",
            base_url="https://api.test.com/v1"
        )

    @pytest.fixture
    def mock_response(self):
        return {
            "success": True,
            "data": {
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "generating"
            }
        }

    def test_constructor_default(self):
        """Test client constructor with default values"""
        client = ContentGemClient("test_key")
        assert client.api_key == "test_key"
        assert client.base_url == "https://gemcontent.com/api/v1"
        assert client.timeout == 30

    def test_constructor_custom(self):
        """Test client constructor with custom values"""
        client = ContentGemClient(
            api_key="test_key",
            base_url="https://custom.com/api",
            timeout=60
        )
        assert client.api_key == "test_key"
        assert client.base_url == "https://custom.com/api"
        assert client.timeout == 60

    @responses.activate
    def test_generate_publication_success(self, client, mock_response):
        """Test successful publication generation"""
        responses.add(
            responses.POST,
            "https://api.test.com/v1/publications/generate",
            json=mock_response,
            status=200
        )

        company_info = CompanyInfo(
            name="Test Company",
            description="Test description"
        )
        
        request = GenerationRequest(
            prompt="Write about AI in business",
            company_info=company_info
        )

        result = client.generate_publication(request)

        assert result.success is True
        assert result.data["publicationId"] == "pub_123"
        assert result.data["sessionId"] == "sess_456"

    @responses.activate
    def test_generate_publication_error(self, client):
        """Test publication generation with API error"""
        error_response = {
            "success": False,
            "error": "INVALID_PROMPT",
            "message": "Prompt is too short"
        }

        responses.add(
            responses.POST,
            "https://api.test.com/v1/publications/generate",
            json=error_response,
            status=400
        )

        request = GenerationRequest(prompt="AI")

        result = client.generate_publication(request)

        assert result.success is False
        assert result.error == "INVALID_PROMPT"

    @responses.activate
    def test_check_generation_status(self, client):
        """Test checking generation status"""
        status_response = {
            "success": True,
            "data": {
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "completed",
                "content": "Generated content here..."
            }
        }

        responses.add(
            responses.GET,
            "https://api.test.com/v1/publications/generation-status/sess_456",
            json=status_response,
            status=200
        )

        result = client.check_generation_status("sess_456")

        assert result.success is True
        assert result.data["status"] == "completed"
        assert result.data["content"] == "Generated content here..."

    @responses.activate
    def test_get_publications(self, client):
        """Test getting publications with pagination"""
        publications_response = {
            "success": True,
            "data": {
                "publications": [
                    {
                        "id": "pub_1",
                        "title": "Test Publication",
                        "content": "Test content",
                        "type": "blog",
                        "status": "published",
                        "contentLength": 100,
                        "imagesCount": 0,
                        "createdAt": "2024-01-01T00:00:00Z",
                        "updatedAt": "2024-01-01T00:00:00Z"
                    }
                ],
                "pagination": {
                    "currentPage": 1,
                    "totalPages": 1,
                    "totalItems": 1,
                    "itemsPerPage": 10
                }
            }
        }

        responses.add(
            responses.GET,
            "https://api.test.com/v1/publications?page=1&limit=10",
            json=publications_response,
            status=200
        )

        result = client.get_publications(page=1, limit=10)

        assert result.success is True
        assert len(result.data["publications"]) == 1
        assert result.data["publications"][0]["title"] == "Test Publication"

    @responses.activate
    def test_wait_for_generation_success(self, client):
        """Test waiting for generation to complete"""
        generating_response = {
            "success": True,
            "data": {
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "generating"
            }
        }

        completed_response = {
            "success": True,
            "data": {
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "completed",
                "content": "Generated content here..."
            }
        }

        responses.add(
            responses.GET,
            "https://api.test.com/v1/publications/generation-status/sess_456",
            json=generating_response,
            status=200
        )
        responses.add(
            responses.GET,
            "https://api.test.com/v1/publications/generation-status/sess_456",
            json=completed_response,
            status=200
        )

        result = client.wait_for_generation("sess_456", max_attempts=2, delay_seconds=0.1)

        assert result.success is True
        assert result.data["status"] == "completed"

    @responses.activate
    def test_wait_for_generation_failure(self, client):
        """Test waiting for generation that fails"""
        failed_response = {
            "success": True,
            "data": {
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "failed"
            }
        }

        responses.add(
            responses.GET,
            "https://api.test.com/v1/publications/generation-status/sess_456",
            json=failed_response,
            status=200
        )

        with pytest.raises(Exception, match="Generation failed"):
            client.wait_for_generation("sess_456", max_attempts=1)

    @responses.activate
    def test_wait_for_generation_timeout(self, client):
        """Test waiting for generation that times out"""
        generating_response = {
            "success": True,
            "data": {
                "publicationId": "pub_123",
                "sessionId": "sess_456",
                "status": "generating"
            }
        }

        responses.add(
            responses.GET,
            "https://api.test.com/v1/publications/generation-status/sess_456",
            json=generating_response,
            status=200
        )

        with pytest.raises(TimeoutError, match="Generation timeout"):
            client.wait_for_generation("sess_456", max_attempts=1)

    @responses.activate
    def test_upload_image(self, client):
        """Test image upload"""
        upload_response = {
            "success": True,
            "data": {
                "image": {
                    "id": "img_123",
                    "filename": "test.jpg",
                    "originalName": "test.jpg",
                    "mimeType": "image/jpeg",
                    "size": 1024,
                    "url": "https://example.com/test.jpg",
                    "createdAt": "2024-01-01T00:00:00Z"
                }
            }
        }

        responses.add(
            responses.POST,
            "https://api.test.com/v1/images/upload",
            json=upload_response,
            status=200
        )

        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value = Mock()
            result = client.upload_image("test.jpg")

        assert result.success is True
        assert result.data["image"]["id"] == "img_123"

    @responses.activate
    def test_get_subscription_status(self, client):
        """Test getting subscription status"""
        subscription_response = {
            "success": True,
            "data": {
                "subscription": {
                    "planName": "Pro",
                    "planSlug": "pro",
                    "price": 29.99,
                    "currency": "USD",
                    "interval": "month",
                    "postsPerMonth": 100,
                    "postsUsed": 25,
                    "postsRemaining": 75,
                    "status": "active",
                    "currentPeriodStart": "2024-01-01T00:00:00Z",
                    "currentPeriodEnd": "2024-02-01T00:00:00Z",
                    "cancelAtPeriodEnd": False,
                    "features": []
                }
            }
        }

        responses.add(
            responses.GET,
            "https://api.test.com/v1/subscription/status",
            json=subscription_response,
            status=200
        )

        result = client.get_subscription_status()

        assert result.success is True
        assert result.data["subscription"]["planName"] == "Pro"
        assert result.data["subscription"]["postsRemaining"] == 75

    @responses.activate
    def test_network_error(self, client):
        """Test handling network errors"""
        responses.add(
            responses.POST,
            "https://api.test.com/v1/publications/generate",
            body=Exception("Network error")
        )

        request = GenerationRequest(prompt="Write about AI")

        with pytest.raises(Exception, match="Request failed: Network error"):
            client.generate_publication(request)

    def test_context_manager(self):
        """Test client as context manager"""
        with ContentGemClient("test_key") as client:
            assert isinstance(client, ContentGemClient)
            # Session should be closed automatically 