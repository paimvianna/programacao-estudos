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
def quick_sort_codigo(self, base: list[Voo], baixo: int, alto: int) -> None:
        """
        QuickSort in-place para ordenar uma cópia do vetor por 'codigo',
        permitindo a aplicação da Busca Binária por código.
        """
        if baixo < alto:
            pivo = base[alto].numero_voo
            i = baixo - 1

            for j in range(baixo, alto):
                if base[j].numero_voo <= pivo:
                    i += 1
                    base[i], base[j] = base[j], base[i]

            base[i + 1], base[alto] = base[alto], base[i + 1]
            indice_pivo = i + 1

            self.quick_sort_codigo(base, baixo, indice_pivo - 1)
            self.quick_sort_codigo(base, indice_pivo + 1, alto)

def buscar_voo_por_numero(self,base: list[Voo], codigo: int) -> int:
    print("[TODO] Implementar busca por número do voo aqui.")
    """
    Busca usando binario e pois havera muitos voos e o quick sort ordena em um vetor auxiliar 
    como no exercicio 7 e apos faz uma busca binaria como no exercicio 6. 
    """
    #teste pra saber se esta vazio.
    if not base:
        return -1
    #ordenando vetor_por_codigo
    vetor_por_codigo = base.copy()
    self.quick_sort_codigo(vetor_por_codigo, 0,len(vetor_por_codigo)-1)

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

def manter_painel_cronologico(painel: list[Voo]) -> list[Voo]:
    print("[TODO] Implementar ordenação cronológica aqui.")
    return painel

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
        print("1. Gerar Base | 2. Ver Amostra (Top 5) | 3. Buscar Voo | 4. Ordenar Cronológico | 0. Sair")
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
                    print(f'\n base') #sistema de controle pra ver o que to gerando e se base e minha lista.
        elif op == "3":
            t0 = time.perf_counter()
            idx = buscar_voo_por_numero(base, int(input("Nº Voo: ")))
            print(f"Índice retornado: {idx} (Tempo: {time.perf_counter() - t0:.6f}s)")
        elif op == "4":
            t0 = time.perf_counter()
            base = manter_painel_cronologico(base)
            print(f"Concluído em {time.perf_counter() - t0:.6f}s.")
        elif op == "0":
            break

if __name__ == "__main__":
    main()
    