"""
This program allows user three tries to guess the correct answer to the question
question = "What is the capital of California? " The answer is "Sacramento".

We first set max_tries = 3. Then we create a loop to iterate three times. For each iteration,
we ask the user for the answer (user input). Then based on the answer the user gives, we check
to see if the user input matches the answer. If so, print "Correct!", then terminate the loop 
with a break statement. 

if the user could not guess the correct answer within the max_tries, then print
"You have used up your allotment of guesses.", "The correct answer is 'California'".
"""

"""
main function
    question = "What is the capital of California?"
    answer = "Sacramento"
    ask(question, answer)
 
ask function
    tries = 0
    loop three times
    increment tries
    ask user input()
    check to see if user input is equal to answer
        if so, print "Correct!" to exist loop
    if not correct
        print to the user "You have used up your allotment of guesses."
        print the correct answer "The correct answer is 'California'"
 
main
"""