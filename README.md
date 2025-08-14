# ContentGem Python SDK

Official Python SDK for the ContentGem API.

## Installation

```bash
pip install contentgem-python
```

## Quick Start

```python
from contentgem import ContentGemClient, CompanyInfo

# Initialize client
client = ContentGemClient(
    api_key="cg_your_api_key_here",
    base_url="https://your-domain.com/api/v1"  # optional
)

# Generate content
company_info = CompanyInfo(
    name="TechCorp",
    description="Leading technology solutions provider",
    industry="Technology"
)

result = client.generate_publication(
    prompt="Write about AI in business",
    company_info=company_info
)

if result.success:
    session_id = result.session_id

    # Wait for generation to complete
    status = client.wait_for_generation(session_id)

    if status.is_completed:
        print("Generated content:", status.content)
```

## Features

- ✅ **Full type hints** with complete type definitions
- ✅ **All API endpoints** covered
- ✅ **Error handling** with detailed error messages
- ✅ **Context manager** support (`with` statement)
- ✅ **Automatic polling** with `wait_for_generation()`
- ✅ **Dataclass models** for easy data handling
- ✅ **Session management** for efficient requests
- ✅ **Bulk generation** support for multiple publications
- ✅ **Company management** with website parsing
- ✅ **Real-time status tracking** for all operations

## API Reference

### Constructor

```python
ContentGemClient(api_key, base_url="https://your-domain.com/api/v1", timeout=30)
```

**Parameters:**

- `api_key` (str): Your ContentGem API key
- `base_url` (str, optional): API base URL
- `timeout` (int, optional): Request timeout in seconds

### Publications

```python
# Get all publications
publications = client.get_publications(page=1, limit=10)

# Get specific publication
publication = client.get_publication(publication_id)

# Create publication
new_pub = client.create_publication(data)

# Generate content
result = client.generate_publication(
    prompt="Your prompt here",
    company_info=company_info
)

# Check generation status
status = client.check_generation_status(session_id)

# Wait for generation to complete
completed = client.wait_for_generation(session_id)

# Update publication
client.update_publication(publication_id, data)

# Delete publication
client.delete_publication(publication_id)

# Publish/Archive
client.publish_publication(publication_id)
client.archive_publication(publication_id)

# Download
client.download_publication(publication_id, "pdf")
```

### Bulk Generation

```python
from contentgem import BulkGenerationRequest

# Bulk generate multiple publications
bulk_request = BulkGenerationRequest(
    prompts=[
        'Write about AI in business',
        'Explain machine learning basics',
        'Discuss the future of automation'
    ],
    company_info=company_info,
    common_settings={
        'length': 'medium',
        'style': 'educational'
    }
)

bulk_result = client.bulk_generate_publications(bulk_request)

# Check bulk generation status
bulk_status = client.check_bulk_generation_status(bulk_session_id)

# Wait for bulk generation to complete
completed_bulk = client.wait_for_bulk_generation(bulk_session_id)
```

### Company Management

```python
from contentgem import CompanyData

# Get company information
company_info = client.get_company_info()

# Update company information
company_data = CompanyData(
    name='Updated Company Name',
    description='Updated description',
    website='https://example.com',
    contact_email='contact@example.com'
)
client.update_company_info(company_data)

# Parse company website
parsing_result = client.parse_company_website('https://example.com')

# Get parsing status
parsing_status = client.get_company_parsing_status()
```

### Images

```python
# Get all images
images = client.get_images(page=1, limit=10)

# Get specific image
image = client.get_image(image_id)

# Upload image
uploaded = client.upload_image(file_path, publication_id)

# Generate AI image
generated = client.generate_image(prompt, style, size)

# Delete image
client.delete_image(image_id)
```

### Subscription & Statistics

```python
# Subscription
status = client.get_subscription_status()
limits = client.get_subscription_limits()
plans = client.get_subscription_plans()

# Statistics
overview = client.get_statistics_overview()
pub_stats = client.get_publication_statistics()
img_stats = client.get_image_statistics()
```

## Data Models

### CompanyInfo

```python
from contentgem import CompanyInfo

company_info = CompanyInfo(
    name="My Company",
    description="Technology company",
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
```

### GenerationRequest

```python
from contentgem import GenerationRequest, CompanyInfo

request = GenerationRequest(
    prompt="Write about AI in business",
    company_info=CompanyInfo(name="TechCorp"),
    keywords=["AI", "business", "automation"]
)
```

## Error Handling

```python
try:
    result = client.generate_publication(
        prompt="Test prompt"
    )

    if result.success:
        print("Success:", result.data)
    else:
        print("API Error:", result.error, result.message)

except requests.exceptions.RequestException as e:
    print("Network Error:", str(e))
```

## Context Manager

```python
with ContentGemClient(api_key="your_key") as client:
    result = client.generate_publication(prompt="Test")
    # Session automatically closed
```

## Development

```bash
# Clone repository
git clone https://github.com/contentgem/contentgem-python.git
cd contentgem-python

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black contentgem/

# Lint
flake8 contentgem/

# Type check
mypy contentgem/
```

## License

MIT License
