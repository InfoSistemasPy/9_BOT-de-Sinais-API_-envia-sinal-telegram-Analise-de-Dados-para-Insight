from sqlite3 import Time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from datetime import datetime
import requests

win = 0
loss = 0
winbranco = 0

chrome_options = Options()
chrome_options.add_argument("-headless")
nav = webdriver.Chrome(options=chrome_options)
nav.get('https://blaze.com/pt/games/double')
cores = []
padraoGeral = True
padrao1 = False
padrao2 = False
padrao3 = False
padrao4 = False
padrao5 = False
padrao6 = False


I_TOKEN = "5294919465:AAH5Ra8-MLyiqJO9lbV0hWSvz8PQq_fsTgw"
I_CHAT_GRUPO = "-705741969"
# MSG MANUTENCAO: ✅ Plis 𝐵𝑂𝑇 Brasil ✅𝑃��� �𝑀𝐴�𝑈�𝐸��̧�̃�𝑂
MSG = "✅ Plis 𝐵𝑂𝑇 Brasil ✅"
I_URL = "https://api.telegram.org/bot" + I_TOKEN + \
    "/sendMessage" + "?chat_id=" + I_CHAT_GRUPO + "&text=" + MSG
I_RESUL = requests.get(I_URL)


def sendMessage(text):
    token = "5294919465:AAH5Ra8-MLyiqJO9lbV0hWSvz8PQq_fsTgw"
    chat_id = "-705741969"
    url_req = "https://api.telegram.org/bot" + token + \
        "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)


