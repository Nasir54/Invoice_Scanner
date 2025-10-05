from database.db_utils import Session
from database.models import User
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password, email):
    session = Session()
    try:
        if session.query(User).filter_by(username=username).first():
            return False, "Username already exists"
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password, email=email)
        session.add(new_user)
        session.commit()
        return True, "User created successfully"
    finally:
        session.close()

def authenticate_user(username, password):
    session = Session()
    try:
        user = session.query(User).filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user.id
        return None
    finally:
        session.close()
