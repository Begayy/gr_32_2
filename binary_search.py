def binary_search(element, lst):
    n = len(lst)
    first = 0
    last = n - 1
    resultOK = False
    result = None
    while first <= last:
        mid = (first + last) // 2
        if lst[mid] == element:
            resultOK = True
            result = mid
            break
        elif lst[mid] < element:
            first = mid + 1
        else:
            last = mid - 1

    if resultOK:
        print(f"Элемент найден на позиции {result}.")
    else:
        print("Элемент не найден.")


lst = [23, 21, 45, 5, 1]
element = 23
print(binary_search(element, lst))
