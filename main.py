from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from rembg import remove

app = FastAPI(
    title="Image Processing API",
    description="API to process images: convert to black and white, remove background"
)

@app.post("/convert-to-bw/")
async def convert_to_black_and_white(file: UploadFile = File(...)):
    # Read the image file
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert the image to grayscale (black and white)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Convert the processed image back to bytes
    is_success, buffer = cv2.imencode(".jpg", gray_image)
    if not is_success:
        return {"error": "Failed to convert image"}
    
    # Create a BytesIO object to store the image
    io_buf = BytesIO(buffer)
    io_buf.seek(0)
    
    # Return the processed image as a streaming response
    return StreamingResponse(io_buf, media_type="image/jpeg")

@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    try:
        # Read the image file
        contents = await file.read()
        input_image = Image.open(BytesIO(contents))
        
        # Remove the background
        output_image = remove(input_image)
        
        # Save the result to a bytes buffer
        output_buffer = BytesIO()
        output_image.save(output_buffer, format='PNG')
        output_buffer.seek(0)
        
        # Return the processed image as a streaming response
        return StreamingResponse(output_buffer, media_type="image/png")
    except Exception as e:
        return {"error": f"Failed to process image: {str(e)}"}

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Image Processing API",
        "endpoints": {
            "/convert-to-bw/": "Convert image to black and white",
            "/remove-background/": "Remove background from image"
        }
    } 