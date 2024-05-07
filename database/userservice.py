from database.models import User
from database import get_db
from datetime import datetime

def registration_user_db(name, surname, email, phone_number, password, country, reg_date):
    db = next(get_db())
    new_user = User(name=name, surname=surname, email=email, phone_number=phone_number, password=password, country=country,
                        reg_date=datetime.now())
    db.add(new_user)
    db.commit()
    return f'This user {name} successfully passed registration'

# check username, useremail, usernum
def check_user_db(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user
    else:
        return 'User not found'


# getting data about user
def get_all_users_db(user_id):
    db = next(get_db())
    all_users = db.query(User).all()
    return all_users

def check_user_phone_number(phone_number):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()
    if checker:
        return checker
    else:
        return 'Num phone not found'

# change data
def edit_user_db(user_id, edit_info, new_info):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()
    if exact_user:
        try:
            if edit_info == "name":
                exact_user.name = new_info
                db.commit()
                return True
            elif edit_info == "phone_number":
                exact_user.phone_number = new_info
                db.commit()
                return True
            elif edit_info == "email":
                exact_user.email = new_info
                db.commit()
                return True
            elif edit_info == "country":
                exact_user.user_city = new_info
                db.commit()
                return True
            elif edit_info == "password":
                exact_user.password = new_info
                db.commit()
                return f'Data of this {user_id} was successfully changed'
            db.commit()
        except:
            return "Unfortunately at this moment changing of data unavailable"
    return False

#Deleting info
def delete_user_db(user_id):
    db = next(get_db())
    user_to_delete = db.query(User).filter_by(user_id=user_id).first()
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()
        return f'This user was deleted'
    return f'Unfortunately this user wasnt deleted'