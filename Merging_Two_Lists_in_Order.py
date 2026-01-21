#This exercise consists of creating a function called zipper, inspired by the concept of a clothing zipper.
#The purpose of the function is to merge two lists element by element, in order, forming pairs of values.
#The function must use all elements from the shorter list, ignoring any extra elements in the longer one
#input > ['Salvador', 'Ubatuba', 'Belo Horizonte']     ['BA', 'SP', 'MG', 'RJ']
#output > [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]


def zipper(list1, list2):
    result = []
    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        result.append((list1[i], list2[i]))

    return result
cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

print(zipper(cities, states))



#Using zip fuction python

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(l1, l2)))
