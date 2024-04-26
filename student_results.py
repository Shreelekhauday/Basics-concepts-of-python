x=input('enter the name or roll number:')
a={'name':'shobha','roll_num':'44','marks':'100','result':'pass'}
b={'name':'shabana','roll_num':'42','marks':'100','result':'pass'}
c={'name':'shreelekha','roll_num':'47','marks':'99','result':'pass'}
d={'name':'shiffa','roll_num':'43','marks':'99.9','result':'pass'}
def student_details(x):
        if x=='shobha' or x=='44':
            print(a)
        elif x=='shabana' or x=='42':
            print(b)
        elif x=='shreelekha' or x=='47':
            print(c)
        elif x=='shiffa' or x=='43':
            print(d)
        else:
            print('name not found')
student_details(x)