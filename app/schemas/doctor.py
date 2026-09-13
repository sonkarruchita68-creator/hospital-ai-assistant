from pydantic import BaseModel


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    department_id: int


class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    department_id: int