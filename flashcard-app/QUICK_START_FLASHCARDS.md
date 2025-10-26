# 🎯 Quick Reference - Flashcard App

## Copy-Paste This Into New Claude Code Chat:

```
I need you to build a vocabulary flashcard web application. Here are the requirements:

BUILD: Single self-contained HTML file (no external dependencies)

DESIGN:
- Premium aesthetic with moving orange gradient blob background (subtle, slow animation)
- White background (#ffffff), dark blue-gray text (#1c2b3a)
- Large bold word (48-72px), smaller emotional texture (18-24px)
- Minimal border-only buttons
- Smooth 3D card flip animation (600ms)
- Hover-reveal navigation arrows on edges

FUNCTIONALITY:
- Fetch vocabulary from Notion API (Database ID: 2932ab6ea09280f19ff4ecca6b020371)
- Filter by Status = "Enriched"
- Front: Show word + emotional texture + "Reveal" button
- Back: Show word + definition + 3 examples + "Got It!" button
- Navigate with arrow keys, hover arrows, or swipe (mobile)
- Space bar to flip card
- Track progress with localStorage (mark words as mastered)
- Show progress counter (5/130)
- Don't show mastered words again

DATA STRUCTURE FROM NOTION:
- Name (title): The vocabulary word
- Brief Definition (text): Short definition
- Emotional Texture (text): Synonyms/related words
- Contextual Examples (text): 3 examples separated by \n\n
- Status (select): Filter for "Enriched"

RESPONSIVE:
- Desktop: Keyboard shortcuts, hover arrows
- Mobile: Touch/swipe gestures, tap to flip

ERROR HANDLING:
- Show friendly message if no API key
- Handle network errors gracefully
- Show loading state
- Handle empty states

USER SETUP:
- User provides Notion integration token
- Must share database with integration
- Paste token into HTML file

The app should feel premium, smooth, and polished. Build it production-ready!
```

---

## Full Detailed Brief:

**Download:** [FLASHCARD_APP_BRIEF.md](computer:///mnt/user-data/outputs/FLASHCARD_APP_BRIEF.md)

This contains:
- Complete technical specifications
- Design guidelines with exact measurements
- Code examples and structure
- All interactions and animations
- Error handling
- Responsive behavior
- Implementation phases
- Success criteria
- Edge cases

---

## 🚀 How to Use:

### Option 1: Quick Start
1. Open new Claude Code chat
2. Paste the short version above
3. Claude will ask clarifying questions
4. Provide the full brief if needed

### Option 2: Detailed Start  
1. Open new Claude Code chat
2. Say: "I have a complete project specification. Please read it carefully."
3. Paste the entire FLASHCARD_APP_BRIEF.md content
4. Say: "Please build this. Ask questions if anything is unclear."

---

## 📋 What You'll Get:

A single HTML file that:
- ✅ Works immediately when opened
- ✅ Looks beautiful and premium
- ✅ Fetches your vocabulary from Notion
- ✅ Has smooth animations
- ✅ Tracks your progress
- ✅ Works on phone and desktop
- ✅ Is portfolio-ready

Estimated build time with Claude Code: **2-3 hours**

---

## 🎯 After Building:

1. **Download the HTML file**
2. **Open in code editor**
3. **Add your Notion API key** (line ~10-15)
4. **Save and open in browser**
5. **Start learning!**

---

Ready to start building in Claude Code? 🚀
