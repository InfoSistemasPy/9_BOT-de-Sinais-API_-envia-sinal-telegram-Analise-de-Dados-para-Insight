import time
from importlib import reload
from pickle import NONE
from sqlite3 import Time

import telebot
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# por informação do seu bot
api_key = ''
user_id = ''
##############################
bot = telebot.TeleBot(token=api_key)

options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)
    
nav.get('https://blaze.com/pt/games/double')

analisar = 0
gale_atual = 0
analisa_open = 0
resultsDouble = []

while True:
    
    def qualnum(x):
    
        if x == '0':
            return 0
        
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
            if x == '0':
                return '⚪️'
                
            if x == '1':
                return '🔴'

            if x == '2':
                return '🔴'

            if x == '3':
                return '🔴'

            if x == '4':
                return '🔴'

            if x == '5':
                return '🔴'

            if x == '6':
                return '🔴'

            if x == '7':
                return '🔴'

            if x == '8':
                return '⚫'

            if x == '9':
                return '⚫'

            if x == '10':
                return '⚫'

            if x == '11':
                return '⚫'

            if x == '12':
                return '⚫'

            if x == '13':
                return '⚫'

            if x == '14':
                return '⚫'
    try:
        resulROOL = nav.find_element(
        By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        print(erro)
        print('ERRO 403')
    except Exception as erro:
        print('ERRO 404')
        
    
        analisar_open = 0
    if resulROOL == 'Girando...':
        analisar_open = 1
        print('analisando')
        time.sleep(15)
        c = nav.page_source
        resultsDouble.clear()
        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                resultsDouble.append(i.getText())
            else:
                resultsDouble.append('0')
        
        resultsDouble = resultsDouble[:-1]
        
        if analisar_open == 1:
        
            default = resultsDouble[0:3]
            
            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            finalnum = list(mapeando)
            finalcor = list(mapeando2)
            
            def CHECK_VERSION(num):
                global analisar
                global gale_atual
                
                
                if analisar == 0:
                    if num == ['🔴', '🔴', '⚫']:
                        analisar = 1
                        bot.send_message(chat_id=user_id, text= '''
PADRÃO ENCONTRADO🎲
SINAL ENVIADO   
ENTRAR NO 🔴 
COBRIR NO ⚪
                            ''')
                        return
                    if num == ['⚫', '⚫', '🔴']:
                        analisar = 1
                        bot.send_message(chat_id=user_id, text= '''
PADRÃO ENCONTRADO🎲
SINAL ENVIADO   
ENTRAR NO ⚫
COBRIR NO ⚪
                            ''')                    
                        return
                elif analisar == 1:

                     if gale_atual == 0:
                     #WIN #['V', 'V', 'P']
                        if num == ['⚫', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅✅WIN✅✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z) 
                            ''') 
                            return
                        
                        if num == ['🔴', '⚫', '⚫']: 
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅✅WIN✅✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return                     
                        if num == ['⚪️', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN BRANCO✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return                     
                        if num == ['⚪️', '⚫', '⚫']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN BRANCO✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return
                       
                        if num == ['⚫', '⚫', '⚫']:
                            gale_atual = gale_atual+1
                            bot.send_message(chat_id=user_id, text= '''
⚠VAMOS PARA GALE 1⚠
                            ''') 
                            return
                        if num == ['🔴', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
⚠VAMOS PARA GALE 1⚠
                            ''') 
                            return
                      
                     if gale_atual == 1:
                    
                        if num == ['⚫', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN GALE 1✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return
                        
                        if num == ['🔴', '⚫', '⚫']: 
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN GALE 1✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return                     
                        if num == ['⚪️', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN BRANCO GALE 1✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)                            ''') 
                            return                     
                        if num == ['⚪️', '⚫', '⚫']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN BRANCO GALE 1✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z) 
                            ''') 
                            return
                       
                        if num == ['⚫', '⚫', '⚫']:
                            gale_atual = gale_atual+1
                            bot.send_message(chat_id=user_id, text= '''
⚠VAMOS PARA GALE 2⚠
                            ''') 
                            return
                        
                        if num == ['🔴', '🔴', '🔴']:
                            gale_atual = gale_atual+1
                            bot.send_message(chat_id=user_id, text= '''
⚠VAMOS PARA GALE 2⚠
                            ''') 
                            return                        

                     if gale_atual == 2:
                        if num == ['⚫', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN GALE 2✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return
                        
                        if num == ['🔴', '⚫', '⚫']: 
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN GALE 2✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return                     
                        if num == ['⚪️', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN BRANCO GALE 2✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return                     
                        if num == ['⚪️', '⚫', '⚫']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
✅WIN BRANCO GALE 2✅
🎲Jogue agora Blaze Double🎲  
(https://blaze.com/r/nb372Z)
                            ''') 
                            return
 
                        if num == ['🔴', '🔴', '🔴']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
❌LOSS❌
                            ''') 
                            return
                        if num == ['⚫', '⚫', '⚫']:
                            analisar = 0
                            gale_atual = 0
                            bot.send_message(chat_id=user_id, text= '''
❌LOSS❌
                            ''') 
                            return
                            
            checkVersion = CHECK_VERSION(finalcor)
            print(checkVersion)
                     