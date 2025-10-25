#!/usr/bin/env python3
"""
Test script to verify API connections are working
Run this before running the main enrichment script
"""

import os
import sys
import requests

def test_notion_connection():
    """Test Notion API connection"""
    print("🔍 Testing Notion API connection...")
    
    api_key = os.getenv("NOTION_API_KEY", "")
    if not api_key:
        print("   ❌ NOTION_API_KEY not set")
        return False
    
    database_id = "2932ab6ea09280f19ff4ecca6b020371"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    
    try:
        url = f"https://api.notion.com/v1/databases/{database_id}/query"
        response = requests.post(url, headers=headers, json={"page_size": 1})
        response.raise_for_status()
        
        data = response.json()
        results = data.get("results", [])
        
        print(f"   ✅ Connected! Found {len(data.get('results', []))} entries in database")
        
        if results:
            # Show first word
            props = results[0].get("properties", {})
            title = props.get("Name", {}).get("title", [])
            word = title[0].get("text", {}).get("content", "N/A") if title else "N/A"
            print(f"   📖 Sample word: '{word}'")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection failed: {e}")
        return False


def test_anthropic_connection():
    """Test Anthropic API connection"""
    print("\n🔍 Testing Anthropic API connection...")
    
    api_key = os.getenv("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("   ❌ ANTHROPIC_API_KEY not set")
        return False
    
    headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }
    
    payload = {
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 50,
        "messages": [
            {
                "role": "user",
                "content": "Say 'API connection successful!' in a friendly way."
            }
        ]
    }
    
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=payload,
            timeout=10
        )
        response.raise_for_status()
        
        content = response.json()["content"][0]["text"]
        print(f"   ✅ Connected! Claude says: {content}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Connection failed: {e}")
        return False


def main():
    print("=" * 60)
    print("🧪 API Connection Test")
    print("=" * 60)
    
    notion_ok = test_notion_connection()
    anthropic_ok = test_anthropic_connection()
    
    print("\n" + "=" * 60)
    if notion_ok and anthropic_ok:
        print("✅ All tests passed! You're ready to run the enrichment script.")
        print("\nRun: python vocab_enricher.py")
    else:
        print("❌ Some tests failed. Please check your API keys.")
        if not notion_ok:
            print("\n📝 To fix Notion:")
            print("   1. Get your key from: https://www.notion.so/my-integrations")
            print("   2. Share your database with the integration")
            print("   3. Set: export NOTION_API_KEY='your-key'")
        if not anthropic_ok:
            print("\n📝 To fix Anthropic:")
            print("   1. Get your key from: https://console.anthropic.com/")
            print("   2. Set: export ANTHROPIC_API_KEY='your-key'")
    print("=" * 60)


if __name__ == "__main__":
    main()
