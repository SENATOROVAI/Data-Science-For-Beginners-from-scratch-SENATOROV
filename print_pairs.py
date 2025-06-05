def print_pairs(lst):
    """Функция выводит элементы списка (i, j) во внутреннем цикле."""
    for i in lst:
        for j in lst:
            print(i, j)


print(print_pairs.__code__.co_code)
print(print_pairs.__code__.co_code.__class__)
