from sqlalchemy.orm import Session
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from app.repositories import employee_repository
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
    EmployeePatch
)

def create_employee(db: Session, employee_data: dict):
    try:
        return employee_repository.create_employee(
            db,
            employee_data
        )

    except IntegrityError as e:
        if "employees_email_key" in str(e.orig):
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

        raise HTTPException(
            status_code=400,
            detail="Database constraint violated"
        )

def get_employees(
    page: int,
    limit: int,
    sort: str | None,
    order: str,
    db: Session
):
    employees = employee_repository.get_employees(
        page,
        limit,
        sort,
        order,
        db
    )

    if not employees:
        raise HTTPException(
            status_code=404,
            detail="No employees found"
        )

    return {
    "msg": "data fetched",
    "page": page,
    "count": len(employees),
    "data": employees
}


def getone_employee(emp_id:int,db:Session):
    employee= employee_repository.getone_employee(emp_id,db)
    if employee:
        return {"msg":"data fetched","data":employee}
    else:
        raise HTTPException(
            status_code=404,
            detail={"msg":"Employee not found"}
        )

    
def update_employee(
    emp_id: int,
    employee_data: EmployeeUpdate,
    db: Session
):
    try:
        emp = employee_repository.update_employee(
            emp_id,
            employee_data.model_dump(),
            db
        )

    except IntegrityError as e:
        if "employees_email_key" in str(e.orig):
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

        raise HTTPException(
            status_code=400,
            detail="Database constraint violated"
        )

    if emp is None:
        raise HTTPException(
            status_code=404,
            detail={"msg": "Id not found"}
        )

    return {
        "msg": "data updated",
        "data": emp
    }


def delete_employee(emp_id: int, db: Session):

    employee = employee_repository.delete_emp(emp_id, db)

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail={"msg": "Employee not found"}
        )

    return {"msg": "Employee deleted", "data": employee}



def search_employee(
    search: str,
    page: int,
    limit: int,
    db: Session
):
    employees = employee_repository.search_employee(
        search,
        page,
        limit,
        db
    )

    if not employees:
        raise HTTPException(
            status_code=404,
            detail={"msg": "No employee found"}
        )

    return {
        "msg": "employees found",
        "data": employees
    }

def get_by_department(department: str, db: Session):

    employees = employee_repository.get_by_department(
        department,
        db
    )

    if not employees:
        raise HTTPException(
            status_code=404,
            detail={"msg": "No employees found in this department"}
        )

    return {
        "msg": "employees found",
        "data": employees
    }



def patch_employee(
    emp_id: int,
    employee_data: EmployeePatch,
    db: Session
):
    data = employee_data.model_dump(exclude_unset=True)

    if not data:
        raise HTTPException(
            status_code=400,
            detail="At least one field is required"
        )

    try:
        employee = employee_repository.patch_employee(
            emp_id,
            data,
            db
        )

    except IntegrityError as e:
        if "employees_email_key" in str(e.orig):
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

        raise HTTPException(
            status_code=400,
            detail="Database constraint violated"
        )

    if employee is None:
        raise HTTPException(
            status_code=404,
            detail={"msg": "Employee not found"}
        )

    return {
        "msg": "Employee partially updated",
        "data": employee
    }