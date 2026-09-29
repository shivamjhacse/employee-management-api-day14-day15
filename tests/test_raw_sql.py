from sqlalchemy import text

from app.db.session import SessionLocal


def test_raw_sql():

    db = SessionLocal()

    try:
        query = text("""
            SELECT
                id,
                name,
                email,
                department,
                designation,
                salary,
                is_active
            FROM employees
        """)

        result = db.execute(query)

        employees = result.mappings().all()

        for employee in employees:
            print(employee)

    finally:
        db.close()

test_raw_sql()

#python -m tests.test_raw_sql