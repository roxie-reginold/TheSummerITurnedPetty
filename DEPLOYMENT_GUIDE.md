# Deployment Guide

This guide will help you deploy the Text Wrecker app with:
- **Backend** on Vercel (Python/Flask API)
- **Frontend** on GitHub Pages (React static site)

## Prerequisites

- A GitHub account
- A Vercel account (free tier is fine)
- A Google Gemini API key ([get one here](https://aistudio.google.com/app/apikey))

---

## Part 1: Deploy Backend to Vercel

### Step 1: Install Vercel CLI (optional but recommended)
```bash
npm install -g vercel
```

### Step 2: Deploy to Vercel

**Option A: Using Vercel CLI**
```bash
# Login to Vercel
vercel login

# Deploy
vercel

# Follow the prompts:
# - Link to existing project? N
# - What's your project's name? text-wrecker-backend (or any name)
# - In which directory is your code located? ./
# - Deploy? Y
```

**Option B: Using Vercel Dashboard**
1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "Add New Project"
3. Import your GitHub repository
4. Vercel will auto-detect the configuration from `vercel.json`
5. Click "Deploy"

### Step 3: Configure Environment Variables in Vercel

After deployment, you need to add your Gemini API key:

1. Go to your project in Vercel Dashboard
2. Click "Settings" → "Environment Variables"
3. Add the following variable:
   - **Name**: `GOOGLE_API_KEY`
   - **Value**: Your Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - **Environment**: Production, Preview, Development (select all)
4. Click "Save"
5. Redeploy your project (go to Deployments tab, click the three dots on the latest deployment, and select "Redeploy")

### Step 4: Note Your Backend URL

After deployment, Vercel will give you a URL like:
```
https://your-project-name.vercel.app
```

Save this URL - you'll need it for the frontend configuration!

---

## Part 2: Deploy Frontend to GitHub Pages

### Step 1: Enable GitHub Pages in Your Repository

1. Go to your GitHub repository
2. Click "Settings" → "Pages"
3. Under "Build and deployment":
   - **Source**: Select "GitHub Actions"
4. Save the settings

### Step 2: Add GitHub Secret for API URL

1. In your GitHub repository, go to "Settings" → "Secrets and variables" → "Actions"
2. Click "New repository secret"
3. Add:
   - **Name**: `VITE_API_URL`
   - **Value**: `https://your-project-name.vercel.app/api` (use your actual Vercel URL from Part 1)
4. Click "Add secret"

### Step 3: Trigger Deployment

The GitHub Actions workflow is already configured! To deploy:

**Option A: Push to main branch**
```bash
git add .
git commit -m "Configure deployment"
git push origin main
```

**Option B: Manual trigger**
1. Go to your repository on GitHub
2. Click "Actions" tab
3. Select "Deploy Frontend to GitHub Pages" workflow
4. Click "Run workflow" → "Run workflow"

### Step 4: Wait for Deployment

1. Go to the "Actions" tab in your repository
2. Watch the workflow run (it takes 1-2 minutes)
3. Once complete (green checkmark), your site will be live!

### Step 5: Access Your App

Your app will be available at:
```
https://your-username.github.io/TheSummerITurnedPetty/
```

For example, if your GitHub username is `johndoe`:
```
https://johndoe.github.io/TheSummerITurnedPetty/
```

---

## Verification

### Test Backend
Visit your Vercel URL:
```bash
curl https://your-project-name.vercel.app/health
```

Should return:
```json
{"status":"ok"}
```

### Test Frontend
1. Open your GitHub Pages URL
2. Enter some text
3. Click "Wreck It!"
4. You should see transformed text and a meme

---

## Troubleshooting

### Frontend shows "AI not configured" or API errors

**Cause**: The frontend can't reach the backend, or the backend doesn't have the API key.

**Solution**:
1. Check that `VITE_API_URL` secret in GitHub is set correctly
2. Check that `GOOGLE_API_KEY` is set in Vercel
3. Verify your Vercel backend URL is accessible
4. Redeploy both frontend and backend

### GitHub Pages shows 404

**Cause**: GitHub Pages might not be enabled correctly.

**Solution**:
1. Go to Settings → Pages
2. Ensure "Source" is set to "GitHub Actions"
3. Wait a few minutes after deployment
4. Check the Actions tab for any errors

### CORS errors in browser console

**Cause**: Browser is blocking requests from GitHub Pages to Vercel.

**Solution**: The backend should already handle CORS properly. If you see this error:
1. Check your backend logs in Vercel
2. Ensure the frontend is using the correct API URL
3. Verify the VITE_API_URL includes `/api` at the end

### Vercel deployment fails

**Cause**: Missing dependencies or configuration issues.

**Solution**:
1. Check the build logs in Vercel dashboard
2. Ensure `backend/requirements.txt` exists and has all dependencies
3. Ensure `api/index.py` is present and correct
4. Try deploying again

---

## Local Development

To run locally:

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend will run on `http://localhost:5000`

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend will run on `http://localhost:5173` with API proxied to backend.

---

## Updating Your Deployment

### Update Backend
```bash
# Make your changes to backend/
git add backend/
git commit -m "Update backend"
git push origin main

# Then in Vercel, it will auto-deploy, or run:
vercel --prod
```

### Update Frontend
```bash
# Make your changes to frontend/
git add frontend/
git commit -m "Update frontend"
git push origin main

# GitHub Actions will automatically deploy
```

---

## Environment Variables Reference

### Backend (Vercel)
- `GOOGLE_API_KEY` - Your Gemini API key (required for AI features)
- Alternative names also work: `GEMINI_API_KEY`, `GOOGLE_GENAI_API_KEY`, `GENAI_API_KEY`

### Frontend (GitHub Actions)
- `VITE_API_URL` - Your Vercel backend URL with `/api` path (e.g., `https://your-project.vercel.app/api`)

---

## Cost

Both services offer free tiers:
- **Vercel**: Free tier includes 100GB bandwidth, serverless functions
- **GitHub Pages**: Free for public repositories
- **Google Gemini API**: Free tier includes generous quota

---

## Support

If you encounter issues:
1. Check the Actions tab on GitHub for frontend deployment logs
2. Check the Vercel dashboard for backend deployment logs
3. Check browser console for frontend errors
4. Check Vercel function logs for backend errors

---

## Summary Checklist

- [ ] Deploy backend to Vercel
- [ ] Add `GOOGLE_API_KEY` to Vercel environment variables
- [ ] Note your Vercel backend URL
- [ ] Enable GitHub Pages (Source: GitHub Actions)
- [ ] Add `VITE_API_URL` secret to GitHub
- [ ] Push code to trigger GitHub Actions deployment
- [ ] Wait for deployment to complete
- [ ] Test your app at `https://your-username.github.io/TheSummerITurnedPetty/`

Happy deploying! 💥
