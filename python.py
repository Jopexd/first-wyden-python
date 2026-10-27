def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Valor Errado! Digite um número.")


dividendo = ler_numero("Digite o dividendo: ")
divisor = ler_numero("Digite o divisor: ")

try:
    resultado = dividendo / divisor
    print("Resultado:", resultado)
except ZeroDivisionError:
    print("Não da pra dividir por zero noob!")