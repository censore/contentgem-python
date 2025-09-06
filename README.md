# GemContent Python SDK

Official Python SDK for the GemContent API v1. This SDK provides a comprehensive interface to interact with GemContent's AI-powered content generation platform.

## Features

- **Content Generation**: Generate AI-powered blog posts and articles
- **Bulk Generation**: Generate multiple publications at once
- **Image Management**: Upload and manage images
- **Company Information**: Manage company profiles and context
- **Subscription Management**: Check subscription status and limits
- **Statistics**: Get detailed usage statistics
- **Type Safety**: Full type hints and data classes
- **Rate Limiting**: Built-in rate limiting handling
- **Error Handling**: Comprehensive error handling and retry logic

## Installation

```bash
pip install gemcontent-python
```

## API Base URL

The default API base URL is `https://gemcontent.com/api/v1`. Make sure you have a valid API key with appropriate permissions for the endpoints you plan to use.

## Quick Start

```python
from gemcontent import GemContentClient, CompanyInfo, ContentPreferences

# Initialize the client
client = GemContentClient(
    api_key="cg_your_api_key_here",
    base_url="https://gemcontent.com/api/v1"  # Updated base URL
)

# Create company information
company_info = CompanyInfo(
    name="Your Company",
    description="Your company description",
    industry="Technology",
    target_audience="Developers",
    content_preferences=ContentPreferences(
        length="medium",
        style="educational",
        include_examples=True,
        include_images=True
    )
)

# Generate content
result = client.generate_publication(
    prompt="Write about AI in business",
    company_info=company_info
)

if result.success:
    session_id = result.session_id

    # Wait for generation to complete
    status = client.wait_for_generation(session_id)

    if status.is_completed:
        print(f"Generated: {status.blog_topic}")
        print(f"Content: {status.content}")
```

## API Reference

### GemContentClient

Main client class for interacting with the GemContent API.

#### Constructor

```python
GemContentClient(
    api_key: str,
    base_url: str = "https://gemcontent.com/api/v1",  # Updated default URL
    timeout: int = 30
)
```

#### Methods

##### Content Generation

- `generate_publication(prompt, company_info=None, keywords=None)` - Generate a single publication
- `bulk_generate_publications(prompts, company_info=None, common_settings=None, keywords=None)` - Generate multiple publications
- `check_generation_status(session_id)` - Check generation status
- `wait_for_generation(session_id, max_attempts=60, delay_seconds=5)` - Wait for generation to complete

##### Publication Management

- `get_publications(page=1, limit=10)` - Get all publications
- `get_publication(publication_id)` - Get specific publication
- `create_publication(data)` - Create new publication
- `update_publication(publication_id, data)` - Update publication
- `delete_publication(publication_id)` - Delete publication
- `publish_publication(publication_id)` - Publish publication
- `archive_publication(publication_id)` - Archive publication
- `download_publication(publication_id, format="pdf")` - Download publication

##### Image Management

- `get_images(page=1, limit=10)` - Get all images
- `get_image(image_id)` - Get specific image
- `upload_image(file_path, publication_id=None)` - Upload image
- `generate_image(prompt, style="realistic", size="1024x1024")` - Generate AI image
- `delete_image(image_id)` - Delete image

##### Company Management

- `get_company_info()` - Get company information
- `update_company_info(company_data)` - Update company information
- `parse_company_website(website_url)` - Parse company website
- `get_company_parsing_status()` - Get parsing status

##### Subscription & Statistics

- `get_subscription_status()` - Get subscription status
- `get_subscription_limits()` - Get subscription limits
- `get_subscription_plans()` - Get available subscription plans
- `get_statistics_overview()` - Get overview statistics
- `get_publication_statistics()` - Get publication statistics
- `get_image_statistics()` - Get image statistics

##### Utility

- `health_check()` - Check API health
- `close()` - Close client session

## Data Models

### CompanyInfo

```python
@dataclass
class CompanyInfo:
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
```

### ContentPreferences

```python
@dataclass
class ContentPreferences:
    length: Optional[str] = None  # short, medium, long
    style: Optional[str] = None  # educational, promotional, technical, etc.
    include_examples: Optional[bool] = None
    include_statistics: Optional[bool] = None
    include_images: Optional[bool] = None
    include_custom_templates: Optional[bool] = None
```

### GenerationResponse

```python
@dataclass
class GenerationResponse:
    success: bool
    data: Optional[Dict[str, Any]] = None
    message: Optional[str] = None
    error: Optional[str] = None

    @property
    def publication_id(self) -> Optional[str]:
        return self.data.get("publicationId") if self.data else None

    @property
    def session_id(self) -> Optional[str]:
        return self.data.get("sessionId") if self.data else None
```

## Examples

### Basic Content Generation

```python
from gemcontent import GemContentClient, CompanyInfo, ContentPreferences

client = GemContentClient(api_key="cg_your_api_key_here")

# Simple generation
result = client.generate_publication(
    prompt="Write about machine learning in healthcare"
)

if result.success:
    status = client.wait_for_generation(result.session_id)
    if status.is_completed:
        print(f"Title: {status.blog_topic}")
        print(f"Content: {status.content}")
```

### Advanced Content Generation with Company Context

