import time
print('Welcome to the Math Multiplication Drill')
start = str(input('Please type start to begin or type cancel to cancel\n'))
if start == 'start':
    score = 0
    n = int(input('Please type the number to mutiply by (Between 1 and 100)\n'))
    if n <= 0 or n >= 100:
        print('Invalid numer, please try again')
    else:
        start = time.time()
        print('Question 1')
        print('What is 1 x',n,'?')
        a1 = int(input(''))
        if a1 == n:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 2')
        print('What is 2 x',n,'?')
        a2 = int(input(''))
        if a2 == n * 2:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 3')
        print('What is 3 x',n,'?')
        a3 = int(input(''))
        if a3 == n * 3:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 4')
        print('What is 4 x',n,'?')
        a4 = int(input(''))
        if a4 == n * 4:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 5')
        print('What is 5 x',n,'?')
        a5 = int(input(''))
        if a5 == n * 5:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')

        print('Question 6')
        print('What is 6 x',n,'?')
        a6 = int(input(''))
        if a6 == n * 6:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 7')
        print('What is 7 x',n,'?')
        a7 = int(input(''))
        if a7 == n * 7:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 8')
        print('What is 8 x',n,'?')
        a8 = int(input(''))
        if a8 == n * 8:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        print('Question 9')
        print('What is 9 x',n,'?')
        a9 = int(input(''))
        if a9 == n * 9:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')
        
        print('Question 10')
        print('What is 10 x',n,'?')
        a10 = int(input(''))
        if a10 == n * 10:
            score += 1
            print('Correct! Good job!')
        else:
            print('Incorrect. Good effort.')

        end = time.time()
        s = end - start
        m = 0
        if s == 60:
            m += 1
            s = 0
            
        print('Good Job, your score is :',score,'out of 10')
        print('Time :',m,'minutes','{:.2f}'.format(s),'seconds')
elif start == 'cancel':
    print('Program cancelled. Have a nice day!')
else:
    print('Wrong input, please try again.')
