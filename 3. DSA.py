# ------------------------------------------------------ Fibonacci Alglorithm ------------------------------------------------------------

# num1 = 0
# num2 = 1

#print(num0)
#print(num1)

# for x in range(18):
#     result = num1 + num2
#     print(result)
#     num1 = num2
#     num2 = result

# print(0)
# print(1)


# def Fibonacci(num1, num2, count = 0):
#     if count <= 19:
#         result = num1 + num2
#         print(result)
#         num1 = num2
#         num2 = result
#         count +=1
#         Fibonacci(num1, num2, count)
#     else:
#         return
# Fibonacci(0,1)        

# def F(n):
#     if n <= 1:
#         return n
#     else:
#         return F(n - 1) + F(n - 2)

# print(F(4))
# --------------------------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------- Lowest Value -------------------------------------------------------------
# myList = [11, 8, 9, 5, 10, 12, 16, 2, 88]

# def FindMinValue(list):
#     minValue = list[0]

#     for x in list:
#         if x < minValue:
#             minValue = x

#     return minValue
# print(FindMinValue(myList))        
# --------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------- Bubble Sort ---------------------------------------------------------------
# How it works:
# 1. Go through the array, one value at a time.
# 2. For each value, compare the value with the next value.
# 3. If the value is higher than the next one, swap the values so that the highest value comes last.
# 4. Go through the array as many times as there are values in the array.

# import random

# def bubble_sort(arr):
#     n = len(arr)
#     counter = 0
#     for i in range(n - 1):
#         swapped = False
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 counter += 1
#                 swapped = True
#         if not swapped:
#             break
#     return arr, counter

# mylist = [random.randint(1, 10) for _ in range(20)]
# sorted_array, num_swaps = bubble_sort(mylist)

# print(f"Sorted Array: {sorted_array}, with {num_swaps} swaps.")
# ------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------- Selection Sort ----------------------------------------------------------
# How it works:
# 1. Go through the array to find the lowest value.
# 2. Move the lowest value to the front of the unsorted part of the array.
# 3. Go through the array again as many times as there are values in the array.

# import random

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n - 1):
#         minIndex = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[minIndex]:
#                 minIndex = j
#         arr[i], arr[minIndex] = arr[minIndex], arr[i]
#     return arr

# mylist = [random.randint(1, 10) for _ in range(10)]
# sorted_array = selection_sort(mylist)

# print("Sorted array:", sorted_array)
# -----------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------- Insertion Sort ---------------------------------------------------------------
#How it works:
# 1. Take the first value from the unsorted part of the array.
# 2. Move the value into the correct place in the sorted part of the array.
# 3. Go through the unsorted part of the array again as many times as there are values.
# -----------------------------------------------------------------------------------------------------------------------------------------

# import random

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         insert_index = i
#         current_value = arr[i]

#         for j in range(i - 1, -1, -1):
#             if arr[j] > current_value:
#                 arr[j + 1] = arr[j]
#                 insert_index = j
#             else:
#                 break

#         arr[insert_index] = current_value
#     return arr

# mylist = [random.randint(1, 10) for _ in range(10)]
# sorted_list = insertion_sort(mylist)

# print("Sorted List:", sorted_list)


# -------------------------------------------------------- Quick Sort ------------------------------------------------------------------------
# How it works: O(n log n)
# 1. Choose a value in the array to be the pivot element.
# 2. Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
# 3. Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
# 4. Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
# ---------------------------------------------------------------------------------------------------------------------------------------------
# import random

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1

# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)

# mylist = [random.randint(1, 10) for _ in range(10)]
# quicksort(mylist)

# print("Sorted array:", mylist)

# --------------------------------------------------------- Counting Sort -----------------------------------------------------------------
# How it works:
# 
# 1. Create a new array for counting how many there are of the different values.
# 2. Go through the array that needs to be sorted.
# 3. For each value, count it by increasing the counting array at the corresponding index.
# 4. After counting the values, go through the counting array to create the sorted array.
# 5. For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index.
# -----------------------------------------------------------------------------------------------------------------------------------------

# import random

# def countingSort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)

#     while len(arr) > 0:
#         num = arr.pop(0)
#         count[num] += 1

