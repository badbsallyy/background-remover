# 🎨 Background Remover

A simple and effective API-powered tool for removing backgrounds from images with a beautiful Web UI and REST API.

## ✨ Features

- 🚀 **Fast & Accurate** - Powered by Clipdrop API for professional-quality background removal
- 🎨 **Beautiful Web UI** - Modern, responsive interface with drag-and-drop support
- 🔌 **REST API** - Easy integration into your applications
- ☁️ **Serverless Ready** - Optimized for Vercel deployment
- 🔑 **API Key Based** - No heavy models to download, uses cloud-based processing

## 🖼️ How It Works

1. Upload your image (PNG, JPG, JPEG)
2. API automatically removes the background using Clipdrop
3. Download your image with transparent background

## 🔑 Setup

### Prerequisites

1. Get a Clipdrop API key from [https://clipdrop.co/apis](https://clipdrop.co/apis)
2. Copy `.env.example` to `.env`
3. Add your API key to `.env`:
   ```
   CLIPDROP_API_KEY=your_actual_api_key_here
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
# Edit .env and add your CLIPDROP_API_KEY

# Run the application
python main.py
```

The application will be available at `http://localhost:8000`

### Using Docker

```bash
# Build the Docker image
docker build -t background-remover .

# Run the container with your API key
docker run -p 8000:8000 -e CLIPDROP_API_KEY=your_api_key background-remover
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

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone)

1. Click the "Deploy with Vercel" button above or go to [Vercel](https://vercel.com)
2. Import this repository
3. Add environment variable:
   - `CLIPDROP_API_KEY`: Your Clipdrop API key
4. Click "Deploy"
5. Your app will be live at `https://your-app.vercel.app`

**Important:** Remember to add your `CLIPDROP_API_KEY` in Vercel's environment variables section (Project Settings → Environment Variables).

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
3. Add environment variable `CLIPDROP_API_KEY`
4. Railway will automatically deploy the application

### Deploy to any Docker host

```bash
# Build the image
docker build -t background-remover .

# Run with your API key
docker run -p 8080:8000 -e PORT=8000 -e CLIPDROP_API_KEY=your_api_key background-remover
```

## 🛠️ Technology Stack

- **Backend:** FastAPI (Python)
- **Image Processing:** Clipdrop API (by Stability AI)
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Deployment:** Vercel (Serverless)

## 📋 Requirements

- Python 3.9+
- Clipdrop API key (free tier available)
- Internet connection for API calls

## 🔑 API Key

Get your free Clipdrop API key at [https://clipdrop.co/apis](https://clipdrop.co/apis)

- Free tier: 100 API calls/month
- Pro plans available for higher usage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Clipdrop](https://clipdrop.co/) - Background removal API by Stability AI
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework for building APIs

## 💬 Support

For issues, questions, or suggestions, please open an issue on GitHub.