# Deployment Architecture

## Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         USER'S BROWSER                       │
│                                                              │
│  https://YOUR-USERNAME.github.io/TheSummerITurnedPetty/     │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ HTML/CSS/JS
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      GITHUB PAGES                            │
│                   (Frontend - React SPA)                     │
│                                                              │
│  • Static files (HTML, CSS, JS)                             │
│  • Built with Vite                                          │
│  • Served from frontend/dist/                               │
│  • Auto-deployed via GitHub Actions                         │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ HTTPS API Calls
                        │ (POST /api/wreck, /api/meme, /api/advice)
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                         VERCEL                               │
│                  (Backend - Flask API)                       │
│                                                              │
│  • Python serverless functions                              │
│  • api/index.py → backend/app.py                            │
│  • Endpoints:                                               │
│    - POST /api/wreck    (text transformation)              │
│    - POST /api/meme     (meme generation)                  │
│    - POST /api/advice   (chaotic advice)                   │
│    - GET  /health       (health check)                     │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        │ API Calls
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                    GOOGLE GEMINI API                         │
│                  (AI Text Generation)                        │
│                                                              │
│  • Gemini 2.5 Flash model                                   │
│  • Generates persona-based text                             │
│  • Generates meme captions                                  │
│  • Generates chaotic advice                                 │
└─────────────────────────────────────────────────────────────┘
```

## Data Flow

### 1. Text Transformation Flow

```
User Input
    ↓
Frontend (GitHub Pages)
    ↓
POST /api/wreck { persona, text }
    ↓
Backend (Vercel)
    ↓
Gemini API (persona-based transformation)
    ↓
Backend returns { output: "transformed text" }
    ↓
Frontend displays result
```

### 2. Meme Generation Flow

```
User clicks "Wreck It!"
    ↓
Frontend (GitHub Pages)
    ↓
POST /api/meme { text }
    ↓
Backend (Vercel)
    ↓
Gemini API (generates captions)
    ↓
Backend constructs memegen.link URL
    ↓
Backend returns { url: "https://..." }
    ↓
Frontend displays meme image
```

### 3. Advice Flow

```
User clicks "Copy Wreckage"
    ↓
Frontend copies to clipboard
    ↓
POST /api/advice { text }
    ↓
Backend (Vercel)
    ↓
Gemini API (generates chaotic advice)
    ↓
Backend returns { advice: "..." }
    ↓
Frontend displays advice banner
```

## Configuration

### Environment Variables

**Frontend (GitHub Actions Secret)**
```bash
VITE_API_URL=https://your-project.vercel.app/api
```
- Used at build time by Vite
- Injected into the React app as `import.meta.env.VITE_API_URL`
- Falls back to `/api` for local development (proxied by Vite)

**Backend (Vercel Environment Variable)**
```bash
GOOGLE_API_KEY=your_gemini_api_key
```
- Used at runtime by Flask app
- Required for AI features
- Loaded by backend/app.py

### Build Process

**Frontend Build (GitHub Actions)**
```bash
cd frontend
npm ci                 # Install dependencies
VITE_API_URL=${{secrets.VITE_API_URL}} npm run build  # Build with API URL
# Output: frontend/dist/
```

**Backend Build (Vercel)**
```bash
# Vercel automatically:
# 1. Detects Python project
# 2. Installs dependencies from backend/requirements.txt
# 3. Routes requests to api/index.py
# 4. api/index.py imports backend/app.py
```

## File Structure

```
TheSummerITurnedPetty/
├── frontend/                    # React frontend
│   ├── src/
│   │   ├── App.jsx             # Main app (API calls)
│   │   └── ...
│   ├── vite.config.js          # Vite config (base path for GH Pages)
│   └── package.json
│
├── backend/                     # Flask backend
│   ├── app.py                  # Main Flask app
│   ├── personas/               # AI persona prompts
│   └── requirements.txt        # Python dependencies
│
├── api/
│   └── index.py                # Vercel serverless entry point
│
├── .github/
│   └── workflows/
│       └── deploy-frontend.yml # GitHub Actions workflow
│
└── vercel.json                 # Vercel configuration
```

## Security Notes

1. **API Key**: Stored securely in Vercel environment variables
2. **CORS**: Backend allows cross-origin requests from GitHub Pages
3. **No Secrets in Frontend**: Frontend only receives the API endpoint URL
4. **HTTPS**: Both GitHub Pages and Vercel use HTTPS by default

## Performance

- **Frontend**: CDN-served static files (fast global delivery)
- **Backend**: Serverless functions (scales automatically)
- **Cold Starts**: First request may be slower (~1-2s), subsequent requests are fast
- **Caching**: Meme images cached by browser

## Costs

- **GitHub Pages**: Free for public repos
- **Vercel**: Free tier (100GB bandwidth, serverless functions)
- **Gemini API**: Free tier (generous quota for personal use)

**Total cost for typical usage: $0/month** 💰
