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
# MSG MANUTENCAO: β Plis π΅ππ Brasil βποΏ½οΏ½οΏ½ οΏ½ππ΄οΏ½ποΏ½πΈοΏ½οΏ½Μ§οΏ½ΜοΏ½π
MSG = "β Plis π΅ππ Brasil β"
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
        if cores[:3] == ['π΄', 'π΄', 'π΄']:
            loss += 1
            print("Loss")
            respresult = f"LOSS DEU {numero_cor}β \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

        if cores[:1] == ['β«οΈ']:
            win += 1
            respresult = f"WIIN ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True

        if cores[:2] == ['π΄', 'β«οΈ']:
            win += 1
            respresult = f"WIIN G1ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True

        if cores[:3] == ['π΄', 'π΄', 'β«οΈ']:
            win += 1
            respresult = f"WIIN G2ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao1 = False
            padraoGeral = True

          # RESULTADO BRANCO PADRAO 1
        if cores[:1] == ['βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14Xββββ! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

        if cores[:2] == ['π΄', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

        if cores[:3] == ['π΄', 'π΄', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao1 = False

    if padrao2 == True:

        # RESULTADO LOSS PADRAO 2
        if cores[:3] == ['β«οΈ', 'β«οΈ', 'β«οΈ']:
            loss += 1
            print("Loss")
            respresult = f"LOSS DEU {numero_cor}β \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

          # RESULTADO WIN PADRAO 2
        if cores[:1] == ['π΄']:
            win += 1
            respresult = f"WIIN ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:2] == ['β«οΈ', 'π΄']:
            win += 1
            respresult = f"WIIN G1ββ ! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:3] == ['β«οΈ', 'β«οΈ', 'π΄']:
            win += 1
            respresult = f"WIIN G2ββ  \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

          # RESULTADO BRANCO PADRAO 2
        if cores[:1] == ['βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14Xββββ! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:2] == ['β«οΈ', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

        if cores[:3] == ['β«οΈ', 'β«οΈ', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao2 = False
            padraoGeral = True

    if padrao3 == True:

        # RESULTADO LOSS PADRAO 3
        if cores[:3] == ['π΄', 'π΄', 'π΄']:
            loss += 1
            print("Loss")
            respresult = f"LOSS DEU {numero_cor}β \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True
          # RESULTADO WIN PADRAO 3
        if cores[:1] == ['β«οΈ']:
            win += 1
            respresult = f"WIIN ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:2] == ['π΄', 'β«οΈ']:
            win += 1
            respresult = f"WIIN G1ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:3] == ['π΄', 'π΄', 'β«οΈ']:
            win += 1
            respresult = f"WIIN G2ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

          # RESULTADO BRANCO PADRAO 3
        if cores[:1] == ['βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14Xββββ! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:2] == ['π΄', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

        if cores[:3] == ['π΄', 'π΄', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padrao3 = False
            padraoGeral = True

    if padrao4 == True:

        # RESULTADO LOSS PADRAO 4
        if cores[:3] == ['β«οΈ', 'β«οΈ', 'β«οΈ']:
            print("Loss")
            loss += 1
            respresult = f"LOSS DEU {numero_cor}β \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"

            resultado = True
            padraoGeral = True
            del cores[:]
            padrao4 = False

          # RESULTADO WIN PADRAO 4
        if cores[:1] == ['π΄']:
            win += 1
            respresult = f"WIIN ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:2] == ['β«οΈ', 'π΄']:
            win += 1
            respresult = f"WIIN G1ββ  \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:3] == ['β«οΈ', 'β«οΈ', 'π΄']:
            win += 1
            respresult = f"WIIN G2ββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

          # RESULTADO BRANCO PADRAO 4
        if cores[:1] == ['βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14Xββββ! \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:2] == ['β«οΈ', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G1ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
            del cores[:]

            resultado = True
            padraoGeral = True
            padrao4 = False

        if cores[:3] == ['β«οΈ', 'β«οΈ', 'βͺοΈ']:
            winbranco += 1
            respresult = f"WIIN PAGOU 14X G2ββββ \n Placar | Win - {win} | Loss - {loss} | Win Branco - {winbranco}"
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
            cores.append('βͺοΈ')

        elif numero_cor > 0 and numero_cor < 8:
            cores.append('π΄')
        else:
            cores.append('β«οΈ')
        print(cores)

        if padraoGeral == True:
            if cores[:3] == ['β«οΈ', 'π΄', 'π΄']:
                resp = f"1πENTRADA CONFIRMADAπ \n \n APOS O: {numero_cor}  \n \n π-ENTRAR : β« [PRETO] \n π’-PROTEGER : βͺ [BRANCO] \n βοΈ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao1 = True
                padraoGeral = False

            if cores[:3] == ['π΄', 'β«οΈ', 'β«οΈ']:
                resp = f"2πENTRADA CONFIRMADAπ \n \n APOS O: {numero_cor}  \n \n π-ENTRAR : π΄ [VERMELHO] \n π’-PROTEGER : βͺ [BRANCO] \n βοΈ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao2 = True
                padraoGeral = False

            if cores[:3] == ['π΄', 'π΄', 'β«οΈ']:
                resp = f"3πENTRADA CONFIRMADAπ \n \n APOS O: {numero_cor}  \n \n π-ENTRAR : β«οΈ [PRETO] \n π’-PROTEGER : βͺ [BRANCO] \n βοΈ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao3 = True
                padraoGeral = False

            if cores[:3] == ['β«οΈ', 'β«οΈ', 'π΄']:
                resp = f"4πENTRADA CONFIRMADAπ \n \n APOS O: {numero_cor}  \n \n π-ENTRAR : π΄ [VERMELHO] \n π’-PROTEGER : βͺ [BRANCO] \n βοΈ REALIZAR ATE 2 MARTINGALE!"
                entrada = True
                del cores[:]
                padrao4 = True
                padraoGeral = False

            if cores[2:] == ['β«οΈ', 'π΄']:
                resp = f"πANALIZANDO MERCADOπ"
                del cores[:]
                entrada = True

            if cores[2:] == ['π΄', 'β«οΈ']:
                resp = f"πANALIZANDO MERCADOπ"
                del cores[:]
                entrada = True

        if cores[:4] == ['β«οΈ', 'β«οΈ', 'β«οΈ', 'β«οΈ']:
            del cores[:]

        if cores[:4] == ['π΄', 'π΄', 'π΄', 'π΄']:
            del cores[:]

        if cores[:3] == ['π΄', 'β«οΈ', 'π΄']:
            del cores[:]

        if cores[:3] == ['β«οΈ', 'π΄', 'β«οΈ']:
            del cores[:]

        if cores[:4] == ['π΄', 'π΄', 'π΄', 'βͺοΈ']:
            del cores[:]

        if cores[:4] == ['β«οΈ', 'β«οΈ', 'β«οΈ', 'βͺοΈ']:
            del cores[:]

        if cores[:4] == ['π΄', 'π΄', 'π΄', 'β«οΈ']:
            del cores[:]

        if cores[:4] == ['β«οΈ', 'β«οΈ', 'β«οΈ', 'π΄']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'β«οΈ', 'β«οΈ']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'βͺοΈ', 'β«οΈ']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'βͺοΈ', 'βͺοΈ']:
            del cores[:]

        if cores[:3] == ['β«οΈ', 'βͺοΈ', 'βͺοΈ']:
            del cores[:]

        if padrao4 == False:
            if cores[:3] == ['β«οΈ', 'β«οΈ', 'βͺοΈ']:
                del cores[:]

        if cores[:3] == ['β«οΈ', 'βͺοΈ', 'β«οΈ']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'π΄', 'π΄']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'β«οΈ', 'π΄']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'π΄', 'β«οΈ']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'βͺοΈ', 'π΄']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'βͺοΈ', 'βͺοΈ']:
            del cores[:]

        if cores[:3] == ['π΄', 'βͺοΈ', 'βͺοΈ']:
            del cores[:]

        if padrao3 == False:
            if cores[:3] == ['π΄', 'π΄', 'βͺοΈ']:
                del cores[:]

        if cores[:3] == ['π΄', 'βͺοΈ', 'π΄']:
            del cores[:]

        if cores[:3] == ['π΄', 'βͺοΈ', 'β«οΈ']:
            del cores[:]

        if cores[:3] == ['β«οΈ', 'βͺοΈ', 'π΄']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'π΄', 'βͺοΈ']:
            del cores[:]

        if cores[:3] == ['βͺοΈ', 'β«οΈ', 'βͺοΈ']:
            del cores[:]

        if cores[:3] == ['β«οΈ', 'π΄', 'βͺοΈ']:
            del cores[:]

        if cores[:3] == ['π΄', 'β«οΈ', 'βͺοΈ']:
            del cores[:]

        if entrada == True:
            if resp:
                sendMessage(resp)
            entrada == False
            print("Entrada Enviada")

    time.sleep(3.5)