#     for i in range(len(count)):
#         while count[i] > 0:
#             arr.append(i)
#             count[i] -= 1

#     return arr

# unsortedArr = [random.randint(1, 10) for _ in range(10)]
# sortedArr = countingSort(unsortedArr)

# print("Sorted array:", sortedArr)

# ------------------------------------------------------ Radix Sort -----------------------------------------------------------------
# How it works:
# 
# 1. Start with the least significant digit (rightmost digit).
# 2. Sort the values based on the digit in focus by first putting the values 
#    in the correct bucket based on the digit in focus, and then put them back into array in the correct order.
# 3. Move to the next digit, and sort again, like in the step above, until there are no digits left.
# -----------------------------------------------------------------------------------------------------------------------------------

# import random
# myArray = [random.randint(1 , 10) for _ in range(10)]

# def RadixSort(array):
#     radixArray = [[], [], [], [], [], [], [], [], [], []]
#     maxValu = max(array)
#     exp = 1

#     while maxValu // exp > 0:
#         while len(array) > 0:
#             val = array.pop()
#             radixIndex = (val // exp) % 10
#             radixArray[radixIndex].append(val)

#         for bucket in radixArray:
#             while len(bucket) > 0:
#                 val = bucket.pop()
#                 array.append(val)

#         exp *= 10
#         return array

# print("Sorted Array: ", RadixSort(myArray))

# ------------------------------------------------- Merge Sort ------------------------------------------------------------------------
# How it works:
# 1. Divide the unsorted array into two sub-arrays, half the size of the original.
# 2. Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
# 3. Merge two sub-arrays together by always putting the lowest value first
# 4. Keep merging until there are no sub-arrays left.
# -------------------------------------------------------------------------------------------------------------------------------------

# def mergeSort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     leftHalf = arr[:mid]
#     rightHalf = arr[mid:]

#     sortedLeft = mergeSort(leftHalf)
#     sortedRight = mergeSort(rightHalf)

#     return merge(sortedLeft, sortedRight)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]

# sortedArr = mergeSort(unsortedArr)
# print("Sorted array:", sortedArr)

# ---------------------------------------------- Linear Search ---------------------------------------------------------
# How it works:
# 1. Go through the array value by value from the start.
# 2. Compare each value to check if it is equal to the value we are looking for.
# 3. If the value is found, return the index of that value.
# 4. If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.
# ----------------------------------------------------------------------------------------------------------------------
# import random

# def LinearSearch(arr, targetVal):
#     for i in range(len(arr)):
#         if arr[i] == targetVal:
#             return i
#     return -1    

# myArry = [random.randint(1, 10) for _ in range(15)]
# targetValue = 9      

# result = LinearSearch(myArry, targetValue)
# print(myArry)

# if result == -1:
#     print(f"Value {targetValue} not found!")
# else:
#     print(f"Target value {targetValue} found at index {result}")    

# --------------------------------------------------------------- Binary Search -------------------------------------------------------------
# How it works:
# 1. Check the value in the center of the array.
# 2. If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
# 3. Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
# 4. If the value is found, return the target value index. If the target value is not found, return -1.

# import random

# def binarySearch(arr, targetVal):
#     left = 0
#     right = len(arr) - 1

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == targetVal:
#             return mid        
        
#         if arr[mid] < targetVal:
#             left = mid + 1
        
#         else:
#             right = mid - 1

#     return -1            




# myList = [random.randint(1, 20) for _ in range(10) ]
# quicksort(myList)

# TargetValue = 6

# result = binarySearch(myList, TargetValue)

# if result == -1:
#     print(f"Target value {TargetValue} not found!")
# else:
#     print(f"Target value {TargetValue} found at index {result}")   

# --------------------------------------------------------------- Linked List -------------------------------------------------------------
# 1. Singly linked list
# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node2.next = node3
# node3.next = node4

# currentNode = node1
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("null")

# 2. Doubly Linked List
# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None

# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3

# print("\nTraversing forward:")
# currentNode = node1
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("null")

# print("\nTraversing backward:")
# currentNode = node4
# while currentNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev
# print("null")

# 3. Circular Singly Linked List
# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None

# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node1

# currentNode = node1
# startNode = node1
# print(currentNode.data, end=" -> ") 
# currentNode = currentNode.next 

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next

