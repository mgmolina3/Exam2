# Problem8

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Step1: Define the problem/solution recursively

This problem can be defined recursively in the following way:
We want to find the minimum number of perfect square numbers that add up to n. One way of doing this recursively would be to find all possible combinations of perfect square numbers that sum to n, for example:
let n = 12
Starting at the smallest square in n:
4 + 4 + 4 = 12
4 + 9 > 12, so we move on to the next square in n:
9 + 1 + 1 + 1 = 12

(we could also do all combinations involving 1, but that wouldn't make sense since it would not be the least number of squares)
Looking at the above, we can see that the solution is 4 + 4 + 4, meaning the answer is 3. 
One way to look at this would be that we start at the largest square inside of n, and we compare the result using the largest square to that of the result using the next largest square, and so on, recursively calling this method on each possible combination and square until we return the minimum found. While this might work, it involves a lot of repetitive work and unnecessary iterations, so we could take advantage of this recursive definition to use dynamic programming and minimize the steps needed. 
So, rather than iterating throught this:
return min(minSquare(largestSquareInN), minSquare(secondLargestSquareInN)) (for example)
we could use a data structure to keep track of things we might have already solved.

# Step2: Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem)

I plan on using an array to store solutions to subproblems, and then bringing these solutions together to solve the bigger problem. 
My approach is to take the number n and break it down into the sum of all the smallest square possiblem each time creating a new, larger square where possible. For example:
let n = 13
step 1: break it down into the sum of the smallest square (other than 1):
4 + 4 + 4 + (here, we check if adding another 4 would mean the sum is > 13, and since it is, we go to the next smallest square, 1) + 1.
So we have: 4 + 4 + 4 + 1. 
My idea is to then check if it is possible to combine any of these squares into a larger square. As we see that 4 + 4 + 1 = 9, we replace these three squares with the 9, and are left with 4 + 9.
So we return a 2. 
I will use the array to store the break down of the squares, such as the 4 + 4 + 4 + 1, then another for loop to iterate through this result to combine it into larger squares, and return the length of the final array. 

# Step3: Talk about how you used IDEAL and Duke 7 to tackle the problem

I used IDEAL and Duke's 7 Steps to tackle this problem by:
I: Identify the Problem: The problem was to find the minimum perfect square numbers that add to input n.

D & Duke Step 1: I defined the problem by drawing out instances of the problem by hand. I drew out and traced different inputs for the problem to understand how to go about solving the problem. I realized that I could find the addition of all the smallest perfect square numbers, store these in an array, and from there iterate through them to see if it is possible to create larger perfect square numbers in order to reduce the perfect square numbers needed to find the minimum.  

E & Duke Steps 2&3: I explored different strategies by tracing over different inputs with different algorithms, trying to find the best one that would work on different inputs. I traced over my ideas to find if this would work, and I found that on paper this worked, but I could not get the code to fully work. I retraced what I did on paper and understood my algorithm a little better, but I still could not get the code to fully work. 

A & Duke Steps 4&5: I acted on these solutions by starting to code them and continuing to trace by hand, coming up with a general algorithm to solve the problem. I started to find some of my mistakes in regards to how I was keeping track of the perfect square numbers and how I was going about trying to find larger perfect square numbers, but I could not fully fix my code. I tried tracing it over several times but was unable to get it to work for different inputs. It works for some inputs but not for all. However, my idea remained the same because this algorithm worked on paper whenever I went back to trace it over by hand with different inputs, it was just translating this algorithm into code where I struggled and couldn't make it work. 

L & Duke Steps 6&7: I learned that sometimes, while your algorithm might work on paper, you might not be able to fully make it work in code. I also learned that it might be that my algorithm simply is not the best for this problem, but I could not think of any other ways to solve this problem which is why I stuck to this solution. I tried making it work the best I could but I was not able to. I tried changing it around a bit without success, however my idea does work on paper, I was just not able to make it work in code. 