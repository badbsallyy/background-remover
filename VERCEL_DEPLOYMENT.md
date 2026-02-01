# 🚀 Vercel Deployment Guide

This guide provides step-by-step instructions for deploying the Background Remover application to Vercel.

## Prerequisites

Before you begin, make sure you have:

1. ✅ A GitHub account
2. ✅ A Vercel account (free at [vercel.com](https://vercel.com))
3. ✅ A Pollinations AI API key from [enter.pollinations.ai](https://enter.pollinations.ai)

## Deployment Methods

### Method 1: One-Click Deploy (Fastest) ⚡

1. Click the deploy button:

   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/badbsallyy/background-remover&env=POLLINATION_API_KEY&envDescription=Pollinations%20AI%20API%20key%20for%20background%20removal&envLink=https://enter.pollinations.ai)

2. Sign in to Vercel (if not already signed in)

3. Click "Create" to clone the repository

4. Enter your environment variables:
   - **Name:** `POLLINATION_API_KEY`
   - **Value:** Your Pollinations AI API key
   - Check all three environments: Production, Preview, and Development

5. Click "Deploy"

6. Wait 1-2 minutes for the build to complete

7. Your app is now live! 🎉
   - Click "Visit" to see your deployed application
   - The URL will be something like: `https://your-project-name.vercel.app`

### Method 2: Deploy from GitHub (Recommended) 📦

1. **Fork the repository:**
   - Go to [this repository](https://github.com/badbsallyy/background-remover)
   - Click the "Fork" button in the top-right corner
   - This creates a copy in your GitHub account

2. **Connect to Vercel:**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New..." → "Project"
   - Click "Continue with GitHub"
   - Authorize Vercel to access your GitHub account (if needed)

3. **Import your repository:**
   - Find your forked repository in the list
   - Click "Import"

4. **Configure the project:**
   - **Project Name:** Choose a name (or keep the default)
   - **Framework Preset:** Vercel should auto-detect it (or select "Other")
   - **Root Directory:** Leave as `./` (root)
   - **Build Command:** Leave empty (not needed for this project)
   - **Output Directory:** Leave empty

5. **Add environment variables:**
   - Expand the "Environment Variables" section
   - Add:
     - **Name:** `POLLINATION_API_KEY`
     - **Value:** Your Pollinations AI API key from enter.pollinations.ai
   - Make sure it's set for all three environments:
     - ✅ Production
     - ✅ Preview
     - ✅ Development

6. **Deploy:**
   - Click "Deploy"
   - Wait for the build to complete (usually 1-2 minutes)
   - You'll see a success screen with your deployment URL

7. **Access your app:**
   - Click "Visit" or go to `https://your-project-name.vercel.app`
   - Test the background removal functionality

### Method 3: Deploy with Vercel CLI 💻

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/badbsallyy/background-remover.git
   cd background-remover
   ```

3. **Login to Vercel:**
   ```bash
   vercel login
   ```

4. **Deploy to development:**
   ```bash
   vercel
   ```
   
   Follow the prompts:
   - Set up and deploy? `Y`
   - Which scope? Choose your account
   - Link to existing project? `N`
   - Project name? (press Enter for default)
   - In which directory is your code? `./`
   - Override settings? `N`

5. **Add environment variable:**
   ```bash
   vercel env add POLLINATION_API_KEY
   ```
   
   - Enter your Pollinations AI API key when prompted
   - Select which environments (choose all: production, preview, development)

6. **Deploy to production:**
   ```bash
   vercel --prod
   ```

7. **Your app is live!** The CLI will output your production URL.

## Post-Deployment

### Automatic Deployments

Once connected to GitHub, Vercel automatically deploys:
- **Production:** When you push to `main` branch
- **Preview:** When you create a pull request or push to other branches

### Updating Environment Variables

If you need to change your API key later:

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to "Settings" → "Environment Variables"
4. Find `POLLINATION_API_KEY`
5. Click "Edit" → Enter new value → "Save"
6. Go to "Deployments" → Click "..." on latest deployment → "Redeploy"

### Custom Domain

To add a custom domain:

1. Go to your project in Vercel Dashboard
2. Click "Settings" → "Domains"
3. Add your domain
4. Follow the DNS configuration instructions
5. Wait for DNS propagation (usually 5-10 minutes)

## Testing Your Deployment

After deployment, test these endpoints:

1. **Home Page:**
   - Go to `https://your-project.vercel.app/`
   - You should see the Background Remover UI

2. **Health Check:**
   - Go to `https://your-project.vercel.app/health`
   - Should return: `{"status":"healthy","service":"background-remover"}`

3. **API Documentation:**
   - Go to `https://your-project.vercel.app/docs`
   - You should see the FastAPI Swagger UI

4. **Upload an image:**
   - Use the web UI to upload a test image
   - Verify the background is removed successfully

## Project Structure (Vercel-specific)

```
background-remover/
├── api/                      # Serverless functions
│   ├── index.py             # Main FastAPI application
│   └── requirements.txt     # Python dependencies
├── public/                   # Static files (served by Vercel)
│   ├── index.html
│   ├── script.js
│   └── style.css
├── vercel.json              # Vercel configuration
├── runtime.txt              # Python version specification
└── .vercelignore            # Files to exclude from deployment
```

## Configuration Files

### `vercel.json`

This file configures:
- Build settings (Python serverless functions)
- Routing rules (API endpoints and static files)
- Static file serving from the `public` directory

### `runtime.txt`

Specifies Python version (3.9) for Vercel to use.

### `.vercelignore`

Excludes unnecessary files from deployment to reduce bundle size.

## Troubleshooting

### Build Fails

**Issue:** Build fails with "No such file or directory"
- **Solution:** Make sure all required files exist in your repository
- Check that `api/index.py` and `api/requirements.txt` are present

**Issue:** Build fails with Python errors
- **Solution:** Check that `runtime.txt` specifies Python 3.9
- Verify all dependencies in `requirements.txt` are compatible

### Environment Variables Not Working

**Issue:** API returns "API key not configured"
- **Solution:** 
  1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
  2. Make sure `POLLINATION_API_KEY` is set
  3. Verify it's enabled for all environments
  4. Redeploy the project

**Issue:** Environment variable changes not taking effect
- **Solution:** After changing environment variables, you must redeploy
  - Go to Deployments → Click "..." → "Redeploy"

### Static Files Not Loading

**Issue:** CSS/JS files return 404
- **Solution:** 
  1. Check that files exist in the `public` directory
  2. Verify routing in `vercel.json` is correct
  3. Check file paths in HTML (should be `/style.css`, not `/static/style.css`)

### API Endpoints Not Working

**Issue:** `/api/remove-background` returns 404 or 500
- **Solution:**
  1. Check Vercel function logs: Dashboard → Your Project → Deployments → Click deployment → "Functions" tab
  2. Verify `api/index.py` exists and has no syntax errors
  3. Check that `POLLINATION_API_KEY` is set correctly

### Timeout Errors

**Issue:** Request timeout on image processing
- **Solution:** 
  - Vercel serverless functions have a 10-second timeout on the Hobby plan
  - Upgrade to Pro plan for 60-second timeout if processing large images
  - Or reduce image size before uploading

## Performance Optimization

### Cold Starts

Vercel serverless functions may have "cold starts" (first request takes longer):
- **Expected:** First request may take 3-5 seconds
- **Normal operation:** Subsequent requests are fast (< 1 second)
- **Pro plan:** Reduced cold starts with "Serverless Function Execution" optimization

### Image Size Limits

- **Hobby plan:** 4.5 MB request body limit
- **Pro plan:** 5 MB request body limit
- **Recommendation:** Compress images before upload for better performance

## Cost

### Free (Hobby) Plan Includes:
- ✅ 100 GB bandwidth per month
- ✅ 100,000 serverless function invocations per day
- ✅ Automatic HTTPS
- ✅ Unlimited deployments
- ✅ Preview deployments for PRs

This is usually more than enough for personal projects and small applications.

### Pro Plan ($20/month):
- 1 TB bandwidth
- Longer timeout (60 seconds vs 10 seconds)
- Priority support
- Advanced analytics

## Support

### Resources:
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI on Vercel](https://vercel.com/docs/frameworks/python)
- [Vercel Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [GitHub Repository Issues](https://github.com/badbsallyy/background-remover/issues)

### Common Questions:

**Q: Do I need to pay for Vercel?**
A: No! The free Hobby plan is perfect for this application.

**Q: Can I use my own domain?**
A: Yes! You can add custom domains in the Vercel Dashboard.

**Q: How do I update the application?**
A: Just push to your GitHub repository. Vercel will automatically deploy updates.

**Q: Is my API key safe?**
A: Yes! Environment variables in Vercel are encrypted and never exposed to the client.

**Q: Can I see deployment logs?**
A: Yes! Go to your project → Deployments → Click a deployment → View logs

## Next Steps

After successful deployment:

1. ✅ Test all functionality
2. ✅ Share your deployment URL
3. ✅ Set up a custom domain (optional)
4. ✅ Monitor usage in Vercel Dashboard
5. ✅ Set up automatic deployments from GitHub

---

**Congratulations!** 🎉 Your Background Remover is now live on Vercel!

If you encounter any issues, please open an issue on [GitHub](https://github.com/badbsallyy/background-remover/issues).
