# 🎨 Background Remover

A simple and effective API-powered tool for removing backgrounds from images with a beautiful Web UI and REST API.

## ✨ Features

- 🚀 **Fast & Accurate** - Powered by Pollinations AI for professional-quality background removal
- 🎨 **Beautiful Web UI** - Modern, responsive interface with drag-and-drop support
- 🔌 **REST API** - Easy integration into your applications
- ☁️ **Serverless Ready** - Optimized for Vercel deployment
- 🔑 **API Key Based** - No heavy models to download, uses cloud-based processing

## 🖼️ How It Works

1. Upload your image (PNG, JPG, JPEG)
2. API automatically removes the background using Pollinations AI
3. Download your image with transparent background

## 🔑 Setup

### Prerequisites

1. Get a Pollinations AI API key from [https://enter.pollinations.ai](https://enter.pollinations.ai)
2. Copy `.env.example` to `.env`
3. Add your API key to `.env`:
   ```
   POLLINATION_API_KEY=your_actual_api_key_here
   ```

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/background-remover.git
cd background-remover

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your POLLINATION_API_KEY

# Run the application
python main.py
```

The application will be available at `http://localhost:8000`

### Using Docker

```bash
# Build the Docker image
docker build -t background-remover .

# Run the container with your API key
docker run -p 8000:8000 -e POLLINATION_API_KEY=your_api_key background-remover
```

## 📚 API Documentation

### Remove Background

**Endpoint:** `POST /api/remove-background`

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: Image file (PNG, JPG, JPEG)

**Response:**
- Content-Type: image/png
- Body: PNG image with transparent background

**Example using cURL:**

```bash
curl -X POST -F "file=@your-image.jpg" http://localhost:8000/api/remove-background -o result.png
```

**Example using Python:**

```python
import requests

with open('your-image.jpg', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/remove-background',
        files={'file': f}
    )

with open('result.png', 'wb') as f:
    f.write(response.content)
```

**Example using JavaScript:**

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

const response = await fetch('/api/remove-background', {
    method: 'POST',
    body: formData
});

const blob = await response.blob();
const url = URL.createObjectURL(blob);
```

### Health Check

**Endpoint:** `GET /health`

Returns the health status of the service.

### API Documentation

Visit `/docs` for interactive API documentation (Swagger UI).

## 🌐 Deployment

### Deploy to Vercel (Recommended)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/badbsallyy/background-remover&env=POLLINATION_API_KEY&envDescription=Pollinations%20AI%20API%20key%20for%20background%20removal&envLink=https://enter.pollinations.ai)

**Quick Deploy:**
1. Click the "Deploy with Vercel" button above
2. Sign in to Vercel (free account)
3. Add your `POLLINATION_API_KEY` environment variable
4. Click "Deploy"
5. Your app will be live in 1-2 minutes! 🎉

**Detailed Instructions:**
See [VERCEL_DEPLOYMENT.md](./VERCEL_DEPLOYMENT.md) for comprehensive deployment guide including:
- One-click deployment
- GitHub integration
- CLI deployment
- Troubleshooting
- Custom domains

**Important:** Remember to add your `POLLINATION_API_KEY` in Vercel's environment variables section (Project Settings → Environment Variables).

### Deploy to Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. Fork this repository
2. Create a new Web Service on Render
3. Connect your repository
4. Render will automatically detect the `render.yaml` configuration
5. Click "Deploy"

### Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app)

1. Click the button above
2. Select this repository
3. Add environment variable `POLLINATION_API_KEY`
4. Railway will automatically deploy the application

### Deploy to any Docker host

```bash
# Build the image
docker build -t background-remover .

# Run with your API key
docker run -p 8080:8000 -e PORT=8000 -e POLLINATION_API_KEY=your_api_key background-remover
```

## 🛠️ Technology Stack

- **Backend:** FastAPI (Python)
- **Image Processing:** Pollinations AI
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Deployment:** Vercel (Serverless)

## 📋 Requirements

- Python 3.9+
- Pollinations AI API key (free tier available)
- Internet connection for API calls

## 🔑 API Key

Get your free Pollinations AI API key at [https://enter.pollinations.ai](https://enter.pollinations.ai)

- Free tier: Daily pollen grants available
- Pro plans available for higher usage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Pollinations AI](https://pollinations.ai/) - Open-source multimodal AI API
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework for building APIs

## 💬 Support

For issues, questions, or suggestions, please open an issue on GitHub.