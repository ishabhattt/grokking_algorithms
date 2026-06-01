"""Suppose you have a sorted lists of 128 numbers 
and you're searching through it using binary search"""


def bineary_search(item):
 val= list(range(0,128))

 low=0
 high=len(val)-1
 while low <= high:
  mid=(low+high)//2
  guess= val[mid]
  if guess== item:
   return mid
  elif guess>item:
   high= mid-1
  else:
   low = mid+1
 return None


print(bineary_search(64))