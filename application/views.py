from flask import current_app as app, jsonify, request
from flask_security import auth_required, roles_required
from .models import User, db
from .sec import datastore
from werkzeug.security import check_password_hash


@app.get('/')
def home():
    return "hello world"


@app.get('/admin')
@auth_required("token")
@roles_required("admin")
def admin():
    return "Hello Admin"


@app.get('/activate/inst/<int:inst_id>')
@auth_required("token")
@roles_required("admin")
def activate(inst_id):
    instructor = User.query.get(inst_id)
    if not instructor or "inst" not in instructor.roles:
        return jsonify({"message": "instructor is not found"}), 404

    instructor.active = True
    db.session.commit()
    return jsonify({"message": "User activated "})


@app.post("/user-login")
def user_login():
    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"message": "email not provided"}), 400

    user = datastore.find_user(email=email)
    if not user:
        return jsonify({"message": "user not found"}), 404
    if check_password_hash(user.password, data.get("password")):
        return {"token":user.get_auth_token(),"email":user.email,"role":user.roles[0].name }

    else:
        return jsonify({"message": "wrong password"}), 400
