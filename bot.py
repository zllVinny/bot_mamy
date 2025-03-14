import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command

# Substitua pelo token do seu bot (do BotFather)
TOKEN = "8091105033:AAHHP_YPvs4zdvbf14l3h_kmRDntk6SkaiE"

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

# Comando /start
async def start(message: types.Message):
    print(f"Mensagem recebida de {message.from_user.first_name}: {message.text}")  # Debug

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔞 Grupo de Prévias", url="https://t.me/+t1UoLIfgBhszOWEx")],
        [InlineKeyboardButton(text="💰 Privacy", url="https://privacy.com.br/checkout/mariarosagacina")],
        [InlineKeyboardButton(text="🐦 Twitter", url="https://x.com/mariarosagacina")],
        [InlineKeyboardButton(text="📸 Instagram", url="https://www.instagram.com/mariarosagacina/")]
    ])

    await message.answer(
        f"Olá, {message.from_user.first_name}! 🔥\n\n"
        "Bem-vindo ao bot da Mamy! ‍🔥🌹👠\n\n"
	"Escolha uma opção abaixo para continuar:",
        reply_markup=keyboard
    )

async def main():
    dp.message.register(start, Command("start"))  # Corrigido para aiogram 3.x
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

# Executando o bot
if __name__ == '__main__':
    asyncio.run(main())