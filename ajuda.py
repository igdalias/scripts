def find_defs(Exemplo):
    funcoes=dir(Exemplo)

    minhas_funcoes=[]

    for f in range(0, len(funcoes)):
        if "__" in funcoes[f]:pass
        
        else:minhas_funcoes.append(funcoes[f])
    
    return minhas_funcoes