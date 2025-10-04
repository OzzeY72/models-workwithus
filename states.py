from aiogram.fsm.state import State, StatesGroup

class CreateMaster(StatesGroup):
  name = State()
  age = State()
  phonenumber = State()
  address = State()
  height = State()
  weight = State()
  cupsize = State()
  clothsize = State()
  price_1h = State()
  price_2h = State()
  price_full_day = State()
  photo = State()

class EditMaster(StatesGroup):
  view = State()
  field = State()  
  value = State()

class SearchMasters(StatesGroup):
  selecting_param = State()
  entering_value = State()

class CreateApplication(StatesGroup):
  name = State()
  age = State()
  phonenumber = State()
  address = State()
  height = State()
  weight = State()
  cupsize = State()
  clothsize = State()
  price_1h = State()
  price_2h = State()
  price_full_day = State()
  photo = State()

class CreateAgencySpa(StatesGroup):
    name = State()
    phone = State()
    address = State()
    photos = State()