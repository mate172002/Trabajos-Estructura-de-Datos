def find_max_min(arr):
    
   # Encuentra el valor maximo y minimo de un arreglo.
   # :param arr: List[int] - Arreglo de enteros.
   # :return: Tuple[int, int] - (Max, Min)
    
    return max(arr), min(arr)

# Ejemplo de uso
if __name__ == "__main__":
    array = [5, 3, 8, 6, 2, 7]
    max_val, min_val = find_max_min(array)
    print(f"Maximo: {max_val}, Minimo: {min_val}")
