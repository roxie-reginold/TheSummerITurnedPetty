# Deployment Checklist

Use this checklist to deploy your app step by step.

## Pre-Deployment Checklist

- [ ] You have a GitHub account
- [ ] You have a Vercel account ([sign up free](https://vercel.com))
- [ ] You have a Google Gemini API key ([get one free](https://aistudio.google.com/app/apikey))
- [ ] You have committed and pushed all changes to GitHub

---

## Backend Deployment (Vercel)

### Task 1: Deploy to Vercel

- [ ] Install Vercel CLI: `npm install -g vercel`
- [ ] Login: `vercel login`
- [ ] Deploy: `vercel --prod`
- [ ] Copy your Vercel URL (shown after deployment)

**Your Vercel URL**: `_______________________________`

### Task 2: Configure Environment Variables

- [ ] Go to [Vercel Dashboard](https://vercel.com/dashboard)
- [ ] Select your project
- [ ] Go to Settings → Environment Variables
- [ ] Add variable:
  - Name: `GOOGLE_API_KEY`
  - Value: (paste your Gemini API key)
  - Environments: ✅ Production ✅ Preview ✅ Development
- [ ] Click Save
- [ ] Redeploy: `vercel --prod`

### Task 3: Test Backend

- [ ] Open: `https://your-project.vercel.app/health`
- [ ] Verify response: `{"status":"ok"}`

---

## Frontend Deployment (GitHub Pages)

### Task 4: Enable GitHub Pages

- [ ] Go to your GitHub repository
- [ ] Click Settings → Pages
- [ ] Under "Build and deployment":
  - Source: **GitHub Actions** (important!)
- [ ] Save

### Task 5: Add GitHub Secret

- [ ] Go to Settings → Secrets and variables → Actions
- [ ] Click "New repository secret"
- [ ] Add secret:
  - Name: `VITE_API_URL`
  - Value: `https://your-project.vercel.app/api` (your Vercel URL + `/api`)
- [ ] Click "Add secret"

### Task 6: Deploy Frontend

Choose one option:

**Option A: Push to GitHub**
```bash
git add .
git commit -m "Configure deployment"
git push origin main
```

**Option B: Manual trigger**
- [ ] Go to Actions tab on GitHub
- [ ] Click "Deploy Frontend to GitHub Pages"
- [ ] Click "Run workflow" → "Run workflow"

### Task 7: Wait for Deployment

- [ ] Go to Actions tab
- [ ] Watch the "Deploy Frontend to GitHub Pages" workflow
- [ ] Wait for green checkmark (1-2 minutes)

### Task 8: Test Frontend

- [ ] Open: `https://YOUR-GITHUB-USERNAME.github.io/TheSummerITurnedPetty/`
- [ ] Enter some text
- [ ] Select a persona
- [ ] Click "Wreck It!"
- [ ] Verify:
  - [ ] Text transforms
  - [ ] Meme appears
  - [ ] Copy button works
  - [ ] Advice appears after copying

**Your GitHub Pages URL**: `_______________________________`

---

## Troubleshooting

### ❌ "AI not configured" error

**Fix:**
- [ ] Verify `GOOGLE_API_KEY` is set in Vercel
- [ ] Redeploy backend: `vercel --prod`
- [ ] Clear browser cache and retry

### ❌ 404 on GitHub Pages

**Fix:**
- [ ] Wait 2-3 more minutes
- [ ] Check Settings → Pages is "GitHub Actions"
- [ ] Check Actions tab for errors

### ❌ API errors in browser console

**Fix:**
- [ ] Verify `VITE_API_URL` secret in GitHub
- [ ] Ensure it ends with `/api`
- [ ] Re-run GitHub Actions workflow
- [ ] Check browser Network tab for actual error

---

## Success! 🎉

Once everything is working:

- [ ] Bookmark your deployed app
- [ ] Share the link with friends
- [ ] Star your repo on GitHub
- [ ] Enjoy wrecking text!

---

## Next Steps

### Updating Your App

**Update Backend:**
```bash
# Make changes to backend/
git push origin main
vercel --prod
```

**Update Frontend:**
```bash
# Make changes to frontend/
git push origin main
# GitHub Actions auto-deploys
```

### Monitoring

- [ ] Vercel Dashboard: Monitor backend logs and usage
- [ ] GitHub Actions: Monitor frontend deployment status
- [ ] Google Cloud Console: Monitor API usage and quotas

---

## Quick Reference

| Service | URL | Environment Variable |
|---------|-----|---------------------|
| **Backend** | `https://your-project.vercel.app` | `GOOGLE_API_KEY` |
| **Frontend** | `https://your-username.github.io/TheSummerITurnedPetty/` | `VITE_API_URL` |

---

## Need Help?

- 📖 Detailed guide: [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
- 🚀 Quick reference: [QUICK_DEPLOY_GUIDE.md](./QUICK_DEPLOY_GUIDE.md)
- 🏗️ Architecture: [ARCHITECTURE.md](./ARCHITECTURE.md)

---

**Deployment completed on**: _______________

**Deployed by**: _______________
