from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
    EmployeeListResponse,
    EmployeeSingleResponse,
    EmployeeDeleteResponse,
    EmployeePatch
)
import logging

logger = logging.getLogger(__name__)

from app.core.dependencies import get_db
from app.services import employee_service

router = APIRouter()


@router.post("/employees", status_code=201)
def create_emp(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    logger.info(f"Creating employee: {employee.name}")

    employee_data = employee.model_dump()

    result = employee_service.create_employee(
        db,
        employee_data
    )

    logger.info(f"Employee created successfully: {employee.name}")

    return result


@router.get("/employees", response_model=EmployeeListResponse)
def get_employees(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
    search: str | None = None,
    department: str | None = None,
    sort: str | None = None,
    order: str = Query(default="asc"),
    db: Session = Depends(get_db)
):
    logger.info(
        f"Fetching employees | page={page}, limit={limit}, "
        f"search={search}, department={department}, "
        f"sort={sort}, order={order}"
    )

    if search:
        logger.info(f"Searching employees: {search}")

        return employee_service.search_employee(
            search,
            page,
            limit,
            db
        )

    if department:
        logger.info(f"Filtering employees by department: {department}")

        return employee_service.get_by_department(
            department,
            db
        )

    logger.info(f"Fetching employee list with sorting: {sort} {order}")

    return employee_service.get_employees(
        page,
        limit,
        sort,
        order,
        db
    )


@router.get(
    "/employees/{emp_id}",
    response_model=EmployeeSingleResponse
)
def getone_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    logger.info(f"Fetching employee with ID: {emp_id}")

    result = employee_service.getone_employee(
        emp_id,
        db
    )

    logger.info(f"Employee fetch completed for ID: {emp_id}")

    return result


@router.put(
    "/employees/{emp_id}",
    response_model=EmployeeSingleResponse
)
def update_employee(
    emp_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    logger.info(f"Updating employee with ID: {emp_id}")

    result = employee_service.update_employee(
        emp_id,
        employee_data,
        db
    )

    logger.info(f"Employee updated successfully: {emp_id}")

    return result


@router.delete(
    "/employees/{emp_id}",
    response_model=EmployeeDeleteResponse
)
def delete_employee(
    emp_id: int,
    db: Session = Depends(get_db)
):
    logger.info(f"Deleting employee with ID: {emp_id}")

    result = employee_service.delete_employee(
        emp_id,
        db
    )

    logger.info(f"Employee deleted successfully: {emp_id}")

    return result


@router.patch(
    "/employees/{emp_id}",
    response_model=EmployeeSingleResponse
)
def patch_employee(
    emp_id: int,
    employee_data: EmployeePatch,
    db: Session = Depends(get_db)
):
    logger.info(f"Partially updating employee: {emp_id}")

    result = employee_service.patch_employee(
        emp_id,
        employee_data,
        db
    )

    logger.info(f"Employee partially updated successfully: {emp_id}")

    return result