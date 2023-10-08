def positive_sum(arr):
    sum = 0
    
    for elem in arr:
        if elem > 0:
           sum += elem
    
    return sum
