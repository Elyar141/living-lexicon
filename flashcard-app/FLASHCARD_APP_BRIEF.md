# 📚 Living Lexicon Flashcard App - Complete Project Brief

## 🎯 Project Overview

Build a beautiful, fullscreen flashcard web application that reads vocabulary from a Notion database and helps the user learn words with contextual examples. The app should have a premium, minimalist aesthetic with smooth animations.

---

## 📊 Technical Requirements

### Tech Stack:
- **Single HTML file** - Everything in one file (HTML + CSS + JavaScript)
- **Vanilla JavaScript** - No frameworks
- **Notion API** - Read-only access to fetch vocabulary
- **Browser Local Storage** - Track progress (simple MVP approach)
- **Responsive** - Works on desktop and mobile

### APIs & Credentials:
- **Notion Database ID:** `2932ab6ea09280f19ff4ecca6b020371`
- **Notion API Key:** User will provide their integration token
- **API Version:** `2022-06-28`

---

## 🎨 Design & Aesthetic

### Visual Style:
Based on the premium travel loader design with moving gradient blob background.

**Color Palette:**
- Background: White `#ffffff`
- Text: Dark blue-gray `#1c2b3a`
- Blob gradient: Orange `rgb(255, 140, 0)` with low opacity
- Buttons: Border-only, minimal

**Typography:**
- Word (main): 48-72px, font-weight: 800 (bold)
- Emotional Texture: 18-24px, font-weight: 400-500 (regular/medium)
- Definition: 20-28px, font-weight: 400
- Examples: 16-20px, font-weight: 300-400

**Font Family:**
```css
font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Inter, Helvetica, Arial, sans-serif;
```

### Key Design Elements:
1. **Moving blob background** - Subtle, slow-moving gradient blob (similar to attached HTML)
2. **Centered content** - Card centered on screen
3. **Smooth animations** - All transitions should be smooth (~600-900ms)
4. **Minimalist buttons** - Border-only, no fill
5. **Clean spacing** - Generous whitespace

---

## 📐 Layout Structure

### Desktop Layout:
```
┌────────────────────────────────────────────────┐
│                                                │
│    [Moving blob background - subtle]           │
│                                                │
│                                                │
│              EPHEMERAL                         │ ← 48-72px bold
│          Fleeting, transient                   │ ← 18-24px regular
│                                                │
│                                                │
│           [Reveal Meaning]                     │ ← Border button
│                                                │
│                                                │
│  [←]                                     [→]   │ ← Show on hover
│                                                │
│              Progress: 5/130                   │ ← Small, bottom
└────────────────────────────────────────────────┘
```

### Mobile Layout:
- Full screen, no arrows
- Swipe left/right to navigate
- Tap card to flip
- Slightly smaller typography

---

## 🔄 User Flow & Interactions

### State 1: Front of Card (Default)
**Shows:**
- Word (large, bold)
- Emotional Texture (smaller, below word)
- "Reveal Meaning" button

**Actions:**
- Click button → Flip to back
- Click card → Flip to back
- Press Space → Flip to back
- Hover edges → Show navigation arrows

### State 2: Back of Card (Revealed)
**Shows:**
- Word (smaller, at top)
- Brief Definition
- Contextual Examples (all 3)
- "Got It!" button
- "Next Word" button (or back to front)

**Actions:**
- Click "Got It!" → Mark as mastered, load next word
- Click "Next Word" → Skip to next word
- Press Space → Flip back to front
- Arrows (Left/Right) → Navigate to prev/next word

### Navigation:
- **Left arrow** (←) or **Left key** → Previous word
- **Right arrow** (→) or **Right key** → Next word
- **Space bar** → Flip card
- **Swipe** (mobile) → Navigate between words

### Progress Tracking:
- Count total words loaded
- Count words marked "Got It!"
- Show progress: "5/130"
- Save mastered words to localStorage
- Don't show mastered words again in this session

---

