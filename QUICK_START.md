# 🚀 Quick Start Guide

Get the Background Remover running in under 5 minutes!

## Prerequisites

**Get a Clipdrop API Key (Free)**
1. Visit [https://clipdrop.co/apis](https://clipdrop.co/apis)
2. Sign up for a free account
3. Copy your API key
4. Free tier: 100 API calls/month

## Option 1: Local Python (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add: CLIPDROP_API_KEY=your_actual_api_key

# Run
python main.py

# Open browser to http://localhost:8000
```

## Option 2: Docker

```bash
# Clone and build
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover
docker build -t background-remover .

# Run with your API key
docker run -p 8000:8000 -e CLIPDROP_API_KEY=your_api_key background-remover

# Open browser to http://localhost:8000
```

## Option 3: Deploy to Vercel (Recommended for Production)

### One-Click Deploy
[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)

### Manual Deploy
1. Fork this repository
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click "Add New Project"
4. Import your forked repository
5. Add environment variable:
   - Name: `CLIPDROP_API_KEY`
   - Value: Your Clipdrop API key
6. Click "Deploy"
7. Done! Your app is live at `https://your-project.vercel.app`

## Option 4: Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. Click button above
2. Connect your GitHub account
3. Select this repository
4. Add environment variable `CLIPDROP_API_KEY`
5. Click "Deploy"

## Option 5: Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

1. Click button above
2. Connect repository
3. Add environment variable `CLIPDROP_API_KEY`
4. Deploy automatically

## Test the API

```bash
# Test health endpoint
curl http://localhost:8000/health

# Remove background from an image
curl -X POST -F "file=@your-image.jpg" \
  http://localhost:8000/api/remove-background \
  -o result.png
```

## View API Documentation

Open `http://localhost:8000/docs` in your browser for interactive API docs.

## Need Help?

- See `README.md` for detailed documentation
- See `DEPLOYMENT.md` for deployment options
- Open an issue on GitHub for support
