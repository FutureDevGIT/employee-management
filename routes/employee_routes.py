from flask import Blueprint, request, jsonify
from services.employee_service import EmployeeService
from schemas.employee_schema import EmployeeSchema
from utils.auth import token_required

employee_bp = Blueprint("employee_bp", __name__, url_prefix="/employees")
schema = EmployeeSchema()

# GET all employees with optional pagination & filtering
@employee_bp.route("/", methods=["GET"])
@token_required
def get_employees():
    page = request.args.get("page", type=int)
    per_page = request.args.get("per_page", type=int)
    filters = {}
    department = request.args.get("department")
    if department:
        filters["department"] = department

    employees = EmployeeService.get_all(filters=filters, page=page, per_page=per_page)
    return jsonify([emp.to_dict() for emp in employees]), 200

# GET employee by ID
@employee_bp.route("/<int:emp_id>", methods=["GET"])
@token_required
def get_employee(emp_id):
    employee = EmployeeService.get_by_id(emp_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404
    return jsonify(employee.to_dict()), 200

# POST create employee
@employee_bp.route("/", methods=["POST"])
@token_required
def create_employee():
    data = request.get_json()
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    employee = EmployeeService.create(data)
    return jsonify(employee.to_dict()), 201

# PUT update employee
@employee_bp.route("/<int:emp_id>", methods=["PUT"])
@token_required
def update_employee(emp_id):
    employee = EmployeeService.get_by_id(emp_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    data = request.get_json()
    errors = schema.validate(data, partial=True)
    if errors:
        return jsonify(errors), 400

    updated = EmployeeService.update(employee, data)
    return jsonify(updated.to_dict()), 200

# DELETE employee
@employee_bp.route("/<int:emp_id>", methods=["DELETE"])
@token_required
def delete_employee(emp_id):
    employee = EmployeeService.get_by_id(emp_id)
    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    EmployeeService.delete(employee)
    return jsonify({"message": "Employee deleted"}), 200
