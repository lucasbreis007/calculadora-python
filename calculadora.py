"""
=============================================================================
Calculadora Básica em Python
Autor: Criado para iniciantes em programação
Descrição: Realiza as quatro operações fundamentais (+, -, *, /)
           através de um menu interativo no terminal.
=============================================================================
"""

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração entre dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """
    Retorna a divisão entre dois números.
    Se o divisor for zero, retorna uma mensagem de erro em vez de travar o programa.
    """
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b


def exibir_menu():
    """Exibe as opções disponíveis para o usuário."""
    print("\n" + "=" * 32)
    print("      CALCULADORA EM PYTHON      ")
    print("=" * 32)
    print(" 1 - Adição (+)")
    print(" 2 - Subtração (-)")
    print(" 3 - Multiplicação (*)")
    print(" 4 - Divisão (/)")
    print(" 5 - Sair")
    print("=" * 32)


def obter_numero(mensagem):
    """
    Lê um número digitado pelo usuário.
    Usa 'try/except' para garantir que o programa não trave se o usuário digitar letras.
    """
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")


def main():
    """Função principal que gerencia o fluxo da calculadora."""
    print("Bem-vindo(a) à sua Calculadora em Python!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1 a 5): ").strip()

        # 1. Verifica se o usuário escolheu sair
        if opcao == "5":
            print("\nObrigado por usar a calculadora! Bons estudos na programação.")
            break

        # 2. Verifica se a opção digitada é válida (1, 2, 3 ou 4)
        if opcao not in ["1", "2", "3", "4"]:
            print("\nOpção inválida! Escolha um número entre 1 e 5.")
            continue

        # 3. Coleta os dois números com segurança
        print("\nDigite os números para a operação:")
        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        # 4. Realiza a operação correspondente à opção escolhida
        print("\n" + "-" * 28)
        if opcao == "1":
            resultado = somar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcao == "2":
            resultado = subtrair(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcao == "4":
            resultado = dividir(num1, num2)
            if isinstance(resultado, str):
                # Se for texto, é a mensagem de erro da divisão por zero
                print(resultado)
            else:
                print(f"Resultado: {num1} / {num2} = {resultado}")
        print("-" * 28)

        # 5. Pergunta se deseja realizar mais um cálculo
        repetir = input("\nDeseja fazer outro cálculo? (s/n): ").strip().lower()
        if repetir != "s":
            print("\nPrograma finalizado. Até a próxima!")
            break


# Garante que o script só execute quando chamado diretamente no terminal
if __name__ == "__main__":
    main()