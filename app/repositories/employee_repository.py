from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.employee import Employee
from sqlalchemy.exc import IntegrityError



def create_employee(db: Session, employee_data: dict):
    try:
        employee = Employee(**employee_data)

        db.add(employee)
        db.commit()
        db.refresh(employee)

        return employee

    except IntegrityError:
        db.rollback()
        raise
    

    

def get_employees(
    page: int,
    limit: int,
    sort: str | None,
    order: str,
    db: Session
):
    offset = (page - 1) * limit

    stmt = select(Employee)

    if sort == "name":
        if order == "desc":
            stmt = stmt.order_by(Employee.name.desc())
        else:
            stmt = stmt.order_by(Employee.name.asc())

    stmt = stmt.offset(offset).limit(limit)

    result = db.execute(stmt)
    employees = result.scalars().all()

    return employees

def getone_employee(emp_id:int,db:Session):
    employee= select(Employee).where(Employee.id==emp_id)
    result=db.execute(employee)
    emp = result.scalar_one_or_none()
    return emp


def update_employee(emp_id: int, employee_data: dict, db: Session):
    emp = select(Employee).where(Employee.id == emp_id)
    result = db.execute(emp)
    employee = result.scalar_one_or_none()

    if employee is None:
        return None

    try:
        for key, value in employee_data.items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)

        return employee

    except IntegrityError:
        db.rollback()
        raise


def delete_emp(emp_id: int, db: Session):

    emp = select(Employee).where(Employee.id == emp_id)

    result = db.execute(emp)

    employee = result.scalar_one_or_none()

    if employee is None:
        return None

    db.delete(employee)
    db.commit()

    return employee



def search_employee(
    search: str,
    page: int,
    limit: int,
    db: Session
):
    offset = (page - 1) * limit

    stmt = (
        select(Employee)
        .where(
            Employee.name.ilike(f"%{search}%")
        )
        .offset(offset)
        .limit(limit)
    )

    result = db.execute(stmt)

    employees = result.scalars().all()

    return employees


def get_by_department(department: str, db: Session):

    emp = select(Employee).where(
        Employee.department == department
    )

    result = db.execute(emp)

    employees = result.scalars().all()

    return employees



def patch_employee(
    emp_id: int,
    employee_data: dict,
    db: Session
):
    stmt = select(Employee).where(Employee.id == emp_id)

    result = db.execute(stmt)

    employee = result.scalar_one_or_none()

    if employee is None:
        return None

    try:
        for key, value in employee_data.items():
            setattr(employee, key, value)

        db.commit()
        db.refresh(employee)

        return employee

    except IntegrityError:
        db.rollback()
        raise





