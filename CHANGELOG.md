# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- N/A

### Changed

- N/A

### Deprecated

- N/A

### Removed

- N/A

### Fixed

- N/A

### Security

- N/A

## [1.1.0] - 2024-01-15

### Added

- **Bulk content generation** support with `bulk_generate_publications()` and `wait_for_bulk_generation()`
- **Enhanced CompanyInfo model** with detailed company information including services, expertise, values, mission, vision, and social media
- **ContentPreferences model** for granular content generation settings
- **Company website parsing** functionality with `parse_company_website()` and `get_company_parsing_status()`
- **Advanced filtering** for publications and images with type, status, and search parameters
- **Rich response models** including `PublicationsResponse`, `ImagesResponse`, `SubscriptionLimits`, and more
- **Enhanced error handling** with detailed error codes and messages
- **Comprehensive statistics** support with detailed breakdowns
- **Health check endpoint** with user information and limits
- **New data models**: `Service`, `Expertise`, `Value`, `SocialMedia`, `ContentPreferences`, `BulkGenerationRequest`, `BulkGenerationResponse`, `BulkGenerationStatus`, `PublicationImage`, `GenerationMetadata`, `ImageDimensions`, `Plan`, `Usage`, `PlanFeature`, `SubscriptionPlan`, `SubscriptionLimits`, `Pagination`
- **Updated base URL** to `https://gemcontent.com/api/v1`
- **Example script** demonstrating all new features

### Changed

- **Breaking**: Updated base URL from `https://your-domain.com/api/v1` to `https://gemcontent.com/api/v1`
- **Enhanced**: `get_publications()` now supports filtering by type and status
- **Enhanced**: `get_images()` now supports filtering by publication ID and search terms
- **Enhanced**: `get_publication()` and `get_image()` now return typed objects instead of raw dictionaries
- **Enhanced**: Error messages now include error codes for better debugging
- **Enhanced**: All response models now have proper type hints and properties

### Deprecated

- N/A

### Removed

- N/A

### Fixed

- Improved error handling with better error code extraction
- Fixed type annotations for better IDE support
- Enhanced documentation with comprehensive examples

### Security

- N/A

## [1.0.0] - 2024-01-01

### Added

- Initial release of ContentGem Python SDK
- Support for all ContentGem API endpoints
- Type hints and dataclass models
- Comprehensive error handling
- Context manager support
- Session management
