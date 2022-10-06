from importlib import reload
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time 
import telegram
import os

os.system('cls')
        #Por informações do seu bot aqui #.
api_key = '' 
user_id = ''
bot = telegram.Bot(token=api_key)

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options=chrome_options)

def convert_cor(q):
    if q == 'Vermelho':
        return '🔴'

    if q == 'Preto':
        return '⚫'


xx = 0
nav.get('https://blaze.com/pt/games/double')
while True:
    time.sleep(3) 
    girando = nav.find_element(By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    



    if girando == 'Girando...':
        xx = 1
        print('Analisando...')
        time.sleep(12)
        pegardados = nav.find_element(By.XPATH, '//*[@id="roulette-recent"]').text
        tfg = pegardados.split()
        def qualnum(x):

            if x == '1':
                return 1

            if x == '2':
                return 2

            if x == '3':
                return 3

            if x == '4':
                return 4

            if x == '5':
                return 5

            if x == '6':
                return 6

            if x == '7':
                return 7

            if x == '8':
                return 8

            if x == '9':
                return 9

            if x == '10':
                return 10

            if x == '11':
                return 11

            if x == '12':
                return 12

            if x == '13':
                return 13

            if x == '14':
                return 14


        def qualcor(x):

            if x == '1':
                return 'Vermelho'

            if x == '2':
                return 'Vermelho'

            if x == '3':
                return 'Vermelho'

            if x == '4':
                return 'Vermelho'

            if x == '5':
                return 'Vermelho'

            if x == '6':
                return 'Vermelho'

            if x == '7':
                return 'Vermelho'

            if x == '8':
                return 'Preto'

            if x == '9':
                return 'Preto'

            if x == '10':
                return 'Preto'

            if x == '11':
                return 'Preto'

            if x == '12':
                return 'Preto'

            if x == '13':
                return 'Preto'

            if x == '14':
                return 'Preto'


        pd = tfg[0:4]
        #dp = tfg[0:1]
        # print(dp)

        mapeando = map(qualnum, pd)
        mapeando2 = map(qualcor, pd)

        finalnum = list(mapeando) 
        finalcor = list(mapeando2)



    if xx == 1:
        xx = 0

        def verificarsaida(num):
                if num == ['Preto','Preto','Preto','Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Vermelho','Vermelho','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Vermelho','Preto','Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto','Preto','Vermelho','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Preto','Vermelho','Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto','Vermelho','Preto','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto','Preto','Preto','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Vermelho','Vermelho','Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Preto','Preto','Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto','Vermelho','Vermelho','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto', 'Preto', 'Vermelho', 'Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto', 'Vermelho', 'Vermelho', 'Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Preto','Preto','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Preto', 'Vermelho', 'Preto', 'Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')

                if num == ['Preto','Preto','Vermelho','Preto']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! 🔴
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
                if num == ['Vermelho','Vermelho','Preto','Vermelho']:
                    return bot.send_message(chat_id=user_id, text='''
🔔⚠️🚨Atenção🚨⚠️🔔 
✅Entrada confirmada! ⚫
✅Proteção no: ⚪️
✅Ate Gale 2 🐓🐓 
🎲Jogue agora Blaze Double🎲  
  (https://blaze.com/r/LnX9VB)      
                                             💬 
por: t.me/xX1chatbot 🥷🏾
                ''')
        print(finalnum)
        print(finalcor)
        testando = verificarsaida(finalcor)
        print(testando)


        #time.sleep(27)
        #print(time.sleep)
