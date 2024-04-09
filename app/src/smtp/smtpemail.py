from fastapi import HTTPException

from app.src.smtp.schemas import EmailSchemas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import settings

# env = Environment(
#     loader=PackageLoader('app', 'templates'),
#     autoescape=select_autoescape(['html', 'xml'])
# )




        

        
def send_email(email: EmailSchemas):
        # template = env.get_template(f'{template}.html')

        msg= MIMEMultipart()
        msg['From'] = email.sender_email
        msg['To'] = email.receiver_email
        msg['Subject'] = email.subject
        msg.attach(MIMEText(email.body, 'plain'))
        # msg.attach(MIMEText(html, 'html'))
        try:
            server = smtplib.SMTP(email.smtp_server, email.smtp_port)
            server.starttls()
            server.login(email.smtp_username, email.smtp_password)
            server.sendmail(email.sender_email, email.receiver_email, msg.as_string())
            server.quit()
        except smtplib.SMTPException as e:
            raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

    