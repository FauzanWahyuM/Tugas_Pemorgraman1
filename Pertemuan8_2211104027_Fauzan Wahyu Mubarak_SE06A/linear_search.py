def linear_search(keyword, data):
    for i in range(len(data)):
        if data[i] == keyword:
            print(f"Keyword {keyword} has found at index {i}")
            return i
    print(f"Keyword {keyword} not found")   
    return -1


data = [32, 7, 44, 21, 61, 25, 45]
keyword = int(input("Input Keyword: "))
linear_search(keyword, data)
