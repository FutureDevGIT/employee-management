from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.employee_service import EmployeeService

frontend_bp = Blueprint("frontend", __name__)

@frontend_bp.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("frontend.login"))

    employees = EmployeeService.get_all()
    return render_template("employees.html", employees=employees)

@frontend_bp.route("/add", methods=["GET", "POST"])
def add_employee():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "department": request.form["department"],
            "salary": request.form["salary"]
        }

        try:
            EmployeeService.create_employee(data)
            flash("Employee added successfully", "success")
            return redirect(url_for("frontend.home"))
        except Exception:
            flash("Failed to add employee", "danger")
    return render_template("add_employee.html")

@frontend_bp.route("/edit/<int:emp_id>", methods=["GET", "POST"])
def edit_employee(emp_id):
    employee = EmployeeService.get_by_id(emp_id)

    if not employee:
        flash("Employee not found", "warning")
        return redirect(url_for("frontend.home"))

    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "department": request.form["department"],
            "salary": request.form["salary"]
        }
        try:
            EmployeeService.update(employee, data)
            flash("Employee updated successfully", "success")
            return redirect(url_for("frontend.home"))
        except Exception:
            flash("Update failed", "danger")
            return redirect(url_for("frontend.home"))

    return render_template("edit_employee.html", employee=employee)

@frontend_bp.route("/delete/<int:emp_id>")
def delete_employee(emp_id):
    employee = EmployeeService.get_by_id(emp_id)

    if not employee:
        flash("Employee not found", "warning")
    else:
        EmployeeService.delete(employee)
        flash("Employee deleted successfully", "success")

    return redirect(url_for("frontend.home"))

@frontend_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin":
            session["user"] = request.form["username"]
            flash("Login successful", "success")
            return redirect("/")
        else:
            flash("Invalid credentials", "danger")
    return render_template("login.html")

@frontend_bp.route("/logout")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "info")
    return redirect("/login")