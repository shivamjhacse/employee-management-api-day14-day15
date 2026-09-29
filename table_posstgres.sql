CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    department VARCHAR(50) NOT NULL,
    designation VARCHAR(50) NOT NULL,
    salary NUMERIC(12, 2) NOT NULL CHECK (salary > 0),
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);


