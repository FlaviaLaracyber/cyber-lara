from flask import Flask, request, jsonify
app = Flask(__name__)

def resposta_guardiao(msg):
    msg = msg.lower()
    if "python" in msg:
        return "🐍 Python é nossa arma aqui em Cyber-Indaiatuba! Flask deixa tudo online rápido. Quer ver meu código no GitHub?"
    if "lara" in msg or "quem é você" in msg or "você" in msg:
        return "Eu sou o Guardião de Cyber-Indaiatuba, criado pela Lara Ananias, Dev Python Jr de Indaiatuba-SP! 🛡️"
    if "vaga" in msg or "trabalho" in msg or "estágio" in msg:
        return "A Lara tá buscando vaga Jr/Estágio Backend Python! Indaiatuba ou remoto. Contrata ela! 🚀 LinkedIn na tela!"
    if "cidade" in msg or "cyber" in msg:
        return "Cyber-Indaiatuba: 47 drones, néon infinito, e código Python rodando 24h. Você tá dentro dela agora!"
    if "oi" in msg or "olá" in msg or "ola" in msg:
        return "Olá, visitante! Bem-vindo à Cyber-Indaiatuba! Pergunta algo sobre Python, vaga ou a cidade!"
    return f"Interessante! Você disse: '{msg}'. Me pergunta sobre Python, sobre a Lara ou sobre nossa cidade!"

@app.route("/")
def home():
    return """
<body style="margin:0; background:#000; color:white; font-family:monospace;">
<div style="position:fixed; inset:0; background:url('https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=1920') center/cover; filter:brightness(0.3); z-index:-1;"></div>
<div style="background:linear-gradient(90deg,red,orange); color:white; text-align:center; padding:8px; font-size:11px; letter-spacing:2px; font-weight:bold;">⚠️ CYBER-INDAIATUBA v2 ONLINE - GUARDIÃO COM IA - LARA ANANIAS ⚠️</div>
<div style="max-width:1100px; margin:auto; padding:20px; display:flex; gap:20px; flex-wrap:wrap;">
<div style="flex:1.2; background:rgba(0,0,0,0.85); border:1px solid #00ff88; border-radius:16px; padding:24px; backdrop-filter:blur(10px);">
<h1 style="font-size:50px; margin:0; line-height:0.9;">LARA<br><span style="color:#ff3333;">ANANIAS</span></h1>
<p style="color:#00ff88;">> Dev Python Jr. | Backend Flask | API</p>
<p style="color:#ccc; font-size:13px; border-left:3px solid #ff3333; padding-left:12px; margin:15px 0;">Criei meu mundo cibernético Cyber-Indaiatuba com Python. De erro .txt pra cidade neon online com IA.</p>
<div style="margin:20px 0; background:#0a0a0a; border:1px solid #333; border-radius:12px; padding:12px; height:240px; display:flex; flex-direction:column;">
<div id="chat" style="flex:1; overflow-y:auto; font-size:12px; color:#00ff88; line-height:1.6;"><div style="color:#666; background:#111; padding:8px; border-radius:8px;">🤖 Guardião: Fala, visitante! Eu tô online! Pergunta sobre Python, vaga ou cidade...</div></div>
<div style="display:flex; gap:8px; margin-top:10px;">
<input id="msg" placeholder="Digite aqui..." style="flex:1; background:#000; border:1px solid #00ff88; color:white; padding:10px 14px; border-radius:20px; font-size:12px; outline:none;">
<button onclick="enviar()" style="background:#00ff88; color:black; border:none; padding:10px 18px; border-radius:20px; font-weight:bold; cursor:pointer;">ENVIAR</button>
</div>
</div>
<a href="https://www.linkedin.com/in/lara-ananias-267994437" target="_blank" style="background:#00ff88; color:black; padding:10px 22px; text-decoration:none; border-radius:20px; font-weight:bold; display:inline-block; font-size:12px;">Meu LinkedIn ↗</a>
<a href="https://github.com/FlaviaLaracyber/cyber-lara" target="_blank" style="margin-left:8px; font-size:10px; color:#888; text-decoration:none; border:1px solid #333; padding:8px 12px; border-radius:20px;">github.com/FlaviaLaracyber/cyber-lara</a>
</div>
<div style="flex:0.8; text-align:center;">
<div style="font-size:140px; filter:drop-shadow(0 0 30px red);">🤖</div>
<div style="background:black; border:1px solid #ff3333; color:#00ff88; font-size:10px; padding:8px 14px; border-radius:20px; margin-top:10px; display:inline-block; letter-spacing:1px;">CHAT IA ATIVO • v2 • 47 DRONES • ONLINE</div>
<div style="margin-top:15px; font-size:9px; color:#555;">Indaiatuba-SP | Python | Flask | Render</div>
</div>
</div>
<script>
async function enviar(){
  let input = document.getElementById('msg');
  let chat = document.getElementById('chat');
  let texto = input.value.trim(); if(!texto) return;
  chat.innerHTML += `<div style='color:white; margin:6px 0; background:#222; padding:6px 10px; border-radius:12px; text-align:right;'>Você: ${texto}</div>`;
  input.value = '';
  chat.scrollTop = chat.scrollHeight;
  let res = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({message:texto})});
  let data = await res.json();
  chat.innerHTML += `<div style='color:#00ff88; margin:6px 0; background:#0a1a0a; padding:6px 10px; border-radius:12px; border-left:2px solid #00ff88;'>🤖 Guardião: ${data.reply}</div>`;
  chat.scrollTop = chat.scrollHeight;
}
document.getElementById('msg').addEventListener('keypress', e=>{ if(e.key==='Enter') enviar(); });
</script>
</body>
    """

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message","")
    return jsonify({"reply": resposta_guardiao(msg)})

if __name__ == "__main__":
    app.run()
