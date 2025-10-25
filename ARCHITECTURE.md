# System Architecture - Elshan's Living Lexicon

## 📐 Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPTURE LAYER                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [Browser]          [iOS]           [Any App]               │
│      │                │                 │                    │
│      ├── Extension ───┤                 │                    │
│      └── Shortcut ────┴── Share Sheet ─┘                    │
│                          │                                   │
│                          ▼                                   │
│                    [Notion API]                              │
│                          │                                   │
└──────────────────────────┼───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    STORAGE LAYER                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│              Notion Database: "Living Lexicon"               │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Word (Title)    │ Date     │ Status               │    │
│  │ Liminal         │ 10/25/25 │ Ready                │    │
│  │ Ephemeral       │ 10/25/25 │ Ready                │    │
│  │ Provenance      │ 10/24/25 │ Enriched             │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                 ENRICHMENT LAYER                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│               [vocab_enricher.py]                            │
│                      │                                       │
│         1. Query Notion for Status="Ready"                  │
│                      │                                       │
│         2. For each word:                                   │
│            ├── Send to Claude AI                           │
│            │   "Generate contextual examples                │
│            │    for design/creative contexts"               │
│            │                                                 │
│            ├── Receive enrichment:                          │
│            │   • Brief Definition                           │
│            │   • Emotional Texture                          │
│            │   • 3 Contextual Examples                      │
│            │                                                 │
│            └── Update Notion                                │
│                Set Status="Enriched"                        │
│                                                              │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   PRACTICE LAYER                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│           [Flashcard Web App] (To be built)                 │
│                      │                                       │
│         1. Read from Notion (Status="Enriched")             │
│         2. Display fullscreen flashcards                    │
│         3. Track learning progress                          │
│         4. Update Status: Learning → Mastered               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow

### 1. Word Capture Flow
```
User sees word "Liminal"
    ↓
Selects text & clicks extension
    ↓
Extension sends to Notion API
    ↓
New entry created:
    - Word: "Liminal"
    - Date Added: Today
    - Status: "Ready"
    - All other fields: Empty
```

### 2. Enrichment Flow
```
User runs: python vocab_enricher.py
    ↓
Script queries Notion:
    "SELECT * WHERE Status='Ready'"
    ↓
For each word (e.g., "Liminal"):
    ↓
    Send to Claude API with prompt:
    "Generate contextual definition and 
     examples for 'Liminal' in design context"
    ↓
    Claude returns JSON:
    {
      "brief_definition": "...",
      "emotional_texture": "...",
      "contextual_examples": "..."
    }
    ↓
    Update Notion entry:
    - Fill in definition
    - Fill in texture
    - Fill in examples
    - Change Status to "Enriched"
```

### 3. Practice Flow (Future)
```
User opens flashcard app
    ↓
App queries Notion:
    "SELECT * WHERE Status='Enriched'"
    ↓
Display word → User thinks → Reveals definition & examples
    ↓
User marks: "Learning" or "Mastered"
    ↓
App updates Notion Status
```

## 🔌 API Integrations

### Notion API
- **Endpoint:** `https://api.notion.com/v1`
- **Authentication:** Bearer token
- **Operations:**
  - Query database (GET filtered results)
  - Update page (PATCH properties)
- **Rate Limit:** 3 requests/second
- **Cost:** Free

### Anthropic API
- **Endpoint:** `https://api.anthropic.com/v1/messages`
- **Authentication:** x-api-key header
- **Model:** claude-sonnet-4-20250514
- **Operations:**
  - Send message with prompt
  - Receive structured JSON response
- **Rate Limit:** Varies by tier
- **Cost:** ~$3 per million input tokens, ~$15 per million output tokens

## 📊 Database Schema

### Notion Database: "Elshan's Living Lexicon"