```python
from gemcontent import (
    ContentGemClient,
    CompanyInfo,
    ContentPreferences,
    Service,
    Expertise,
    Value,
    SocialMedia
)

client = GemContentClient(api_key="cg_your_api_key_here")

# Detailed company information
company_info = CompanyInfo(
    name="TechCorp Solutions",
    description="Leading AI solutions provider",
    industry="Technology",
    target_audience="Business executives",
    website="https://techcorp.com",
    services=[
        Service(
            name="AI Consulting",
            description="AI implementation consulting"
        )
    ],
    expertise=[
        Expertise(
            area="Machine Learning",
            description="ML algorithms and implementation",
            years_of_experience=5
        )
    ],
    values=[
        Value(
            value="Innovation",
            description="Cutting-edge solutions"
        )
    ],
    mission="Transform businesses with AI",
    vision="AI-first future",
    social_media=SocialMedia(
        linkedin="https://linkedin.com/company/techcorp",
        twitter="https://twitter.com/techcorp"
    ),
    content_preferences=ContentPreferences(
        length="long",
        style="educational",
        include_examples=True,
        include_statistics=True,
        include_images=True
    ),
    tone="professional"
)

# Generate with company context
result = client.generate_publication(
    prompt="Write about AI in business automation",
    company_info=company_info,
    keywords=["AI", "automation", "business", "efficiency"]
)

if result.success:
    status = client.wait_for_generation(result.session_id)
    if status.is_completed:
        print(f"Generated: {status.blog_topic}")
```

### Bulk Generation

```python
from contentgem import ContentGemClient, CompanyInfo

client = GemContentClient(api_key="cg_your_api_key_here")

company_info = CompanyInfo(
    name="Your Company",
    description="Your description",
    industry="Technology"
)

# Bulk generation with correct structure
result = client.bulk_generate_publications(
    prompts=[
        "Write about machine learning",
        "Explain AI in healthcare",
        "Discuss automation benefits"
    ],
    company_info=company_info,
    common_settings={
        "length": "medium",
        "style": "educational",
        "include_examples": True
    },
    keywords=["AI", "technology", "innovation"]
)

if result.success:
    print(f"Started {result.total_prompts} generations")
    print(f"Success: {result.success_count}, Errors: {result.error_count}")
```

### Image Management

```python
from contentgem import ContentGemClient

client = GemContentClient(api_key="cg_your_api_key_here")

# Upload image
upload_result = client.upload_image(
    file_path="/path/to/image.jpg",
    publication_id="publication_id_here"
)

# Generate AI image
generate_result = client.generate_image(
    prompt="Modern office with AI technology",
    style="realistic",
    size="1024x1024"
)

# Get images
images = client.get_images(page=1, limit=10)
if images.success and images.images:
    for image in images.images:
        print(f"Image: {image.filename} - {image.public_url}")
```

### Subscription and Statistics

```python
from contentgem import ContentGemClient

client = GemContentClient(api_key="cg_your_api_key_here")

# Check subscription
subscription = client.get_subscription_status()
if subscription.success and subscription.plan:
    print(f"Plan: {subscription.plan.name}")
    if subscription.usage:
        print(f"Usage: {subscription.usage.posts_used}/{subscription.usage.posts_per_month}")

# Get subscription limits
limits = client.get_subscription_limits()
if limits.success:
    print(f"Current plan: {limits.current_plan}")
    if limits.limits:
        print(f"Publications: {limits.limits.get('publications', {})}")

# Get available plans
plans = client.get_subscription_plans()
if plans.success and plans.get('data', {}).get('plans'):
    for plan in plans['data']['plans']:
        print(f"Plan: {plan['name']} - ${plan['price']}/{plan['interval']}")

# Get statistics
stats = client.get_statistics_overview()
if stats.success:
    if stats.publications:
        print(f"Total publications: {stats.publications.get('total', 0)}")
        print(f"Published: {stats.publications.get('published', 0)}")
        print(f"Draft: {stats.publications.get('draft', 0)}")

    if stats.images:
        print(f"Total images: {stats.images.get('totalImages', 0)}")
```

## Error Handling

The SDK provides comprehensive error handling:

```python
from contentgem import ContentGemClient
from requests.exceptions import RequestException

client = GemContentClient(api_key="cg_your_api_key_here")

try:
    result = client.generate_publication("Write about AI")

    if not result.success:
        print(f"Generation failed: {result.error} - {result.message}")
    else:
        # Process successful result
        pass

except RequestException as e:
    print(f"Request failed: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Rate Limiting

The SDK automatically handles rate limiting. If you hit rate limits, the SDK will raise appropriate exceptions:

```python
from contentgem import ContentGemClient
from requests.exceptions import RequestException

client = GemContentClient(api_key="cg_your_api_key_here")

try:
    # Multiple rapid requests
    for i in range(10):
        result = client.generate_publication(f"Prompt {i}")

except RequestException as e:
    if "rate limit" in str(e).lower():
        print("Rate limit exceeded. Please wait before making more requests.")
    else:
        print(f"Request failed: {e}")
```

## Context Manager

The client supports context manager for automatic resource cleanup:

```python
from contentgem import ContentGemClient

with GemContentClient(api_key="cg_your_api_key_here") as client:
    result = client.generate_publication("Write about AI")
    # Client is automatically closed when exiting the context
```

## API Authentication

The SDK uses API key authentication. Get your API key from the GemContent dashboard:

1. Sign up for GemContent
2. Navigate to API Keys section
3. Create a new API key with appropriate permissions
4. Use the key in your client initialization

### Required Permissions

- `publications:read` - Read publications
- `publications:write` - Create/edit publications
- `publications:generate` - Generate AI content
- `publications:delete` - Delete publications
- `images:read` - Read images
- `images:write` - Upload images
- `images:delete` - Delete images
- `subscription:read` - Read subscription info
- `statistics:read` - Read statistics
- `company:read` - Read company info
- `company:write` - Update company info

## Requirements

- Python 3.7+
- requests >= 2.25.0

## License

MIT License

## Support

For support and questions:

- Documentation / API Reference: https://gemcontent.com/api-documentation
- GitHub Issues: https://github.com/gemcontent/python-sdk/issues