# print("...")
# 4. Circular Doubly Linked List
# class Node:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.next = None
#         self.prev = None

# node1 = Node(3)
# node2 = Node(5)
# node3 = Node(13)
# node4 = Node(2)

# node1.next = node2
# node1.prev = node4

# node2.next = node3
# node2.prev = node1

# node3.next = node4
# node3.prev = node2

# node4.next = node1
# node4.prev = node3

# print("\nTraversing forward:")
# currentNode = node1
# startNode = node1
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.next

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.next
# print("...")

# print("\nTraversing backward:")
# currentNode = node4
# startNode = node4
# print(currentNode.data, end=" -> ")
# currentNode = currentNode.prev

# while currentNode != startNode:
#     print(currentNode.data, end=" -> ")
#     currentNode = currentNode.prev
# print("...")

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def traverseAndPrint(head):
#     currentNode = head
#     while currentNode:
#         print(currentNode.data, end=" -> ")
#         currentNode = currentNode.next
#     print("null")

# def deleteSpecificNode(head, nodeToDelete):

#     if head == nodeToDelete:
#         return head.next

#     currentNode = head
#     while currentNode.next and currentNode.next != nodeToDelete:
#         currentNode = currentNode.next

#     if currentNode.next is None:
#         return head

#     currentNode.next = currentNode.next.next

#     return head

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print("Before deletion:")
# traverseAndPrint(node1)

# # Delete node4
# node1 = deleteSpecificNode(node1, node4)

# print("\nAfter deletion:")
# traverseAndPrint(node1)

# stack = []

# # Push
# stack.append('A')
# stack.append('B')
# stack.append('C')
# print("Stack: ", stack)

# # Pop
# element = stack.pop()
# print("Pop: ", element)

# # Peek
# topElement = stack[-1]
# print("Peek: ", topElement)

# # isEmpty
# isEmpty = not bool(stack)
# print("isEmpty: ", isEmpty)

# # Size
# print("Size: ",len(stack))

# queue = []

# # Enqueue
# queue.append('A')
# queue.append('B')
# queue.append('C')
# print("Queue: ", queue)

# # Dequeue
# element = queue.pop(0)
# print("Dequeue: ", element)

# # Peek
# frontElement = queue[0]
# print("Peek: ", frontElement)

# # isEmpty
# isEmpty = not bool(queue)
# print("isEmpty: ", isEmpty)

# # Size
# print("Size: ", len(queue))

# --------------------------------------------------- Binary Trees --------------------------------------------------

# class TreeNode:
#     def __init__(self, data) -> None:
#         self.data = data
#         self.left = None
#         self.right = None

# NodeR = TreeNode('R')        
# NodeA = TreeNode('A')        
# NodeB = TreeNode('B')        
# NodeC = TreeNode('C')    
# NodeD = TreeNode('D')        
# NodeE = TreeNode('E')
# NodeF = TreeNode('F')
# NodeG = TreeNode('G')

# # Root Node
# NodeR.left = NodeA
# NodeR.right = NodeB

# NodeA.left = NodeC
# NodeA.right = NodeD

# NodeB.left = NodeE
# NodeB.right = NodeF

# NodeF.left = NodeG

# Pre-Order Traversal R -> A -> C -> D -> B -> E -> F -> G
# def PreOrderTraversal(node):
#     if node is None:
#         return
#     print(node.data, end = " -> ")
#     PreOrderTraversal(node.left)
#     PreOrderTraversal(node.right)

# print(PreOrderTraversal(NodeR))

# print('#' * 50)

# In-order Traversal C -> A -> D -> R -> E -> B -> G -> F
# def InOrderTraversal(node):
#     if node is None:
#         return
#     InOrderTraversal(node.left)
#     print(node.data, end = " -> ")
#     InOrderTraversal(node.right)

# print(InOrderTraversal(NodeR)) 

# print('#' * 50)

# Post-order Traversal
# def PostOrderTraversal(node):
#     if node is None:
#         return
#     PostOrderTraversal(node.left)
#     PostOrderTraversal(node.right)
#     print(node.data, end = " -> ")

# print(PostOrderTraversal(NodeR))

