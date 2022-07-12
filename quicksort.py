# Author: Meher Kalra
# Date: 21 Feb 2022
# Purpose: Lab-3 - writing the quicksort algorithm

# Purpose: defining a function to compare two values in a list and switching their places with the greater value
# with parameters the_list, p, r, compare_func
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p

    pivot = the_list[r]
    while j < r:
        if compare_func(the_list[j], pivot):
            i = i + 1
            the_list[i], the_list[j] = the_list[j], the_list[i]
        j = j + 1
    the_list[r], the_list[i+1] = the_list[i+1], the_list[j]
    return i + 1

# Purpose: defining a function to call the partition function (recursively) with parameters the_list, r, p, compare_func
# compare_func(to compare names, pop, latitude, etc on a list the list is sorted

def quicksort(the_list, p, r, compare_func):
    if len(the_list[p:r+1]) >= 2:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q - 1, compare_func)
        quicksort(the_list, q + 1, r, compare_func)

# Purpose: applying the quicksort function to sort a list referenced by the_list
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)


