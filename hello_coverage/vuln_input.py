# Vulnerabilidade REAL: credenciais hardcoded
USERNAME = "admin"
PASSWORD = "123456"  # Sonar marca isso como Vulnerability

def autenticar(usuario, senha):
    return usuario == USERNAME and senha == PASSWORD
