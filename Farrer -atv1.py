

def main(args):
	print('∆ 1.12.1.  Fazer um algoritmo que:\n \
	- Leia um número indeterminado de linhas contendo cada uma a idade de um indivíduo.\n \
	A última linha que não entrará nos cálculos, contém o valor da idade igual a zero.\n\
	- Calcule e escreva a idade média deste grupo de indivíduos. \n')
	i=0
	cont=0
	idade=int(input('Digite uma didade: '))
	while(idade>0):
		i+=1
		print(i)
		cont+=idade
		idade=int(input('Digite outra didade: '))
	cont=cont/i
	print('a idade média é:{}'.format(cont))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
