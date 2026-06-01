Binary search is an algorithm, its input is a sorted list of elements. If an element you are looking for is in that list binary search returns the position where its located, otherwise binary search return null

For any list of n, binary search will take log2 n steps to run the worst case.
where simple search will take n steps

Binary search runs in logarithimc time or log time

Big O notation tells you how fast an algorithm is. Big O notation lets you compare the number of operations. It tells you how fast an algorithm grows.

O(n)
O= Big O
n= number of operations

Some Common big O run times

O(logn) also knows as log time. EX- binary search
O(n) also known as linear time, EX- simple search
O(n * log n ) EX- a fast sorting algorithm, like quicksort
O(n*n or n square) EX- a slow sorting algorithm, like selection sort
O(n!) EX- a really slow algorithm, like the travelling salesperson

Important--
-Algorithm speed isn't measured in seconds but in growth of the number of operations
-Instead of seconds, we talk about how quickly the run time of an algorithm increases as the size of the input increases
-Run time of algorithms is expressed in big O notation
-O(log n ) is faster than O(n) and it gets a lot faster as the list of items you are searching grows
