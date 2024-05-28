def verificar_conteudo_carbono(pc_carbono: float) ->bool:
    return pc_carbono < 7


def verificar_dureza_rockwell(dureza: float) ->bool:
    return  dureza > 50



def varificar_resistencia_tracao(resistencia: float) ->bool:
     return resistencia > 80000

def calcular_grau_aco(pc_carbono: float, dureza: float, resistencia: float) ->int:
    resultado_carbono = verificar_conteudo_carbono(pc_carbono)
    resultado_dureza_rockwell = verificar_dureza_rockwell(dureza)
    resultado_resistencia_tracao = varificar_resistencia_tracao(resistencia)

    if resultado_carbono and resultado_dureza_rockwell and resultado_resistencia_tracao:
        return  10
    elif resultado_carbono and resultado_dureza_rockwell:
        return  9
    elif resultado_carbono:
        return  8
    else:
        return  7
