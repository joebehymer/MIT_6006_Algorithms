Data Structures

Interface (e.g. API) versus Data Structure.  Interface says what you want to do, Data Structure says how you do it.
Interface:
 - specification
 - what data can store
 - what operations are supported
 - "problem statement"

Data Structure:
 - representation 
 - how to store data
 - algorithms to support the operations
 - "algorithmic solution to problem"


Two main interfaces, today we focus mostly on Sequences
 - Set (e.g. [2,9,5,7] in any order)
 - Sequence (e.g. [5,2,9,7] in order)

Two main approaches to data structures:
 - Arrays
 - Pointer based

Static Sequence Interface (number of items doesn't change, but items can)
 - n items, x0 to xn-1
 - build(x[]): makes new data structure with x[]
 - len() - returns N, length of sequence
 - iter_seq() - iterates through all n items
 - get_at(i) - gets item at ith index
 - set_at(i, x) - sets item at ith index to x
 - get_first(), get_last() 
 - set_first(x), set_last(x) (we note these specifically because they may have better complexity than a generic set_at(i))

Natural Solution to above interface is a "Static Array".  (Note: Python only has dynamic arrays)

Remember: Word RAM is our model of computation
 - memory is an array of w-bit words [word1,word2,etc].  Has random access.
 - "array" is a consecutive chunk of memory.  It may start at word2 and end at word17.
 - To access array at index i, means to access memory array at array start address plus index: `array[i] = memory[address(array) + i]`
 - Array access is O(1) time.
 - Assumption: w >= log(n), where w is word size.  (e.g., 32 bit only could access 4GB in hard drive)

 Static Array as a solution gives us (array based data structure):
  - O(1) for get_at, set_at, len.  
  - O(n) for build and iter_seq 

Memory Allocation Model: allocate an array of size n in O(n) time.
When using arrays, space = O(time).  

Dynamic Sequence Interface (number of items can change)
 - static sequence interface, plus
 - insert_at(i, x): shifts items after index i over to the right to fit x
 - delete_at(i): deletes item at i, shifts items after index i to the left to not have an empty spot in our array.
 - insert_first(x), insert_last(x)
 - delete_first(), delete_last()

Linked Lists (pointer based data structure):
 - store items in nodes, nodes point to next node 
 - keep track of the head of the list
 - could store length as we insert/remove

Lets look at some data structures and think about how well they handle these interfaces.

Dynamic Sequence Operation analysis for a Static Array versus a Linked List.
Static Array:
 - insert/delete - O(n) everybody has to shift over OR we may have to allocate a second array if we are inserting at the end

Linked List:
 - insert_first/delete_first - O(1)
 - get_at(i)/set_at(i) - THETA(i), O(n)

Puzzle - how to solve get_last in a linked list in constant time? (Doubly-linked-list is a good idea but not the right answer.  Just need to store a pointer to the tail element.)

How do we get the best of both linked lists and static arrays at the same time? Dynamic Arrays!

Dynamic Arrays (python calls these lists)
 - relax constraint that the size of the array we use internally is the size of the number of the items (n) in the sequence.  Size of array at least n, at most 2n.
 - maintain A[i] == xi.
 - store len, size, so if len grows to size you can make a new array with a bigger size
  - if we double new array size, then we resize at n=[1,2,4,8,16,..]
  - resize_cost = O(1+2+3+4...k) == O(2^i) == O(2^(k+1)-1) = O(2^lg(n)) = O(n) 
  - Since most operations don't have resize_cost, we can call this O(1) amortized time.

Definition: Amortization
 - An operation takes T(n) amortized time, if any k of those operations take <= k*T(n)
 - Average over operation sequence.


 Data Structure | get_at(i) | insert_first(x) | insert_last(x)   | insert_at(i, x)

 Array          | O(1)      |  O(n)           |  O(n)            | O(n)
 Linked List    | O(n)      |  O(1)           |  O(n)            | O(n)
 Dynamic Array  | O(1)      |  O(n)           |  O(1)(amortized) | O(n)