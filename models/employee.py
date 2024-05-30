from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import date
from enum import Enum
from uuid import uuid4


# Define an enum class for the employee status
class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    retired = "retired"


class GenderEnum(str, Enum):
    male = "male"
    female = "female"
    other = "other"


# Define a base model for the employee
class Employee(BaseModel):
    emp_id: Optional[str] = Field(default_factory=lambda: str(uuid4()), read_only=True)
    emp_name: str = Field(min_length=3, max_length=50)
    emp_gender: GenderEnum
    emp_status: StatusEnum
    emp_email: EmailStr
    emp_address: str
    emp_phone: str = Field(min_length=10, max_length=10, pattern=r"^[0-9]{10}$")
    emp_designation: str
    emp_department: str
    emp_salary: float = Field(gt=0)
    emp_skills: List[str] = Field(min_items=1, default_factory=list)
    created_date: Optional[str] = Field(
        default=date.today().isoformat(),
        title="Created at",
        read_only=True,
        description="The date of creation",
    )
    created_time: Optional[str] = Field(
        default=datetime.now().time().isoformat(),
        title="Created at",
        read_only=True,
        description="The time of creation",
    )

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "emp_name": "Alice",
                    "emp_gender": "female",
                    "emp_status": "active",
                    "emp_email": "alice@example.com",
                    "emp_address": "123 Main Street",
                    "emp_phone": "9876543210",
                    "emp_designation": "software engineer",
                    "emp_department": "ESBU",
                    "emp_salary": 50000.0,
                    "emp_skills": ["Communication", "Leadership", "Negotiation"],
                }
            ]
        }
