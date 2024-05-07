from fastapi import APIRouter

from database import get_db
from database.models import UserCard, Transfer, User
from datetime import datetime

card_routers = APIRouter(prefix="/cards",
                          tags=["Cards management"])

#add card
@card_routers.post("/api/add_card")
async def add_card(user_id: int, card_number: int, exp_date: int):
    new_card = UserCard(user_id=user_id, card_number=card_number, exp_date=exp_date)
    if new_card:
        return {"status": 1, "message": "Card successfully added"}
    return {"status":0, "message": "Card wasn't added"}

#get all cards

@card_routers.get("api/cards/")
async def get_all_cards(user_id=0):
    card = get_all_cards(user_id)
    if card:
        return {"status":1, "message": card}
    return {"status": 0, "message": "Card not found"}

# change data
@card_routers.put("api/cards/")
async def change_user_card(user_id: int, card_number: int, exp_date: int):
    if user_id and card_number and exp_date:
        change_user_card(user_id=user_id, new_card_num=card_number, new_exp_date=exp_date)
        return {"status":1, "message":"Card data was successfully changed"}
    return {"status":0, "message":"Error"}

#delete card
@card_routers.delete("api/cards")
async def delete_user_card(user_id: int):
    try:
        delete_user_card(user_id)
        return {"status":1, "message": "Card successfully deleted"}
    except:
        return {"status": 0, "message": "Card wasn't deleted "}


#check a card in database
@card_routers.get("api/cards")
def check_user_card_db(card_number: int):
    db = next(get_db())
    checker_card = db.query(User).filter_by(card_number=card_number).first()
    if checker_card:
        return "This usercard already exist"
    else:
        return "This card not found"
    return True

