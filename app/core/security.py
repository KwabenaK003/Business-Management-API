from passlib.context import CryptContext
# from pydantic import BaseModel, constr, ValidationError

pwd_context = CryptContext(schemes=["bcrypt_sha256"], deprecated="auto",  bcrypt_sha256__rounds=12)

# Hash password
def hash_password(password: str) -> str:
    if not password:
        raise ValueError("Password cannot be empty")
    if len(password) > 1024:  # extremely long passwords rejected
        raise ValueError("Password too long")
    return pwd_context.hash(password[:72])

# Verify password
def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(str(password), hashed)
