# Problem3

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
The function should return the number of arithmetic slices in the array A.

# Step1: Define the problem/solution recursively

This problem can be defined recursively in the following way:
Input: A = [1,2,3,4,5]
First we have our base cases:
if len(A) < 3, return 0
if len(A) == 3, return 1 if we have verfied that it is an arithmetic slice, else 0. We verify this by checking if A[1] - A[0] == A[2] - A[1]
if len(A) is > 3, we do the following:
We will iterate through the list, each time checking if the difference of each pair of consecutive numbers is the same. For example:
is A[1] - A[0] == A[2] - A[1] ?
We use a variable to keep track of how many times this executes to be true. We can iterate several times through this array, checking the different sizes and combinations of arithmetic slices, which would take several iterations which include repeated work. For example, if we know that A[1] - A[0] == A[2] - A[1] is true, then we have an arithmetic slice of size 3, but when we move to A[2] - A[1] == A[3] - A[2], not only did we find another slice of size 3, but we can also further know that this means that there is another arithmetic slice from A[0] through A[3].
Using this tactic, we are doing extra work and repetitive work since it would take another loop checking for arithmetic slices of length = 4 to make this reasoning again, but this is redundant. 
Instead, we can use a data structure to keep track of work we have already performed, this way iterating through A only once. For example:
If we have already proven than a1 = [1,2,3] and a2 = [2,3,4] are arithmetic slices, then we can also say that a3 = [1,2,3,4] is an arithmetic slice, and with just two iterations, we've found 3 arithmetic slices rather than redoing the work of 4-3 = 3-2 = 2-1.
This is why this problem has a recursive solution, because we take apart the problem and break it into smaller problems in order to solve the bigger problem. We will iterate through the list solving for smaller slices at a time which can help us make assumptions about bigger arithmetic slices. 

For example: 
A = [1,2,3,4,5]
Rather than using recursion to break the list into smaller pieces to find how many arithmetic slices can be found in this list, we can use a for-loop and the recursive definition of breaking the list into smaller pieces inside the loop so we can reduce the number of iterations performed while at the same time not perform repeated work. 

# Step2: Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem)

In order to solve this problem using dynamic programming, I have decided to use a dictionary to store solutions to what would otherwise be "repeated work". I will trace an example of my solution here to better illustrate my algorithm: 

Input: A = [1,2,3,4,5]
Our base cases do not apply here. 
Let's name our dictionary d. 
Before entering the loop, let's set the first value in our dictionary, which will be 1 if if A[1] - A[0] == A[2] - A[1] or 0 if false. 
In this case, d[0] = 1 (this means we have found 1 arithmetic slice so far)
We also have a variable slices which we set to 1 in this case.
In the loop:
Since we already know that [1,2,3] is an arithmetic slice, we will start at i = 1 and x = 3:
is A[x] - A[i+1] == A[i+1] - A[i] ? -> 4 - 3 == 3 - 2 ? yes! 
Since the above is true, we will set d[i] (d[1]) = 1 + d[i-1]
Why? 
First off, we set it equal to 1 because we found 1 more arithmetic slice. The reason we add this 1 to 
d[i-1] is because we want to check if the previous iteration had also found a slice, and if so, how many. In this case, the previous iteration was [1,2,3], and we had said that this was an arithmetic slice so d[0] = 1. 
Now, we have found a total of 2 (d[1] = 2) separate arithmetic slices. 
We also have to update the variable slices. In this case, we do slices = slices + d[i], so slices = 3
Why?
Not only did we find that [1,2,3] and [2,3,4] are arithmetic slices, but we can also further assume (without doing any additional steps nor repeated work) that [1,2,3,4] is an arithmetic slice, meaning that we have found 3 slices so far. 
Now we increment both x and i: 
x = 4
i = 2
is A[x] - A[i+1] == A[i+1] - A[i] ? -> 5 - 4 == 4 - 3 ? yes! 
Since the above is true, we will set d[i] (d[2]) = 1 + d[i-1] = 3
slices = slices + d[i] = 3 + 3 = 6
Now we increment both x and i:
x = 5
i = 3
However, since x is no longer < len(A), we exit the loop, and we have a total of 6 arithmetic slices.

It is beneficial and easy to use a dictionary because we only create extra space when necessary, and we can access an element in constant time. For this reason, we take advantage of the .get() method from Python in order to access an element from the dictionary iff it exists. In the case that it does not exist, we add a 0 and continue, and we do not create unnecessary space. 

# Step3: Talk about how you used IDEAL and Duke 7 to tackle the problem

I used IDEAL and Duke's 7 Steps to tackle this problem by:
I: Identify the Problem: The problem was to find the number of arithmetic slices possible in a given list of numbers

D & Duke Step 1: I defined the problem by drawing out and tracing different inputs for the problem by hand. I drew up different inputs and expected outputs to understand the problem and start thinking about possible solutions. 

E & Duke Steps 2&3: I explored different strategies by tracing over different inputs with different algorithms, trying to find the best one that would work on different inputs. I first thought about using a queue to make all possible combinations of arithmetic slices, and while it could have worked, I noticed that it involved repetitive work and multiple iterations, so I decided to think about other data structures that could help me store parts of the problem that had already been solved. I wrote down different ideas and traced over them, and I also tried using a boolean array which kept track of up to which point the given list contained an arithmetic slice. As I tried this approach I noticed it was too complicated and decided to take a step back. Then I came upon using the dictionary when I traced over by hand multiple times and I noticed that once you find one arithmetic slice, you can find multiple by keeping track of those you already found. 

A & Duke Steps 4&5: I acted on these solutions by starting to code them and continuing to trace by hand, coming up with a general algorithm (mentioned in Step 1) to solve the problem. I also tested my algorithm (by hand and by code) with different inputs. This helped me realize that rather than accessing a key in the dictionary by using d[i], it was better to use d.get since we only create a key when we find an arithmetic slice, so we can run into the situation where d[i] does not exist and d.get takes care of handling this issue for us. I would not have noticed this if I had not tested my algorithm.

L & Duke Steps 6&7: I learned that dictionaries are very cool data structures for keeping track of solved work while at the same time, allowing constant access and allowing me to create a new key only when necessary. I will keep this in mind when solving more dynamic programming problems. I also learend how to start solving the problem while in the loop, rather than storing everything in the dictionary and adding up all the slices in the end (which I had originally been doing but later realized this could be optimized in the way I did). I wrote up different test cases as well and debugged where necessary.   