# storing left child node on index 2i+1
# right child node on index 2i+2

# To avoid wasting memory, binary tree using array must be perfect or nearly perfect
#binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']
#binary_tree_array = ['0', '1', '2', '3', '4', '5', '6', None, None, None, None, None, None, '13']
#perfect_binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F']

# def left_child_index(index):
#     return 2 * index + 1

# def right_child_index(index):
#     return 2 * index + 2

# def get_data(index):
#     if 0 <= index < len(binary_tree_array):
#         return binary_tree_array[index]
#     return None

# def pre_order(index):
#     if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#         return []
#     return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index))

# def in_order(index):
#     if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#         return []
#     return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

# def post_order(index):
#     if index >= len(binary_tree_array) or binary_tree_array[index] is None:
#         return []
#     return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

# print("Pre-order Traversal:", pre_order(0))
# print("In-order Traversal:", in_order(0))
# print("Post-order Traversal:", post_order(0))

# A Binary Search Tree is a Binary Tree where every node's left child has a lower value, and every node's right child has a higher value.
# The time complexity for searching a BST for a value is O(h), where his the height of the tree.
    
# properties must be true for any node "X" in the tree:
# 1. The X node's left child and all of its descendants (children, children's children, and so on) have lower values than X's value.
# 2. The right child, and all its descendants have higher values than X's value.
# 3. Left and right subtrees must also be Binary Search Trees.

# class TreeNode():
#     def __init__(self, data) -> None:
#         self.data = data
#         self.right = None
#         self.left = None

# RootNode  = TreeNode(13)
# NodeOne   = TreeNode(7)
# NodeTwo = TreeNode(15)
# NodeThree  = TreeNode(3)
# NodeFour  = TreeNode(8)
# NodeFive   = TreeNode(14)
# NodeSix = TreeNode(19)
# NodeSeven = TreeNode(18)

# RootNode.left = NodeOne
# RootNode.right = NodeTwo

# NodeOne.left = NodeThree
# NodeOne.right = NodeFour

# NodeTwo.left = NodeFive
# NodeTwo.right = NodeSix

# NodeSix.left = NodeSeven

# #PreOrderTraversal(RootNode)

# def SearchTree(Node, TargetVal, index=0):
#     if Node is None:
#         print(f"Target Value {TargetVal} not found!")
#         return
#     elif Node.data == TargetVal:
#         print(f"Target Value {TargetVal} found at index {index}!")
#         return
#     elif TargetVal < Node.data:
#         SearchTree(Node.left, TargetVal, index=index*2+1)
#     elif TargetVal > Node.data:
#         SearchTree(Node.right, TargetVal, index=index*2+2)

# def insert(node, data):
#     if node is None:
#         return TreeNode(data)
#     else:
#         if data < node.data:
#             node.left = insert(node.left, data)
#         elif data > node.data:
#             node.right = insert(node.right, data)
#     return node

# def minValueNode(node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current

# def delete(node, data):
#     if not node:
#         return None

#     if data < node.data:
#         node.left = delete(node.left, data)
#     elif data > node.data:
#         node.right = delete(node.right, data)
#     else:
#         # Node with only one child or no child
#         if not node.left:
#             temp = node.right
#             node = None
#             return temp
#         elif not node.right:
#             temp = node.left
#             node = None
#             return temp

#         # Node with two children, get the in-order successor
#         node.data = minValueNode(node.right).data
#         node.right = delete(node.right, node.data)

#     return node
    
# TargetValue = 19
# #SearchTree(RootNode, TargetValue)
# insert(RootNode, 10)
# PreOrderTraversal(RootNode)
# Minimum = minValueNode(RootNode)
# print(Minimum)

# AVL Trees
# BF(X) = height(rightSubtree(X)) - height(leftSubtree(X))
# 0: The node is in balance
# more than 0: The node is "right heavy"
# less than 0: The node is "Left heavy"

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#         self.height = 1

# def getHeight(node):
#     if not node:
#         return 0
#     return node.height

# def getBalance(node):
#     if not node:
#         return 0
#     return getHeight(node.left) - getHeight(node.right)

