// Living Lexicon Flashcard App - Local Server
// Serves the HTML app and proxies Notion API requests

require('dotenv').config();
const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;
const DATABASE_ID = '2932ab6ea09280f19ff4ecca6b020371';
const NOTION_VERSION = '2022-06-28';

// Parse JSON bodies
app.use(express.json());

// Serve static files (HTML, CSS, JS)
app.use(express.static(__dirname));

// API endpoint to check if setup is complete
app.get('/api/config', (req, res) => {
  // Check if token is configured
  if (!process.env.NOTION_API_KEY) {
    return res.status(400).json({
      error: 'NOTION_API_KEY not found in .env file',
      setup: true
    });
  }

  res.json({
    ready: true,
    databaseId: DATABASE_ID
  });
});

// Proxy endpoint for Notion API (avoids CORS issues)
app.post('/api/vocabulary', async (req, res) => {
  try {
    // Check if token is configured
    if (!process.env.NOTION_API_KEY) {
      console.error('❌ NOTION_API_KEY not found in .env file');
      return res.status(400).json({
        error: 'NOTION_API_KEY not found in .env file',
        setup: true
      });
    }

    console.log('📡 Fetching vocabulary from Notion...');

    // Make request to Notion API from server (no CORS issues)
    const notionResponse = await fetch(
      `https://api.notion.com/v1/databases/${DATABASE_ID}/query`,
      {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.NOTION_API_KEY}`,
          'Notion-Version': NOTION_VERSION,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          filter: {
            property: "Status",
            select: { equals: "Enriched" }
          }
        })
      }
    );

    console.log(`📊 Notion API responded with status: ${notionResponse.status}`);

    if (!notionResponse.ok) {
      const errorData = await notionResponse.json();
      console.error('❌ Notion API error:', errorData);
      return res.status(notionResponse.status).json({
        error: errorData.message || 'Notion API error',
        details: errorData
      });
    }

    const data = await notionResponse.json();
    console.log(`✅ Successfully fetched ${data.results.length} words`);

    if (data.results.length === 0) {
      console.warn('⚠️  No words found with Status = "Enriched"');
    }

    res.json(data);

  } catch (error) {
    console.error('❌ Server error:', error);
    res.status(500).json({
      error: 'Server error: ' + error.message
    });
  }
});

// Serve the main HTML file
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(PORT, () => {
  console.log('\n🎓 Living Lexicon Flashcard App');
  console.log('================================');
  console.log(`✅ Server running at: http://localhost:${PORT}`);
  console.log(`📖 Open this URL in your browser to start learning!`);
  console.log('\nPress Ctrl+C to stop the server\n');
});

// Handle graceful shutdown
process.on('SIGTERM', () => {
  console.log('\n👋 Shutting down server...');
  process.exit(0);
});
