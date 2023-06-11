print("\nNama 10 Anggota Organisasi")

def selection_sort(array):
     for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i],array[min_index] = array[min_index], array[i]  
     return array


list_1 = ["Zhafira", "Nirmala", "Aksara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print(f"before : {list_1}")
selection_sort(list_1)
print(f"After : {list_1}") 
