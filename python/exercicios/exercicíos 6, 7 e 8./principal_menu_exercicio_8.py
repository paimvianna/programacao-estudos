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
    resultado_codigo = sistema.buscar_por_codigo_binaria(codigo_busca)
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
    resultados_destino = sistema.buscar_por_destino_linear(destino_busca)
    for voo in resultados_destino:
        print(voo)