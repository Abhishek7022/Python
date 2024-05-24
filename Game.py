stri = 'This is a string to test your asfk understanding of split and for loops'

t1 = stri.split()

for c in t1:
    i = 0
    j = 0
    if c[i][j] == 's':
     i += 1
     j += 1
     print(c)


print('Printing Even numbers :')
for i in range(0, 10):
   if i%2 == 0:
      print(i)


print('List comprehension of numbers divisible by 3')
numb = [a for a in range(0,50) if a%3 == 0]
print(numb)


leng = 'Go through the length of this string and if it is even print it'
print(leng.split())

for e in leng.split():
    if len((e))%2 == 0:
     print(e, 'is even',)


t5 = '''Print the numbers from 1 to 100, for multples of 3 print fizz, for 5
       print buzz and for both 3 and 5 print fizzbuzz'''
print(t5)

for i in range(0,101):
   if i%3 == 0 and i%5 == 0:
      print('fizzbuzz')
   elif i%5 == 0:
      print('buzz')
   elif i%3 == 0:
      print('fizz')
   else:
      print(i)


t6 = 'Make a list of the first letters of this string let us see how you do this'
print(t6)

m = []
for r in t6.split():
    i = 0
    m.append(r[i])
    i += 1
print(m)

t7 = [x[0] for x in t6.split()]
print(t7, 'List comprehension method')