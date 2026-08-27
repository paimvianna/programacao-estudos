import sys 
import time
def demosntrar_comportamento_memoria():
    print("==INVESTIGANDO A MEMÓRIA DA LISTA DO PYTHON==")
    minha_lista =[]

    tamnaho_anterior = sys.getsizeof(minha_lista)
    print(f"Lista vazia : 0 elementos | Tamanho na RAM: {tamnaho_anterior} bytes.")

    for i in range (1, 1000000):
        inicio =time.perf_counter()
        minha_lista.insert(1,i)
        tamnaho_atual = sys.getsizeof(minha_lista)

        if tamnaho_atual != tamnaho_anterior:
            print(
                f"->REALOCAÇÃO DETECTADA!{i} elementos | tamanho na RAM:"
                f"{tamnaho_atual} bytes (Salto de "
                f"+ {tamnaho_atual - tamnaho_anterior} bytes)."
            )
            tamnaho_anterior = tamnaho_atual
        fim =time.perf_counter()
    tempo_total =fim - inicio
    print(f"Tarefa concluida em {tempo_total} segundos.")

if __name__== "__main__":
    demosntrar_comportamento_memoria()