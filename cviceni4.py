
def my_range(start, stop, step):
    """
    Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range
    """
    seznam_hodnot = []
    value = start
    while value < stop:
        seznam_hodnot.append(start)
        value += step
    return seznam_hodnot


def my_enumerate(iterable , start = 0):

    """
    Nase vlastni implementace enumerate(), chceme, aby se chovala uplne stejne jako enumerate
    """
    
    result = []
    index = 0
    for value in iterable:
        result.append((index, value))
        index += 1
        return result
    
def while_enumerat(iterable, start = 0):

    result = []
    i = 0

    while i < len(iterable):
        result.append( ( i, iterable[i] ) )
        i += 1

    return result


def my_zip(*iterables):

    """
    Nase vlastni implementace zip(), chceme, aby se chovala uplne stejne jako zip
    """
    results = []
    lenght = len(iterables[0])

    for i in range(0, lenght):
        subresult = []

        for iterable in iterables:
            subresult.append(iterable[i])
        results.append(tuple(subresult))

    return results


if __name__ == "__main__":

    #print(list(range(1, 10)))
    #print(my_range(1, 10, 3))

    #print(list(enumerate("abcdef")))
    #print(my_enumerate("abcdef"))

    #print(list(enumerate(['Alice', 'Bob', 'Eva'])))
    #print(my_enumerate(["Alice", "Bob", "Eva"]))

    #print(list(zip([1,2,3], [4,5,6], [7,8,9], [10,11,12])))
    print(my_zip([1,2,3], [4,5,6], [7,8,9], [10,11,12]))