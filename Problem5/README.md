# Problem5

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order. 

# Step1: Define the problem/solution recursively

This problem can be defined recursively in the following way:
We have a list of pairs as input, and we want to find the longest chain possible with the constraint that pair1[1] must be < pair2[0], and so on. 
One way to do this would be to compare each pair in the list to each other pair in the list in order to find evey possible combination of chains, then find the longest one, such as:
Input: nums = [[1,2],[3,4],[4,5],[5,6],[6,7]]
Let's say we've run through this algorithm and are left with the following chains:
[1,2]->[3,4]->[5,6]
[1,2]->[4,5]->[6,7]
[1,2]->[5,6]
[1,2]->[6,7]
[3,4]->[5,6]->[6,7]
[3,4]->[6,7]
[4,5]->[6,7]
These are all the possible, valid chains. We are recursively finding all possible combinations of chains.However, as we can see, we are doing so much repetitive work and most of it is unnecessary because why would we want to create a chain of a length smaller than the other chain we already created which is longer? It is unnecessarily repetitive, and instead of finding all possible combinations and then finding which is the longest, we could use the recursive definition of keeping track of the longest chain, only creating a new chain iff it will be longed than the previous. 

We can use a data structure to keep track of the lengths of the chains and also to keep track of the maximum length

# Step2: Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem)

I plan to use an array and an int variable to store solutions to sub-problems and keep track of the longest chain so far. 

I plan to do the following:
Create an array called chains of the same length as the total number of pairs in our pairs input. I will then iterate through the pairs, each time creating new lengths and keeping track of the maximum length.
For example: Input: pairs = [[1,5],[2,3],[4,5],[6,7]]
First, if the paris are not sorted, I would sort them to make things easier. Since this pairs is already sorted, I continue:
let chains = [1,1,1,1] and maxChain = 1 (because as of now, the longest possible chain is of length 1)
Now we will iterate through the pairs:
lets pair1 = [1,5] and pair2 = [2,3]
is pair1[1] < pair2[0]? no. So pair2 = [4,5]
is pair1[1] < pair2[0]? no. So pair2 = [6,7]
is pair1[1] < pair2[0]? yes! so chains[3] (why 3? Because the chain we are making is [1,5]->[6,7], and [6,7] (the last pair of the chain) is in position 3 of pairs) chains[3] = max(chains[0]+1, maxChain). Why? Position chains[0] currently holds the longest length chain for pair1 ([1,5]), and we add 1 more chain to that. We also compare this to maxChain in case maxChain is currently greater than the other value. 
In this case, chains[3] = 2
then we set maxChain = 2
Now we move on to the next pair1 = [2,3], pair2 = [4,5]
We follow the same algorithm:
is pair1[1] < pair2[0]? yes! So chains[2] = 2, maxChain = 2
is pair1[1] < pair2[0]? yes! So chains[3] = 3, maxChain = 3
This would be the idea, to use what we already know before in order to calculate the maximum length. We are storing the lengths in chains and taking the maximum value from what we already calculated and what we just calculated in the current iteration. 
In this case, we would return maxChain = 3

# Step3: Talk about how you used IDEAL and Duke 7 to tackle the problem

I used IDEAL and Duke's 7 Steps to tackle this problem by:
I: Identify the Problem: The problem was to find the maximum length of the chain that can be created from a given list of pairs.

D & Duke Step 1: I defined the problem by drawing out instances of the problem by hand. I drew out and traced different inputs for the problem to understand how to go about solving the problem. I realized that it was important to sort the pairs first in order to make it easier to solve the problem. 

E & Duke Steps 2&3: I explored different strategies by tracing over different inputs with different algorithms, trying to find the best one that would work on different inputs. I first tried just finding all possible combinations of chains that can be made, then finding the length of the longest one. After realizing that this was a recursive definition to solve the problem, I started thinking about how I could store solutions to parts of the problem to help me solve the problem quicker without resolving parts of the problem that had already been solved before.  

A & Duke Steps 4&5: I acted on these solutions by starting to code them and continuing to trace by hand, coming up with a general algorithm to solve the problem. It took a while for me to identify how I could use an array to store the solutions to parts of the problem that had already been solved. I realized I could also keep track of the maxChain along the way. I tested different inputs to make sure my solution worked and I fixed the issues that came up. 

L & Duke Steps 6&7: I learned how I could use an array to keep track of the previous lengths I had calculated and how to use this to find the longest chain. I kept on testing with different inputs and I also realized that I had an error originally because in trying to keep track of the previous lengths, I was adding the new lengths incorrectly and getting odd length results. I then fixed these mistakes and kept testing and optimizing my solution. 