| Column Name | Type | Auto-Fill | Purpose |
|-------------|------|-----------|---------|
| **Word** | Title | ❌ Manual | The vocabulary word |
| **Date Added** | Date | ✅ Created time | Timestamp of capture |
| **Status** | Select | ✅ Default: "Ready" | Workflow state |
| **Brief Definition** | Text | 🤖 AI | Concise definition |
| **Emotional Texture** | Text | 🤖 AI | Synonyms/feelings |
| **Contextual Examples** | Text | 🤖 AI | 3 usage examples |

### Status Values:
- **Ready** - Word captured, needs enrichment
- **Enriched** - AI has added definition and examples
- **Learning** - User is actively studying
- **Mastered** - User has learned the word

## 🎨 AI Prompt Engineering

The enrichment prompt is carefully crafted to:

1. **Provide Context:** 
   - "User works in design"
   - "Listens to design/business podcasts"

2. **Set Constraints:**
   - Brief definition (1-2 sentences max)
   - 2-3 synonyms for texture
   - Exactly 3 examples

3. **Specify Format:**
   - Structured JSON output
   - Consistent field names

4. **Ensure Relevance:**
   - Examples from design scenarios
   - Professional/creative contexts
   - Real-world usage

### Example Prompt:
```
You are helping enrich a personal vocabulary database 
for Elshan, who works in design and regularly listens 
to design/business podcasts.

Word: "Liminal"

Generate:
1. Brief Definition (1-2 sentences)
2. Emotional Texture (2-3 synonyms)
3. Contextual Examples (3 examples in design/creative contexts)

Format as JSON: {...}
```

## 🏗️ Tech Stack

### Core Technologies
- **Python 3.8+** - Main programming language
- **requests** - HTTP library for API calls
- **json** - JSON parsing and formatting

### External Services
- **Notion** - Database and storage
- **Anthropic Claude** - AI enrichment
- **Browser Extensions** - Capture layer

### Future Additions
- **HTML/CSS/JavaScript** - Flashcard web app
- **Notion API (read-only)** - Flashcard data source
- **Local Storage** - Practice progress tracking

## 📈 Scalability Considerations

### Current Capacity
- **Words per run:** Unlimited (with rate limiting)
- **Processing speed:** ~2-3 seconds per word
- **API costs:** ~$0.003 per word
- **Storage:** Unlimited (Notion)

### Bottlenecks
1. **Anthropic API rate limits** - Add delays between requests
2. **Notion API rate limits** - 3 req/sec max
3. **Cost** - Enriching 1000 words = ~$3

### Future Optimizations
- Batch processing multiple words in one Claude prompt
- Caching common definitions
- Incremental enrichment (only missing fields)

## 🔐 Security & Privacy

### Data Flow
- ✅ All data stays in your Notion workspace
- ✅ API keys stored as environment variables
- ✅ No third-party tracking
- ✅ No data persistence in script

### API Key Management
- Never commit keys to git
- Use environment variables
- Regenerate if compromised
- Separate keys per environment

## 🚀 Deployment Options

### Option 1: Manual Run (Current)
- Run script when you want
- Full control
- No infrastructure needed

### Option 2: Scheduled Run (Next Step)
- Cron job (Mac/Linux)
- Task Scheduler (Windows)
- Runs daily automatically

### Option 3: Cloud Function (Advanced)
- AWS Lambda
- Google Cloud Functions
- Triggered by Notion webhook
- Instant enrichment

## 📊 Metrics to Track

For portfolio presentation:
- Total words captured
- Words enriched per week
- Time saved vs manual research
- Learning progress (mastered words)
- System uptime/reliability

## 🎯 Success Metrics

- **Capture speed:** <2 seconds per word
- **Enrichment quality:** Contextually relevant examples
- **System reliability:** 99%+ successful enrichments
- **Cost efficiency:** <$0.01 per word all-in
- **User satisfaction:** Actually use it daily!

---

This architecture is designed to be:
- ✅ Simple to understand
- ✅ Easy to modify
- ✅ Scalable for growth
- ✅ Portfolio-ready
- ✅ Actually useful!
