from flask import Flask
from routes import employee_bp

app = Flask(__name__)
app.register_blueprint(employee_bp)

@app.route("/")
def home():
    return {"message": "Employee Management API Running"}

if __name__ == "__main__":
    app.run(debug=True)
