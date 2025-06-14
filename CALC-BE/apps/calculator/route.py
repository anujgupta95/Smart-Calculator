from fastapi import APIRouter, HTTPException
import base64
from io import BytesIO
from apps.calculator.utils import analyze_image
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post("")
async def run(data: ImageData):
    image_data = base64.b64decode(data.image.split(",")[1])
    image_bytes = BytesIO(image_data)
    image = Image.open(image_bytes)
    responses = analyze_image(image, data.dict_of_vars)
    data = []
    for response in responses:
        data.append(response)
    print(f"Data in Route: {data}")
    return {
        "message" : "Image processed",
        "type" : "success",
        "data" : data,
    }