# def rightRotate(y):
#     print('Rotate right on node',y.data)
#     x = y.left
#     T2 = x.right
#     x.right = y
#     y.left = T2
#     y.height = 1 + max(getHeight(y.left), getHeight(y.right))
#     x.height = 1 + max(getHeight(x.left), getHeight(x.right))
#     return x

# def leftRotate(x):
#     print('Rotate left on node',x.data)
#     y = x.right
#     T2 = y.left
#     y.left = x
#     x.right = T2
#     x.height = 1 + max(getHeight(x.left), getHeight(x.right))
#     y.height = 1 + max(getHeight(y.left), getHeight(y.right))
#     return y

# def insert(node, data):
#     if not node:
#         return TreeNode(data)

#     if data < node.data:
#         node.left = insert(node.left, data)
#     elif data > node.data:
#         node.right = insert(node.right, data)

#     node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#     balance = getBalance(node)

#     # Left Left
#     if balance > 1 and data < node.left.data:
#         return rightRotate(node)

#     # Right Right
#     if balance < -1 and data > node.right.data:
#         return leftRotate(node)

#     # Left Right
#     if balance > 1 and data > node.left.data:
#         node.left = leftRotate(node.left)
#         return rightRotate(node)

#     # Right Left
#     if balance < -1 and data < node.right.data:
#         node.right = rightRotate(node.right)
#         return leftRotate(node)

#     return node

# def inOrderTraversal(node):
#     if node is None:
#         return
#     inOrderTraversal(node.left)
#     print(node.data, end=", ")
#     inOrderTraversal(node.right)

# def minValueNode(node):
#     current = node
#     while current.left is not None:
#         current = current.left
#     return current

# def delete(node, data):
#     if not node:
#         return node

#     if data < node.data:
#         node.left = delete(node.left, data)
#     elif data > node.data:
#         node.right = delete(node.right, data)
#     else:
#         if node.left is None:
#             temp = node.right
#             node = None
#             return temp
#         elif node.right is None:
#             temp = node.left
#             node = None
#             return temp

#         temp = minValueNode(node.right)
#         node.data = temp.data
#         node.right = delete(node.right, temp.data)

#     if node is None:
#         return node

#     # Update the balance factor and balance the tree
#     node.height = 1 + max(getHeight(node.left), getHeight(node.right))
#     balance = getBalance(node)

#     # Balancing the tree
#     # Left Left
#     if balance > 1 and getBalance(node.left) >= 0:
#         return rightRotate(node)

#     # Left Right
#     if balance > 1 and getBalance(node.left) < 0:
#         node.left = leftRotate(node.left)
#         return rightRotate(node)

#     # Right Right
#     if balance < -1 and getBalance(node.right) <= 0:
#         return leftRotate(node)

#     # Right Left
#     if balance < -1 and getBalance(node.right) > 0:
#         node.right = rightRotate(node.right)
#         return leftRotate(node)

#     return node
# # Inserting nodes
# root = None
# letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
# for letter in letters:
#     root = insert(root, letter)

# inOrderTraversal(root)    

# ------------------------------------------------------------ Graphs --------------------------------------------------------------------------
# A Graph is a non-linear data structure that consists of vertices (nodes) and edges.
# Graph representations store information about which vertices are adjacent
# and how the edges between the vertices are. 
# Two vertices are adjacent, or neighbors, if there is an edge between them.

# The Adjacency Matrix is a 2D array (matrix) where each cell on index (i,j)
# stores information about the edge from vertex i to vertex j.

# vertexData = [ 'A', 'B', 'C', 'D']

# adjacency_matrix = [
#     [0, 1, 1, 1],  # Edges for A
#     [1, 0, 1, 0],  # Edges for B
#     [1, 1, 0, 0],  # Edges for C
#     [1, 0, 0, 0]   # Edges for D
# ]

# def print_adjacency_matrix(matrix):
#     print("\nAdjacency Matrix:")
#     for row in matrix:
#         print(row)

# def print_connections(matrix, vertices):
#     print("\nConnections for each vertex:")
#     for i in range(len(vertices)):
#         print(f"{vertices[i]}: ", end="")
#         for j in range(len(vertices)):
#             if matrix[i][j]:  # if there is a connection
#                 print(vertices[j], end=" ")
#         print()  # new line

# print(print_connections(adjacency_matrix, vertexData))

