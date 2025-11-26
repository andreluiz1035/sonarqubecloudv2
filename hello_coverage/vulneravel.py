# Vulnerabilidade proposital: uso de eval()
def executar_expressao(expr):
    return eval(expr)

# Outra vulnerabilidade: autenticação insegura
def autenticar(usuario, senha):
    # Comparação insegura (string literal no código)
    if usuario == "admin" and senha == "123456":
        return True
    return False
