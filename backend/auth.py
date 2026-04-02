# backend/auth.py

from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "smartcampus2026secretkey"
ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ─────────────────────────────────────────────
# HARDCODED USERS FOR DEMO
# ─────────────────────────────────────────────

USERS_DB = {
    # Students
    "arjun@campus.com": {
        "student_id": "student-001",
        "name": "Arjun",
        "password": "arjun123",
        "role": "student"
    },
    "priya@campus.com": {
        "student_id": "student-002",
        "name": "Priya",
        "password": "priya123",
        "role": "student"
    },
    "rahul@campus.com": {
        "student_id": "student-003",
        "name": "Rahul",
        "password": "rahul123",
        "role": "student"
    },
    "sneha@campus.com": {
        "student_id": "student-004",
        "name": "Sneha",
        "password": "sneha123",
        "role": "student"
    },
    # Admin
    "admin@campus.com": {
        "student_id": "admin-001",
        "name": "Admin",
        "password": "admin123",
        "role": "admin"
    },
}


# ─────────────────────────────────────────────
# AUTH FUNCTIONS
# ─────────────────────────────────────────────

def verify_login(email: str, password: str) -> dict | None:
    user = USERS_DB.get(email)
    if not user:
        return None
    if user["password"] != password:
        return None
    return user


def create_token(user: dict) -> str:
    payload = {
        "student_id": user["student_id"],
        "name": user["name"],
        "role": user["role"],
        "email": list(USERS_DB.keys())[
            list(USERS_DB.values()).index(user)
        ],
        "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRE_HOURS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None