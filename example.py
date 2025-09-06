#!/usr/bin/env python3
"""
ContentGem Python SDK Example

This example demonstrates how to use the ContentGem Python SDK
to interact with all available API endpoints.

Usage:
    python example.py --api-key YOUR_API_KEY [--action ACTION] [--base-url URL]

Actions:
    health          - Check API health
    subscription    - Get subscription status and limits
    generate        - Generate a single publication
    bulk            - Generate multiple publications
    publications    - List publications
    publication     - Get specific publication details
    images          - List images
    upload-image    - Upload an image
    company         - Get company information
    update-company  - Update company information
    statistics      - Get statistics overview
    plans           - Get subscription plans
    limits          - Get subscription limits
    all             - Run all examples (default)
"""

import argparse
import sys
import time
from typing import Optional, List, Dict, Any

from contentgem import (
    ContentGemClient, 
    CompanyInfo, 
    ContentPreferences, 
    Service,
    Expertise,
    Value,
    SocialMedia
)


def create_sample_company_info() -> CompanyInfo:
    """Create sample company information for testing."""
    return CompanyInfo(
        name="TechCorp Solutions",
        description="Leading technology solutions provider specializing in AI and automation",
        industry="Technology",
        target_audience="Business executives and IT professionals",
        website="https://techcorp-solutions.com",
        services=[
            Service(
                name="AI Consulting",
                description="Consulting on AI implementation in business processes"
            ),
            Service(
                name="Automation Solutions",
                description="Custom automation solutions for enterprise clients"
            )
        ],
        expertise=[
            Expertise(
                area="Machine Learning",
                description="Specialization in machine learning algorithms and implementation",
                years_of_experience=5
            ),
            Expertise(
                area="Business Process Automation",
                description="Expertise in automating complex business workflows",
                years_of_experience=8
            )
        ],
        values=[
            Value(
                value="Innovation",
                description="Constant pursuit of innovation and cutting-edge solutions"
            ),
            Value(
                value="Quality",
                description="Commitment to delivering high-quality solutions"
            )
        ],
        mission="Help businesses grow with advanced technologies",
        vision="Become a leader in technology solutions and AI implementation",
        social_media=SocialMedia(
            linkedin="https://linkedin.com/company/techcorp-solutions",
            twitter="https://twitter.com/techcorp_sol"
        ),
        content_preferences=ContentPreferences(
            length="long",
            style="educational",
            include_examples=True,
            include_statistics=True,
            include_images=True,
            include_custom_templates=False
        ),
        tone="professional"
    )
    

def health_check_example(client: ContentGemClient) -> None:
    """Example: Health check."""
    print("🔍 Checking API health...")
    try:
        health = client.health_check()
        if health.get("success"):
            user_info = health.get('user', {})
            print(f"✅ API is healthy")
            print(f"👤 User: {user_info.get('email', 'Unknown')}")
            print(f"📊 Plan: {user_info.get('plan', 'Unknown')}")
            print(f"🆔 User ID: {user_info.get('id', 'Unknown')}")
        else:
            print("❌ API health check failed")
    except Exception as e:
        print(f"❌ Health check error: {str(e)}")


def subscription_example(client: ContentGemClient) -> None:
    """Example: Get subscription status."""
    print("\n📋 Getting subscription status...")
    try:
        subscription = client.get_subscription_status()
        if hasattr(subscription, 'success'):
            if subscription.success:
                if subscription.plan:
                    print(f"📦 Plan: {subscription.plan.name}")
                    print(f"💰 Price: ${subscription.plan.price}/month")
                    print(f"📝 Posts per month: {subscription.plan.posts_per_month}")
                
                if subscription.usage:
                    print(f"📈 Usage: {subscription.usage.posts_used}/{subscription.usage.posts_per_month} posts used")
                    print(f"📉 Remaining: {subscription.usage.posts_remaining} posts")
                    print(f"📅 Reset date: {subscription.usage.reset_date}")
            else:
                print(f"❌ Failed to get subscription status: {subscription.message or 'Unknown error'}")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Subscription error: {str(e)}")


