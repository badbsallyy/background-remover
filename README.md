# 🎨 Background Remover

A simple and effective AI-powered tool for removing backgrounds from images with a beautiful Web UI and REST API.

## ✨ Features

- 🚀 **Fast & Accurate** - AI-powered background removal using U2-Net model
- 🎨 **Beautiful Web UI** - Modern, responsive interface with drag-and-drop support
- 🔌 **REST API** - Easy integration into your applications
- 🐳 **Docker Support** - Containerized for easy deployment
- 🆓 **Free & Open Source** - No registration or API keys required

## 🖼️ How It Works

1. Upload your image (PNG, JPG, JPEG)
2. AI automatically removes the background
3. Download your image with transparent background

## 🚀 Quick Start

### Using Docker (Recommended)

```bash
# Build and run with Docker Compose
docker-compose up -d

# Or build and run manually
docker build -t background-remover .
docker run -p 8000:8000 background-remover
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py
```

The application will be available at `http://localhost:8000`

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
3. Railway will automatically deploy using the Dockerfile

### Deploy to any Docker host

```bash
# Build the image
docker build -t background-remover .

# Run on any port
docker run -p 8080:8000 -e PORT=8000 background-remover
```

## 🛠️ Technology Stack

- **Backend:** FastAPI (Python)
- **AI Model:** U2-Net via rembg library
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Container:** Docker

## 📋 Requirements

- Python 3.9+
- 2GB RAM minimum (4GB recommended)
- Docker (for containerized deployment)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [rembg](https://github.com/danielgatis/rembg) - Background removal library
- [U2-Net](https://github.com/xuebinqin/U-2-Net) - Deep learning model for salient object detection

## 💬 Support

For issues, questions, or suggestions, please open an issue on GitHub.