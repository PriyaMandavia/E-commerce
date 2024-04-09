from fastapi import APIRouter
from app.src.business import endpoint as businessendpoint
from app.src.owner import endpoint as ownerendpoint
from app.src.product import endpoint as productendpoint

# app = FastAPI()
router = APIRouter()

router.include_router(businessendpoint.router)
router.include_router(ownerendpoint.router)
router.include_router(productendpoint.router)





