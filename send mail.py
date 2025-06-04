from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn, smtplib
from email.message import EmailMessage

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/send")
async def send(request: Request):
    data = await request.json()
    try:
        msg = EmailMessage()
        msg['From'] = data['from']
        msg['To'] = data['to']
        msg['Subject'] = data['subject']
        msg.set_content(data['message'])

        with smtplib.SMTP(data['smtpIp'], 1025) as server:
            server.send_message(msg)

        return "Mail sent successfully!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
