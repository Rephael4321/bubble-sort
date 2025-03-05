STEPS = 0

def bubbleSort(lst: list[int]) -> list[int]:
    global STEPS
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            STEPS += 1
    return lst

if __name__ == '__main__':
    test_list = [145, 8, 1, 86, 9, 68, 12, 74, 23, 1, 6, 34, 7, 2, 5, 0, 0, 0, 4, 0]
    sorted_list = bubbleSort(test_list)
    print(sorted_list)
    print(f"sorted in {STEPS} steps")
