
def analisa(entrada, saida):
	cont = {}

	for i in ['A', 'T', 'C', 'G']:
		for j in ['A', 'T', 'C', 'G']:
			cont[i+j] = 0


	entrada = entrada.replace("\n","") 
	entrada = entrada.replace("N", "")
	for k in range(len(entrada)-1):
		cont[entrada[k]+entrada[k+1]] += 1


	#html
	i = 1
	for  k in cont:
		transparencia = cont[k]/max(cont.values())
		saida.write("<div style='width:100px; border:1px solid #111;color:#fff; height:100px;  float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"')>"+k+"</div>")

		if i%4 == 0:
			saida.write("<div style='clear:both'></div>")
		i+=1
	saida.close()
	
entrada1 = open("rnaEscherichia.fasta").read()
saida1 = open("bacteria.html", "w")
analisa(entrada1, saida1)

entrada2 = open("rnaHumano.fasta").read()
saida2 = open("humano.html", "w")
analisa(entrada2, saida2)