def generate_publication_example(client: ContentGemClient) -> None:
    """Example: Generate a single publication."""
    print("\n🤖 Generating single publication...")
    try:
        company_info = create_sample_company_info()
        
        result = client.generate_publication(
            prompt="Write a comprehensive article about the importance of artificial intelligence in modern business operations, including real-world examples and statistics",
            company_info=company_info,
            keywords=["artificial intelligence", "business automation", "machine learning", "digital transformation"]
        )
        
        if result.success:
            session_id = result.session_id
            print(f"✅ Generation started. Session ID: {session_id}")
            
            # Wait for generation to complete
            print("⏳ Waiting for generation to complete...")
            status = client.wait_for_generation(session_id, max_attempts=60, delay_seconds=5)
            
            if status.is_completed:
                print("🎉 Generation completed successfully!")
                print(f"📝 Blog Topic: {status.blog_topic}")
                print(f"📄 Content Length: {len(status.content) if status.content else 0} characters")
                
                if status.content:
                    # Show first 200 characters of content
                    preview = status.content[:200] + "..." if len(status.content) > 200 else status.content
                    print(f"📖 Content Preview: {preview}")
                
                # Get publication details
                if result.publication_id:
                    print(f"\n📚 Getting publication details...")
                    publication = client.get_publication(result.publication_id)
                    if hasattr(publication, 'title'):
                        print(f"📰 Title: {publication.title}")
                        print(f"🏷️ Type: {publication.type}")
                        print(f"📊 Status: {publication.status}")
                        print(f"⭐ Quality Score: {publication.quality_score}")
                        print(f"🖼️ Images Count: {publication.images_count}")
            else:
                print("❌ Generation failed or timed out")
        else:
            print(f"❌ Generation failed: {result.error} - {result.message}")
    except Exception as e:
        print(f"❌ Generation error: {str(e)}")


def bulk_generation_example(client: ContentGemClient) -> None:
    """Example: Bulk generation."""
    print("\n🚀 Bulk generation example...")
    try:
        company_info = create_sample_company_info()
        
        bulk_result = client.bulk_generate_publications(
            prompts=[
                "Write about machine learning fundamentals",
                "Explain the benefits of business process automation",
                "Discuss the future of AI in healthcare"
            ],
            company_info=company_info,
            common_settings={
                "length": "medium",
                "style": "educational",
                "include_examples": True
            },
            keywords=["technology", "innovation", "digital transformation"]
        )
        
        if bulk_result.success:
            print(f"✅ Bulk generation started. Total prompts: {bulk_result.total_prompts}")
            print(f"📊 Success count: {bulk_result.success_count}, Error count: {bulk_result.error_count}")
            
            if bulk_result.publications:
                print("📝 Generated publications:")
                for pub in bulk_result.publications:
                    print(f"  - ID: {pub.get('id')}, Session: {pub.get('sessionId')}")
        else:
            print(f"❌ Bulk generation failed: {bulk_result.error} - {bulk_result.message}")
    except Exception as e:
        print(f"❌ Bulk generation error: {str(e)}")

        
def publications_list_example(client: ContentGemClient) -> None:
    """Example: List publications."""
    print("\n📚 Getting publications list...")
    try:
        publications = client.get_publications(page=1, limit=5)
        if isinstance(publications, dict):
            if publications.get("success"):
                publications_data = publications.get("data", {}).get("publications", [])
                if publications_data:
                    print(f"📖 Found {len(publications_data)} publications:")
                    for pub in publications_data:
                        print(f"  - {pub.get('title', 'No title')} ({pub.get('status', 'Unknown')}) - {pub.get('type', 'Unknown')}")
                        print(f"    ID: {pub.get('id', 'Unknown')}, Created: {pub.get('created_at', 'Unknown')}")
                else:
                    print("📖 No publications found")
            else:
                print(f"❌ Failed to get publications list: {publications.get('message', 'Unknown error')}")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Publications list error: {str(e)}")


def publication_details_example(client: ContentGemClient, publication_id: Optional[str] = None) -> None:
    """Example: Get specific publication details."""
    if not publication_id:
        print("\n📰 Getting publication details (requires publication ID)...")
        print("❌ No publication ID provided. Skipping this example.")
        return
    
    print(f"\n📰 Getting publication details for ID: {publication_id}")
    try:
        publication = client.get_publication(publication_id)
        if hasattr(publication, 'title'):
            print(f"📰 Title: {publication.title}")
            print(f"🏷️ Type: {publication.type}")
            print(f"📊 Status: {publication.status}")
            print(f"⭐ Quality Score: {publication.quality_score}")
            print(f"🖼️ Images Count: {publication.images_count}")
            print(f"📅 Created: {publication.created_at}")
            print(f"📝 Content Length: {len(publication.content) if publication.content else 0} characters")
        else:
            print("❌ Failed to get publication details")
    except Exception as e:
        print(f"❌ Publication details error: {str(e)}")


