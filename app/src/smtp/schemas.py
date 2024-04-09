from pydantic import BaseModel

class EmailSchemas(BaseModel):
    sender_email: str
    receiver_email: str
    subject: str
    body: str
    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str

