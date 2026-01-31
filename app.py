from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from models import init_db
from auth import register_user, authenticate_user

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "change-this-secret"
jwt = JWTManager(app)

init_db()

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"msg": "Invalid input"}), 400

    if register_user(data["username"], data["password"]):
        return jsonify({"msg": "User registered"}), 201
    return jsonify({"msg": "User already exists"}), 409


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user_id = authenticate_user(data.get("username"), data.get("password"))

    if not user_id:
        return jsonify({"msg": "Invalid credentials"}), 401

    token = create_access_token(identity=str(user_id))
    return jsonify(access_token=token), 200


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    return jsonify({"msg": f"Access granted for user {user_id}"}), 200


if __name__ == "__main__":
    app.run(debug=True)
