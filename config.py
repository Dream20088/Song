import os

class Config:
    API_ID = int(os.environ.get("API_ID", "25114508")) #Karışmayın
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce") #Karışmayın
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6715543188:AAGn4xU1LF9Hj_VBsvjqqJ_HRux9UQIhChs") #Botunuzun Tokenini Girin .  
