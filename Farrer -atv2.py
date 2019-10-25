import random

def f_preencherS():
	sexo='MF'
	s=''
	for i in range(1):
		s+=random.choice(sexo)
	return s

def main(args):
	print('∆ 1.12.2. Tem-se um conjunto de dados contendo a altura e o sexo (masculino, feminino) de 50 pessoas.\n \
	Fazer um algoritmo que calcule e escreva: \n\
	- a maior e a menor altura do grupo; \n\
	- a média de altura das mulheres; \n\
	- o número de homens;\n ')
	
	cont_F=0
	cont_M=0
	md_altF=0
	i=1
	p=0
	alt=random.randrange(150,196)/100
	sex=f_preencherS()
	while(i<11):
		p=i
		print(alt, sex, i,'\n')
		if(i==1):
			mr_alt=alt
			mn_alt=alt
		else:
			if(alt>mr_alt):
				mr_alt=alt
				p=i
			if(alt<mn_alt):
				mn_alt=alt
				p=i
		if(sex=='F'):
			md_altF+=alt
			cont_F+=1
			p=i
		else:
			cont_M+=1
		i+=1
		alt=random.randrange(150,196)/100
		sex=f_preencherS()
	print('a maior e a menor altura do grupo são: {}/{} e {}/{}.'.format(mr_alt,p,mn_alt,p))
	print('a média de altura das mulheres é: {}'.format(md_altF/cont_F))
	print('o número de homens é: {}.'.format(cont_M))
	return 0
			
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
