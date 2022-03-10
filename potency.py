


def potencia(base, exp):
    resultado = 1.0
    for i in range(abs(exp)):
        resultado *= base
    return resultado if exp >= 0 else 1/resultado


def main():
    repetir = True
    while repetir:
        print()
        print("CÁLCULO DE POTÊNCIAS")    
        base = float(input("{:>10}: ".format("Base")))
        exp  = int(input("{:>10}: ".format("Expoente")))

        print("{:>10}: {}".format("R", potencia(base, exp)))

        while True:
            print()
            opcao = input("Deseja repetir? [s/N] ").strip().lower()
            if opcao in ('sim', 's'):
                break
            elif opcao in ('não', 'nao', 'n', ''):
                repetir = False
                break
            else:
                print("ATENÇÃO: Introduza apenas [S]im/[n]ão!")


if __name__ == '__main__':
    main()
