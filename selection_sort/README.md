# Selection Sort Algorithm

This repository contains an implementation of the **Selection Sort** algorithm in Python. Below is a detailed explanation of the code and answers to common questions about the implementation.

---

## Code Overview

The implementation consists of two functions:

1. `findsmallest(arr)`: Finds the index of the smallest element in an array.
2. `selectionSort(arr)`: Sorts an array using the Selection Sort algorithm.

---

## Questions and Explanations

### 1. **Why use `for i in range(len(copiedArr)):` in Python?**

The `for i in range(len(copiedArr)):` loop is used to iterate over the array `copiedArr` a specific number of times. The `len(copiedArr)` gives the total number of elements in the array, and the `range()` function generates a sequence of numbers from `0` to `len(copiedArr) - 1`. This ensures that the loop runs exactly once for each element in the array.

In this case, the loop is used to repeatedly find the smallest element in the array and remove it until all elements are sorted and added to the new array `newArr`.

---

### 2. **Why use `list(arr)` again if already passing an array?**

The `list(arr)` is used to create a **copy** of the input array `arr`. This is important because the `selectionSort` function modifies the array by removing elements using `pop()`. If you directly modify the input array, it will affect the original array outside the function, which is generally not desirable.

By creating a copy (`copiedArr = list(arr)`), the original array remains unchanged, and all modifications are performed on the copy.

---

### 3. **What is the `findsmallest` function doing?**

The `findsmallest` function is designed to find the **index of the smallest element** in a given array. Here's how it works:

1. It assumes the first element of the array is the smallest.
2. It iterates through the rest of the array, comparing each element with the current smallest value.
3. If a smaller element is found, it updates the smallest value and its index.
4. Finally, it returns the index of the smallest element.

Example:
Input: [5, 3, 6, 2, 10]
Output: 3 (index of the smallest element, 2)

### 4. **The code uses two for loops because the Selection Sort algorithm involves two distinct tasks:**


Outer Loop:

In selectionSort, the outer loop (for i in range(len(copiedArr))) ensures that the sorting process is repeated for every element in the array.
It runs n times, where n is the length of the array.
Inner Loop:

In findsmallest, the inner loop (for i in range(1, len(arr))) finds the smallest element in the current unsorted portion of the array.
It runs approximately n, n-1, n-2, ..., 1 times over the course of the algorithm.
The two loops together give the algorithm a time complexity of ( O(n^2) ).

### 5. **What does newArr.append(copiedArr.pop(smallest)) do?:**
This line performs two operations:

copiedArr.pop(smallest):

Removes the smallest element (at index smallest) from the copiedArr array and returns it.
This modifies the copiedArr array by removing the smallest element.
newArr.append(...):

Appends the removed smallest element to the newArr array, which is being used to store the sorted elements.
Together, this line moves the smallest element from the unsorted array (copiedArr) to the sorted array (newArr).

### 6. **Why is findsmallest called inside the loop?**

The findsmallest function is called inside the loop because the smallest element needs to be found repeatedly for the remaining unsorted portion of the array. After each iteration, the smallest element is removed from the unsorted array (copiedArr), so the next smallest element must be found in the updated array.

### 7. **Why is the original array not modified?**

The original array is not modified because a copy of the array is created using list(arr). All operations, such as removing elements with pop(), are performed on the copied array (copiedArr), leaving the original array unchanged.

### 8. **What is the time complexity of this implementation?**

The time complexity of this implementation is ( O(n^2) ), where n is the length of the array. This is because:

The outer loop runs n times.
The inner loop (in findsmallest) runs approximately n, n-1, n-2, ..., 1 times over the course of the algorithm.
The total number of iterations is proportional to ( n + (n-1) + (n-2) + ... + 1 = \frac{n(n+1)}{2} ), which simplifies to ( O(n^2) ).


Example Walkthrough
Input: [5, 3, 6, 2, 10]

Iteration 1:

findsmallest finds 2 (index 3).
2 is removed from copiedArr and added to newArr.
copiedArr = [5, 3, 6, 10], newArr = [2].
Iteration 2:

findsmallest finds 3 (index 1).
3 is removed from copiedArr and added to newArr.
copiedArr = [5, 6, 10], newArr = [2, 3].
Iteration 3:

findsmallest finds 5 (index 0).
5 is removed from copiedArr and added to newArr.
copiedArr = [6, 10], newArr = [2, 3, 5].
Iteration 4:

findsmallest finds 6 (index 0).
6 is removed from copiedArr and added to newArr.
copiedArr = [10], newArr = [2, 3, 5, 6].
Iteration 5:

findsmallest finds 10 (index 0).
10 is removed from copiedArr and added to newArr.
copiedArr = [], newArr = [2, 3, 5, 6, 10].
Output: [2, 3, 5, 6, 10]

This implementation of Selection Sort is simple and easy to understand but not the most efficient for large datasets due to its ( O(n^2) ) time complexity. It is useful for educational purposes and small datasets. ```
````
