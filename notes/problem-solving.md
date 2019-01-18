# A process for solving small programming problems

Unlike real programming problems faced by programmers performing their jobs, technical interviews usually consist of small bite-sized questions.  The small problem size gives us an opportunity to develop a problem-solving script you can follow.  

You might have a successful interview even if you can't solve a specific problem, if you demonstrate a solid problem-solving process. Multiple interviewers have told me that they are mostly interested in how a candidate solves problems. A common tactic, in fact, is to provide an ill-specified or incompletely specified problem. The interviewer wants to see how you clarify and nail down the actual problem. No one wants to hire a person that has to be spoonfed and told precisely how to solve problems.

Here's a good summary of the process I follow when solving a small programming problem.

### First, UNDERSTAND <img align="right" src="images/Thinking-Woman-PNG.png" width="60">

1. Read the description(3x) then restate the problem, either on paper or out loud
2. Ask if you've understood it correctly
3. Ask if there are speed or size requirements
4. Describe and write out a minimal but *representative* example of both the intended input data or data structure *and* the expected output; ask if it is correct
5. Identify any edge cases you can think of by example

## Second, SOLVE <img align="right" src="images/solve-icon.png" width="55">

Solving the problem has nothing to do with the computer; you might not even be asked to code the solution. If you can't walk through a correct sequence of operations by hand on paper, no amount of coding skill will help you. 

1. **Explore**. Look at the input-output example and imagine how you can manually operate on the input to get the output. Attempt any manual sequence of operations that appears to be in the right direction, even if you know it's not quite right. Exploration helps you understand the problem and will trigger more questions, so ask questions.

2. **Reduce**. Can you reduce the problem to known solution by preprocessing the input a bit? E.g., to compute the median, first sort the data then grab the middle value.

3. **Reuse**. Look for and reuse familiar programming patterns like vector sum, min, and find. E.g., to sort a list of numbers (slowly), repeatedly pull then delete the minimum value out of one array and add it to the end of another.

4. **Systematize**. Simplify and organize the steps in your process as pseudo-code; this is your algorithm.

5. **Verify**. Check that your algorithm solves the main problem and the edge cases.  Check your algorithm's complexity. If it's not good enough for the interviewer's constraints, identify the key loops or operations fundamental to your algorithm's complexity. Iterate on this problem-solving process to reduce complexity. E.g., can you get rid of a factor of *n* by converting a linear search to a hash table lookup?

## Third, CODE <img align="right" src="https://image.freepik.com/free-photo/cropped-view-of-hands-typing-on-laptop_1262-3196.jpg" width="70">

And now the easiest part: expressing yourself in the syntax and semantics of a programming language.

1. Write a function definition that takes your input as a parameter or parameters. The return value of your function will typically be the expected problem result.
2. Write a main script that acquires the data, passes it to your function, and sends the results to the appropriate file or standard output.
3. Translate the algorithm steps into statements in your function. It's okay if you create helper functions.

## What to do when you get stuck

1. Identify exactly what you don't know how to do. Identifying the key tricky bit is a skill that the interviewer should look for.  It's a good idea to express verbally, "*Ah. This is what makes this problem tricky.*" The interviewer might be waiting for you to ask for a hint because they've given you a challenging problem and want to see how you work through it.
<p>
For example, computing the median is straightforward for an array sitting on a single machine but what about data spread across multiple machines? Identifying that you can't just take the median of the remote subarray medians is a key part of the interview process. (This is from an actual interview.)

2. What would make this problem easier? Try to convert your problem to this easier version by preprocessing the input. Failing that, solve the simpler version and then work on the harder, more general case.

Multiple failed attempts is part of the game because interviewers won't ask trivial problems, except perhaps during an initial phone screen.


## Some advice

* Details matter, pay careful attention to the interviewer.

* When reading the problem description, identify who is doing what to whom? What are the nouns and verbs used in the description? The nouns are usually data sources or data elements; the verbs are often operations you need to perform. Look for keywords like min, max, average, median, sort, argmax, sum, find, search, collect, etc... Regardless of how you do it, clearly identify:
    1. the source and format of data
    1. the operation
    1. the expected result
    1. the output location and format.

*  Choose the simplest possible algorithm and implementation that will work. At first, ignore performance then worry about getting it into the complexity constraints of the problem.

* The typical problem pipeline is:

    1. fetch data
    1. organize it into a data structure
    1. process the data structure
    1. emit output
 
* Make sure you fully understand the constraints.  Are the input data elements strings, ints, floats?  If they are values, are they always between 0 and 1?  Can they be negative? Is the input sorted? Is speed or space an issue? Can you see all of the data at once or do you have to worry about streaming data? Can you bound the maximum size of the input? This might matter if you need to make an nxn matrix for example.

