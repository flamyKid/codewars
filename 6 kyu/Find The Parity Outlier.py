# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    odd = []
    even = []

    for num in integers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]