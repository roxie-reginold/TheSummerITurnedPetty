# Quick Deployment Guide

## 🚀 5-Minute Deployment

### Step 1: Deploy Backend to Vercel (2 minutes)

```bash
# Install Vercel CLI if you haven't
npm install -g vercel

# Login
vercel login

# Deploy
vercel --prod
```

**After deployment:**
1. Copy your Vercel URL (e.g., `https://your-project.vercel.app`)
2. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
3. Add: `GOOGLE_API_KEY` = your Gemini API key ([get key here](https://aistudio.google.com/app/apikey))
4. Redeploy: `vercel --prod`

---

### Step 2: Deploy Frontend to GitHub Pages (2 minutes)

```bash
# 1. Enable GitHub Pages
# Go to: GitHub repo → Settings → Pages → Source: "GitHub Actions"

# 2. Add API URL secret
# Go to: GitHub repo → Settings → Secrets and variables → Actions
# Add secret: 
#   Name: VITE_API_URL
#   Value: https://your-project.vercel.app/api

# 3. Push to trigger deployment
git add .
git commit -m "Deploy frontend"
git push origin main
```

**Wait 1-2 minutes**, then visit:
```
https://YOUR-GITHUB-USERNAME.github.io/TheSummerITurnedPetty/
```

---

## ✅ Quick Verification

### Test Backend
```bash
curl https://your-project.vercel.app/health
# Should return: {"status":"ok"}
```

### Test Frontend
Open your GitHub Pages URL and try wrecking some text!

---

## 🔧 Common Issues

### "AI not configured" error
- ✅ Add `GOOGLE_API_KEY` in Vercel
- ✅ Redeploy Vercel backend
- ✅ Add `VITE_API_URL` in GitHub secrets
- ✅ Re-run GitHub Actions

### 404 on GitHub Pages
- ✅ Wait 2-3 minutes after deployment
- ✅ Check Settings → Pages is set to "GitHub Actions"
- ✅ Check Actions tab for deployment status

---

## 📋 URLs to Remember

- **Backend (Vercel)**: https://your-project.vercel.app
- **Frontend (GitHub Pages)**: https://your-username.github.io/TheSummerITurnedPetty/
- **Vercel Dashboard**: https://vercel.com/dashboard
- **GitHub Actions**: https://github.com/your-username/TheSummerITurnedPetty/actions

---

For detailed instructions, see [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)
