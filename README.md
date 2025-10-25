# 📚 Living Lexicon - AI-Powered Vocabulary Builder

> Automatically enrich your personal vocabulary with contextually relevant definitions and examples using Claude AI and Notion.

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Notion API](https://img.shields.io/badge/Notion-API-black.svg)](https://developers.notion.com/)
[![Claude AI](https://img.shields.io/badge/Claude-AI-orange.svg)](https://www.anthropic.com/)

A smart vocabulary learning system that captures words from anywhere, enriches them with AI-generated contextual examples, and helps you learn in your own context.

## ✨ Features

- 🚀 **One-click capture** from any website or app
- 🤖 **AI-powered enrichment** with Claude Sonnet 4
- 🎨 **Contextual examples** tailored to design and creative work
- 📊 **Notion integration** for seamless storage and tracking
- 💰 **Cost-effective** (~$0.003 per word)
- 🔒 **Privacy-focused** - your data stays in your Notion workspace

## 🎯 Why This Project?

Built to solve a real problem: learning vocabulary from podcasts, articles, and professional content with examples that actually matter. Generic dictionary definitions don't stick - contextual examples in your field do.

Perfect for:
- Designers learning industry terminology
- Professionals expanding vocabulary in their domain
- Podcast listeners capturing new words
- Anyone who wants vocabulary learning that fits their context

---

## Demo

[Screenshot or GIF of the enrichment process will go here]

---

Automatically enriches your Notion vocabulary database with AI-generated contextual definitions and examples.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install directly:
```bash
pip install requests
```

### 2. Set Up API Keys

You need two API keys:

**Notion API Key:**
- Go to: https://www.notion.so/my-integrations
- Create new integration or use existing
- Copy the "Internal Integration Token"
- Make sure the integration has access to your "Living Lexicon" database

**Anthropic API Key:**
- Go to: https://console.anthropic.com/
- Sign up/login
- Go to API Keys section
- Create new API key
- Copy it

### 3. Set Environment Variables

**On Windows (Command Prompt):**
```cmd
set NOTION_API_KEY=your-notion-key-here
set ANTHROPIC_API_KEY=your-anthropic-key-here
```

**On Windows (PowerShell):**
```powershell
$env:NOTION_API_KEY="your-notion-key-here"
$env:ANTHROPIC_API_KEY="your-anthropic-key-here"
```

**On Mac/Linux:**
```bash
export NOTION_API_KEY="your-notion-key-here"
export ANTHROPIC_API_KEY="your-anthropic-key-here"
```

### 4. Run the Script

```bash
python vocab_enricher.py
```

## 📖 What It Does

1. **Finds** all words in your Notion database with Status = "Ready"
2. **Enriches** each word using Claude AI to generate:
   - Brief Definition (clear, concise)
   - Emotional Texture (synonyms and related feelings)
   - Contextual Examples (3 examples relevant to design/creative work)
3. **Updates** your Notion database with the enriched content
4. **Sets** Status to "Enriched" when done

## 🎯 Example Output

```
🚀 Elshan's Living Lexicon - Vocabulary Enrichment Tool
============================================================

📖 Fetching words that need enrichment...
📝 Found 3 word(s) to enrich

[1/3] Processing: 'Liminal'
------------------------------------------------------------
   🤖 Asking Claude for enrichment...
   ✨ Definition: Occupying a position at or on both sides of a boundary...
   💫 Texture: Transitional, in-between, threshold
   📚 Examples: Generated 3 examples
   💾 Updating Notion...
   ✅ Successfully enriched 'Liminal'!

============================================================
📊 Enrichment Complete!
   ✅ Successfully enriched: 3 word(s)
============================================================
```

## 🔧 Configuration

The script uses these settings:
- **Notion Database ID**: `2932ab6ea09280f19ff4ecca6b020371` (hardcoded)
- **Claude Model**: `claude-sonnet-4-20250514` (latest Sonnet)
- **API Rate Limit**: 1 second delay between requests

To change the database ID, edit the `NOTION_DATABASE_ID` variable in `vocab_enricher.py`.

## 🎨 Contextual Examples

The AI is specifically instructed to generate examples relevant to:
- Design and UX work
- Product development
- Creative contexts
- Podcast discussions
- Professional scenarios

Examples are tailored to YOUR interests and learning context!

## 💡 Usage Tips

**Run daily or weekly:**
- Add words throughout the day via browser extension or iOS shortcut
- Run the script once to enrich them all at once
- Practice with your flashcard app

**Batch processing:**
- The script processes all "Ready" words in one run
- Safe to run multiple times (skips already enriched words)
- No duplicate processing

**Manual override:**
- If you want to re-enrich a word, change its Status back to "Ready"
- The script will process it again

## 🐛 Troubleshooting

**"No words found with Status='Ready'"**
- Make sure you have words in your database
- Check that the Status column exists and has "Ready" as an option
- Verify the Status is set to "Ready" for words you want to enrich

**"Error: NOTION_API_KEY environment variable not set"**
- Set the environment variable before running the script
- Make sure there are no typos in the key
- Verify the integration has access to your database

**"Error calling Claude API"**
- Check your Anthropic API key is correct
- Verify you have API credits available
- Check your internet connection

**"Error parsing Claude response"**
- This is rare - the script will show the raw response for debugging
- Try running again - sometimes API responses vary

## 📊 Cost Estimate

**Anthropic API Costs:**
- Using Claude Sonnet 4
- ~500 tokens per word enrichment
- At current rates: ~$0.003 per word
- For 100 words: ~$0.30

Very affordable for personal use!

## 🚀 Next Steps

After enrichment:
1. Check your Notion database - words should have full definitions and examples
2. Build the flashcard practice app
3. Start learning!

## 📝 Notes

- The script is designed to be safe - it won't duplicate work
- All enrichment happens through official APIs (no web scraping)
- Your data stays private (only shared with Notion and Anthropic APIs)
