import os
import json
import urllib.parse
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CANAL = "@promocoes24hrd"

mensagem = (
    "🤖 Robô Achadinhos Ofertas 24hrs está conectado!\n\n"
    "Em breve você receberá nossas ofertas!"
)

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

dados = urllib.parse.urlencode({
    "chat_id": CANAL,
    "text": mensagem
}).encode()

requisicao = urllib.request.Request(url, data=dados)

with urllib.request.urlopen(requisicao) as resposta:
    resultado = json.loads(resposta.read())

print("Mensagem publicada!" if resultado["ok"] else resultado)
