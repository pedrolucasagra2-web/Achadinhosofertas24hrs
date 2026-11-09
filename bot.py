import os
import json
import urllib.parse
import urllib.request

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CANAL = "@promocoes24hrd"

def enviar_mensagem(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    dados = urllib.parse.urlencode({
        "chat_id": CANAL,
        "text": texto
    }).encode()

    req = urllib.request.Request(url, data=dados)

    with urllib.request.urlopen(req) as resposta:
        resultado = json.loads(resposta.read())

    if not resultado.get("ok"):
        raise Exception(resultado)

with open("ofertas.json", "r", encoding="utf-8") as arquivo:
    ofertas = json.load(arquivo)

publicadas = 0

for produto in ofertas:
    if produto.get("publicado", False):
        continue

    desconto = produto["desconto"]

    mensagem = f"""
🔥🚨 ACHADINHO IMPERDÍVEL!

📱 {produto['nome']}

❌ De: R$ {produto['preco_antigo']:.2f}
✅ Por: R$ {produto['preco_atual']:.2f}

🔥 {desconto:.1f}% DE DESCONTO!

🛒 COMPRE AQUI:
{produto['link_afiliado']}

⚡ Aproveite enquanto estiver disponível!

📢 @promocoes24hrd
"""

    enviar_mensagem(mensagem)
    produto["publicado"] = True
    publicadas += 1

with open("ofertas.json", "w", encoding="utf-8") as arquivo:
    json.dump(ofertas, arquivo, ensure_ascii=False, indent=2)

print(f"Ofertas publicadas: {publicadas}")
