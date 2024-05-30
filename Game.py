# Test to print the word s in a given string:
stri = 'This is a string to test your understanding of split and for loops'

t1 = stri.split()

for c in t1:
    i = 0
    j = 0
    if c[i][j] == 's':
     i += 1
     j += 1
     print(c)


# Print all the even numbers:
print('Printing Even numbers :')
for i in range(0, 10):
   if i%2 == 0:
      print(i)


# List comprehension of numbers divisible by 3:
print('List comprehension of numbers divisible by 3')
numb = [a for a in range(0,50) if a%3 == 0]
print(numb)


# Test to print all words that are even in length:
leng = 'Go through the length of this string and if it is even print it'
print(leng.split())

for e in leng.split():
    if len((e))%2 == 0:
     print(e, 'is even',)


# Print fizz for multiples of 3, buzz for multiples of 5 and fizbuzz for both:
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


# Print a list of all the first letters of words in a given string:
t6 = 'Make a list of the first letters of this string let us see how you do this'
print(t6)

m = []
for r in t6.split():
    i = 0
    m.append(r[i])
    i += 1
print(m)

t61 = [x[0] for x in t6.split()]
print(t61, 'List comprehension method')


# Print all prime numbers for a given range:
t7 = 'Print all the prime numbers for a given range'
mynum = range(1, 70)

def prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

primes = list(filter(prime, mynum))
print(primes)


# Write a function to return lesser of two evens:
def lesser_of_two_evens(a1, b1):
    if a1%2 == 0 and b1%2 == 0:
        if a1 < b1:
           return a1
        else:
           return b1
    elif a1%2 != 0 or b1%2 != 0:
        if a1 < b1:
           return b1
        else:
           return a1

print(lesser_of_two_evens(6, 2))


# Write a function that accepts two strings and if both the starting letters are same, print true. Else false.
def animal_crackers(animal):
   ph = animal.split()
   if ph[0][0].lower() == ph[1][0].lower():
      return True
   else:
      return False

print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy kangaroo'))


# Write a function to print True if sum of two integers is 20.
def make_twenty(s, t):
   if s == 20 or t ==20:
      return True
   return s+t == 20

print(make_twenty(20, 4))
print(make_twenty(15, 5))
print(make_twenty(4, 7))


# Write a function to capitalize the 1st and 4th letters in a string:
def cap_name(namaya):
   new = []
   for i in namaya.capitalize().split():
      new.append(i[0:3])
      new.append(i[3].upper())
      new.append(i[4:])

   return ''.join(new)


print(cap_name('Matthew'))


# Write a function to reverse the given words in a string:

def rev_words(stg):
   lol = stg.split()
   lol.reverse()
   return ' '.join(lol)

print(rev_words('Hello how are you'))


# Write a function to return true if a given integer is within 10 of either

def almost_there(at):
   if at >= 90 and at < 190:
      for x in range(90, 111):
         if x%at == 0:
            return True
      return False
   elif at >= 190:
      for x in range(190, 211):
         if x%at == 0:
            return True
      return False
# There is another way of doing this using the abs function:
# def almost_there(at):
#     return (abs(100 - at) <= 10) or (abs(200 - at) <= 10)

print(almost_there(90))
print(almost_there(110))
print(almost_there(150))
print(almost_there(209))


# Write a function that returns true if two consecutive numbers are equal.

list1 = [1, 2, 3, 4]
list2 = [3, 3, 2, 1]
list3 = [5, 6, 3, 3]
def has_33(nlist):
   for x in range(len(nlist) - 1):
      if nlist[x] == 3 and nlist[x+1] == 3:
         return True
   return False

print(has_33(list1))
print(has_33(list2))
print(has_33(list3))


# Given a string, return 3 times the same characters in the string.

def estr(wods):
   w = []
   for x in wods:
      w.append(x*3)
   return ''.join(w)

print(estr('Hello'))


# Write a function about blackjack game:

def blackjack(b, l, j):
   if b+l+j <= 21:
      return b+l+j
   elif  b+l+j <= 31 and 11 in [b, l, j]:
      return b+l+j - 10
   else:
      return 'BUST'

print(blackjack(8,9,2))
print(blackjack(7,9,11))
print(blackjack(9, 9, 9))


# Write a function about an array of numbers:

def summer(arr):
   ig = []
   if len(arr) == 0:
      return 0
   else:
      for x in arr:
         if x not in [6, 7, 8, 9]:
            ig.append(x)
      return sum(ig)
      

lala = [1,4,5,6,7,8,9]
la = [2,1,6,9,11]
le = [1,4,2]

print(summer(lala))
print(summer(la))
print(summer(le))


# Write a function to print true if a given list has 0, 0, 7 in order.

def bond(nolist):
   nl = [0, 0, 7, 'x']
   for x in nolist:
      if x == nl[0]:
         nl.pop(0)
   return len(nl) == 1

yrr = [1, 2, 4, 3, 0, 0, 7, 6]
yre = [6,3,0,4,0,1,7]
yra = [3,7,1,0,3,0,9]

print(bond(yrr))
print(bond(yre))
print(bond(yra))


# Write a function to count prime:

def count_primes(num):
   if num == 1:
      return False
   for x in range(2,num):
      if num%x == 0:
         return False
   return True

neww = range(1, 100)

print(len(list(filter(count_primes, neww))))



