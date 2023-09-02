menu = """ 
	Menu Inicial

	[d] = Depositar
	[s] = Sacar
	[e] = Estrato
	[q] = Sair

=> """

saldo = 0
limite = 500
extrato = ""
quant_saques = 0
LIMITE_SAQUES = 3

while True:
	opcao = input(menu)
	if opcao == "d":
		valor = float(input("Informe o valor do depósito: "))

		if valor > 0:
			saldo += valor
			extrato += f"Depósito: R$ {valor:.2f}\n"
			print(f"\nValor depositado: {valor:.2f} ")
		else:
			print("\nOperação falhou! O valor informado e inválido.")
	elif opcao == "s":
		valor = float(input("Informe o valor do saque: "))

		excedeu_saldo = valor > saldo
		excedeu_limite = valor > limite
		excedeu_saques = quant_saques >= LIMITE_SAQUES

		if excedeu_saldo:
			print("\nOperação falhou! Você não tem saldo suficiente")
		elif excedeu_limite:
			print("\nOperação falhou! O valor do saque excede o limite.")
		elif excedeu_saques:
			print("\nOperação falhou! Quantidade de saques excedido.")
		elif valor > 0:
			saldo -= valor
			extrato += f"Saque: R$ {valor:.2f}\n"
			print(f"\nValor sacado: {valor:.2f}")
			quant_saques +=1
		else:
			print("\nOperação falhou! Valor informado é inválido")
	elif opcao == "e":
		print("\n============== EXTRATO ==============")
		print("Não foram realizadas movimentações." if not extrato else extrato)
		print(f"Saldo: R$ {saldo:.2f}")
		print("======================================")
	elif opcao == "q":
		break
	else:
		print("\nOperação inválida, por favor seleciona a operação desejada")

