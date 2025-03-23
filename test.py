from typing import Any

def mymin(lst: list[Any]) -> Any:
    '''Возвращает минимальное значение из списка'''
    mn = lst[0]

    for item in lst:
        if mn > item:
            mn = item

    return mn


def mymax(lst: list[Any]) -> Any:
    '''Возвращает максимальное значение из списка'''
    mx = lst[0]

    for item in lst:
        if mx < item:
            mx = item

    return mx


def get_data_words(words: list[str]) -> tuple[int, int, float]:
    '''Возвращает кортеж, состоящий из трёх чисел:
       длина самого короткого слова, длина самого линного слова,
       средняя длина слова'''
    total = 0
    counter = 0
    mn_word = mx_word = len(words[0])

    for word in words:
        length = len(word)
        total += length
        counter += 1

        if length < mn_word:
            mn_word = length

        if length > mx_word:
            mx_word = length

    avg_word = total / counter

    return mn_word, mx_word, avg_word


def main():
    print(get_data_words(['лев', 'рынок', 'яблоко', 'лампочка']))


if __name__ == '__main__':
    main()


        
    