#A = "[a,b,c]"

#list1NZXZ = []


list5 = [25, 17, [3, 5, 7], 88, 12, 'Python']


print(list5[2]) # [3, 5, 7]
print(list5[2][1]) # 5
print(list5[-1]) # Python
print(list5[-1][-4]) # h

print("-"*100)



dict1 = {'a': 123,
         34 : 56.78,
         23.33 : (5, 7, 8),
         (4, 5, 7) : [5, 88, 12],
         True : {'a': 123, 'b': 345},
         (2) : (2,3,4),
          #[1, 2, 3 ]: 'Python'} # TypeError: unhashable type: 'list'
         }
print(dict1);


set1 = {4, 5, 5.6, 'Hello', (5, 7, 8), True, None, 4, 5,}
print(set1)