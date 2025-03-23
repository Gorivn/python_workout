import mysum

def myavg(numbers: list[int]) -> float:
    '''Возвращает среднее арифметическое чисел списка'''
    result = mysum.mysum(numbers) / len(numbers)
    return result


def main():
    print(myavg([10, 30, 40, 50]))


if __name__ == "__main__":
    main()