def images_list_example(client: ContentGemClient) -> None:
    """Example: List images."""
    print("\n🖼️ Getting images list...")
    try:
        images = client.get_images(page=1, limit=5)
        if isinstance(images, dict):
            if images.get("success"):
                images_data = images.get("data", {}).get("images", [])
                if images_data:
                    print(f"🖼️ Found {len(images_data)} images:")
                    for img in images_data:
                        print(f"  - {img.get('filename', 'No filename')} ({img.get('size', 0)} bytes)")
                        print(f"    ID: {img.get('id', 'Unknown')}, Created: {img.get('created_at', 'Unknown')}")
                else:
                    print("🖼️ No images found")
            else:
                print(f"❌ Failed to get images list: {images.get('message', 'Unknown error')}")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Images list error: {str(e)}")


def upload_image_example(client: ContentGemClient, image_path: Optional[str] = None) -> None:
    """Example: Upload an image."""
    if not image_path:
        print("\n📤 Upload image example (requires image path)...")
        print("❌ No image path provided. Skipping this example.")
        return
    
    print(f"\n📤 Uploading image: {image_path}")
    try:
        with open(image_path, 'rb') as f:
            image_data = f.read()
        
        result = client.upload_image(image_data, "test_image.jpg")
        if result.success:
            print(f"✅ Image uploaded successfully. ID: {result.image_id}")
        else:
            print(f"❌ Image upload failed: {result.error} - {result.message}")
    except Exception as e:
        print(f"❌ Image upload error: {str(e)}")


def company_info_example(client: ContentGemClient) -> None:
    """Example: Get company information."""
    print("\n🏢 Getting company information...")
    try:
        company = client.get_company_info()
        if isinstance(company, dict):
            if company.get("success"):
                company_data = company.get("data", {}).get("company", {})
                if company_data:
                    print(f"🏢 Company: {company_data.get('name', 'Unknown')}")
                    print(f"📝 Description: {company_data.get('description', 'No description')}")
                    print(f"🏭 Industry: {company_data.get('industry', 'Unknown')}")
                    print(f"🎯 Target Audience: {company_data.get('target_audience', 'Unknown')}")
                    print(f"🌐 Website: {company_data.get('website', 'No website')}")
                else:
                    print("🏢 No company information found")
            else:
                print(f"❌ Failed to get company information: {company.get('message', 'Unknown error')}")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Company info error: {str(e)}")


def update_company_example(client: ContentGemClient) -> None:
    """Example: Update company information."""
    print("\n✏️ Updating company information...")
    try:
        company_info = create_sample_company_info()
        company_info.name = "Updated TechCorp Solutions"
        company_info.description = "Updated description for testing purposes"
        
        result = client.update_company_info(company_info)
        if result.success:
            print("✅ Company information updated successfully")
        else:
            print(f"❌ Company update failed: {result.error} - {result.message}")
    except Exception as e:
        print(f"❌ Company update error: {str(e)}")


def statistics_example(client: ContentGemClient) -> None:
    """Example: Get statistics overview."""
    print("\n📊 Getting statistics overview...")
    try:
        stats = client.get_statistics_overview()
        if hasattr(stats, 'success'):
            if stats.success:
                if stats.publications:
                    print(f"📰 Publications: {stats.publications.get('total', 0)} total")
                    print(f"  - Published: {stats.publications.get('published', 0)}")
                    print(f"  - Draft: {stats.publications.get('draft', 0)}")
                    print(f"  - This month: {stats.publications.get('thisMonth', 0)}")
                
                if stats.images:
                    print(f"🖼️ Images: {stats.images.get('totalImages', 0)} total")
                    print(f"  - Total size: {stats.images.get('totalSize', 0)} bytes")
                
                if stats.user_limits:
                    print(f"📈 Usage: {stats.user_limits.get('postsUsed', 0)}/{stats.user_limits.get('postsPerMonth', 0)} posts used")
            else:
                print(f"❌ Failed to get statistics: {stats.message or 'Unknown error'}")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Statistics error: {str(e)}")


