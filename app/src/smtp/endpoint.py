from fastapi import APIRouter
from app.src.smtp import smtpemail,schemas
from app.src.smtp.smtpemail import send_email


router = APIRouter(prefix="/smtp" , tags=["smtp"])

@router.post("/send-email/" ,tags=["SMTP"])
def send_email_api(email:schemas.EmailSchemas):
        send_email(email)
        return {"message": "Email sent successfully!"}
