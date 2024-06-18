from fastapi import APIRouter
from app.models.request import AdditionRequest
from app.models.response import AdditionResponse
from app.add_library.addition import add_numbers

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_list_of_numbers(request: AdditionRequest):
    return add_numbers(request)

# @router.get("/")
# async def home():
#     await "this is home page."