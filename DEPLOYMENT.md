# Deployment Guide

This guide provides step-by-step instructions for deploying the Background Remover application.

## Prerequisites

- Docker and Docker Compose (for containerized deployment)
- Python 3.9+ (for local deployment)
- 2GB RAM minimum (4GB recommended)
- Internet connection for downloading AI models

## Local Deployment

### Using Docker Compose (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover
```

2. Build and start the container:
```bash
docker-compose up -d
```

3. Access the application at `http://localhost:8000`

4. To stop the application:
```bash
docker-compose down
```

### Using Docker

1. Build the Docker image:
```bash
docker build -t background-remover .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 --name bg-remover background-remover
```

3. Access the application at `http://localhost:8000`

### Using Python Directly

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

3. Access the application at `http://localhost:8000`

## Cloud Deployment

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

6. Click "Create Web Service"

7. Render will automatically:
   - Detect the `render.yaml` configuration
   - Build the Docker image
   - Deploy the application
   - Provide a URL like `https://background-remover-xxxx.onrender.com`

### Deploy to Railway

1. Go to [Railway](https://railway.app/)

2. Click "Start a New Project"

3. Select "Deploy from GitHub repo"

4. Choose this repository

5. Railway will automatically:
   - Detect the Dockerfile
   - Build and deploy the application
   - Provide a URL

6. Configure environment variables if needed:
   - `PORT`: 8000 (default)

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

You can customize the application using these environment variables:

- `PORT`: Port number for the application (default: 8000)

Example with Docker:
```bash
docker run -d -p 80:80 -e PORT=80 background-remover
```

## Health Check

All deployments should configure health checks:
- **Health Check Endpoint**: `/health`
- **Expected Response**: `{"status":"healthy","service":"background-remover"}`
- **Interval**: 30 seconds
- **Timeout**: 10 seconds

## Scaling Considerations

For production deployments:

1. **Memory**: Allocate at least 2GB RAM, 4GB recommended
2. **CPU**: AI model processing is CPU-intensive
3. **Storage**: Models are downloaded on first run (~200MB)
4. **Timeout**: Set request timeout to at least 30 seconds for large images

## Monitoring

Monitor these metrics:

- Response time for `/api/remove-background`
- Memory usage (should be stable around 500MB-1GB)
- Error rate
- Health check status

## Troubleshooting

### Application won't start
- Check that port 8000 is available
- Ensure sufficient memory (minimum 2GB)
- Verify all dependencies are installed

### Background removal is slow
- First request downloads the AI model (~200MB)
- Subsequent requests should be faster
- Consider using a larger instance size

### Out of memory errors
- Increase memory allocation to 4GB
- Limit concurrent requests
- Implement request queuing

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
