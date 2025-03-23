def mysum(numbers: list, start: int=0) -> int:
    '''Возвращает сумму чисел'''
    output = start

    for number in numbers:
        output += number
    
    return output


def main():
    print(mysum([1, 2, 3], 4))


if __name__ == '__main__':
    main()