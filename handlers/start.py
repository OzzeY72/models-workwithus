from dotenv import load_dotenv
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command
from aiogram.types import CallbackQuery
import os

import tempfile

router = Router()

load_dotenv()
API_URL_HTTPS = os.getenv("API_URL_HTTPS")
API_KEY = os.getenv("API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_main_menu():
  return InlineKeyboardMarkup(
      inline_keyboard=[
          # [
          #     InlineKeyboardButton(text="Top Escort", callback_data="show_models:top"),
          #     InlineKeyboardButton(text="Escort", callback_data="show_models:regular"),
          # ],
          # [
          #     InlineKeyboardButton(text="Agencies", callback_data="show_agencyspa:agencies"),
          #     InlineKeyboardButton(text="SPA", callback_data="show_agencyspa:spa"),
          # ],
          [
            InlineKeyboardButton(
                    text="Work with us",
                    web_app=WebAppInfo(url=f"{API_URL_HTTPS}/static/miniapp/index.html")
                )
          ]
          # [
          #     InlineKeyboardButton(text="Work with us", callback_data="work"),
          # ],
      ]
  )

async def hello_message(message: Message):
  photo_path = os.path.join(BASE_DIR, "..", "static","welcome.png")
  welcome_image = FSInputFile(photo_path)

  text = (
      "TEMPLATE\n"
      "Welcome to our massage salon catalogue! 💆\n\n"
      "Discover top escorts, agencies, SPA options, and more.\n"
      "Use the buttons below to navigate."
  )

  await message.answer_photo(photo=welcome_image, caption=text, reply_markup=get_main_menu())

@router.message(Command("start"))
async def start(message: Message):
  await hello_message(message)

@router.callback_query(F.data.startswith("go_home"))
async def go_home(callback: CallbackQuery):
  await hello_message(callback.message)
  await callback.answer()