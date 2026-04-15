# arr = [50, 40, 60, 30, 20, 10]

# def partition(arr, low, high):
#     #low is 0 pos and high is size-1 pivot is high 
#     pivot = arr[high]
#     i = low - 1
#     print(i)
#     for j in range(low, high):
#         # print(j)
#         if arr[j] < pivot:
#             # print(i)
#             i += 1
#             # print(arr[i], arr[j])
#             arr[i], arr[j] = arr[j], arr[i]
#             # print(arr[i], arr[j])

#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1

# def quick_sort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quick_sort(arr, low, pi - 1)
#         quick_sort(arr, pi + 1, high)

# quick_sort(arr, 0, len(arr) - 1)
# print(arr)

class QuickSort:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] >= pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quick_sort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)

arr = [50, 40, 60, 30, 20, 10]
qs = QuickSort()
qs.quick_sort(arr, 0, len(arr) - 1)
print(arr)  