def subscription_plans_example(client: ContentGemClient) -> None:
    """Example: Get subscription plans."""
    print("\n📦 Getting subscription plans...")
    try:
        plans = client.get_subscription_plans()
        if isinstance(plans, dict):
            if plans.get("success"):
                plans_data = plans.get("data", [])
                if plans_data:
                    print(f"📦 Found {len(plans_data)} subscription plans:")
                    for plan in plans_data:
                        print(f"  - {plan.get('name', 'Unknown')}: ${plan.get('price', 0)/100}/month")
                        print(f"    Posts per month: {plan.get('postsPerMonth', 0)}")
                        features = plan.get('features', [])
                        feature_names = [f.get('name', 'Unknown') for f in features if isinstance(f, dict)]
                        print(f"    Features: {', '.join(feature_names) if feature_names else 'None'}")
                else:
                    print("📦 No subscription plans found")
            else:
                print(f"❌ Failed to get subscription plans: {plans.get('message', 'Unknown error')}")
        elif isinstance(plans, list):
            # Handle case where API returns list directly
            if plans:
                print(f"📦 Found {len(plans)} subscription plans:")
                for plan in plans:
                    if isinstance(plan, dict):
                        print(f"  - {plan.get('name', 'Unknown')}: ${plan.get('price', 0)}/month")
                        print(f"    Posts per month: {plan.get('posts_per_month', 0)}")
                        features = plan.get('features', [])
                        print(f"    Features: {', '.join(features) if features else 'None'}")
                    else:
                        print(f"  - {plan}")
            else:
                print("📦 No subscription plans found")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Subscription plans error: {str(e)}")


def subscription_limits_example(client: ContentGemClient) -> None:
    """Example: Get subscription limits."""
    print("\n📊 Getting subscription limits...")
    try:
        limits = client.get_subscription_limits()
        if isinstance(limits, dict):
            if limits.get("success"):
                limits_data = limits.get("data", {}).get("limits", {})
                if limits_data:
                    print(f"📊 Current limits:")
                    print(f"  - Posts per month: {limits_data.get('posts_per_month', 'Unknown')}")
                    print(f"  - Images per month: {limits_data.get('images_per_month', 'Unknown')}")
                    print(f"  - Max content length: {limits_data.get('max_content_length', 'Unknown')}")
                else:
                    print("📊 No limits data found")
            else:
                print(f"❌ Failed to get subscription limits: {limits.get('message', 'Unknown error')}")
        else:
            print("❌ Unexpected response format")
    except Exception as e:
        print(f"❌ Subscription limits error: {str(e)}")


def run_all_examples(client: ContentGemClient) -> None:
    """Run all examples."""
    print("🚀 Running all ContentGem API examples...\n")
    
    # Basic operations
    health_check_example(client)
    subscription_example(client)
    
    # Content generation
    generate_publication_example(client)
    bulk_generation_example(client)
    
    # Data retrieval
    publications_list_example(client)
    images_list_example(client)
    company_info_example(client)
    
    # Statistics and plans
    statistics_example(client)
    subscription_plans_example(client)
    subscription_limits_example(client)
    
    print("\n✅ All examples completed!")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description="ContentGem Python SDK Example",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    
    parser.add_argument(
        "--api-key",
        required=True,
        help="Your ContentGem API key"
    )
    
    parser.add_argument(
        "--action",
        choices=[
            "health", "subscription", "generate", "bulk", "publications", 
            "publication", "images", "upload-image", "company", "update-company",
            "statistics", "plans", "limits", "all"
        ],
        default="all",
        help="Action to perform (default: all)"
    )
    
    parser.add_argument(
        "--base-url",
        default="https://gemcontent.com/api/v1",
        help="API base URL (default: https://gemcontent.com/api/v1)"
    )
    
    parser.add_argument(
        "--publication-id",
        help="Publication ID for publication details example"
    )
    
    parser.add_argument(
        "--image-path",
        help="Path to image file for upload example"
    )
    
    args = parser.parse_args()
    
    # Initialize the client
    try:
        client = ContentGemClient(
            api_key=args.api_key,
            base_url=args.base_url
        )
        print(f"🔗 Connected to ContentGem API at {args.base_url}")
    except Exception as e:
        print(f"❌ Failed to initialize client: {str(e)}")
        sys.exit(1)
    
    try:
        # Run the selected action
        if args.action == "health":
            health_check_example(client)
        elif args.action == "subscription":
            subscription_example(client)
        elif args.action == "generate":
            generate_publication_example(client)
        elif args.action == "bulk":
            bulk_generation_example(client)
        elif args.action == "publications":
            publications_list_example(client)
        elif args.action == "publication":
            publication_details_example(client, args.publication_id)
        elif args.action == "images":
            images_list_example(client)
        elif args.action == "upload-image":
            upload_image_example(client, args.image_path)
        elif args.action == "company":
            company_info_example(client)
        elif args.action == "update-company":
            update_company_example(client)
        elif args.action == "statistics":
            statistics_example(client)
        elif args.action == "plans":
            subscription_plans_example(client)
        elif args.action == "limits":
            subscription_limits_example(client)
        elif args.action == "all":
            run_all_examples(client)
        
    except KeyboardInterrupt:
        print("\n⏹️ Interrupted by user")
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
    finally:
        # Close the client
        client.close()
        print("\n👋 Client closed. Goodbye!")


if __name__ == "__main__":
    main()