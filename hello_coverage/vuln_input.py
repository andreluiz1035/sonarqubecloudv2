# Exemplo de vulnerabilidade simples:
# Uso de eval() — extremamente perigoso — o Sonar detecta como Security Hotspot.

def executar_expressao(expr):
    # Vulnerabilidade proposital
    return eval(expr)  
