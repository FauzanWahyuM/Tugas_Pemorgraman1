def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


def binary_search(keyword, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right)//2
        if data[mid] > keyword:
            right = mid - 1
        elif data[mid] < keyword:
            left = mid + 1
        else:
            print(f"Keyword {keyword} has found in index {mid}")
            return mid

    print(f"Keyword {keyword} not found")
    return -1


data = [32, 7, 44, 21, 61, 25, 45]
keyword = int(input("Input Keyword: "))
bubble_sort(data)
binary_search(keyword, data)
