def heapify(arr, n, i):
    """
    Esta função heapify é usada para manter
    a propriedade do heap (máximo, neste caso)
    em um determinado índice i no array arrde tamanho n.
    """
    largest = i
    """
    Inicializa uma variável largest como o índice atual (i),
    assumindo que o maior elemento está na posição i (raiz).
    """
    left = 2 * i + 1  # Calcula o índice do filho esquerdo do nó atual.
    """
    O filho esquerdo de um nodo no indice i pode ser calculado como 2 x i + 1.
    Isso ocorre pq, na representacao de um heap como um array,
    o filho esquerdo de um no em i esta localizado na posicao 2 x i + 1 no array.
    """
    right = 2 * i + 2  # Calcula o índice do filho direito do nó atual.
    """
    O filho direito de um nodo no indice i pode ser calculado como 2 x i + 2.
    Isso ocorre pq, na representacao de um heap como um array,
    o filho direito de um no em i esta localizado na posicao 2 x i + 2 no array.
    """
    # Verifica se o filho da esquerda da raiz existe e se é maior que a raiz
    if left < n and arr[i] < arr[left]:
        largest = left
    """
    Verifica se o indice do filho esquerdo esta dentro dos limites do array (left < n)
    e se o valor do filho esquerdo eh maior que o valor do no atual. Se for verdadeiro,
    atualiza o indice do 'largest' para o no esquerdo.
    """
    # Verifica se o filho da direita da raiz existe e se é maior que a raiz
    if right < n and arr[largest] < arr[right]:
        largest = right
    """
    Verifica se o indice do filho direito esta dentro dos limites do array (right < n)
    e se o valor do filho direito eh maior que o valor do no atualmente considerado como o maior (largest).
    Se for verdadeiro, atualiza o indice do 'largest' para o no direito.
    """
    # Troca a raiz se necessário
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Troca
        # Heapify a subárvore afetada
        heapify(arr, n, largest)
    """
    Verifica se o indice 'largest' foi atualizado. Se for diferente do indice original ('i'),
    significa que o nó atual não é o maior. Então, ocorre uma troca entre o nó atual('arr[i]')
    e o no maior('arr[largest]'), seguida por uma chamada recursiva para 'heapify' na subarvore afetada
    """


def heapsort(arr): # Esta função heapsort executa o algoritmo de ordenação Heap Sort.
    n = len(arr) # Obtém o tamanho do array.

    # Constrói um maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    """
    Constrói um heap máximo. Começa pelo meio do array e vai até o primeiro elemento,
    chamando 'heapify' em cada no para garantir que a propriedade do heap seja mantida.
    """
    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Troca
        heapify(arr, i, 0)

    """
    Extrai elementos um por um. Troca o primeiro elemento (que é o maior no heap máximo)
    com o último elemento não ordenado e chama 'heapify' na subarvore reduzida para reorganizar heap.
    """


# Exemplo de uso:
arr = [8, 11, 13, 6, 12, 7] # array desordenado
heapsort(arr) # chama a funcao heap sort para ordenar o array
print("Array ordenado:")
print(arr)
