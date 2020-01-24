#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
---- O(n)
a = 0
    while (a < n * n * n):
      a = a + n * n
when n=2:
a = 4
a = 8
when n =3:
a = 9
a = 18
a= 27

The function runs n times before reach the limit, so it is O(n)
b)
------O(n^2)
 sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
There are two loop: one is looped n time, the other is looped 1/2n time
so it is O(n*1/2n) ~= O(n^2)

c)
------O(n) 
def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

This is s recursive function. It will run the function (bunnies) times, so it is O(n)
## Exercise II

I am going to use binary search in this quesiton 

when highest - lowest ==0
    return the number
find the middle heigh
    if broken:
        highest == middle height
        repeat the function
    if OK:
        lowest == middle height
        repeat the function
