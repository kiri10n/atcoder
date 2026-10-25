
def bubule_sort(a, n):
    for i in range(n-1, 0, -1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def quick_sort(a, n):
    if n <= 1:
        return a
    
    pivot = a[0]

    left = []
    right = []
    for i in range(1, n):
        if a[i] < pivot:
            left.append(a[i])
        else:
            right.append(a[i])
    return quick_sort(left, len(left)) + [pivot] + quick_sort(right, len(right))

def merge(left, right):
    merged_list = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1
    if i<len(left):
        merged_list += left[i:]
    elif j<len(right):
        merged_list += right[j:]
    return merged_list

def merge_sort(a, n):
    if n <= 1:
        return a
    mid = n // 2
    left = merge_sort(a[:mid], mid)
    right = merge_sort(a[mid:], n-mid)
    return merge(left, right)
    
    

def main():
    n = int(input())
    a = list(map(int, input().split()))

    sorted_a = merge_sort(a, n)

    print(" ".join(map(str, sorted_a)))

if __name__ == '__main__':
    main()