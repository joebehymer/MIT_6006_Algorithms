Class 1: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-spring-2020/lecture-videos/lecture-1-algorithms-and-computation/

Goals of course:
 * solve computational problems
 * prove and communicate correctness
 * argue and communicate efficiency

Use induction to prove algorithms are correct. 

 Example problem: set of 300 people, find if two of them have the same birthdate+hour.  

 Algorithm:
 for each student
  - interview to find out birthhour
  - check if birthhour matches any of the other birthhours we have stored
   - if so, return that pair
   - else, add pair to set we search 

For inductive proof we need:
 - base case
 - statement/hypothesis
 - inductive step, take small value of this thing, use the hypothesis, use it to argue it applies to the whole set of inputs

 After I've interviewed k students, if there WAS a match, be sure I returned that pair from my algorithm.

 Inductive hypothesis (IH): if first k students contain a match, algorithm returns a match before interviewing student k+1 
 Base case: k = 0 (interviewing zero students).  Predicate holds for this!
 Assume IH true for k = k1, then we have two cases:
    1: first k already had a match, so for IH we have already returned a match
    2: doesn't have a match, then we interview k+1 student.  IF there is a match on the next iteration (after checking k1+1 against all k1 students in the record), then it will include the k1+1 student (since the first k1 didnt have a match) and we will return the result including the k1+1 student

Induction has proven the algorithm to be correct, now we want to argue that it is efficient.  Efficiency in this case means:
 - not only how fast does it run, but also
 - how fast it compares to other possible solutions

Assume that some operation that a computer does takes a fixed amount of time, then figure out how many of those operations your algorithm takes.  We expect performance to depend on input size (n).  This is using asymptotic analysis.  O(n) - upper bounds.  OMEGA(n) - lower bounds.  THETA(n) - both O(n) AND OMEGA(n)  

O(1) - constant time
O(log n) - log time, almost as good as constant
O(n) - linear time
O(n log n)
O(n^2) - polynomial time
O(n^c) 
O(c^n)

How do we measure these things?  Define a model of computation for what our computer is allowed to do in constant time.  
In this class, we use "Word-RAM".  Word is how many bytes can the CPU take into memory at once.  Usually 64 bits. 
32 bit word - 4GB space
64 bit word - 20 exabytes

Things CPUs can do:
 - int arithmetic
 - logic (if)
 - bit shifting

 Generally CPUs work on 2 words in memory and spit a third word out.

 First 8 lectures will talk about different types of data structures.  They support large amounts of data and support operations on that data.

 To solve algorithm problem in class, we will:
  - reduce to a problem we know how to solve (using existing data structure)
  - OR, design your own (recursive) algorithm (greedy, dynamic, etc)
