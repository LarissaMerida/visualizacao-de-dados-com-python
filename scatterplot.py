import matplotlib.pyplot as plt


x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [20, 5, 100, 33, 10]

titulo = "Scatterplot: gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x, y, label="Meus pontos", color="k", marker="h", s=z)
plt.plot(x,y, color="k", linestyle="-.")
plt.legend()
#plt.show()
#dpi aumenta tamanho
plt.savefig("figura1.png", dpi=300)



