#!/usr/bin/env python3
"""
Elshan's Living Lexicon - AI Vocabulary Enrichment Tool
Automatically enriches vocabulary entries with contextual definitions and examples
using Claude AI, tailored for design and creative contexts.
"""

import os
import sys
import time
from typing import List, Dict, Optional
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
NOTION_DATABASE_ID = "2932ab6ea09280f19ff4ecca6b020371"
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")

# API Endpoints
NOTION_API_VERSION = "2022-06-28"
NOTION_BASE_URL = "https://api.notion.com/v1"
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"


class NotionClient:
    """Handle all Notion API interactions"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Notion-Version": NOTION_API_VERSION,
            "Content-Type": "application/json"
        }
    
    def query_database(self, database_id: str, filter_params: Optional[Dict] = None) -> List[Dict]:
        """Query Notion database with optional filters"""
        url = f"{NOTION_BASE_URL}/databases/{database_id}/query"
        
        payload = {}
        if filter_params:
            payload["filter"] = filter_params
        
        try:
            response = requests.post(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json().get("results", [])
        except requests.exceptions.RequestException as e:
            print(f"❌ Error querying Notion database: {e}")
            return []
    
    def update_page(self, page_id: str, properties: Dict) -> bool:
        """Update a Notion page with new properties"""
        url = f"{NOTION_BASE_URL}/pages/{page_id}"
        
        payload = {"properties": properties}
        
        try:
            response = requests.patch(url, headers=self.headers, json=payload)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"❌ Error updating page: {e}")
            return False
    
    def get_words_to_enrich(self, database_id: str) -> List[Dict]:
        """Get all words with Status = 'Ready' that need enrichment"""
        filter_params = {
            "property": "Status",
            "select": {
                "equals": "Ready"
            }
        }
        return self.query_database(database_id, filter_params)
    
    def extract_word_data(self, page: Dict) -> Dict:
        """Extract word information from Notion page"""
        properties = page.get("properties", {})
        
        # Get the word (title)
        title_prop = properties.get("Name", {}).get("title", [])
        word = title_prop[0].get("text", {}).get("content", "") if title_prop else ""
        
        # Get existing definition if any
        brief_def_prop = properties.get("Brief Definition", {}).get("rich_text", [])
        brief_definition = brief_def_prop[0].get("text", {}).get("content", "") if brief_def_prop else ""
        
        # Get existing emotional texture if any
        emotion_prop = properties.get("Emotional Texture", {}).get("rich_text", [])
        emotional_texture = emotion_prop[0].get("text", {}).get("content", "") if emotion_prop else ""
        
        return {
            "page_id": page.get("id"),
            "word": word,
            "brief_definition": brief_definition,
            "emotional_texture": emotional_texture
        }


class ClaudeEnricher:
    """Use Claude AI to generate contextual vocabulary enrichments"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            "x-api-key": api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
    
    def generate_enrichment(self, word: str, existing_definition: str = "", 
                          existing_texture: str = "") -> Optional[Dict]:
        """Generate contextual definition and examples using Claude"""
        
        # Create prompt tailored to Elshan's context
        prompt = f"""You are helping enrich a personal vocabulary database for Elshan, who works in design and regularly listens to design/business podcasts.

Word: "{word}"

Your task: Generate enrichment for this vocabulary word that is:
1. Contextually relevant to design, UX, product development, and creative work
2. Uses examples from design scenarios, podcasts, or professional contexts
3. Clear and memorable

{f'Existing definition: {existing_definition}' if existing_definition else ''}
{f'Existing emotional texture: {existing_texture}' if existing_texture else ''}

Please provide:
1. **Brief Definition**: A concise, clear definition (1-2 sentences max)
2. **Emotional Texture**: 2-3 synonyms or related feeling words (comma-separated)
3. **Contextual Examples**: 3 distinct examples showing how this word appears in design/creative/podcast contexts. Each example should be 1-2 sentences and demonstrate real-world usage.

Format your response as JSON:
{{
  "brief_definition": "...",
  "emotional_texture": "...",
  "contextual_examples": "Example 1: ...\\n\\nExample 2: ...\\n\\nExample 3: ..."
}}

Make the examples engaging, specific, and relevant to Elshan's interests in design and creative work."""

        payload = {
            "model": "claude-sonnet-4-20250514",
            "max_tokens": 1024,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
        
        try:
            response = requests.post(
                ANTHROPIC_API_URL,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            
            # Extract Claude's response
            content = response.json()["content"][0]["text"]
            
            # Parse JSON response
            # Try to extract JSON from markdown code blocks if present
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()
            
            enrichment = json.loads(content)
            return enrichment
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error calling Claude API: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing Claude response: {e}")
            print(f"Raw response: {content}")
            return None


def format_notion_properties(enrichment: Dict) -> Dict:
    """Format enrichment data for Notion API"""
    properties = {}
    
    if enrichment.get("brief_definition"):
        properties["Brief Definition"] = {
            "rich_text": [{"text": {"content": enrichment["brief_definition"]}}]
        }
    
    if enrichment.get("emotional_texture"):
        properties["Emotional Texture"] = {
            "rich_text": [{"text": {"content": enrichment["emotional_texture"]}}]
        }
    
    if enrichment.get("contextual_examples"):
        properties["Contextual Examples"] = {
            "rich_text": [{"text": {"content": enrichment["contextual_examples"]}}]
        }
    
    # Update status to "Enriched"
    properties["Status"] = {
        "select": {"name": "Enriched"}
    }
    
    return properties


def main():
    """Main enrichment workflow"""
    
    print("🚀 Elshan's Living Lexicon - Vocabulary Enrichment Tool")
    print("=" * 60)
    
    # Validate API keys
    if not NOTION_API_KEY:
        print("❌ Error: NOTION_API_KEY environment variable not set")
        print("   Set it with: export NOTION_API_KEY='your-key-here'")
        sys.exit(1)
    
    if not ANTHROPIC_API_KEY:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set")
        print("   Set it with: export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)
    
    # Initialize clients
    notion = NotionClient(NOTION_API_KEY)
    claude = ClaudeEnricher(ANTHROPIC_API_KEY)
    
    print("\n📖 Fetching words that need enrichment...")
    words_to_enrich = notion.get_words_to_enrich(NOTION_DATABASE_ID)
    
    if not words_to_enrich:
        print("✅ No words found with Status='Ready'. All caught up!")
        return
    
    print(f"📝 Found {len(words_to_enrich)} word(s) to enrich\n")
    
    # Process each word
    enriched_count = 0
    failed_count = 0
    
    for i, page in enumerate(words_to_enrich, 1):
        word_data = notion.extract_word_data(page)
        word = word_data["word"]
        
        if not word:
            print(f"⚠️  Skipping entry {i}: No word found")
            failed_count += 1
            continue
        
        print(f"\n[{i}/{len(words_to_enrich)}] Processing: '{word}'")
        print("-" * 60)
        
        # Generate enrichment with Claude
        print("   🤖 Asking Claude for enrichment...")
        enrichment = claude.generate_enrichment(
            word,
            word_data.get("brief_definition", ""),
            word_data.get("emotional_texture", "")
        )
        
        if not enrichment:
            print(f"   ❌ Failed to generate enrichment for '{word}'")
            failed_count += 1
            continue
        
        # Display what we got
        print(f"   ✨ Definition: {enrichment.get('brief_definition', 'N/A')[:80]}...")
        print(f"   💫 Texture: {enrichment.get('emotional_texture', 'N/A')}")
        print(f"   📚 Examples: Generated {len(enrichment.get('contextual_examples', '').split('Example'))-1} examples")
        
        # Update Notion
        print("   💾 Updating Notion...")
        properties = format_notion_properties(enrichment)
        
        if notion.update_page(word_data["page_id"], properties):
            print(f"   ✅ Successfully enriched '{word}'!")
            enriched_count += 1
        else:
            print(f"   ❌ Failed to update Notion for '{word}'")
            failed_count += 1
        
        # Be nice to the APIs - add a small delay
        if i < len(words_to_enrich):
            time.sleep(1)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 Enrichment Complete!")
    print(f"   ✅ Successfully enriched: {enriched_count} word(s)")
    if failed_count > 0:
        print(f"   ❌ Failed: {failed_count} word(s)")
    print("=" * 60)


if __name__ == "__main__":
    main()
