# Image Processing API

This is a FastAPI application that provides image processing capabilities:
1. Convert color images to black and white using OpenCV
2. Remove background from images using rembg

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn main:app --reload
```

The server will start at `http://localhost:8000`

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns welcome message and available endpoints

### 2. Convert Image to Black and White
- **URL**: `/convert-to-bw/`
- **Method**: `POST`
- **Description**: Converts uploaded image to black and white
- **Request Body**: Form data with image file
- **Returns**: Black and white image in JPEG format

### 3. Remove Background
- **URL**: `/remove-background/`
- **Method**: `POST`
- **Description**: Removes the background from the uploaded image
- **Request Body**: Form data with image file
- **Returns**: Transparent PNG image with background removed

## How to Use

### Using cURL

1. Convert to Black and White:
```bash
curl -X POST -F "file=@path_to_your_image.jpg" http://localhost:8000/convert-to-bw/ --output bw_output.jpg
```

2. Remove Background:
```bash
curl -X POST -F "file=@path_to_your_image.jpg" http://localhost:8000/remove-background/ --output no_bg_output.png
```

### Using Python Requests

1. Convert to Black and White:
```python
import requests

files = {'file': open('path_to_your_image.jpg', 'rb')}
response = requests.post('http://localhost:8000/convert-to-bw/', files=files)

with open('bw_output.jpg', 'wb') as f:
    f.write(response.content)
```

2. Remove Background:
```python
import requests

files = {'file': open('path_to_your_image.jpg', 'rb')}
response = requests.post('http://localhost:8000/remove-background/', files=files)

with open('no_bg_output.png', 'wb') as f:
    f.write(response.content)
```

### Using Swagger UI
1. Open `http://localhost:8000/docs` in your browser
2. Try out either endpoint:
   - `/convert-to-bw/` for black and white conversion
   - `/remove-background/` for background removal
3. Upload an image and execute the request 