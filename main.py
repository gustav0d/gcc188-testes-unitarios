from calculadora import calcular_media, dividir, multiplicar, potencia, somar, subtrair

OPCOES = {
    "1": ("Somar", somar),
    "2": ("Subtrair", subtrair),
    "3": ("Multiplicar", multiplicar),
    "4": ("Dividir", dividir),
    "5": ("Potencia", potencia),
    "6": ("Media de lista", None),
}


def menu():
    print("\n--- Calculadora ---")
    for k, (nome, _) in OPCOES.items():
        print(f"  {k}. {nome}")
    print("  0. Sair")


def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Numero invalido, tenta de novo.")


def executar_media():
    entrada = input("Digite os numeros separados por virgula: ")
    try:
        lista = [float(x.strip()) for x in entrada.split(",")]
        resultado = calcular_media(lista)
        print(f"Resultado: {resultado}")
    except ValueError as e:
        print(f"Erro: {e}")


def executar_operacao(func):
    a = ler_numero("Primeiro numero: ")
    b = ler_numero("Segundo numero: ")
    try:
        resultado = func(a, b)
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("Erro: divisao por zero.")


def main():
    while True:
        menu()
        opcao = input("\nEscolha uma opcao: ").strip()

        if opcao == "0":
            break
        elif opcao == "6":
            executar_media()
        elif opcao in OPCOES:
            _, func = OPCOES[opcao]
            executar_operacao(func)
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    main()
