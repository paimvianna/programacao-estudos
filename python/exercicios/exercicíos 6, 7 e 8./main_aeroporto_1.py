import random
import time
from dataclasses import dataclass

@dataclass
class Voo:
    numero_voo: int
    destino: str
    horario_partida: str
    portao: str

# ==========================================
# ÁREA DO ALUNO: ESCOLHA E IMPLEMENTE AS ESTRATÉGIAS
# ==========================================
def quick_sort_base(base: list[Voo], baixo: int, alto: int, variavel_ordenacao: str) -> None:
        """
        QuickSort in-place para ordenar uma cópia do vetor por 'codigo',
        permitindo a aplicação da Busca Binária por código.
        """
        if baixo < alto:
            #pivo = base[alto].numero_voo
            pivo = getattr(base[alto], variavel_ordenacao)
            i = baixo - 1

            for j in range(baixo, alto):
                #if base[j].numero_voo <= pivo:
                if getattr(base[j],variavel_ordenacao) <= pivo:
                    i += 1
                    base[i], base[j] = base[j], base[i]

            base[i + 1], base[alto] = base[alto], base[i + 1]
            indice_pivo = i + 1

            quick_sort_base(base, baixo, indice_pivo - 1, variavel_ordenacao)
            quick_sort_base(base, indice_pivo + 1, alto, variavel_ordenacao)

def encontrar_posicao_insercao_horario(base: list[Voo], horario: str) -> int:
    """
    Busca binaria para encontrar a posição de inserção correta
    mantendo a ordem cronologica por 'horario_partida'
    """
    inicio = 0
    fim = len(base) - 1
    posicao = len(base)

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if base[meio].horario_partida >= horario:
            posicao = meio
            fim = meio -1 #tenta achar uma posição anterior valida
        else:
            inicio = meio + 1
    return posicao

"""def quick_sort_horario(base: list[Voo], baixo: int, alto: int) -> None:
    #quickSort para ordenar os objetos Voo com base no atributo 'horario'.
    if baixo < alto:
        pivo = base[alto].horario_partida
        i = baixo -1

        for j in range(baixo, alto):
            if base[j].horario_partida <= pivo:
                i += 1
                base[i], base[j] = base[j],  base[i]
        base[i+1], base[alto] = base[alto], base[i+1]
        indice_pivo = i + 1

        quick_sort_horario(base, baixo, indice_pivo - 1)
        quick_sort_horario(base, indice_pivo + 1, alto)"""

def buscar_voo_por_numero(base: list[Voo], codigo: int):
    #print("[TODO] Implementar busca por número do voo aqui.")
    """
    Busca usando binario e pois havera muitos voos e o quick sort ordena em um vetor auxiliar 
    como no exercicio 7 e apos faz uma busca binaria como no exercicio 6. 
    """
    #teste pra saber se esta vazio.
    if not base:
        return -1
    #ordenando vetor_por_codigo
    vetor_por_codigo = base.copy()
    quick_sort_base(vetor_por_codigo, 0,len(vetor_por_codigo)-1, "numero_voo")

    #busca binaria
    inicio = 0
    fim = len(vetor_por_codigo) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor_por_codigo[meio].numero_voo == codigo:
            return vetor_por_codigo[meio]
        elif codigo < vetor_por_codigo[meio].numero_voo:
            fim = meio - 1  # Descarta metade direita
        else:
            inicio = meio + 1  # Descarta metade esquerda

    return -1

def buscar_voos_por_destino(base: list[Voo], destino: str) -> list[Voo]:
    if not base:
        return[]
    base_organizada = base.copy()
    quick_sort_base(base_organizada, 0, len(base_organizada)-1,"horario_partida")
    destino_escolhido = destino.strip().lower()
    resultado = []
    for voo in base_organizada:
        if destino_escolhido in voo.destino.strip().lower():
            resultado.append(voo)
    return resultado

def manter_painel_cronologico(painel: list[Voo]) -> list[Voo]:
    #print("[TODO] Implementar ordenação cronológica aqui.")
    if not painel:
        return painel
    quick_sort_base(painel, 0, len(painel)-1,"horario_partida")
    return painel