## 📊 Data Structure

### From Notion API:
Fetch all entries where `Status = "Enriched"`

**Expected Properties:**
```javascript
{
  id: "page-id-123",
  properties: {
    "Name": {
      title: [{ text: { content: "Ephemeral" } }]
    },
    "Brief Definition": {
      rich_text: [{ text: { content: "Lasting for a very short time..." } }]
    },
    "Emotional Texture": {
      rich_text: [{ text: { content: "Fleeting, transient, momentary" } }]
    },
    "Contextual Examples": {
      rich_text: [{ text: { content: "Example 1: ...\n\nExample 2: ...\n\nExample 3: ..." } }]
    },
    "Status": {
      select: { name: "Enriched" }
    }
  }
}
```

### Parsed Data Structure:
```javascript
{
  id: "page-id-123",
  word: "Ephemeral",
  definition: "Lasting for a very short time; temporary and fleeting.",
  texture: "Fleeting, transient, momentary",
  examples: [
    "Example 1: In the design podcast...",
    "Example 2: The product team...",
    "Example 3: During the critique..."
  ],
  status: "Enriched"
}
```

---

## 🎬 Animations & Transitions

### Card Flip Animation:
```css
/* 3D flip effect */
.card-inner {
  transition: transform 0.6s;
  transform-style: preserve-3d;
}

.card.flipped .card-inner {
  transform: rotateY(180deg);
}
```

### Word Change Animation:
```css
/* Crossfade when changing words */
.card {
  transition: opacity 900ms ease;
}

.card.changing {
  opacity: 0;
}
```

### Navigation Arrows:
```css
/* Show on hover */
.nav-arrow {
  opacity: 0;
  transition: opacity 300ms ease;
  pointer-events: none;
}

.container:hover .nav-arrow {
  opacity: 0.6;
  pointer-events: auto;
}

.nav-arrow:hover {
  opacity: 1;
}
```

### Blob Background:
Use the exact animation from the provided HTML file:
- Smooth drift motion
- 42s duration
- Ease-in-out timing
- Respect prefers-reduced-motion

---

## 🔧 Technical Implementation Details

### API Integration:

