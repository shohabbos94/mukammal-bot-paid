# from environs import Env

# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()

# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili

import os
BOT_TOKEN = str(os.environ.get("BOT_TOKEN")) #bot tokenni olish
ADMINS = list(os.environ.get("ADMINS")) # Adminlar ro'yxatini yuklab olish uchun
IP = str(os.environ.get("ip")) # Hosting ip manzili
# PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN")) 
