print("""\nSeja bem vindo!
Esse progama vai dizer se um ano é Bissexto ou não. Basta digitar o ano logo abaixo.
\033[33mATENÇÃO! POR FAVOR UTILIZE APENAS NÚMEROS!\033[m""")

ano = int(input("\nDigite um ano do calendário: "))
bissexto = ano / 4

if str(bissexto)[-1] == "0" and str(ano)[-2:] != "00":  # se o ano for bissexto e não terminar em 00
    print(f"\n\033[1;32m{ano} é BISSEXTO.\033[m\n")

elif str(ano)[-1] == "0" and str(ano)[-2] == "0":  # se o ano terminar em 00
    bissexto00 = ano / 400
    if str(bissexto00)[-1] == "0":  # se for bissexto
        print(f"\n\033[1;32m{ano:} é BISSEXTO.\033[m\n")
    else:  # se não for bissexto
        print(f"\n\033[1;31m{ano} não é BISSEXTO.\033[m\n")

else:  # se o ano não for bissexto
    print(f"\n\033[1;31m{ano} não é BISSEXTO.\033[m\n")