```javascript
const NOTION_API_KEY = "user-will-provide";
const DATABASE_ID = "2932ab6ea09280f19ff4ecca6b020371";

async function fetchVocabulary() {
  const response = await fetch(
    `https://api.notion.com/v1/databases/${DATABASE_ID}/query`,
    {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${NOTION_API_KEY}`,
        'Notion-Version': '2022-06-28',
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
  return await response.json();
}
```

### Local Storage Tracking:

```javascript
// Save mastered words
function markAsMastered(wordId) {
  const mastered = JSON.parse(localStorage.getItem('masteredWords') || '[]');
  if (!mastered.includes(wordId)) {
    mastered.push(wordId);
    localStorage.setItem('masteredWords', JSON.stringify(mastered));
  }
}

// Get mastered words
function getMasteredWords() {
  return JSON.parse(localStorage.getItem('masteredWords') || '[]');
}

// Filter out mastered words
function getActiveWords(allWords) {
  const mastered = getMasteredWords();
  return allWords.filter(word => !mastered.includes(word.id));
}
```

### Keyboard Shortcuts:

```javascript
document.addEventListener('keydown', (e) => {
  if (e.code === 'Space') {
    e.preventDefault();
    flipCard();
  } else if (e.code === 'ArrowLeft') {
    previousWord();
  } else if (e.code === 'ArrowRight') {
    nextWord();
  }
});
```

---

## 📱 Responsive Design

### Breakpoints:
- **Desktop:** > 768px
- **Mobile:** ≤ 768px

### Desktop Features:
- Hover-triggered navigation arrows
- Larger typography
- Spacebar shortcuts
- Mouse interactions

### Mobile Features:
- Touch/swipe navigation
- Tap to flip
- Optimized touch targets (min 44x44px)
- Slightly smaller text (responsive scaling)
- Full viewport height

### Mobile Gestures:
```javascript
let touchStartX = 0;
let touchEndX = 0;

element.addEventListener('touchstart', e => {
  touchStartX = e.changedTouches[0].screenX;
});

element.addEventListener('touchend', e => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
});

function handleSwipe() {
  if (touchEndX < touchStartX - 50) nextWord(); // Swipe left
  if (touchEndX > touchStartX + 50) previousWord(); // Swipe right
}
```

---

## 🎯 MVP Features (Must Have)

### Core Functionality:
- [x] Fetch vocabulary from Notion (Status = "Enriched")
- [x] Display word + emotional texture (front of card)
- [x] Flip card to show definition + examples (back)
- [x] Navigate between words (carousel)
- [x] Mark words as "Got It!" (mastered)
- [x] Track progress locally (localStorage)
- [x] Show progress counter (5/130)
- [x] Keyboard navigation (Space, Arrow keys)
- [x] Responsive design (desktop + mobile)

### Visual Elements:
- [x] Moving blob background
- [x] Premium typography
- [x] Smooth flip animation
- [x] Fade transitions between words
- [x] Hover-reveal navigation arrows
- [x] Minimal button styling

### User Experience:
- [x] Clear call-to-action buttons
- [x] Visual feedback on interactions
- [x] Progress indication
- [x] Don't repeat mastered words
- [x] Smooth, polished feel

---

## 🚫 Out of Scope (For Now)

These features are intentionally excluded from MVP to keep it simple:

- ❌ Sound effects (add in V2)
- ❌ Updating Notion database (read-only for now)
- ❌ Spaced repetition algorithm
- ❌ Multiple databases
- ❌ Search/filter functionality
- ❌ Statistics dashboard
- ❌ Export progress
- ❌ User accounts
- ❌ Dark mode toggle
- ❌ Custom themes

---

## 🎨 Reference HTML (Blob Background)

Use this as the base for the moving blob background:

```html
<!-- From premium_travel_loader_boldline.html -->
<div class="field" aria-hidden="true">
  <div class="blob"></div>
</div>

<style>
  :root {
    --blob-color: 255,140,0;
    --blob-strength: 0.16;
    --blob-size: 70vmin;
    --blur: 110px;
    --speed: 42s;
  }
  
  .field {
    position: fixed;
    inset: -22vmax;
    z-index: 0;
    pointer-events: none;
  }
  
  .blob {
    position: absolute;
    width: var(--blob-size);
    height: var(--blob-size);
    border-radius: 50%;
    background: radial-gradient(circle at 50% 50%,
      rgba(var(--blob-color), var(--blob-strength)) 0%,
      rgba(var(--blob-color), calc(var(--blob-strength)*0.55)) 32%,
      rgba(var(--blob-color), 0) 70%);
    filter: blur(var(--blur));
    animation: drift var(--speed) ease-in-out infinite;
  }
  
  @keyframes drift {
    0%   { transform: translate3d(-18vw, -8vh, 0); }
    20%  { transform: translate3d(46vw, -14vh, 0); }
    40%  { transform: translate3d(34vw, 58vh, 0); }
    60%  { transform: translate3d(-12vw, 44vh, 0); }
    80%  { transform: translate3d(0vw, -4vh, 0); }
    100% { transform: translate3d(-18vw, -8vh, 0); }
  }
</style>
```

---

## 📋 File Structure

Single HTML file containing:

```
flashcards.html
├── <!DOCTYPE html>
├── <head>
│   ├── <meta charset, viewport>
│   ├── <title>Living Lexicon Flashcards</title>
│   └── <style>
│       ├── CSS Variables
│       ├── Reset & Base Styles
│       ├── Blob Background
│       ├── Card Layout & Typography
│       ├── Flip Animation
│       ├── Navigation Arrows
│       ├── Buttons
│       ├── Progress Indicator
│       └── Responsive Media Queries
│   </style>
├── <body>
│   ├── <div class="field"> (blob background)
│   ├── <section class="card-container">
│   │   ├── <div class="card">
│   │   │   ├── <div class="front">
│   │   │   │   ├── <h1> (word)
│   │   │   │   ├── <p> (texture)
│   │   │   │   └── <button> (flip)
│   │   │   └── <div class="back">
│   │   │       ├── <h2> (word)
│   │   │       ├── <p> (definition)
│   │   │       ├── <div> (examples)
│   │   │       └── <div> (buttons)
│   │   ├── <button class="nav-left">
│   │   ├── <button class="nav-right">
│   │   └── <div class="progress">
│   └── <script>
│       ├── Configuration (API keys)
│       ├── State Management
│       ├── Notion API Functions
│       ├── Local Storage Functions
│       ├── Card Rendering
│       ├── Flip Logic
│       ├── Navigation Logic
│       ├── Keyboard Handlers
│       ├── Touch Handlers (mobile)
│       └── Initialization
└── </body>
```

---

## 🔑 User Setup Required

The user will need to:

1. **Get Notion Integration Token:**
   - Go to: https://www.notion.so/my-integrations
   - Create integration or use existing
   - Copy token

2. **Share Database with Integration:**
   - Open Living Lexicon database in Notion
   - Click ••• → Connections
   - Add the integration

3. **Add API Key to HTML:**
   - Open the HTML file
   - Find: `const NOTION_API_KEY = "your-key-here";`
   - Paste their integration token
   - Save file

4. **Open in Browser:**
   - Double-click HTML file
   - Or drag into browser
   - Should work immediately!

---

## ✅ Success Criteria

The flashcard app is successful if:

1. **Loads vocabulary** - Fetches all enriched words from Notion
2. **Displays beautifully** - Premium aesthetic with blob background
3. **Flips smoothly** - Card flip animation works well
4. **Navigates easily** - Arrow keys and buttons work
5. **Tracks progress** - Counts mastered words correctly
6. **Works on mobile** - Responsive and touch-friendly
7. **No errors** - Handles API failures gracefully
8. **Fast** - Loads quickly, animations are smooth
9. **Intuitive** - User knows what to do without instructions
10. **Actually useful** - User wants to use it to learn!

---

## 🎯 Edge Cases to Handle

### Error Handling:
- **No API key:** Show friendly message with setup instructions
- **API failure:** Show error, offer retry button
- **No enriched words:** Show "No words found, enrich some first!"
- **Network offline:** Show cached words if available
- **Malformed data:** Skip invalid entries, show what works

### Empty States:
- **No words loaded yet:** Show loading spinner
- **All words mastered:** Show celebration message + "Reset Progress" button
- **Last word:** Loop back to first word

### Data Validation:
- Check that word, definition, texture exist
- Handle missing examples gracefully
- Skip entries with critical data missing

---

## 📊 Example Content (For Testing)

If user wants to test without Notion setup, provide sample data:

```javascript
const SAMPLE_DATA = [
  {
    id: "1",
    word: "Ephemeral",
    texture: "Fleeting, transient, momentary",
    definition: "Lasting for a very short time; temporary and fleeting in nature.",
    examples: [
      "In the design podcast discussion about Snapchat's innovation, they emphasized how ephemeral content fundamentally changed user psychology around sharing.",
      "The product team debated whether to implement ephemeral notifications that disappear after viewing, weighing the reduced cognitive load against potential information loss.",
      "During the design critique, the mentor noted that trends in UI design are increasingly ephemeral, with popular patterns shifting every 6-12 months."
    ]
  },
  {
    id: "2",
    word: "Liminal",
    texture: "Transitional, in-between, threshold",
    definition: "Occupying a position at or on both sides of a boundary or threshold; relating to a transitional state.",
    examples: [
      "In the podcast episode on user onboarding, they discussed how the loading screen creates a liminal space where users transition from anticipation to engagement.",
      "The design team debated whether the navigation drawer was too liminal, existing neither as a permanent element nor a clear modal, potentially confusing users.",
      "During the portfolio review, the mentor noted that the designer's work occupied a liminal position between illustration and interface design."
    ]
  },
  {
    id: "3",
    word: "Provenance",
    texture: "Origin, source, lineage",
    definition: "The place of origin or earliest known history of something; the beginning of something's existence.",
    examples: [
      "When presenting the design system to stakeholders, understanding the provenance of each component helped justify our design decisions.",
      "In the podcast about design ethics, they discussed the provenance of data used in AI training models and its implications for design.",
      "The provenance of this design pattern traces back to early iOS interfaces, which influenced how we approach navigation today."
    ]
  }
];
```

---

## 🚀 Development Approach

### Phase 1: Structure (30 min)
1. Set up HTML boilerplate
2. Add blob background (from reference)
3. Create card layout structure
4. Add basic styling

### Phase 2: Functionality (60 min)
1. Implement Notion API fetch
2. Parse and format data
3. Render first card
4. Add flip functionality
5. Add navigation (prev/next)

### Phase 3: Interactions (45 min)
1. Add keyboard shortcuts
2. Add touch gestures (mobile)
3. Implement progress tracking
4. Add "Got It!" functionality
5. LocalStorage integration

### Phase 4: Polish (45 min)
1. Smooth all animations
2. Add transitions
3. Responsive design tweaks
4. Error handling
5. Loading states
6. Edge cases

---

## 💡 Code Quality Guidelines

### Code Style:
- Use semantic HTML
- Clear, descriptive variable names
- Add comments for complex logic
- Keep functions small and focused
- Use modern JavaScript (ES6+)

### Performance:
- Minimize DOM manipulation
- Debounce rapid interactions
- Lazy load if many words
- Optimize animations (use transform/opacity)

### Accessibility:
- Semantic HTML tags
- ARIA labels where needed
- Keyboard navigation
- Focus states
- Reduced motion support

### Error Handling:
```javascript
try {
  const data = await fetchVocabulary();
  renderCard(data);
} catch (error) {
  showError("Couldn't load vocabulary. Check your API key and try again.");
  console.error("API Error:", error);
}
```

---

## 🎨 Final Polish Checklist

Before considering it done:

- [ ] Blob background animates smoothly
- [ ] Card flip is smooth and 3D
- [ ] Typography scales responsively
- [ ] Buttons have hover states
- [ ] Keyboard shortcuts work
- [ ] Mobile swipe gestures work
- [ ] Progress updates correctly
- [ ] LocalStorage persists
- [ ] No console errors
- [ ] Works in Chrome, Firefox, Safari
- [ ] Mobile browsers tested
- [ ] Loading state is shown
- [ ] Error states are handled
- [ ] Empty state is graceful
- [ ] Code is clean and commented

---

## 📦 Deliverable

**Single HTML file named:** `living-lexicon-flashcards.html`

**Size:** ~15-25KB (including all CSS and JS)

**Dependencies:** None (fully self-contained)

**Browser Support:**
- Chrome/Edge (latest 2 versions)
- Firefox (latest 2 versions)
- Safari (latest 2 versions)
- Mobile browsers (iOS Safari, Chrome Android)

---

## 🎯 What to Tell Claude Code

When starting the new chat, say:

> "I need you to build a flashcard web application based on this complete specification. Please read through all the details carefully and build a single, self-contained HTML file that implements all the MVP features. The app should be beautiful, smooth, and production-ready. Ask clarifying questions if anything is unclear, otherwise start building!"

Then paste this entire document.

---

## ✨ Success!

This app will be:
- 🎨 Beautiful and premium-looking
- ⚡ Fast and smooth
- 📱 Mobile-friendly
- 🎯 Actually useful for learning
- 💼 Portfolio-ready
- 🔧 Extensible for future features

Good luck building! 🚀
