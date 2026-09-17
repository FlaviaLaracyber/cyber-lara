from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<body style="margin:0; background:#000; color:white; font-family:monospace;">
<div style="position:fixed; inset:0; background:url('https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=1920') center/cover; filter:brightness(0.4); z-index:-1;"></div>
<div style="background:red; color:white; text-align:center; padding:8px; font-size:12px;">⚠️ CYBER-INDAIATUBA ONLINE - LARA ANANIAS - v1 LIVE ⚠️</div>
<div style="max-width:1000px; margin:auto; padding:50px 20px; display:flex; gap:30px; flex-wrap:wrap; align-items:center;">
<div style="flex:1; background:rgba(0,0,0,0.75); border:1px solid #00ff88; border-radius:20px; padding:30px;">
<h1 style="font-size:60px; line-height:0.9; margin:0;">LARA<br><span style="color:red;">ANANIAS</span></h1>
<p style="color:#00ff88;">> Dev Python Jr. | Backend Flask</p>
<p style="color:#ccc; border-left:2px solid red; padding-left:12px;">Criei meu mundo cibernético Cyber-Indaiatuba com Python. De erro .txt pra cidade neon online. Buscando vaga Jr/Estágio.</p>
<p style="font-size:11px; color:#666;">Indaiatuba-SP | Python | Flask | API</p>
<a href="https://www.linkedin.com/in/lara-ananias-267994437" style="background:#00ff88; color:black; padding:12px 24px; text-decoration:none; border-radius:30px; font-weight:bold; display:inline-block; margin-top:10px;">Meu LinkedIn ↗</a>
</div>
<div style="flex:1; text-align:center;">
<img src="https://cdn-icons-png.flaticon.com/512/4712/4712027.png" style="width:300px; filter:drop-shadow(0 0 30px red);">
<div style="background:black; border:1px solid red; color:#00ff88; font-size:10px; padding:8px; border-radius:8px; margin-top:10px; display:inline-block;">MUNDO ONLINE 24H | 47 DRONES</div>
</div>
</div>
</body>
    """

if __name__ == "__main__":
    app.run()