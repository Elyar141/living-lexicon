// Quick test script to verify Notion API connection
require('dotenv').config();

const DATABASE_ID = '2932ab6ea09280f19ff4ecca6b020371';
const NOTION_VERSION = '2022-06-28';

async function testNotionAPI() {
  console.log('\n🔍 Testing Notion API Connection...\n');

  // Check if API key exists
  if (!process.env.NOTION_API_KEY) {
    console.error('❌ ERROR: NOTION_API_KEY not found in .env file');
    console.log('\nPlease add your Notion integration token to the .env file:');
    console.log('NOTION_API_KEY=your_token_here\n');
    return;
  }

  console.log('✓ API key found in .env');
  console.log('✓ Database ID:', DATABASE_ID);
  console.log('\n📡 Fetching data from Notion...\n');

  try {
    const response = await fetch(
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

    console.log('Response status:', response.status, response.statusText);

    if (!response.ok) {
      const errorData = await response.json();
      console.error('\n❌ Notion API Error:');
      console.error(JSON.stringify(errorData, null, 2));

      if (response.status === 401) {
        console.log('\n💡 This usually means:');
        console.log('   1. Your API token is invalid');
        console.log('   2. You need to share the database with your integration');
        console.log('\nTo fix:');
        console.log('   1. Go to your Notion database');
        console.log('   2. Click the ••• menu → Connections');
        console.log('   3. Add your integration\n');
      }
      return;
    }

    const data = await response.json();

    console.log('✅ Success! Retrieved data from Notion\n');
    console.log('Total results:', data.results.length);

    if (data.results.length === 0) {
      console.log('\n⚠️  WARNING: No words found with Status = "Enriched"');
      console.log('\nMake sure you have words in your Notion database with:');
      console.log('   - Status property set to "Enriched"\n');
    } else {
      console.log('\n📚 Sample words found:');
      data.results.slice(0, 3).forEach((page, i) => {
        const word = page.properties.Name?.title?.[0]?.text?.content || 'Unknown';
        const definition = page.properties["Brief Definition"]?.rich_text?.[0]?.text?.content || 'No definition';
        console.log(`\n${i + 1}. ${word}`);
        console.log(`   ${definition.substring(0, 80)}...`);
      });

      console.log('\n✅ Everything looks good! The app should work.\n');
    }

  } catch (error) {
    console.error('\n❌ Network Error:', error.message);
    console.log('\nThis might mean:');
    console.log('   - No internet connection');
    console.log('   - Firewall blocking the request');
    console.log('   - Invalid database ID\n');
  }
}

testNotionAPI();
