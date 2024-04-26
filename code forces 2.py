n= int(input('Enter the number of problems: '))
def unsolved_problems(n):
   solved_problems=0
   unsolved_problem=0
   for i in range(n):
        a=int(input('enter the probality of solving the problem'))
        b=int(input('enter the probality of solving the problem'))
        c=int(input('enter the probality of solving the problem'))
        if a+b+c>=2:
            solved_problems+=1
        else:
                 unsolved_problem-=1

   return solved_problems

print(unsolved_problems(n))