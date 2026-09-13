from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import departments,auth,doctor,patient,appointment,upload,chat,pdf_reader

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(
    departments.router,
    prefix="/departments",
    tags=["Departments"]
)
app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)
app.include_router(
    doctor.router,
    prefix="/doctors",
    tags=["Doctors"]
)
app.include_router(
    patient.router,
    prefix="/patients",
    tags=["Patients"]
)
app.include_router(
    appointment.router,
    prefix="/appointments",
    tags=["Appointments"]
)
app.include_router(
    upload.router,
    prefix="/upload",
    tags=["Documents"]
)
app.include_router(
    chat.router,
    prefix="/chat",
    tags=["Chatbot"]
)
app.include_router(
    pdf_reader.router,
    prefix="/pdf",
    tags=["PDF Reader"]
)
@app.get("/")
def root():
    return {"message": "Hospital AI Assistant is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

