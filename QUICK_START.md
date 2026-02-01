# 🚀 Quick Start Guide

Get the Background Remover running in under 2 minutes!

## Option 1: Docker Compose (Easiest)

```bash
# Clone and run
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover
docker-compose up -d

# Open browser to http://localhost:8000
```

## Option 2: Python

```bash
# Clone and install
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover
pip install -r requirements.txt

# Run
python main.py

# Open browser to http://localhost:8000
```

## Option 3: One-Click Deploy

### Deploy to Render
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. Click button above
2. Connect your GitHub account
3. Select this repository
4. Click "Deploy"

### Deploy to Railway
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

1. Click button above
2. Connect repository
3. Deploy automatically

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
