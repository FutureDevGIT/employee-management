from models.employee import Employee
from extensions import db

class EmployeeService:

    @staticmethod
    def get_all(filters=None, page=None, per_page=None):
        """
        Get all employees with optional filtering and pagination.
        """
        query = Employee.query
        if filters:
            query = query.filter_by(**filters)

        if page and per_page:
            query = query.offset((page - 1) * per_page).limit(per_page)

        return query.all()

    @staticmethod
    def create_employee(data):
        """
        Create a new employee record.
        """
        employee = Employee(**data)
        db.session.add(employee)
        db.session.commit()
        return employee

    @staticmethod
    def get_by_id(emp_id):
        """
        Get employee by ID.
        """
        return Employee.query.get(emp_id)

    @staticmethod
    def update(employee, data):
        """
        Update employee fields.
        """
        for key, value in data.items():
            setattr(employee, key, value)
        db.session.commit()
        return employee

    @staticmethod
    def delete(employee):
        """
        Delete employee record.
        """
        db.session.delete(employee)
        db.session.commit()
