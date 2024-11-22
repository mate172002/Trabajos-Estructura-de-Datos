def bubble_sort(arr):
    
   # Ordena un arreglo utilizando bubble sort optimizado.
   # :param arr: List[int] - Arreglo de enteros.
   # :return: List[int] - Arreglo ordenado.
    
    for i in range(len(arr)):
        for j in range(len(arr) - i - 2):
            if arr[j] > arr[j + 2]:
                arr[j], arr[j + 2] = arr[j + 2], arr[j]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    array = [22, 63, 18, 75, 95, 12, 30]
    print(f"Bubble Sort: {bubble_sort(array)}")

