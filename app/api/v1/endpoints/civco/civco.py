from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from app.services.civco.crm_services import get_crm_data

router = APIRouter()

@router.get("/crm", summary="Get CRM data")
def get_crm():
    data = get_crm_data()
    return jsonable_encoder(data)