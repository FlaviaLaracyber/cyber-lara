from flask import Flask, request, jsonify
app = Flask(__name__)

def resposta_guardiao(msg):
    msg = msg.lower()
    if "onde nasceu" in msg or "onde nasci" in msg or "nasceu" in msg or "guaxupe" in msg or "guaxupé" in msg or "natural" in msg:
        return "Nasceu em Guaxupé-MG! 🧀☕ Mineirinha de raiz, hoje em Indaiatuba-SP!"
    if "idade" in msg or "quantos anos" in msg or "anos" in msg:
        return "A Lara tem 29 anos! 🖤"
    if "solteira" in msg or "namora" in msg or "casada" in msg:
        return "Sim! Solteira sim! 💖 Focada em código!"
    if "faculdade" in msg or "estuda" in msg or "formação" in msg or "curso" in msg:
        return "Faculdade? A VIDA! 🎓😂 Aprendi Python na raça!"
    if "mora" in msg or "onde mora" in msg:
        return "Mora em Indaiatuba-SP, mas nasceu em Guaxupé-MG!"
    if "python" in msg or "flask" in msg:
        return "🐍 Python + Flask! Foi assim que ela me criou!"
    if "oi" in msg or "ola" in msg:
        return "Olá! 👋 Pergunta: onde nasceu, idade, solteira, faculdade"
    return f"Você disse: '{msg}'. Tenta: onde nasceu, idade, solteira, faculdade"

@app.route("/")
def home():
    return """<body style="margin:0;background:#000;color:white;font-family:monospace;"><div style="background:linear-gradient(90deg,red,orange);text-align:center;padding:8px;font-size:11px;font-weight:bold;">⚠️ CYBER-INDAIATUBA v3 - GUARDIÃO ATUALIZADO - FLAVIA LARA ⚠️</div><div style="max-width:1000px;margin:auto;padding:20px;display:flex;gap:20px;flex-wrap:wrap;"><div style="flex:1;background:rgba(0,0,0,0.85);border:1px solid #00ff88;border-radius:16px;padding:24px;"><h1 style="font-size:50px;margin:0;">FLAVIA<br><span style="color:#ff3333;">ANANIAS</span></h1><p style="color:#00ff88;">> 29 anos | Guaxupé-MG > Indaiatuba-SP | Dev Python Jr</p><div style="margin:20px 0;background:#0a0a0a;border:1px solid #333;border-radius:12px;padding:12px;height:240px;display:flex;flex-direction:column;"><div id="chat" style="flex:1;overflow-y:auto;font-size:12px;color:#00ff88;"><div style="color:#666;background:#111;padding:8px;border-radius:8px;">🤖 Guardião v3: Fala! Pergunta onde nasci, idade, solteira, faculdade...</div></div><div style="display:flex;gap:8px;margin-top:10px;"><input id="msg" placeholder="Digite..." style="flex:1;background:#000;border:1px solid #00ff88;color:white;padding:10px 14px;border-radius:20px;outline:none;"><button onclick="enviar()" style="background:#00ff88;color:black;border:none;padding:10px 18px;border-radius:20px;font-weight:bold;cursor:pointer;">ENVIAR</button></div></div><a href="https://www.linkedin.com/in/lara-ananias-267994437" target="_blank" style="background:#00ff88;color:black;padding:10px 22px;text-decoration:none;border-radius:20px;font-weight:bold;display:inline-block;font-size:12px;">LinkedIn ↗</a></div><div style="flex:0.8;text-align:center;"><div style="font-size:140px;">🤖</div><div style="background:black;border:1px solid #ff3333;color:#00ff88;font-size:10px;padding:8px 14px;border-radius:20px;display:inline-block;">GUAXUPÉ-MG • 29 ANOS • ONLINE</div></div></div><script>async function enviar(){let i=document.getElementById('msg');let c=document.getElementById('chat');let t=i.value.trim();if(!t)return;c.innerHTML+=`<div style='color:white;margin:6px 0;background:#222;padding:6px 10px;border-radius:12px;text-align:right;'>Você: ${t}</div>`;i.value='';c.scrollTop=c.scrollHeight;let r=await fetch('/api/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})});let d=await r.json();c.innerHTML+=`<div style='color:#00ff88;margin:6px 0;background:#0a1a0a;padding:6px 10px;border-radius:12px;border-left:2px solid #00ff88;'>🤖 Guardião: ${d.reply}</div>`;c.scrollTop=c.scrollHeight;}document.getElementById('msg').addEventListener('keypress',e=>{if(e.key==='Enter')enviar();});</script></body>"""

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"reply": resposta_guardiao(data.get("message",""))})

if __name__ == "__main__":
    app.run()
