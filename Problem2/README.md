# Problem2

Given a string, your task is to count how many palindromic substrings in this string. 
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters. 

# Step1: Define the problem/solution recursively

The problem of determining how many palindromic substrings are in the given string can be defined recursively in the following way:
Input: s = "aaa"
We can start by having a base case where if the len(s) == 0, return 0
We have another base case where the len(s) == 1, return 1
Then, if len(s) is greater than 1, we can do the following:
We know that there are at least as many palindromes as there are characters in s, so we can define p to be the number of palindromes in s to be: p = len(s)
Then, starting at the center index of s, we can compare if s[center] == s[center+1] and s[center] == s[center-1], and if s[center-1] == s[center+1]:
We must have two center pointers: centerLeft and centerRight (for the cases of even and odd numbers of characters), where centerLeft = centerRight-1
Every time we have an equal, we increment p by 1. For example: input: s = "aaa"
centerRight = 1, so centerLeft = 0
is s[1] == s[0]? yes! p = 4, so we increment centerRight by 1: (and we would decrement centerLeft by 1 but we are already at index 0)
is s[2] == s[0]? yes! p = 5
While it seems that we are done, we actually also do p+=1 one more time because we never compared s[1] to s[2], but since we know that s[0] is equal to both s[1] and s[2], by the transitive property, s[1] == s[2], so p = 6.

The idea is to continue to expand outwards each time and check if s[i] == s[i+1] and s[i] == s[i-1] and if s[i-1] == s[i+1], each time incrementing p by 1 if true. Let's trace another input: s = "nellen"
centerRight = len(s)//2 = 6//2 = 3
centerLeft = 2
p = len(s) = 6
is s[3] == s[2]? yes! p = 7
This time we expand outwards with both center indexes by doing center+=1 and centerLeft-=1:
is s[4] == s[1]? yes! p = 8
is s[5] == s[0]? yes! p = 9
And we are done traversing the entire string, and p = 9.
We can then have two separate loops, one for odd number of characters and one for even. 
In the case that we have an odd number of characters, we increment p at the end of the loop iff 
s[centerLeft] == s[centerRight]
Otherwise, this is not necessary as it will be taken care of in the loop. 

The reason this is a recursive definition of the problem is because we are taking apart the string and solving smaller parts of the problem in order to get to the big picture. We traverse the string looking for palindromes while keeping track of how many palindromes we have, traversing parts of the string at a time. 
While we may not have a recursive method call, we do have a recursive definition of taking apart the problem into smaller pieces, assuming we know the answer to those smaller pieces in order to solve the bigger pieces. For example, we only assume that the entire string of "nellen" is a palindrome because we know that "elle" is a palindrome and s[0] == s[5], and we know "elle" is a palindrome similarly because we know "ll" is a palindrome and s[1] == s[4], and so on. 

# Step2: Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem)

I don't actually think we need a specific data structure to store sub-problems for this problem because we are using the indexes and booleans to keep track of palindrome substrings. Going back to the example of "nellen": we don't need to specifically store in a data structure that "elle" is a palindrome because we already executed s[1] == s[4] and know that to be true. We simply use if statements to increment p, and p is incremented in this case.
In other words, since we are solving smaller parts of the problem at the time, and each time expanding outwards keeping track of the boolean values, we can solve the bigger problem quicker. Rather than re-evaluating if "elle" is a palindrome in order to evaluate that "nellen" is a palindrome, we know from the previous iteration in the loop that "elle" is a palindrome, and from a previous iteration that "ll" is a palindrome. So, by definition at this point, "nellen" is a palindrome iff s[0] == s[5], without needing to check for anything else since we already know the answers to the subproblems and have kept track of those answers with booleans and the transitive property. 

So let's say that we have "nxllen" instead. We execute s[3] == s[2] to be true, then "xlle" is a palindrome iff s[4] == s[1], which is false. By definition of a palindrome, we then know that "nxllen" is not a palindrome without even having to execute it because the answer to the previous subproblem was false. 

# Step3: Talk about how you used IDEAL and Duke 7 to tackle the problem

I used IDEAL and Duke's 7 Steps to tackle this problem by:
I: Identify the Problem: The problem was to calculate the number of substrings that are palindromes from a given string.

D & Duke Step 1: I defined the problem by drawing out and tracing different inputs for the problem by hand, similar to what I did above with "aaa" and "nellen". This way, I could understand the problem better while starting to think up solutions and algorithms. 

E & Duke Steps 2&3: I explored different strategies by tracing over different inputs with different algorithms, trying to find the best one that would work on different inputs. Originally, I though of traversing the word from the start and trying to count the substring palindromes. I realized this worked for "aaa", but not for "nellen" because I wasn't ever iterating over the substring palindromes of "elle" and "nellen", so I decided to optimize my solution. I also wrote down what it is that I did so that I could understand potential solutions to the problem and start thinking about what this might look like in code. I started to generalize a solution and considered different inputs. 

A & Duke Steps 4&5: I acted on these solutions by starting to code them and continuing to trace by hand, coming up with a general algorithm (mentioned in Step 1) to solve the problem. I continued to test my solution by hand since I started to notice some problems with my algorithm and it helped to trace my algorithm by hand, making adjustments along the way. Then I translated completely to code, again trying out different inputs and optimizing/fixing mistakes. 

L & Duke Steps 6&7: I learned how to implement dynamic programming into my solution by using a loop and keeping track of previously solved work with variables. I also learned to optimize my algorithm for different inputs, not just one certain type of input. As for testing and debugging, I also did this more for my code, trying to find ways to get it to work for "aaa" and "nellen" since these inputs were different in the way that they are to be solved. 
