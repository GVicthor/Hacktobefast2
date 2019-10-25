
def main(args):
	
	cont1=0
	cont2=0
	cont3=0
	tcompra=0
	tvenda=0
	tlucro=0
	mercadoria=input('Digite o nome da mercadoria: ')
	pvenda=float(input('Digite o preço de venda: '))
	pcompra=float(input('Digite o preço de compra: \n'))
	while(mercadoria!=''):
		mercadoria=input('Digite o nome da mercadoria: ')
		pvenda=float(input('Digite o preço de venda: '))
		pcompra=float(input('Digite o preço de compra: \n'))
		lucro=pvenda-pcompra
		if(lucro<pvenda+pcompra/10):
			cont1+=1
		elif(pvenda+pcompra/10<=lucro)and(lucro<=pvenda+pcompra/20):
			cont2+=1
		else:
			cont3+=1
		tcompra+=pcompra
		tvenda+=pvenda
	tlucro=tvenda-tcompra
	print('Houveram {} mercadorias com lucro menor que 10%\n ,{} mercadorias com lucro entre 10% e 20%\n , {} mercadorias com lucro.'.format(cont1,cont2,cont3))
	print()
	print('O valor total de compras R$ {}, O total de vendas R$ {},O lucro total = R$ {}.'.format(tcompra,tvenda,tlucro))
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
