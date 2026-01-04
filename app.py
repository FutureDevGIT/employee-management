from flask import Flask
from extensions import db
from routes.auth_routes import auth_bp
from routes.employee_routes import employee_bp
from routes.frontend_routes import frontend_bp

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(frontend_bp)

@app.errorhandler(404)
def not_found(e):
    return {"error": "Resource not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)