# Deployment Guide

This guide provides step-by-step instructions for deploying the Background Remover application.

## Prerequisites

- Pollinations AI API key (get it from https://enter.pollinations.ai)
- Python 3.9+ (for local deployment)
- Internet connection for API calls

## Local Deployment

### Using Python Directly (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your POLLINATION_API_KEY
```

4. Run the application:
```bash
python main.py
```

5. Access the application at `http://localhost:8000`

### Using Docker

1. Build the Docker image:
```bash
docker build -t background-remover .
```

2. Run the container with your API key:
```bash
docker run -d -p 8000:8000 -e POLLINATION_API_KEY=your_api_key --name bg-remover background-remover
```

3. Access the application at `http://localhost:8000`

## Cloud Deployment

### Deploy to Vercel (Recommended)

Vercel provides the fastest and easiest serverless deployment for this application.

#### Method 1: Deploy via Vercel Dashboard (Recommended)

1. **Prerequisites:**
   - GitHub account
   - Vercel account (free) at [vercel.com](https://vercel.com)
   - Pollinations AI API key from [enter.pollinations.ai](https://enter.pollinations.ai)

2. **Fork and import:**
   - Fork this repository to your GitHub account
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New..." → "Project"
   - Import your forked repository

3. **Configure environment variables:**
   - In the import screen, expand "Environment Variables"
   - Add: `POLLINATION_API_KEY` = `your_actual_api_key`
   - Make sure to add it for Production, Preview, and Development environments

4. **Deploy:**
   - Click "Deploy"
   - Wait for the build to complete (usually 1-2 minutes)
   - Your app will be live at `https://your-project.vercel.app`

5. **Update environment variables later (if needed):**
   - Go to your project in Vercel Dashboard
   - Settings → Environment Variables
   - Add/Edit `POLLINATION_API_KEY`
   - Redeploy from Deployments tab

#### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   cd background-remover
   vercel
   ```

4. **Follow the prompts:**
   - Link to existing project or create new one
   - Set up project settings
   - Add environment variable when prompted:
     - `POLLINATION_API_KEY`: Your API key

5. **For production deployment:**
   ```bash
   vercel --prod
   ```

#### Method 3: One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/badbsallyy/background-remover&env=POLLINATION_API_KEY&envDescription=Pollinations%20AI%20API%20key%20for%20background%20removal&envLink=https://enter.pollinations.ai)

1. Click the button above
2. Enter your Pollinations AI API key when prompted
3. Click "Deploy"
4. Your app will be live in minutes!

**Vercel Deployment Features:**
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Automatic deployments on git push
- ✅ Zero downtime deployments
- ✅ Serverless functions (no servers to manage)
- ✅ Free tier available

**Important Notes:**
- The application uses Vercel's serverless function architecture
- Static files are served from the `public` directory
- API endpoints are automatically routed through `/api/`
- Environment variables are configured in Vercel Dashboard
- Automatic deployments trigger on every push to main branch

### Deploy to Render

1. Fork this repository to your GitHub account

2. Go to [Render Dashboard](https://dashboard.render.com/)

3. Click "New +" and select "Web Service"

4. Connect your GitHub repository

5. Configure the service:
   - **Name**: background-remover
   - **Environment**: Docker
   - **Region**: Choose closest to your users
   - **Branch**: main
   - **Plan**: Free (or higher for production)

6. Add environment variable:
   - Key: `POLLINATION_API_KEY`
   - Value: Your Pollinations AI API key

7. Click "Create Web Service"

8. Render will automatically:
   - Detect the `render.yaml` configuration
   - Build the Docker image
   - Deploy the application
   - Provide a URL like `https://background-remover-xxxx.onrender.com`

### Deploy to Railway

1. Go to [Railway](https://railway.app/)

2. Click "Start a New Project"

3. Select "Deploy from GitHub repo"

4. Choose this repository

5. Add environment variable:
   - Key: `POLLINATION_API_KEY`
   - Value: Your Pollinations AI API key

6. Railway will automatically:
   - Detect the Dockerfile
   - Build and deploy the application
   - Provide a URL

### Deploy to Heroku

1. Install the Heroku CLI

2. Login to Heroku:
```bash
heroku login
```

3. Create a new Heroku app:
```bash
heroku create your-app-name
```

4. Set the stack to container:
```bash
heroku stack:set container
```

5. Deploy:
```bash
git push heroku main
```

6. Open your application:
```bash
heroku open
```

### Deploy to DigitalOcean App Platform

1. Go to [DigitalOcean App Platform](https://cloud.digitalocean.com/apps)

2. Click "Create App"

3. Select "GitHub" as the source

4. Choose this repository

5. Configure:
   - **Name**: background-remover
   - **Environment Type**: Web Service
   - **Instance Size**: Basic (1GB RAM minimum)
   - **HTTP Port**: 8000

6. Click "Create Resources"

### Deploy to AWS (Elastic Beanstalk)

1. Install the EB CLI:
```bash
pip install awsebcli
```

2. Initialize EB:
```bash
eb init -p docker background-remover
```

3. Create an environment and deploy:
```bash
eb create background-remover-env
```

4. Open the application:
```bash
eb open
```

## Environment Variables

The application requires the following environment variable:

- `POLLINATION_API_KEY`: Your Pollinations AI API key (required)
- `PORT`: Port number for the application (default: 8000, optional)

### Setting Environment Variables

**Vercel:**
- Project Settings → Environment Variables → Add `POLLINATION_API_KEY`

**Render:**
- Environment tab → Add `POLLINATION_API_KEY`

**Railway:**
- Variables tab → Add `POLLINATION_API_KEY`

**Docker:**
```bash
docker run -d -p 80:80 -e PORT=80 -e POLLINATION_API_KEY=your_key background-remover
```

**Local Development:**
```bash
cp .env.example .env
# Edit .env and add your POLLINATION_API_KEY
```

## Health Check

All deployments should configure health checks:
- **Health Check Endpoint**: `/health`
- **Expected Response**: `{"status":"healthy","service":"background-remover"}`
- **Interval**: 30 seconds
- **Timeout**: 10 seconds

## Scaling Considerations

For production deployments:

1. **Memory**: Minimal memory required (serverless functions use ~128MB)
2. **Timeout**: Set request timeout to at least 60 seconds for large images and AI processing
3. **API Limits**: Monitor your Pollinations AI usage and pollen balance
4. **Rate Limiting**: Consider implementing rate limiting for public endpoints

## Monitoring

Monitor these metrics:

- Response time for `/api/remove-background`
- API call success/error rate
- Pollinations AI usage and pollen balance
- Health check status

## Troubleshooting

### Application won't start
- Check that `POLLINATION_API_KEY` is set correctly
- Verify API key is valid at enter.pollinations.ai
- Check application logs for error messages

### Background removal fails
- Verify API key is valid
- Check pollen balance hasn't been exceeded
- Ensure image format is supported (PNG, JPG, JPEG)
- Check image size (large images may take longer to process)

### API rate limiting
- Check your Pollinations AI pollen balance
- Implement client-side rate limiting
- Consider upgrading your Pollinations AI tier

## Security

- CORS is configured to allow all origins by default
- For production, modify `main.py` to restrict origins:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-domain.com"],
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)
```

## Updates

To update the deployed application:

1. Make changes to the code
2. Commit and push to your repository
3. Most platforms will auto-deploy on push
4. Or manually trigger a deployment from the platform dashboard

## Support

For issues or questions:
- Open an issue on GitHub
- Check the README for documentation
- Visit `/docs` for API documentation