def inserir_voo(base):
    print(f"==== Cadastro de Voos: ====")
    try:
        numero_voo = int(input(f"Informe o numero do Voo: "))
    except ValueError:
        print('[Erro] O número do voo deve ser um número inteiro.')
        return
    destinos = {
        "1":"São Paulo (GRU)",
        "2":"Rio de Janeiro (GIG)",
        "3":"Brasília (BSB)",
        "4":"Buenos Aires (EZE)",
        "5": "Lisboa (LIS)",
        "6": "Miami (MIA)"   
    }
    print("Informe o Destino:\n 1. São Paulo (GRU), 2.Rio de Janeiro (GIG), 3.Brasília (BSB), 4.Buenos Aires (EZE), 5.Lisboa (LIS), 6.Miami (MIA)")
    op_dest = input("Opção: ").strip()
    if op_dest not in destinos:
        print("[Erro] Opção de destino inválida.")
        return
    destino = destinos[op_dest]

    horario_partida = input(f"Informe o horario (HH:MM): ").strip()
    num_portao = input(f"Informe o numero do Portão de 1 a 15: ")
    portao = f"Gate {num_portao}"
    novo_voo = Voo(numero_voo, destino, horario_partida, portao)
    #Verifiaca se ja esta ordenada por horario
    esta_ordenada = all(
        base[i].horario_partida <= base[i+1].horario_partida
        for i in range(len(base)-1)
    )
    if esta_ordenada and len(base) > 0:
        posicao = encontrar_posicao_insercao_horario(base,horario_partida)
        base.insert(posicao,novo_voo)
        print(f"Voo {numero_voo} inserido na posição {posicao}(mantendo a ordem cronológica)!")
    else:
        #Se a base nao estiver ordenada, ordenamos e inserimos. 
        quick_sort_base(base, 0, len(base)-1,"horario_partida")
        posicao = encontrar_posicao_insercao_horario(base,horario_partida)
        base.insert(posicao,novo_voo)
        print(f"Voo {numero_voo} inserido na posição {posicao}(mantendo a ordem cronológica)!")

# ==========================================
# INFRAESTRUTURA DO SISTEMA (NÃO ALTERAR)
# ==========================================

def gerar_base_dados(quantidade: int) -> list[Voo]:
    destinos = ["São Paulo (GRU)", "Rio de Janeiro (GIG)", "Brasília (BSB)", "Buenos Aires (EZE)", "Lisboa (LIS)", "Miami (MIA)"]
    nums = random.sample(range(1000, 1000 + quantidade * 2), quantidade)
    return [
        Voo(numero_voo=nums[i], destino=random.choice(destinos), horario_partida=f"{random.randint(0,23):02d}:{random.randint(0,59):02d}", portao=f"Gate {random.randint(1,15)}")
        for i in range(quantidade)
    ]

def main():
    base = []
    while True:
        print("\n--- SISTEMA: AEROPORTO PAINEL ---")
        print("1. Gerar Base | 2. Ver Amostra (Top 5) | 3. Buscar Voo | 4.Buscar Voos Por Destino | \n |5. Ordenar Cronológico | 6. Inserção de Vooo | 0. Sair")
        op = input("Opção: ").strip()
        if op == "1":
            base = gerar_base_dados(int(input("Qtd: ")))
            print(f"Painel gerado com {len(base)} voos.")
            print(base)
        elif op == "2":
            if not base:
                print("[Aviso] Gere a base de dados primeiro.")
            else:
                print("\n--- Amostra de Registros (Primeiros 5) ---")
                for item in base[:5]:
                    print(item)
        elif op == "3":
            t0 = time.perf_counter()
            idx = buscar_voo_por_numero(base, int(input("Nº Voo: ")))
            print(f"Índice retornado: {idx} (Tempo: {time.perf_counter() - t0:.6f}s)")
        elif op == "4":
            """if not base_organizada:
                print("[Aviso] Aplique a primeira organização do Banco dos Voos.")
            else:"""
            destino = input(str(f'Informe o destino: '))
            t0 = time.perf_counter()
            destinoVoos = buscar_voos_por_destino(base, destino)
            print(f"Retorno da busca: {destino} Tempo: {time.perf_counter() - t0:.6f}s\n Voos: {destinoVoos}")            
        elif op == "5":
            t0 = time.perf_counter()
            base = manter_painel_cronologico(base)
            print(f"Concluído em {time.perf_counter() - t0:.6f}s.")
        elif op == "6":
            inserir_voo(base)
        elif op == "0":
            break

if __name__ == "__main__":
    main()
    