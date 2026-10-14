# PLP Python Week 3 Assignment

* `grade_reporter.py`: Categorizes student scores into letter grades, counts passes and fails, and calculates the rounded average score.
* `bug_hunt.py`: Identifies and fixes syntax, logical, and type errors in a while loop program to correctly sum numbers from 1 to 5.

### Reflection
The hardest bug to find in Part B was the loop boundary condition (`count < 5`), because it generated no error message and allowed the program to run successfully while outputting the wrong sum. I knew something was wrong when the result printed 10 instead of 15, prompting me to trace the loop iterations manually to catch the missing number.