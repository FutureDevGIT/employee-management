from flask import Blueprint, request, jsonify
from database import get_db_connection

employee_bp = Blueprint("employee", __name__)

# GET all employees
@employee_bp.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    employees = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()

    return jsonify([dict(emp) for emp in employees]), 200


# GET employee by ID
@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    conn = get_db_connection()
    employee = conn.execute(
        "SELECT * FROM employees WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    if employee is None:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(dict(employee)), 200


# CREATE employee
@employee_bp.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()

    if not all([name, email, department, salary]):
        return jsonify({"error": "All fields are required"}), 400

    if not data:
        return jsonify({"error": "Invalid input"}), 400

    name = data.get("name")
    email = data.get("email")
    department = data.get("department")
    salary = data.get("salary")

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO employees (name, email, department, salary) VALUES (?, ?, ?, ?)",
        (name, email, department, salary),
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee created successfully"}), 201


# UPDATE employee
@employee_bp.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    data = request.get_json()

    conn = get_db_connection()
    conn.execute(
        "UPDATE employees SET name=?, email=?, department=?, salary=? WHERE id=?",
        (
            data["name"],
            data["email"],
            data["department"],
            data["salary"],
            id,
        ),
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee updated"}), 200


# DELETE employee
@employee_bp.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee deleted"}), 200
