<h2>Project Requirements</h2>

<ul>
<li><h4>Output:</h4></li>
<ul>
<li>First print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.</li>
<li>Then the program should print out each number from 1 to some value n, replacing numbers divisible by both 3 and 5 with “fizz buzz”, those divisible by only 3 with “fizz”, and those divisible by only 5 with “buzz”. You should print the digits rather than the text representation of the number (i.e. print 13 rather than thirteen). Each number should go on a new line.</li>
</ul>
<li><h4>Two Versions</h4></li>
<ul>
<li>v1: Hard Coded Upper Limit</li>
<ul>
<li>Hard code in 100 as value for upper limit to count up to when the program runs.</li>
<li>Verify your program works by running it from the command line with python my_script.py, substituting in your Python file name.</li>
</ul>
<li>v2: User Supplied Inputs</li>
<ul>
<li>If user supplies value at command line when script runs, we'll use that value.</li>
<li>Otherwise, we'll use the raw_input() dialogue to get an input from the user.</li>
</ul>
</ul>
<li><h4>Version Control</h4></li>
<ul>
<li>Get to v1, commit to master, and push to remote repo.</li>
<li>For v2, branch from master onto a new feature branch. When you've completed v2, commit it in your feature branch, and push the branch up to the remote repo.</li>
</ul>
</ul>


<h2>Extra Challenge</h2>

In the previous assignment you learned about exception handling. Practice this skill by writing code that handles the situation when users supply non-numeric inputs to either sys.argv or raw_input(). You should figure out where this user behavior would raise an exception in your code, use a try/except block to catch it, and then respond by print a message to the user that they need to supply numeric inputs for the program, then follow that up by using raw_input() to ask for a new numeric value.