# class Graph():
#     def __init__(self, size) -> None:
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size
#         self.parent = [i for i in range(size)]  # Union-Find array


#     def add_edge(self, unweighted_edge, vertix):
#         if  self.size > unweighted_edge >= 0 and self.size > vertix >= 0:
#             self.adj_matrix[unweighted_edge][vertix] = 1
#             self.adj_matrix[vertix][unweighted_edge] = 1
    
#     def add_weighted_edge(self, weighted_edge, vertix, weight):
#         if  self.size > weighted_edge >= 0 and self.size > vertix >= 0:
#             self.adj_matrix[weighted_edge][vertix] = weight

#     def add_vertex_data(self, vertex, data):
#         if self.size > vertex >= 0:
#             self.vertex_data[vertex] = data

#     def print_graph(self):
#         print("Adjacency Matrix:")
#         for row in self.adj_matrix:
#             print(' '.join(map(str, row)))
#         print("\nVertex Data:")
#         for vertex, data in enumerate(self.vertex_data):
#             print(f"Vertex {vertex}: {data}")
    
#     # 1. Depth First Search (DFS) using Stack
#     def DFS_util(self, vertex, visited):
#         visited[vertex] = True
#         print(self.vertex_data[vertex], end=' ')                         

#         for i in range(self.size):
#             if self.adj_matrix[vertex][i] == 1 and not visited[i]:
#                 self.DFS_util(i, visited) 

#     def DFS(self, star_vertex_data):
#         visited = [False] * self.size
#         star_vertex = self.vertex_data.index(star_vertex_data)
#         self.DFS_util(star_vertex, visited)        
    
#     # 2. Breadth First Search (BFS) usimg Queue
#     def BFS(self, start_vertex_data):
#         queue = [self.vertex_data.index(start_vertex_data)]
#         visited = [False] * self.size
#         visited[queue[0]] = True
        
#         while queue:
#             current_vertex = queue.pop(0)
#             print(self.vertex_data[current_vertex], end=' ')

#             for i in range(self.size):
#                 if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
#                     queue.append(i)
#                     visited[i] = True   
   
#     def dfs_util(self, v, visited, parent):
#         visited[v] = True

#         for i in range(self.size):
#             if self.adj_matrix[v][i] == 1:
#                 if not visited[i]:
#                     if self.dfs_util(i, visited, v):
#                         return True
#                 elif parent != i:
#                     return True
#         return False

#     def is_cyclic_dfs(self):
#         visited = [False] * self.size
#         for i in range(self.size):
#             if not visited[i]:
#                 if self.dfs_util(i, visited, -1):
#                     return True
#         return False


#     def find(self, i):
#         if self.parent[i] == i:
#             return i
#         return self.find(self.parent[i])

#     def union(self, x, y):
#         x_root = self.find(x)
#         y_root = self.find(y)
#         print('Union:',self.vertex_data[x],'+',self.vertex_data[y])
#         self.parent[x_root] = y_root
#         print(self.parent,'\n')

#     def is_cyclic_union(self):
#         for i in range(self.size):
#             for j in range(i + 1, self.size):
#                 if self.adj_matrix[i][j]:
#                     x = self.find(i)
#                     y = self.find(j)
#                     if x == y:
#                         return True
#                     self.union(x, y)
#         return False                        


# g = Graph(7)

# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

# g.add_edge(3, 0)  # D - A
# g.add_edge(0, 2)  # A - C
# g.add_edge(0, 3)  # A - D
# g.add_edge(0, 4)  # A - E
# g.add_edge(4, 2)  # E - C
# g.add_edge(2, 5)  # C - F
# g.add_edge(2, 1)  # C - B
# g.add_edge(2, 6)  # C - G
# g.add_edge(1, 5)  # B - F

# g.print_graph()

# print("\nGraph has cycle:", g.is_cyclic_union())

# -------------------------------------------------------------  Shortest Path Problem -------------------------------------------------------------------------
# Finding the shortest paths becomes impossible if a graph has negative cycles.
# Luckily, the the Bellman-Ford algorithm, that runs on graphs with negative edges, can be implemented with detection for negative cycles.

# 1. Dijkstra's Algorithm
# class Graph:
#     def __init__(self, size):
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size

