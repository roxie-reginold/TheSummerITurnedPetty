# 💥 The Summer I Turned Petty - Text Wrecker

A single-page app that "wrecks" user text with hilarious persona-based transformations using AI. Built for hackathon meme-ability and maximum chaos. 🔥

**Live Demo:** [https://roxie-reginold.github.io/TheSummerITurnedPetty/](https://roxie-reginold.github.io/TheSummerITurnedPetty/)

---

## ✨ Features

### 🎭 7 Chaotic Personas
Transform your text with AI-powered personalities:
- **Corporate Robot** - Buzzword-laden business speak
- **Passive-Aggressive Nightmare** - Politely hostile communication
- **Shakespearean Drama King** - Elizabethan theatrical flair
- **Teen Angst Poet** - Melodramatic existential dread
- **Belly** - Emotionally manipulative star-crossed drama
- **Jeremiah** - Overly enthusiastic hype energy
- **Conrad** - Pretentious literary sophistication

### 🎨 Early 2000s Cursed Aesthetic
- Comic Neue font everywhere
- Hot pink containers with neon accents
- Flashing header animation
- Random meme reactions
- Error sound effects on click

### 🤖 AI-Powered Features
- **Text Transformation** - Gemini AI rewrites your text in chosen persona
- **Meme Generation** - Auto-generated memes with custom captions
- **Chaotic Advice** - Post-copy encouragement to "send it anyway"

### 🎯 User Experience
1. Type your message
2. Select a persona
3. Click "Wreck It!" (with chaos confirmation)
4. Get transformed text + reaction meme
5. Copy as image to clipboard
6. Receive terrible life advice

---

## 🏗️ Architecture

```
Frontend (GitHub Pages)
    ↓ HTTPS API calls
Backend (Vercel)
    ↓ AI requests
Google Gemini API
```

### Tech Stack
- **Frontend:** React + Vite + CSS animations
- **Backend:** Flask (Python) + Google Gemini AI
- **Deployment:** GitHub Pages (frontend) + Vercel (backend)
- **Styling:** Google Fonts (Comic Neue) + Custom CSS

---

## 🚀 Quick Start

### Local Development

**Frontend:**
```bash
cd frontend
npm install
npm run dev
# Opens at http://localhost:5173
```

**Backend (optional for local testing):**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Set your Gemini API key
export GOOGLE_API_KEY="your-api-key-here"

python app.py
# Runs at http://localhost:5000
```

Get your Gemini API key: [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 📦 Deployment

We provide comprehensive deployment guides:

### 🎯 Quick Deploy (5 minutes)
See **[QUICK_DEPLOY_GUIDE.md](./QUICK_DEPLOY_GUIDE.md)** for rapid deployment

### 📖 Full Deployment Guide
See **[DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)** for detailed instructions

### ✅ Deployment Checklist
See **[DEPLOYMENT_CHECKLIST.md](./DEPLOYMENT_CHECKLIST.md)** for step-by-step checklist

### 🏗️ Architecture Details
See **[ARCHITECTURE.md](./ARCHITECTURE.md)** for system architecture

**Summary:**
1. **Backend:** Deploy to Vercel with Gemini API key
2. **Frontend:** Deploy to GitHub Pages with backend URL
3. **Total time:** ~5 minutes
4. **Cost:** $0 (free tiers)

---

## 🗂️ Project Structure

```
TheSummerITurnedPetty/
├── frontend/                 # React frontend
│   ├── src/
│   │   ├── App.jsx          # Main app component
│   │   ├── OnlyPans.jsx     # Easter egg feature
│   │   ├── SocialShare.jsx  # Share functionality
│   │   ├── index.css        # Global styles
│   │   └── assets/          # Images
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
├── backend/                  # Flask API
│   ├── app.py               # Main Flask application
│   ├── personas/            # AI persona prompts
│   │   ├── corporate_robot.txt
│   │   ├── passive_aggressive_nightmare.txt
│   │   ├── shakespearean_drama_king.txt
│   │   ├── teen_angst_poet.txt
│   │   ├── belly.txt
│   │   ├── jeremiah.txt
│   │   └── conrad.txt
│   └── requirements.txt
│
├── api/
│   └── index.py             # Vercel serverless entry
│
├── .github/
│   └── workflows/
│       └── deploy-frontend.yml  # GitHub Actions
│
└── vercel.json              # Vercel configuration
```

---

## 🔌 API Endpoints

### `POST /api/wreck`
Transform text with AI persona
```json
Request: { "persona": "Corporate Robot", "text": "Let's talk" }
Response: { "output": "Let's circle back to touch base on synergy alignment" }
```

### `POST /api/meme`
Generate meme with custom captions
```json
Request: { "text": "I sent the text" }
Response: { "url": "https://api.memegen.link/images/custom/..." }
```

### `POST /api/advice`
Get chaotic post-copy advice
```json
Request: { "text": "Should I send this?" }
Response: { "advice": "100% send it. What's the worst that could happen?" }
```

### `GET /health`
Health check endpoint
```json
Response: { "status": "ok" }
```

---

## 🎮 UI Elements

Core DOM elements (for testing/automation):
- `.flashing-text` - Animated header
- `#personalitySelect` - Persona dropdown
- `#userInput` - Text input area
- `#wreckButton` - Transform button
- `#output` - Result display
- `#copyButton` - Copy to clipboard
- `#memeImage` - Generated meme
- `#errorSound` - Sound effect audio

---

## 🔒 Security & Accessibility

### Security
- ✅ No `innerHTML` - All user text rendered safely
- ✅ CORS enabled for GitHub Pages
- ✅ API keys stored securely in environment variables
- ✅ HTTPS everywhere

### Accessibility
- ✅ Keyboard navigation support
- ✅ Labeled form controls
- ✅ High contrast text
- ✅ Screen reader friendly
- ✅ Focus indicators

---

## 🎨 Customization

### Add New Personas
1. Create `backend/personas/new_persona.txt` with prompt
2. Add to `filename_by_persona` dict in `backend/app.py`
3. Add to persona list in `frontend/src/App.jsx`
4. Redeploy

### Modify Styling
Edit `frontend/src/index.css` for:
- Colors (CSS variables)
- Animations
- Layout
- Fonts

---

## 🐛 Troubleshooting

### "AI not configured" error
- Add `GOOGLE_API_KEY` in Vercel environment variables
- Redeploy backend

### Frontend can't reach backend
- Verify `VITE_API_URL` secret in GitHub Actions
- Check CORS settings in `backend/app.py`
- Disable Vercel Deployment Protection

### GitHub Pages 404
- Ensure Pages source is "GitHub Actions"
- Wait 2-3 minutes after deployment
- Check workflow run in Actions tab

---

## 📄 License

MIT License - Feel free to fork and modify!

---

## 🤝 Contributing

Built for [Toronto Stupid Hackathon](https://github.com/sophian098/TorontoStupidHackathon). Contributions welcome!

---

## 🎉 Credits

- **AI:** Google Gemini 2.5 Flash
- **Memes:** memegen.link API
- **Font:** Comic Neue (Google Fonts)
- **Deployment:** Vercel + GitHub Pages
- **Inspiration:** The absolute chaos of modern texting

---

**Made with 💥 and questionable life choices**