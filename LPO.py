# pip install aima3
from aima3.logic import expr,FolKB, fol_fc_ask

clauses = []



# clauses.append(expr("Progenitor(Maria,Joao)"))
# clauses.append(expr("Progenitor(Jose,Joao)"))
# clauses.append(expr("Progenitor(Maria,Ana)"))
# clauses.append(expr("Progenitor(Jose,Ana)"))

#BANCO DE DADOS = RELACAO
clauses.append(expr("Progenitor(Pedro,Joao)"))
clauses.append(expr("Progenitor(Pedro,Clara)"))
clauses.append(expr("Progenitor(Pedro,Francisco)"))
clauses.append(expr("Progenitor(Pedro,Ana)"))
clauses.append(expr("Progenitor(Antonia,Joao)"))
clauses.append(expr("Progenitor(Antonia,Clara)"))
clauses.append(expr("Progenitor(Antonia,Francisco)"))
clauses.append(expr("Progenitor(Antonia,Ana)"))
clauses.append(expr("Progenitor(Ana, Helena)"))
clauses.append(expr("Progenitor(Ana, Joana)"))
clauses.append(expr("Progenitor(Joao,Mario)"))
clauses.append(expr("Progenitor(Helena,Carlos)"))
clauses.append(expr("Progenitor(Mario,Carlos)"))
clauses.append(expr("Progenitor(Clara,Pietro)"))
clauses.append(expr("Progenitor(Clara,Enzo)"))

#FUNCAO = PESSOA
clauses.append(expr("Progenitor(x,y) ==> Pessoa(x)"))
clauses.append(expr("Progenitor(x,y) ==> Pessoa(y)"))

#BANCO DE DADOS = SEXO
clauses.append(expr("Sexo(Pedro,Masculino)"))
clauses.append(expr("Sexo(Antonia,Feminino)"))
clauses.append(expr("Sexo(Joao,Masculino)"))
clauses.append(expr("Sexo(Clara,Feminino)"))
clauses.append(expr("Sexo(Francisco,Masculino)"))
clauses.append(expr("Sexo(Ana,Feminino)"))
clauses.append(expr("Sexo(Helena,Feminino)"))
clauses.append(expr("Sexo(Joana,Feminino)"))
clauses.append(expr("Sexo(Joao,Masculino)"))
clauses.append(expr("Sexo(Mario,Masculino)"))
clauses.append(expr("Sexo(Carlos,Masculino)"))
clauses.append(expr("Sexo(Miline,Feminino)"))
clauses.append(expr("Sexo(Pietro,Masculino)"))
clauses.append(expr("Sexo(Enzo,Masculino)"))
clauses.append(expr("Sexo(Francisca,Feminino)"))

#Descendente e Ascendente
clauses.append(expr("Progenitor(x,y) ==> Descendente(y,x)"))
clauses.append(expr("Descendente(x,y) ==> Ascendente(y,x)"))

#pai e mae 

clauses.append(expr("Progenitor(x,y) & Sexo(x,Masculino) ==> Pai(x,y) "))
clauses.append(expr("Progenitor(x,y) & Sexo(x,Feminino) ==> Mae(x,y) "))

#avo e avo

clauses.append(expr("Progenitor(x,y) & Pai(x,z) ==> AvoM(y,z)"))
clauses.append(expr("Progenitor(x,y) & Mae(x,z) ==> AvoF(y,z)"))


# irmao e irma
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Masculino) ==> Irmao(y,z)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))

clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Masculino) ==> Irmao(y,z)"))
clauses.append(expr("Progenitor(x,y) & Progenitor(x,z) & Sexo(y,Feminino) ==> Irma(y,z)"))

#tio e tia

clauses.append(expr("Pai(x,z) & Irmao(z,y) ==> Tio(x,y)"))
clauses.append(expr("Pai(x,z) & Irma(z,y) ==> Tio(x,y)"))

clauses.append(expr("Mae(x,z) & Irmao(z,y) ==> Tia(x,y)"))
clauses.append(expr("Mae(x,z) & Irma(z,y) ==> Tia(x,y)"))

# #primos e primas: Tio -- Descendente(do Tio) 

clauses.append(expr("Tio(x,z) & Descendente(g,x) & Sexo(g,Masculino) ==> Primo(x,y)"))
clauses.append(expr("Tio(x,z) & Descendente(g,x) & Sexo(g,Feminino) ==> Prima(x,y)"))

clauses.append(expr("Tia(x,z) & Descendente(g,x) & Sexo(g,Masculino) ==> Primo(x,y)"))
clauses.append(expr("Tia(x,z) & Descendente(g,x) & Sexo(g,Feminino) ==> Prima(x,y)"))


Genealogia = FolKB(clauses)


perguntas = ["Sexo(x, Masculino)",
             "Tio(x, Francisco)",
             "Primo(x, y)",
             "Prima(x, y)",
             "Sexo(Maria, x)",
             "Irmao(x, Ana)",
             "Irma(x, Joao)",
             "Descendente(x, Maria)",
             "Descendente(Joao, x)",
             "Pessoa(x)",
             "Mae(x, y)",
             "Pai(x, y)"]



for i in perguntas:
    resposta = fol_fc_ask(Genealogia, expr(i))
    print("%s -> %s" %(i, (list(resposta))))