while True:
    time.sleep(1.5)
    resp = ""
    respresult = ""
    entrada = False
    resultado = False

    # RESULTADO WIN PADRAO 1
    if padrao1 == True:

        # RESULTADO LOSS PADRAO 1
        if cores[:3] == ['🔴', '🔴', '🔴']:
            loss += 1
            print("Loss")
            respresult = f"LOSS DEU {numero_cor}❌ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

        if cores[:1] == ['⚫️']:
            win += 1
            respresult = f"WIIN ✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True

        if cores[:2] == ['🔴', '⚫️']:
            win += 1
            respresult = f"WIIN G1✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True

        if cores[:3] == ['🔴', '🔴', '⚫️']:
            win += 1
            respresult = f"WIIN G2✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True

          # RESULTADO BRANCO PADRAO 1
        if cores[:1] == ['⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X✅✅✅✅! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

        if cores[:2] == ['🔴', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

        if cores[:3] == ['🔴', '🔴', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

    if padrao2 == True:

        # RESULTADO LOSS PADRAO 2
        if cores[:3] == ['⚫️', '⚫️', '⚫️']:
            loss += 1
            print("Loss")
            respresult = f"LOSS DEU {numero_cor}❌ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

          # RESULTADO WIN PADRAO 2
        if cores[:1] == ['🔴']:
            win += 1
            respresult = f"WIIN ✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:2] == ['⚫️', '🔴']:
            win += 1
            respresult = f"WIIN G1✅✅ ! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:3] == ['⚫️', '⚫️', '🔴']:
            win += 1
            respresult = f"WIIN G2✅✅  \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

          # RESULTADO BRANCO PADRAO 2
        if cores[:1] == ['⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X✅✅✅✅! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:2] == ['⚫️', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:3] == ['⚫️', '⚫️', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

    if padrao3 == True:

        # RESULTADO LOSS PADRAO 3
        if cores[:3] == ['🔴', '🔴', '🔴']:
            loss += 1
            print("Loss")
            respresult = f"LOSS DEU {numero_cor}❌ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True
          # RESULTADO WIN PADRAO 3
        if cores[:1] == ['⚫️']:
            win += 1
            respresult = f"WIIN ✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:2] == ['🔴', '⚫️']:
            win += 1
            respresult = f"WIIN G1✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:3] == ['🔴', '🔴', '⚫️']:
            win += 1
            respresult = f"WIIN G2✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

          # RESULTADO BRANCO PADRAO 3
        if cores[:1] == ['⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X✅✅✅✅! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:2] == ['🔴', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:3] == ['🔴', '🔴', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

    if padrao4 == True:

        # RESULTADO LOSS PADRAO 4
        if cores[:3] == ['⚫️', '⚫️', '⚫️']:
            print("Loss")
            loss += 1
            respresult = f"LOSS DEU {numero_cor}❌ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"

            resultado = True
            padraoGeral = True
            del cores[:]
            padrao4 = False

          # RESULTADO WIN PADRAO 4
        if cores[:1] == ['🔴']:
            win += 1
            respresult = f"WIIN ✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:2] == ['⚫️', '🔴']:
            win += 1
            respresult = f"WIIN G1✅✅  \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:3] == ['⚫️', '⚫️', '🔴']:
            win += 1
            respresult = f"WIIN G2✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

          # RESULTADO BRANCO PADRAO 4
        if cores[:1] == ['⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X✅✅✅✅! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:2] == ['⚫️', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:3] == ['⚫️', '⚫️', '⚪️']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2✅✅✅✅ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

    if resultado == True:
        if respresult:
            sendMessage(respresult)
        resultado == False
        print("Resultado Enviado")

    c = nav.page_source
    soup = BeautifulSoup(c, 'html.parser')
    dat = soup.find('div', class_="time-left")
    if 'Blaze Girou' in dat.getText():
        numero_cor = int(dat.getText().strip("Blaze Girou !"))
        if numero_cor == 0:
            cores.append('⚪️')

        elif numero_cor > 0 and numero_cor < 8:
            cores.append('🔴')
        else:
            cores.append('⚫️')
        print(cores)

        if padraoGeral == True:
            if cores[:3] == ['⚫️', '🔴', '🔴']:
                resp = f"1🔔ENTRADA CONFIRMADA🔔 \n \n APOS O: {numero_cor}  \n \n 📌-ENTRAR : ⚫ [PRETO] \n 📢-PROTEGER : ⚪ [BRANCO] \n ❗️ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao1 = True
                padraoGeral = False

            if cores[:3] == ['🔴', '⚫️', '⚫️']:
                resp = f"2🔔ENTRADA CONFIRMADA🔔 \n \n APOS O: {numero_cor}  \n \n 📌-ENTRAR : 🔴 [VERMELHO] \n 📢-PROTEGER : ⚪ [BRANCO] \n ❗️ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao2 = True
                padraoGeral = False

            if cores[:3] == ['🔴', '🔴', '⚫️']:
                resp = f"3🔔ENTRADA CONFIRMADA🔔 \n \n APOS O: {numero_cor}  \n \n 📌-ENTRAR : ⚫️ [PRETO] \n 📢-PROTEGER : ⚪ [BRANCO] \n ❗️ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao3 = True
                padraoGeral = False

            if cores[:3] == ['⚫️', '⚫️', '🔴']:
                resp = f"4🔔ENTRADA CONFIRMADA🔔 \n \n APOS O: {numero_cor}  \n \n 📌-ENTRAR : 🔴 [VERMELHO] \n 📢-PROTEGER : ⚪ [BRANCO] \n ❗️ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao4 = True
                padraoGeral = False

            if cores[2:] == ['⚫️', '🔴']:
                resp = f"🔔ANALIZANDO MERCADO🔔"
                del cores[:]
                entrada = True

            if cores[2:] == ['🔴', '⚫️']:
                resp = f"🔔ANALIZANDO MERCADO🔔"
                del cores[:]
                entrada = True

        if cores[:4] == ['⚫️', '⚫️', '⚫️', '⚫️']:
            del cores[:]

        if cores[:4] == ['🔴', '🔴', '🔴', '🔴']:
            del cores[:]

        if cores[:3] == ['🔴', '⚫️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚫️', '🔴', '⚫️']:
            del cores[:]

        if cores[:4] == ['🔴', '🔴', '🔴', '⚪️']:
            del cores[:]

        if cores[:4] == ['⚫️', '⚫️', '⚫️', '⚪️']:
            del cores[:]

        if cores[:4] == ['🔴', '🔴', '🔴', '⚫️']:
            del cores[:]

        if cores[:4] == ['⚫️', '⚫️', '⚫️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚫️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '⚪️']:
            del cores[:]

        if cores[:3] == ['⚫️', '⚪️', '⚪️']:
            del cores[:]

        if padrao4 == False:
            if cores[:3] == ['⚫️', '⚫️', '⚪️']:
                del cores[:]

        if cores[:3] == ['⚫️', '⚪️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '🔴', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚫️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '🔴', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚪️', '⚪️']:
            del cores[:]

        if cores[:3] == ['🔴', '⚪️', '⚪️']:
            del cores[:]

        if padrao3 == False:
            if cores[:3] == ['🔴', '🔴', '⚪️']:
                del cores[:]

        if cores[:3] == ['🔴', '⚪️', '🔴']:
            del cores[:]

        if cores[:3] == ['🔴', '⚪️', '⚫️']:
            del cores[:]

        if cores[:3] == ['⚫️', '⚪️', '🔴']:
            del cores[:]

        if cores[:3] == ['⚪️', '🔴', '⚪️']:
            del cores[:]

        if cores[:3] == ['⚪️', '⚫️', '⚪️']:
            del cores[:]

        if cores[:3] == ['⚫️', '🔴', '⚪️']:
            del cores[:]

        if cores[:3] == ['🔴', '⚫️', '⚪️']:
            del cores[:]

        if entrada == True:
            if resp:
                sendMessage(resp)
            entrada == False
            print("Entrada Enviada")

    time.sleep(3.5)
