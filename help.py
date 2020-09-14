class Exemplo:
    def funcoes_do_programa():pass
    def meu_jogo():pass
    def python():pass
    
funcoes=dir(Exemplo)

minhas_funcoes=[]

for f in range(0, len(funcoes)):
    if "__" in funcoes[f]:pass
    
    else:minhas_funcoes.append(funcoes[f])

for x in range(0, len(minhas_funcoes)):
    print(minhas_funcoes[x])