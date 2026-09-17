def resposta_guardiao(msg):
    msg = msg.lower()
    if "onde nasceu" in msg or "onde nasci" in msg or "natural" in msg or "guaxupe" in msg or "guaxupé" in msg:
        return "Nasceu em Guaxupé-MG! 🧀☕ Mineirinha de raiz, mas hoje brilha em Cyber-Indaiatuba-SP!"
    if "idade" in msg or "quantos anos" in msg:
        return "A Lara tem 29 anos! 🖤 Dev Jr com energia de Sênior!"
    if "solteira" in msg or "namora" in msg or "casada" in msg:
        return "Sim! Solteira sim! 💖 100% focada em código e em Cyber-Indaiatuba agora!"
    if "faculdade" in msg or "estuda" in msg or "formação" in msg or "curso" in msg:
        return "Faculdade? A VIDA! 🎓😂 Aprendi Python na raça, com Google, YouTube e muito erro .txt!"
    if "mora" in msg or "onde mora" in msg or "indaiatuba" in msg or "cidade" in msg:
        return "Hoje mora em Indaiatuba-SP, mas nasceu em Guaxupé-MG! Criou Cyber-Indaiatuba unindo os dois mundos!"
    if "lara" in msg or "quem é você" in msg:
        return "Eu sou o Guardião 🤖, criado pela Lara Ananias, 29 anos, de Guaxupé-MG, Dev Python Jr de Indaiatuba-SP!"
    if "python" in msg or "flask" in msg:
        return "🐍 Python + Flask! A stack que a mineirinha de Guaxupé usa pra colocar cidade inteira online!"
    if "vaga" in msg or "trabalho" in msg or "estágio" in msg:
        return "A Lara, 29, de Guaxupé-MG, formada na faculdade da vida, tá OPEN TO WORK! 🚀 Python Jr em Indaiatuba/Campinas ou remoto!"
    return f"Você disse: '{msg}'. Tenta: onde nasceu, idade, solteira, faculdade, python, vaga"
