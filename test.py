def test(num1, num2=1):
    data = 0
    for n1 in range(num1):
        for n2 in range(num2):
            data += n1 * n2
    return data


def disp(n1, n2):
    print(test(n1, n2))


disp(5, 10)
