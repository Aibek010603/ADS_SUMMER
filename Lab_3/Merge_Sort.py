def merge_sort(arr):
    #Базовый случай: если длина массива 0 или 1, он уже отсортирован
    if len(arr) <= 1:
        return arr

    #Разделение массива на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #Рекурсивная сортировка обеих половин
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    #Объединение двух отсортированных половин
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    #Сравнение элементов из обеих половин и сбор наименьших
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    #Добавление оставшихся элементов 
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

#Пример
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
