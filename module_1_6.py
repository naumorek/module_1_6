
#2

my_dict = {'Петя': 1995, 'Женя': 1959, 'Василиса': 1976, 'Антуанета': 1984}
print(my_dict)
print(my_dict.get('Женя'))
print(my_dict.get('Джимми', 'таких нету'))
my_dict.update({'Джордж': 2001, 'Камила': 2007})
print(my_dict)
a=my_dict.pop('Петя')
print(a)
print(my_dict)

#3

my_set={1,5,6,2,5,31,5,512,54,4,2,3,1,4,512,24,34121,31,415,3}
print(my_set)
my_set.add(988)
my_set.add(888)
my_set.remove(1)
print(my_set)