#     def add_edge(self, u, v, weight):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = weight
#             #self.adj_matrix[v][u] = weight  # For undirected graph

#     def add_vertex_data(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data

#     def dijkstra(self, start_vertex_data):
#         start_vertex = self.vertex_data.index(start_vertex_data)
#         distances = [float('inf')] * self.size
#         distances[start_vertex] = 0
#         visited = [False] * self.size

#         for _ in range(self.size):
#             min_distance = float('inf')
#             u = None
#             for i in range(self.size):
#                 if not visited[i] and distances[i] < min_distance:
#                     min_distance = distances[i]
#                     u = i

#             if u is None:
#                 break

#             visited[u] = True

#             for v in range(self.size):
#                 if self.adj_matrix[u][v] != 0 and not visited[v]:
#                     alt = distances[u] + self.adj_matrix[u][v]
#                     if alt < distances[v]:
#                         distances[v] = alt

#         return distances   

# g = Graph(7)

# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

# g.add_edge(3, 0, 4)  # D - A, weight 5
# g.add_edge(3, 4, 2)  # D - E, weight 2
# g.add_edge(0, 2, 3)  # A - C, weight 3
# g.add_edge(0, 4, 4)  # A - E, weight 4
# g.add_edge(4, 2, 4)  # E - C, weight 4
# g.add_edge(4, 6, 5)  # E - G, weight 5
# g.add_edge(2, 5, 5)  # C - F, weight 5
# g.add_edge(2, 1, 2)  # C - B, weight 2
# g.add_edge(1, 5, 2)  # B - F, weight 2
# g.add_edge(6, 5, 5)  # G - F, weight 5

# # Dijkstra's algorithm from D to all vertices
# print("\nDijkstra's Algorithm starting from vertex D:")
# TargetVertix = 'D'
# distances = g.dijkstra(TargetVertix)
# for i, d in enumerate(distances):
#     print(f"Distance from {TargetVertix} to {g.vertex_data[i]}: {d}")

# 2. Bellman-Ford Algorithm
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size

    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            #self.adj_matrix[v][u] = weight  # For undirected graph

    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data

    def bellman_ford(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0

        for i in range(self.size - 1):
            for u in range(self.size):
                for v in range(self.size):
                    if self.adj_matrix[u][v] != 0:
                        if distances[u] + self.adj_matrix[u][v] < distances[v]:
                            distances[v] = distances[u] + self.adj_matrix[u][v]
                            predecessors[v] = u
                            print(f"Relaxing edge {self.vertex_data[u]}->{self.vertex_data[v]}, Updated distance to {self.vertex_data[v]}: {distances[v]}")

        # Negative cycle detection
        for u in range(self.size):
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0:
                    if distances[u] + self.adj_matrix[u][v] < distances[v]:
                        return (True, None, None)  # Indicate a negative cycle was found

        return (False, distances, predecessors)  # Indicate no negative cycle and return distances
    
    def get_path(self, predecessors, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessors[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)

g = Graph(5)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')

g.add_edge(3, 0, 4)  # D -> A, weight 4
g.add_edge(3, 2, 7)  # D -> C, weight 7
g.add_edge(3, 4, 3)  # D -> E, weight 3
g.add_edge(0, 2, 4)  # A -> C, weight 4
g.add_edge(2, 0, -3) # C -> A, weight -3
g.add_edge(0, 4, 5)  # A -> E, weight 5
g.add_edge(4, 2, 3)  # E -> C, weight 3
g.add_edge(1, 2, -4) # B -> C, weight -4
g.add_edge(4, 1, 2)  # E -> B, weight 2

# Running the Bellman-Ford algorithm from D to all vertices
print("\nThe Bellman-Ford Algorithm starting from vertex D:")
negative_cycle, distances, predecessors = g.bellman_ford('D')
if not negative_cycle:
    for i, d in enumerate(distances):
        if d != float('inf'):
            path = g.get_path(predecessors, 'D', g.vertex_data[i])
            print(f"{path}, Distance: {d}")
        else:
            print(f"No path from D to {g.vertex_data[i]}, Distance: Infinity")
else:
    print("Negative weight cycle detected. Cannot compute shortest paths.")