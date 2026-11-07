"""
• Proposta 5: Gestão de Aeroporto
• Contexto do Problema: Um terminal aeroportuário de grande
fluxo precisa gerenciar em tempo real o painel eletrônico de
partidas e chegadas de aeronaves.
• O Desafio para o Grupo:
• Estratégia de Busca: A equipe de solo precisa localizar rapidamente um
voo específico informando o código numérico do voo versus localizar
voos por destino textualmente. Quais algoritmos de busca você
implementará para garantir respostas ágeis ao operador?
*criar entidade class voo, com matricula e destino.
• Estratégia de Ordenação: O painel precisa manter os voos
rigorosamente ordenados por ordem cronológica de partida. Você deve
reordenar a estrutura completa a cada alteração ou existe uma
abordagem mais inteligente com base nos algoritmos estudados?
*criar sistema de ordenação de voos que saem que seria uma fila ao meu entendimento,
depois creio que possa criar dois algoritmos ou funções de ordenação para busca, 
um para codigo de voo que vai ser numerico quick sort o mais eficiente,
 o outro pode ser um select sort ou bubblesort para destinos semelhantes.
"""
class Voo():
    def __init__(self, codigo: int, destino: str, horario: str, status: str) -> None:
        self.codigo = codigo    #Codigo numérico(ex:1020)
        self.destino = destino  #Destino textual(ex:"Lisboa")
        self.horario = horario  #Horário no formato "HH:MM"
        self.status = status    #"Confirmado", "Atrasado", "Cancelado" e etc.

    def __str__(self) -> str:
        return f"[{self.horario}] Voo {self.codigo} => {self.destino} | Status:{self.status}"

class GestaoAeroporto:

    def __init__(self):
        self.painel_partidas = [] #ordenado por horario.


    def quick_sort_horario(self, vetor: list[Voo], baixo: int, alto: int) -> None:
        """
        QuickSort in-place (Lomuto) para carga inicial do painel.
        Ordena os objetos Voo com base no atributo 'horario'.
        """
        if baixo < alto:
            pivo = vetor[alto].horario
            i = baixo - 1

            for j in range(baixo, alto):
                if vetor[j].horario <= pivo:
                    i += 1
                    vetor[i], vetor[j] = vetor[j], vetor[i]

            vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]
            indice_pivo = i + 1

            self.quick_sort_horario(vetor, baixo, indice_pivo - 1)
            self.quick_sort_horario(vetor, indice_pivo + 1, alto)

    def quick_sort_codigo(self, vetor: list[Voo], baixo: int, alto: int) -> None:
        """
        QuickSort in-place para ordenar uma cópia do vetor por 'codigo',
        permitindo a aplicação da Busca Binária por código.
        """
        if baixo < alto:
            pivo = vetor[alto].codigo
            i = baixo - 1

            for j in range(baixo, alto):
                if vetor[j].codigo <= pivo:
                    i += 1
                    vetor[i], vetor[j] = vetor[j], vetor[i]

            vetor[i + 1], vetor[alto] = vetor[alto], vetor[i + 1]
            indice_pivo = i + 1

            self.quick_sort_codigo(vetor, baixo, indice_pivo - 1)
            self.quick_sort_codigo(vetor, indice_pivo + 1, alto)
    
    def adicionar_voo(self, voo:Voo):
        """
        Adiciona o voo mantendo a ordenação cronológica sem reordenar tudo do zero.
        """
        self.painel_partidas.append(voo)
        i = len(self.painel_partidas)-1 # ultimo endereço do vetor painel partidas
        chave = self.painel_partidas[i]#colocando em chave a referencia do ultimo elemente incluido.
        #deslocando os voos com horario posteriores para abrir espaço
        while i > 0 and self.painel_partidas[i-1].horario > chave.horario: # to contando de tras pra frente e verificando ao mesmo tempo todos que tem horarios apos ao voo novo.
            self.painel_partidas[i] = self.painel_partidas[i-1]
            i -= 1
        self.painel_partidas[i] = chave

    def buscar_por_codigo_binario(self,codigo: int):
        """
        Busca usando binario e pois havera muitos voos e o quick sort ordena em um vetor auxiliar 
        como no exercicio 7 e apos faz uma busca binaria como no exercicio 6. 
        """
        #teste pra saber se esta vazio.
        if not self.painel_partidas:
            return None
        #ordenando vetor_por_codigo
        vetor_por_codigo = self.painel_partidas.copy()
        self.quick_sort_codigo(vetor_por_codigo, 0,len(vetor_por_codigo)-1)

        #busca binaria
        inicio = 0
        fim = len(vetor_por_codigo) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2

            if vetor_por_codigo[meio].codigo == codigo:
                return vetor_por_codigo[meio]
            elif codigo < vetor_por_codigo[meio].codigo:
                fim = meio - 1  # Descarta metade direita
            else:
                inicio = meio + 1  # Descarta metade esquerda

        return None

    def buscar_por_codigo_linear(self, destino: str):
        """
        Busca usando linear ordenado os voos estão ordenados por horario 
        como no exercicio 7 e apos faz uma busca linear como no exercicio 6, 
        saindo em ordem conforme cronologia. 
        """
        destino_norm =destino.strip().lower()
        resultados = []
        for voo in self.painel_partidas:
            if voo.destino.strip().lower() == destino_norm:
                resultados.append(voo)
        return resultados 

    def exibir_painel(self) -> None:
        print(f"\n====PAINEL ELETRÔNICO DE PARTIDAS (ORDEM CRONOLÓGICA)====")
        for voo in self.painel_partidas:
            print(voo)

# --- DEMONSTRAÇÃO DE USO ---
if __name__ == "__main__":
    sistema = GestaoAeroporto()

    # 1. Cadastro individual de voos fora de ordem
    print("Inserindo voos no sistema...")
    sistema.adicionar_voo(Voo(1020, "Rio de Janeiro", "14:30", "Confirmado"))
    sistema.adicionar_voo(Voo(5040, "São Paulo", "10:15", "Confirmado"))
    sistema.adicionar_voo(Voo(3011, "Rio de Janeiro", "08:00", "Embarque"))
    sistema.adicionar_voo(Voo(2022, "Lisboa", "12:00", "Atrasado"))

    # Exibe o painel mantido em ordem cronológica
    sistema.exibir_painel()

    # 2. Teste de Busca Binária por Código O(log n)
    codigo_busca = 1020
    print(f"\n[Busca Binária por Código: {codigo_busca}]")
    resultado_codigo = sistema.buscar_por_codigo_binario(codigo_busca)
    if resultado_codigo:
        print(f"Encontrado: {resultado_codigo}")
        # Exemplo de alteração de status posterior
        resultado_codigo.status = "Cancelado"
        print(f"Status atualizado: {resultado_codigo}")
    else:
        print("Voo não encontrado.")

    # 3. Teste de Busca Linear por Destino O(n)
    destino_busca = "Rio de Janeiro"
    print(f"\n[Busca Linear por Destino: '{destino_busca}']")
    resultados_destino = sistema.buscar_por_codigo_linear(destino_busca)
    for voo in resultados_destino:
        print(voo)