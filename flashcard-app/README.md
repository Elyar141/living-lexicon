# 📚 Living Lexicon Flashcards

A beautiful, premium vocabulary flashcard application that syncs with your Notion database. Features smooth animations, a moving gradient blob background, and progress tracking.

![Flashcard App](https://img.shields.io/badge/Status-Ready-success)
![Node](https://img.shields.io/badge/Node.js-Required-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Beautiful Design** - Premium aesthetic with moving gradient blob background
- **Notion Integration** - Syncs with your Notion vocabulary database
- **Smart Progress Tracking** - Remember which words you've mastered
- **Keyboard Shortcuts** - Navigate efficiently with keyboard
- **Mobile Friendly** - Touch gestures and responsive design
- **3D Card Flip** - Smooth animations and transitions
- **Privacy First** - Your API token stays local in .env file

---

## 🚀 Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) (version 14 or higher)
- A Notion account with a vocabulary database
- A Notion integration token

### Installation

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up your Notion integration**
   - Go to [notion.so/my-integrations](https://www.notion.so/my-integrations)
   - Click "New integration"
   - Give it a name (e.g., "Living Lexicon Flashcards")
   - Select your workspace
   - Copy the "Internal Integration Token"

4. **Share your database with the integration**
   - Open your Living Lexicon database in Notion
   - Click the `•••` menu in the top right
   - Go to "Connections"
   - Click "Add connection" and select your integration

5. **Create your .env file**
   ```bash
   cp .env.example .env
   ```

6. **Add your Notion token to .env**

   Open the `.env` file and paste your token:
   ```env
   NOTION_API_KEY=secret_your_actual_token_here
   PORT=3000
   ```

7. **Start the server**
   ```bash
   npm start
   ```

8. **Open in your browser**

   Navigate to: [http://localhost:3000](http://localhost:3000)

---

## 🎮 How to Use

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `Space` | Flip card (reveal/hide meaning) |
| `←` Left Arrow | Previous word |
| `→` Right Arrow | Next word |

### Desktop Controls

- **Hover** near edges to see navigation arrows
- **Click "Reveal Meaning"** to flip card
- **Click "Got It!"** to mark word as mastered
- **Click "Next Word"** to skip to next

### Mobile Controls

- **Tap** the card to flip it
- **Swipe left** to go to next word
- **Swipe right** to go to previous word
- **Tap "Got It!"** to mark word as mastered

---

## 📊 Notion Database Setup

Your Notion database should have the following properties:

| Property Name | Type | Description |
|---------------|------|-------------|
| `Name` | Title | The vocabulary word |
| `Brief Definition` | Text | A clear, concise definition |
| `Emotional Texture` | Text | Synonyms or related words |
| `Contextual Examples` | Text | 3 examples separated by double line breaks |
| `Status` | Select | Must include "Enriched" option |

**Important:** Only words with Status = "Enriched" will appear in the flashcard app.

### Example Entry

**Name:** Ephemeral

**Brief Definition:** Lasting for a very short time; temporary and fleeting in nature.

**Emotional Texture:** Fleeting, transient, momentary

**Contextual Examples:**
```
In the design podcast discussion about Snapchat's innovation, they emphasized how ephemeral content fundamentally changed user psychology around sharing.

The product team debated whether to implement ephemeral notifications that disappear after viewing, weighing the reduced cognitive load against potential information loss.

During the design critique, the mentor noted that trends in UI design are increasingly ephemeral, with popular patterns shifting every 6-12 months.
```

**Status:** Enriched

---

## 🔧 Configuration

### Environment Variables

Edit the `.env` file to configure:

```env
# Required: Your Notion integration token
NOTION_API_KEY=secret_xxxxx

# Optional: Server port (default: 3000)
PORT=3000
```

### Database ID

The database ID is hardcoded in `server.js`:
```javascript
databaseId: '2932ab6ea09280f19ff4ecca6b020371'
```

If you want to use a different database, update this value.

---

## 📁 Project Structure

```
living-lexicon-flashcards/
├── index.html              # Main flashcard app (single-page)
├── server.js               # Local Express server
├── package.json            # Node.js dependencies
├── .env                    # Your API token (git-ignored)
├── .env.example            # Template for .env file
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

---

## 🎨 Customization

### Colors

Edit the CSS variables in `index.html` to customize colors:

```css
:root {
  --blob-color: 255, 140, 0;    /* Orange gradient blob */
  --bg: #ffffff;                /* Background */
  --text: #1c2b3a;              /* Text color */
  --border: rgba(28, 43, 58, 0.15); /* Button borders */
}
```

### Typography

Adjust font sizes:

```css
:root {
  --font-xl: clamp(48px, 8vw, 72px);  /* Main word */
  --font-lg: clamp(20px, 3vw, 28px);  /* Definition */
  --font-md: clamp(18px, 2.5vw, 24px); /* Texture */
  --font-sm: clamp(16px, 2vw, 20px);  /* Examples */
}
```

### Animation Speed

```css
:root {
  --speed: 42s;              /* Blob animation speed */
  --flip-duration: 600ms;    /* Card flip speed */
  --fade-duration: 900ms;    /* Word transition speed */
}
```

---

## 🐛 Troubleshooting

### "Server Not Running" message

**Problem:** You opened `index.html` directly in browser (file://)

**Solution:** Run the server with `npm start` and visit http://localhost:3000

### "Setup Required" message

**Problem:** .env file is missing or NOTION_API_KEY is not set

**Solution:**
1. Create `.env` file from `.env.example`
2. Add your Notion integration token
3. Restart the server

### "Invalid Notion API token" error

**Problem:** Token is incorrect or database not shared with integration

**Solution:**
1. Verify token in .env file is correct
2. Make sure you shared your database with the integration in Notion
3. Restart the server after changing .env

### "No Words Found" message

**Problem:** No entries with Status = "Enriched" in database

**Solution:**
1. Open your Notion database
2. Set Status to "Enriched" for words you want to study
3. Refresh the app

### Port already in use

**Problem:** Port 3000 is already being used by another application

**Solution:** Change the port in `.env`:
```env
PORT=3001
```

---

## 🔒 Security Notes

- **Never commit `.env` file** - It contains your secret API token
- **Never share your .env file** - Keep your token private
- **Server only accepts localhost** - API token endpoint only works locally
- **Use git-ignored .env** - The .gitignore file excludes .env by default

---

## 💾 Data & Privacy

- **Progress stored locally** - Your learning progress is saved in browser localStorage
- **No data sent to external servers** - All data stays between your browser and Notion
- **Read-only access** - App only reads from Notion, never modifies your database
- **Clear progress** - Click "Reset Progress" to clear all mastered words

---

## 🔄 Reset Progress

To reset all your progress and start fresh:

1. **Option 1:** Click "Reset Progress" button when all words are mastered
2. **Option 2:** Clear localStorage in browser DevTools:
   ```javascript
   localStorage.removeItem('livingLexicon_mastered')
   ```
3. **Option 3:** Use incognito/private browsing mode

---

## 📝 Development

### Running in development mode

```bash
npm run dev
```

### Making changes

1. Edit `index.html` for UI/styling changes
2. Edit `server.js` for backend changes
3. Changes to HTML/CSS are instant (just refresh browser)
4. Changes to server.js require server restart

---

## 🚢 Deployment

This app is designed to run locally. If you want to deploy it:

### ⚠️ Security Warning

**Do NOT deploy this to a public server** with your API token in .env. The current setup is **only secure for localhost**.

If you need a hosted version, you would need to:
1. Implement proper authentication
2. Store API tokens securely (database, not .env)
3. Add user accounts
4. Use HTTPS
5. Implement rate limiting

---

## 🤝 Contributing

This is a personal learning tool, but feel free to fork and customize!

---

## 📄 License

MIT License - Feel free to use and modify for your own learning!

---

## 🙏 Acknowledgments

- Notion API for vocabulary data
- Design inspired by premium travel loaders
- Built with vanilla JavaScript (no frameworks!)

---

## 📞 Support

If you encounter issues:

1. Check this README's troubleshooting section
2. Verify your .env file is configured correctly
3. Make sure your Notion database has the correct properties
4. Ensure you've shared the database with your integration

---

## 🎯 Roadmap

Future enhancements could include:

- [ ] Spaced repetition algorithm
- [ ] Statistics dashboard
- [ ] Multiple database support
- [ ] Export/import progress
- [ ] Dark mode
- [ ] Sound effects
- [ ] Customizable themes

---

**Happy Learning! 🚀📚**
