from sqlalchemy.orm import declarative_base

Base = declarative_base()

from app.models.department import Department
from app.models.user import User
from app.models.doctor import Doctor
from app.models.patient import Patient
from app.models.appointment import Appointment