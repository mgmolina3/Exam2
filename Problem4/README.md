# Problem4

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

# Step1: Define the problem/solution recursively

This problem can be defined recursively in the following way:
We have two strings as inputs: s1 and s2, and we must find a way to make the two strings equal where:
(a) We can only delete a character from:
    - s1
    - s2
    - both
    - neither
(b) When we delete, we must sum the ascii value of the character deleted
We must find the minimum sum in order to make both strings equal. 
This problem is very similar to the edit distance problem covered in class, and I followed a similar approach.
First off, with both strings we have 3 options:
    (1) delete char from s1
    (2) delete char from s2
    (3a) delete char from both
    (3b) don't delete char iff char is equal
Similar to the edit distance problem, we must take all paths in order to find the minimum sum. So we are left with the following recursive definition:
If s1 = "sea" and s2 = "eat", we must traverse each string and perform each of the three options to each char in the string, keeping track of the sums and returning the minimum sum. So:
s1[0] = s and s2[0] = e, and s1[0] != s2[0], so:
(1) delete char from s1, then we have: s1 = "ea" and s2 = "eat", minSum = 115
(2) delete char from s2, then we have: s1 = "sea" and s2 = "at", minSum = 101
(3) delete chat from both: s1 = "ea" and s2 = "at", minSum = 216
Now, we make a recursive call for each of the three scenarios mentioned above. So our three recursive calls call the method each with these different inputs: s1 = "ea" & s2 = "eat"; s1 = "sea" & s2 = "at"; s1 = "ea" and s2 = "at". Now, we perform the same algorithm in each of these calls, and this happens over and over again until we find the minimum sum. 
We can see a recursive definition of this problem clearly, with our base cases being that if the length of either string becomes 0, then we return the sum of all the ascii values of the characters in the other string (since we would have to delete every character in the other string to get it to equal to the first string)
However, we can also see that at some point in each recursive call, we will have repeated work, and thus unnecessary calls. As mentioned earlier, this problem is similar to the edit distance problem, and we can follow a similar approach to solve this problem using dynamic programming and reducing the numbers of iterations necessary to solve this problem. 

# Step2: Briefly talk about how you plan to store solutions to sub-problems and combining them to solve the global problem (talk about the data structure/variables you’ll use to solve the problem)

Seeing that this problem was similar to the edit distance problem, I decided to reuse what I learned from that problem and apply it here. I used a matrix to solve this problem, just like in the edit distance problem but with some tweaks. 

Similar to edit distance, we first create a matrix with the size being: len(s1)+1 * len(s2)+1 -> the +1 is because of the empty string. Using s1 = "sea" and s2 = "eat":
  "" s e a
"" 0 0 0 0
e  0 0 0 0
a  0 0 0 0
t  0 0 0 0
The position matrix[0][0] is set to 0 because it takes 0 steps (and thus sum=0) to get from an empty string to an empty string
Next, I populated the first row with the ASCII values of each letter + the value in the previous column:
matrix[0][1] = ascii(s) + matrix[0][0] = 115
matrix[0][2] = ascii(e) + matrix[0][1] = 216
matrix[0][3] = ascii(a) + matrix[0][2] = 313
I did the same thing for eat
The reason for this is because we read the table in the following way: the part:
   "" s e a
"" 
is read: if I am at position matrix[0][1], what is the minSum to get from "s" to the empty string? Well, we delete "s", leaving us with minSum = 115. Next, at position matrix[0][2], what is the minSum to get from "se" to ""? We delete "se", and we already calculated deleting "s", so we simply add the ascii of "e" to get the minSum = 216
And so on. The same logic applies for eat. We are then left with:
  ""   s   e   a
"" 0  115 216 313
e  101 0   0   0
a  198 0   0   0
t  314 0   0   0
Next, we apply the same logic as in the edit distance problem, with the following rules:
if s1[x] == s2[y], matrix[i][j] = matrix[i-1][j-1] because we don't delete
else, matrix[i][j] = min(matrix[i-1][j]+ascii(s1[x]), matrix[i][j-1]+ascii(s2[y])) because we want to see which has the minSum, deleting the current char of s1 OR deleting the current char of s2?
In the end, the result of the minSum will be in matrix[-1][-1]

# Step3: Talk about how you used IDEAL and Duke 7 to tackle the problem

I used IDEAL and Duke's 7 Steps to tackle this problem by:
I: Identify the Problem: The problem was to find the minimum sum of the ascii value of the characters to make s1 = s2

D & Duke Step 1: I defined the problem by drawing out instances of the problem by hand. I then identified that the problem was very similar to the edit distance problem, so I decided to try out a similar solution to the edit distance problem by drawing it out by hand. 

E & Duke Steps 2&3: I explored different strategies by tracing over different inputs with different algorithms, trying to find the best one that would work on different inputs. I knew I could use a matrix to solve this problem because I learned how to do so in the edit distance problem. The challenge was trying to find out how to use it, what each step meant, and how to interpret the different paths that can be taken to solve the problem in the matrix. I drew out different inputs and traced them, trying out different ways to populate and read the matrix until I found a solution that seemed very likely to work. 

A & Duke Steps 4&5: I acted on these solutions by starting to code them and continuing to trace by hand, coming up with a general algorithm (mentioned in Step 1) to solve the problem. I also tested my algorithm (by hand and by code) with different inputs. I realized I needed to traverse the matrix in a certain way to get the correct results, as I was having many mistakes (from indexing) at first. I realized that while my logic and general approach was on the right track, I was traversing the matrix in the wrong way, and it was yielding incorrect results. For this, I went back to tracing by hand to understand how I had to translate my algorithm (which worked) into code. 

L & Duke Steps 6&7: I learned that matrices can be used in different ways to tackle simlar problems. I also learned the importance of practicing these problems because if I had never worked on the edit distance problem before, I am sure I would have taken a lot longer to solve this problem. I also tried out different test cases with strings of different lengths to test my code, and I made the necessary fixes and optimizations. 
