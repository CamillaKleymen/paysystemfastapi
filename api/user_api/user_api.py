from fastapi import APIRouter
from database.userservice import registration_user_db, get_db, get_all_users_db, edit_user_db, check_user_phone_number
from regex import re
from pydantic import BaseModel

user_router = APIRouter(prefix='/user', tags=['Work with users'])

class UserRegistrationValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    country: str

#validator for number

@user_router.post('/register')
async def register_new_user(data: UserRegistrationValidator):
    new_user_data = data.model_dump()
    regex = re.matchr(r'^(\+998|998)\d{9}$', new_user_data.phone_number)

    if regex:
        return True
    else:
        return False