"""
ContentGem Python Client

Main client class for interacting with the ContentGem API.
"""

import time
import requests
from typing import Dict, List, Optional, Any, Union
from requests.exceptions import RequestException

from .types import (
    CompanyInfo,
    GenerationRequest,
    GenerationResponse,
    GenerationStatus,
    Publication,
    Image,
    SubscriptionStatus,
    StatisticsOverview,
    PublicationsResponse,
    ImagesResponse,
    ApiResponse,
    BulkGenerationRequest,
    BulkGenerationResponse,
    BulkGenerationStatus,
    CompanyData,
    CompanyResponse,
    CompanyParsingRequest,
    CompanyParsingResponse,
    CompanyParsingStatus,
)


class ContentGemClient:
    """
    ContentGem API Client
    
    Provides methods to interact with the ContentGem API for content generation,
    publication management, and more.
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://your-domain.com/api/v1",
        timeout: int = 30,
    ):
        """
        Initialize the ContentGem client.
        
        Args:
            api_key: Your ContentGem API key
            base_url: API base URL (default: https://your-domain.com/api/v1)
            timeout: Request timeout in seconds (default: 30)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
        })

    def _make_request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Make HTTP request to the API.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            **kwargs: Additional arguments for requests
            
        Returns:
            API response as dictionary
            
        Raises:
            RequestException: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        
        # Set default timeout
        if "timeout" not in kwargs:
            kwargs["timeout"] = self.timeout
            
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            if hasattr(e, "response") and e.response is not None:
                try:
                    error_data = e.response.json()
                    raise RequestException(
                        f"API Error: {error_data.get('message', str(e))}"
                    )
                except ValueError:
                    raise RequestException(f"HTTP {e.response.status_code}: {e}")
            raise RequestException(f"Request failed: {e}")

    def get_publications(
        self, page: int = 1, limit: int = 10
    ) -> PublicationsResponse:
        """
        Get all publications.
        
        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 10)
            
        Returns:
            Publications response
        """
        params = {"page": page, "limit": limit}
        return self._make_request("GET", "/publications", params=params)

    def get_publication(self, publication_id: str) -> ApiResponse:
        """
        Get specific publication.
        
        Args:
            publication_id: Publication ID
            
        Returns:
            Publication data
        """
        return self._make_request("GET", f"/publications/{publication_id}")

    def create_publication(self, data: Dict[str, Any]) -> ApiResponse:
        """
        Create new publication.
        
        Args:
            data: Publication data
            
        Returns:
            Created publication
        """
        return self._make_request("POST", "/publications", json=data)

    def generate_publication(
        self,
        prompt: str,
        company_info: Optional[Union[CompanyInfo, Dict[str, Any]]] = None,
        keywords: Optional[List[str]] = None,
    ) -> GenerationResponse:
        """
        Generate new publication.
        
        Args:
            prompt: Generation prompt
            company_info: Company information
            keywords: Keywords for generation
            
        Returns:
            Generation response
        """
        request_data = {"prompt": prompt}
        
        if company_info:
            if isinstance(company_info, CompanyInfo):
                request_data["company_info"] = company_info.to_dict()
            else:
                request_data["company_info"] = company_info
                
        if keywords:
            request_data["keywords"] = keywords
            
        response = self._make_request("POST", "/publications/generate", json=request_data)
        return GenerationResponse(**response)

    def check_generation_status(self, session_id: str) -> GenerationStatus:
        """
        Check generation status.
        
        Args:
            session_id: Generation session ID
            
        Returns:
            Generation status
        """
        response = self._make_request("GET", f"/publications/generation-status/{session_id}")
        return GenerationStatus(**response)

    def wait_for_generation(
        self,
        session_id: str,
        max_attempts: int = 60,
        delay_seconds: int = 5,
    ) -> GenerationStatus:
        """
        Wait for generation to complete.
        
        Args:
            session_id: Generation session ID
            max_attempts: Maximum polling attempts
            delay_seconds: Delay between attempts
            
        Returns:
            Final generation status
            
        Raises:
            TimeoutError: If generation doesn't complete within max_attempts
        """
        for attempt in range(max_attempts):
            status = self.check_generation_status(session_id)
            
            if status.is_completed:
                return status
                
            if status.is_failed:
                raise RequestException("Generation failed")
                
            if attempt < max_attempts - 1:
                time.sleep(delay_seconds)
                
        raise TimeoutError("Generation timeout")

    def update_publication(
        self, publication_id: str, data: Dict[str, Any]
    ) -> ApiResponse:
        """
        Update publication.
        
        Args:
            publication_id: Publication ID
            data: Update data
            
        Returns:
            Updated publication
        """
        return self._make_request("PUT", f"/publications/{publication_id}", json=data)

    def delete_publication(self, publication_id: str) -> ApiResponse:
        """
        Delete publication.
        
        Args:
            publication_id: Publication ID
            
        Returns:
            Deletion response
        """
        return self._make_request("DELETE", f"/publications/{publication_id}")

    def publish_publication(self, publication_id: str) -> ApiResponse:
        """
        Publish publication.
        
        Args:
            publication_id: Publication ID
            
        Returns:
            Publish response
        """
        return self._make_request("POST", f"/publications/{publication_id}/publish")

    def archive_publication(self, publication_id: str) -> ApiResponse:
        """
        Archive publication.
        
        Args:
            publication_id: Publication ID
            
        Returns:
            Archive response
        """
        return self._make_request("POST", f"/publications/{publication_id}/archive")

    def download_publication(
        self, publication_id: str, format: str = "pdf"
    ) -> ApiResponse:
        """
        Download publication.
        
        Args:
            publication_id: Publication ID
            format: Download format (pdf, docx, html, markdown)
            
        Returns:
            Download response
        """
        return self._make_request(
            "POST", f"/publications/{publication_id}/download", json={"format": format}
        )

    def get_images(self, page: int = 1, limit: int = 10) -> ImagesResponse:
        """
        Get all images.
        
        Args:
            page: Page number (default: 1)
            limit: Items per page (default: 10)
            
        Returns:
            Images response
        """
        params = {"page": page, "limit": limit}
        return self._make_request("GET", "/images", params=params)

    def get_image(self, image_id: str) -> ApiResponse:
        """
        Get specific image.
        
        Args:
            image_id: Image ID
            
        Returns:
            Image data
        """
        return self._make_request("GET", f"/images/{image_id}")

    def upload_image(
        self, file_path: str, publication_id: Optional[str] = None
    ) -> ApiResponse:
        """
        Upload image.
        
        Args:
            file_path: Path to image file
            publication_id: Optional publication ID to associate with
            
        Returns:
            Upload response
        """
        with open(file_path, "rb") as f:
            files = {"image": f}
            data = {}
            if publication_id:
                data["publicationId"] = publication_id
                
            # Remove Content-Type header for multipart request
            headers = {"X-API-Key": self.api_key}
            
            return self._make_request(
                "POST", "/images/upload", files=files, data=data, headers=headers
            )

    def generate_image(
        self, prompt: str, style: str = "realistic", size: str = "1024x1024"
    ) -> ApiResponse:
        """
        Generate AI image.
        
        Args:
            prompt: Image generation prompt
            style: Image style
            size: Image size
            
        Returns:
            Generation response
        """
        data = {"prompt": prompt, "style": style, "size": size}
        return self._make_request("POST", "/images/generate", json=data)

    def delete_image(self, image_id: str) -> ApiResponse:
        """
        Delete image.
        
        Args:
            image_id: Image ID
            
        Returns:
            Deletion response
        """
        return self._make_request("DELETE", f"/images/{image_id}")

    def get_subscription_status(self) -> SubscriptionStatus:
        """
        Get subscription status.
        
        Returns:
            Subscription status
        """
        response = self._make_request("GET", "/subscription/status")
        return SubscriptionStatus(**response)

    def get_subscription_limits(self) -> ApiResponse:
        """
        Get subscription limits.
        
        Returns:
            Subscription limits
        """
        return self._make_request("GET", "/subscription/limits")

    def get_subscription_plans(self) -> ApiResponse:
        """
        Get available plans.
        
        Returns:
            Available plans
        """
        return self._make_request("GET", "/subscription/plans")

    def get_statistics_overview(self) -> StatisticsOverview:
        """
        Get overview statistics.
        
        Returns:
            Statistics overview
        """
        response = self._make_request("GET", "/statistics/overview")
        return StatisticsOverview(**response)

    def get_publication_statistics(self) -> ApiResponse:
        """
        Get publication statistics.
        
        Returns:
            Publication statistics
        """
        return self._make_request("GET", "/statistics/publications")

    def get_image_statistics(self) -> ApiResponse:
        """
        Get image statistics.
        
        Returns:
            Image statistics
        """
        return self._make_request("GET", "/statistics/images")

    def bulk_generate_publications(
        self, request: BulkGenerationRequest
    ) -> BulkGenerationResponse:
        """
        Bulk generate multiple publications.
        
        Args:
            request: Bulk generation request
            
        Returns:
            Bulk generation response
        """
        response = self._make_request("POST", "/publications/bulk-generate", json=request.to_dict())
        return BulkGenerationResponse(**response)

    def check_bulk_generation_status(self, bulk_session_id: str) -> BulkGenerationStatus:
        """
        Check bulk generation status.
        
        Args:
            bulk_session_id: Bulk session ID
            
        Returns:
            Bulk generation status
        """
        response = self._make_request("POST", "/publications/bulk-status", json={"bulk_session_id": bulk_session_id})
        return BulkGenerationStatus(**response)

    def get_company_info(self) -> CompanyResponse:
        """
        Get company information.
        
        Returns:
            Company information
        """
        response = self._make_request("GET", "/company")
        return CompanyResponse(**response)

    def update_company_info(self, company_data: CompanyData) -> CompanyResponse:
        """
        Update company information.
        
        Args:
            company_data: Company data to update
            
        Returns:
            Update response
        """
        response = self._make_request("PUT", "/company", json=company_data.to_dict())
        return CompanyResponse(**response)

    def parse_company_website(self, website_url: str) -> CompanyParsingResponse:
        """
        Parse company website.
        
        Args:
            website_url: Website URL to parse
            
        Returns:
            Parsing response
        """
        request = CompanyParsingRequest(website_url=website_url)
        response = self._make_request("POST", "/company/parse", json=request.to_dict())
        return CompanyParsingResponse(**response)

    def get_company_parsing_status(self) -> CompanyParsingStatus:
        """
        Get company parsing status.
        
        Returns:
            Parsing status
        """
        response = self._make_request("GET", "/company/parsing-status")
        return CompanyParsingStatus(**response)

    def wait_for_bulk_generation(
        self, bulk_session_id: str, max_attempts: int = 120, delay_seconds: int = 10
    ) -> BulkGenerationStatus:
        """
        Wait for bulk generation to complete.
        
        Args:
            bulk_session_id: Bulk session ID
            max_attempts: Maximum number of attempts
            delay_seconds: Delay between attempts in seconds
            
        Returns:
            Final bulk generation status
            
        Raises:
            TimeoutError: If generation times out
        """
        for attempt in range(max_attempts):
            status = self.check_bulk_generation_status(bulk_session_id)
            
            if status.is_completed:
                return status
                
            if status.is_failed:
                raise Exception("Bulk generation failed")
                
            if attempt < max_attempts - 1:
                time.sleep(delay_seconds)
                
        raise TimeoutError("Bulk generation timeout")

    def health_check(self) -> ApiResponse:
        """
        Health check.
        
        Returns:
            Health status
        """
        return self._make_request("GET", "/health")

    def close(self):
        """Close the client session."""
        self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close() 