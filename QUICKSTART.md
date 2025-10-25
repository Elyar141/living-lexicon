# 🚀 Quick Start Guide - 5 Minutes to First Enrichment

## Step 1: Get Your Anthropic API Key (2 min)

1. Go to: https://console.anthropic.com/
2. Sign up or log in
3. Click "API Keys" in the left sidebar
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-...`)
6. **Save it somewhere safe!**

## Step 2: Set Up API Keys (1 min)

### On Windows:

Open Command Prompt and run:
```cmd
set NOTION_API_KEY=your-notion-integration-token-here
set ANTHROPIC_API_KEY=sk-ant-your-anthropic-key-here
```

**Important:** These are temporary! To make them permanent:
1. Search for "Environment Variables" in Windows
2. Click "Edit the system environment variables"
3. Click "Environment Variables" button
4. Under "User variables", click "New"
5. Add both keys

### On Mac/Linux:

Open Terminal and run:
```bash
export NOTION_API_KEY="your-notion-integration-token-here"
export ANTHROPIC_API_KEY="sk-ant-your-anthropic-key-here"
```

To make permanent, add these lines to your `~/.bashrc` or `~/.zshrc` file.

## Step 3: Install Python Dependencies (30 seconds)

```bash
pip install requests
```

Or using the requirements file:
```bash
pip install -r requirements.txt
```

## Step 4: Test Your Setup (30 seconds)

Run the test script to make sure everything works:

```bash
python test_connection.py
```

You should see:
```
✅ All tests passed! You're ready to run the enrichment script.
```

## Step 5: Add a Test Word (30 seconds)

1. Open your browser
2. Go to any article or page
3. Select a word (like "ephemeral")
4. Use your "Save to Notion" extension
5. Word should appear in your Notion database with Status = "Ready"

## Step 6: Run the Enrichment! (1 min)

### On Windows:
Double-click `run_enrichment.bat`

### Or use command line:
```bash
python vocab_enricher.py
```

You'll see something like:
```
🚀 Elshan's Living Lexicon - Vocabulary Enrichment Tool
============================================================

📖 Fetching words that need enrichment...
📝 Found 1 word(s) to enrich

[1/1] Processing: 'ephemeral'
------------------------------------------------------------
   🤖 Asking Claude for enrichment...
   ✨ Definition: Lasting for a very short time; transitory...
   💫 Texture: Fleeting, temporary, momentary
   📚 Examples: Generated 3 examples
   💾 Updating Notion...
   ✅ Successfully enriched 'ephemeral'!

============================================================
📊 Enrichment Complete!
   ✅ Successfully enriched: 1 word(s)
============================================================
```

## Step 7: Check Notion! ✨

Open your Living Lexicon database in Notion. Your word should now have:
- ✅ Brief Definition
- ✅ Emotional Texture
- ✅ Contextual Examples (relevant to design!)
- ✅ Status changed to "Enriched"

## 🎉 That's It!

You now have a working vocabulary enrichment system!

## 📅 Daily Workflow

1. **Throughout the day:** Add words via browser extension (2 seconds each)
2. **Once a day or week:** Run `python vocab_enricher.py` (enriches all at once)
3. **Practice:** Use your flashcard app with contextually enriched vocabulary!

## 🆘 Troubleshooting

**"NOTION_API_KEY environment variable not set"**
- You need to set the API key in your terminal session
- Or add it to your system environment variables

**"Error calling Claude API"**
- Check your Anthropic API key is correct
- Make sure you have API credits (new accounts get free credits)

**"No words found with Status='Ready'"**
- Make sure you've added words to Notion
- Check that Status is set to "Ready" for words you want to enrich
- Verify your database has a "Status" column with "Ready" option

**Script runs but nothing happens**
- Run `test_connection.py` first to diagnose
- Check both API keys are valid
- Verify the integration has access to your database

## 💰 Cost

Using Claude Sonnet 4:
- ~$0.003 per word
- Enriching 100 words = ~$0.30
- Very affordable for personal use!

## 🎯 Next Steps

After you've enriched some words:
1. Build the flashcard practice app
2. Set up the iOS shortcut for mobile capture
3. Start learning!

Need help? Check the main README.md for more details.
