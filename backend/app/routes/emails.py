from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from app.services.gpt_service import generate_email_content
from app.services.email_service import send_email

router = APIRouter()

class EmailRequest(BaseModel):
    recipient: str
    job_role: str
    company_name: str
    recruiter_name: str

@router.post("/send_email/")
def send_recruitment_email(email_request: EmailRequest, background_tasks: BackgroundTasks):
    email_content = generate_email_content(
        email_request.job_role,
        email_request.company_name,
        email_request.recruiter_name
    )

    background_tasks.add_task(
        send_email,
        email_request.recipient,
        f"Exciting Opportunity at {email_request.company_name}",
        email_content
    )

    return {"message": "Email is being sent in the background!"}
