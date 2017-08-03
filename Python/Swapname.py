name1=['2']
name2=['3']

def swap(name1,name2):
  tmp = name1[0]
  name1[0]= name2[0]
  name2[0]= tmp

print(name1[0])
print(name2[0])

swap(name1,name2)
print(name1[0])
print(name2[0])
