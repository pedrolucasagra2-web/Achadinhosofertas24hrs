import os
import json
import urllib.parse
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CANAL = "@promocoes24hrd"

produto = {
    "nome": "Samsung Galaxy A17 5G",
    "preco_antigo": "R$ 1.855,71",
    "preco_atual": "R$ 989,10",
    "desconto": "46%",
    "link": "https://meli.la/2PvDcUd"
}

mensagem = f"""
🔥🚨 MEGA OFERTA NO MERCADO LIVRE!

📱 {produto['nome']}

❌ De: {produto['preco_antigo']}
✅ POR: {produto['preco_atual']}

🔥 {produto['desconto']} DE DESCONTO!

✔️ 128 GB
✔️ 4 GB RAM
✔️ Câmera de 50 MP
✔️ Tela de 6,7 polegadas
✔️ NFC e proteção IP54

🛒 COMPRE AQUI:
{produto['link']}

⚡ Aproveite enquanto estiver disponível!

📢 @promocoes24hrd
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

dados = urllib.parse.urlencode({
    "chat_id": CANAL,
    "text": mensagem
}).encode()

requisicao = urllib.request.Request(url, data=dados)

with urllib.request.urlopen(requisicao) as resposta:
    resultado = json.loads(resposta.read())

if not resultado["ok"]:
    raise Exception(resultado)

print("Oferta publicada com sucesso!")
