from flask import Flask, request, jsonify
app = Flask(__name__)

# Cérebro do Guardião
def resposta_guardiao(msg):
    msg = msg.lower()
    if "python" in msg:
        return "🐍 Python é nossa arma aqui em Cyber-Indaiatuba! Flask deixa tudo online rápido. Quer ver meu código?"
    if "lara" in msg or "quem é você" in msg:
        return "Eu sou o Guardião de Cyber-Indaiatuba, criado pela Lara Ananias, Dev Python Jr de Indaiatuba-SP! 🛡️"
    if "vaga" in msg or "trabalho" in msg or "estágio" in msg:
        return "A Lara tá buscando vaga Jr/Estágio Backend Python! Indaiatuba ou remoto. Contrata ela! 🚀"
    if "cidade" in msg or "cyber" in msg:
        return "Cyber-Indaiatuba: 47 drones, néon infinito, e código Python rodando 24h. Você tá dentro dela agora!"
    return f"Interessante! Você disse: '{msg}'. Me pergunta sobre Python, sobre a Lara ou sobre nossa cidade cibernética!"

@app.route("/")
def home():
    return """
<body style="margin:0; background:#000; color:white; font-family:monospace;">
<div style="position:fixed; inset:0; background:url('https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=1920') center/cover; filter:brightness(0.3); z-index:-1;"></div>
<div style="background:red; color:white; text-align:center; padding:8px; font-size:11px; letter-spacing:2px;">⚠️ CYBER-INDAIATUBA v2 ONLINE - GUARDIÃO COM IA - LARA ANANIAS ⚠️</div>
<div style="max-width:1100px; margin:auto; padding:20px; display:flex; gap:20px; flex-wrap:wrap;">
<div style="flex:1.2; background:rgba(0,0,0,0.8); border:1px solid #00ff88; border-radius:16px; padding:24px;">
<h1 style="font-size:50px; margin:0; line-height:0.9;">LARA<br><span style="color:red;">ANANIAS</span></h1>
<p style="color:#00ff88;">> Dev Python Jr. | Flask | Deploy</p>
<p style="color:#ccc; font-size:13px; border-left:2px solid red; padding-left:10px;">De .txt com erro pra site com IA online em 1 noite. Meu mundo Cyber-Indaiatuba tá no ar.</p>
<div style="margin:20px 0; background:#111; border:1px solid #333; border-radius:12px; padding:12px; height:220px; display:flex; flex-direction:column;">
<div id="chat" style="flex:1; overflow-y:auto; font-size:12px; color:#00ff88;"><div style="color:#666;">Guardião: Fala, visitante! Pergunta algo sobre Python ou a cidade...</div></div>
<div style="display:flex; gap:8px; margin-top:10px;">
<input id="msg" placeholder="Digite aqui..." style="flex:1; background:#000; border:1px solid #00ff88; color:white; padding:8px 12px; border-radius:20px; font-size:12px;">
<button onclick="enviar()" style="background:#00ff88; color:black; border:none; padding:8px 16px; border-radius:20px; font-weight:bold; cursor:pointer;">ENVIAR</button>
</div>
</div>
<a href="https://www.linkedin.com/in/lara-ananias-267994437" style="background:#00ff88; color:black; padding:10px 20px; text-decoration:none; border-radius:20px; font-weight:bold; display:inline-block;">LinkedIn ↗</a>
<span style="margin-left:10px; font-size:10px; color:#888;">github.com/FlaviaLaracyber/cyber-lara</span>
</div>
<div style="flex:0.8; text-align:center;">
<img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" style="width:260px; filter:drop-shadow(0 0 25px red);">
<div style="background:black; border:1px solid red; color:#00ff88; font-size:10px; padding:6px 10px; border-radius:20px; margin-top:10px; display:inline-block;">CHAT IA ATIVO • 47 DRONES • ONLINE</div>
</div>
</div>
<script>
async function enviar(){
  let input = document.getElementById('msg');
  let chat = document.getElementById('chat');
  let texto = input.value; if(!texto) return;
  chat.innerHTML += `<div style='color:white; margin:4px 0;'>Você: ${texto}</div>`;
  input.value = '';
  let res = await fetch('/api/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({message:texto})});
  let data = await res.json();
  chat.innerHTML += `<div style='color:#00ff88; margin:4px 0;'>Guardião: ${data.reply}</div>`;
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
