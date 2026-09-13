from fastapi import APIRouter, Depends

from app.api.v1.deps import get_current_user

router = APIRouter()

departments = []

@router.get("/")
def get_departments():
    return departments

@router.post("/")
def create_department(
    name: str,
    current_user: dict = Depends(get_current_user)
):
    department = {
        "id": len(departments) + 1,
        "name": name
    }

    departments.append(department)

    return {
        "department": department,
        "created_by": current_user["user_id"]
    }