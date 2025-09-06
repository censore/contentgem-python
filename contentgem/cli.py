#!/usr/bin/env python3
"""
ContentGem CLI

Command-line interface for ContentGem Python SDK.
"""

import argparse
import sys
from typing import Optional

from .client import ContentGemClient


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="ContentGem CLI - Command-line interface for ContentGem API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  contentgem --api-key YOUR_KEY health
  contentgem --api-key YOUR_KEY publications
  contentgem --api-key YOUR_KEY generate "Write about AI"
        """
    )
    
    parser.add_argument(
        "--api-key",
        required=True,
        help="Your ContentGem API key"
    )
    
    parser.add_argument(
        "--base-url",
        default="https://gemcontent.com/api/v1",
        help="API base URL (default: https://gemcontent.com/api/v1)"
    )
    
    parser.add_argument(
        "command",
        choices=["health", "publications", "images", "statistics", "generate"],
        help="Command to execute"
    )
    
    parser.add_argument(
        "args",
        nargs="*",
        help="Additional arguments for the command"
    )
    
    args = parser.parse_args()
    
    try:
        client = ContentGemClient(
            api_key=args.api_key,
            base_url=args.base_url
        )
        
        if args.command == "health":
            health = client.health_check()
            if health.get("success"):
                user_info = health.get('user', {})
                print(f"✅ API is healthy")
                print(f"👤 User: {user_info.get('email', 'Unknown')}")
                print(f"📊 Plan: {user_info.get('plan', 'Unknown')}")
            else:
                print("❌ API health check failed")
                sys.exit(1)
        
        elif args.command == "publications":
            publications = client.get_publications(page=1, limit=10)
            if isinstance(publications, dict) and publications.get("success"):
                publications_data = publications.get("data", {}).get("publications", [])
                if publications_data:
                    print(f"📖 Found {len(publications_data)} publications:")
                    for pub in publications_data:
                        print(f"  - {pub.get('title', 'No title')} ({pub.get('status', 'Unknown')})")
                else:
                    print("📖 No publications found")
            else:
                print("❌ Failed to get publications")
                sys.exit(1)
        
        elif args.command == "images":
            images = client.get_images(page=1, limit=10)
            if isinstance(images, dict) and images.get("success"):
                images_data = images.get("data", {}).get("images", [])
                if images_data:
                    print(f"🖼️ Found {len(images_data)} images:")
                    for img in images_data:
                        print(f"  - {img.get('filename', 'No filename')} ({img.get('size', 0)} bytes)")
                else:
                    print("🖼️ No images found")
            else:
                print("❌ Failed to get images")
                sys.exit(1)
        
        elif args.command == "statistics":
            stats = client.get_statistics_overview()
            if hasattr(stats, 'success') and stats.success:
                if stats.publications:
                    print(f"📰 Publications: {stats.publications.get('total', 0)} total")
                    print(f"  - Published: {stats.publications.get('published', 0)}")
                    print(f"  - Draft: {stats.publications.get('draft', 0)}")
                if stats.images:
                    print(f"🖼️ Images: {stats.images.get('totalImages', 0)} total")
            else:
                print("❌ Failed to get statistics")
                sys.exit(1)
        
        elif args.command == "generate":
            if not args.args:
                print("❌ Please provide a prompt for generation")
                sys.exit(1)
            
            prompt = " ".join(args.args)
            print(f"🤖 Generating content for prompt: {prompt}")
            
            result = client.generate_publication(prompt=prompt)
            if hasattr(result, 'success') and result.success:
                print(f"✅ Generation started. Session ID: {result.session_id}")
            else:
                print(f"❌ Generation failed: {getattr(result, 'message', 'Unknown error')}")
                sys.exit(1)
        
        client.close()
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
