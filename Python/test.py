'''
Countdown Timer
-------------------------------------------------------------
'''


import time


def countdown(user_time):
   while user_time >= 0:
       mins, secs = divmod(user_time, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time -= 1
   print('Lift off!')


if __name__ == '__main__':
   user_time = int(input("Enter a time in seconds: "))
   countdown(user_time)


dictionary = {'python': 'awesome'}
print('Dictionary:', type(dictionary))

a_list = [1, 2, 3, 4]
print('List:', type(a_list))

num = 1
print('Number:',type(num))

def some_function():
    pass
print('Function:',type(some_function))

class Student:
    pass
student = Student()
print('Custom class:', type(student))