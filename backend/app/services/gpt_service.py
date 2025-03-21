from openai import OpenAI
from app.core.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_email_content(job_role, company_name, recruiter_name):
    prompt = (
        f"Write a professional and personalized recruitment email from {recruiter_name} "
        f"at {company_name}, inviting candidates to apply for the {job_role} position. "
        f"Make it engaging and encourage a reply."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a professional recruiter email writer."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
