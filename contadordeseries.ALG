Algoritmo "comparador temporal de series"

// com esse programa você pode saber quantas horas uma série dura, e comparar diferentes séries

Var
q, d, h, m: real
nome, R: caracter


Inicio
escreval("-----------------------------------------------------------------")
escreval("------------------Comparador de séries---------------------------")
escreval("-----------------------------------------------------------------")
repita
      escreva("Digite o nome da série: ")
                      leia(nome)
      escreva("Digite a quantidade de episódios: ")
                      leia(q)
      escreva("Digite a duração média de cada episodio, em minutos: ")
                      leia(d)
                      m <- q*d
                      h <- m/60

      escreval("A série ", nome, " tem", q , " episódios, com a duração média de", d ," minutos, que equivalem a", h , " horas")
      escreva("Digite S para continuar o programa e N para encerrar: ")

                      leia(R)
Ate (R = "N")




Fimalgoritmo
