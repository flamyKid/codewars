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


def test(data, answer):
    assert data == answer, f'{data} should be {answer}'


if __name__ == '__main__':
    test(find_outlier([2, 4, 6, 8, 10, 3]), 3)
    test(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
    test(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
    print('___ Everything test passed ___')
