# Create a code that reads a worker salary and show it's new one, with a 15% increase

salary = float(input('Worker\'s salary: '))
increase = 15/100*salary
new_salary = salary+increase

print('The amount of the increase will be US${:.2f}, and the new salary will be US${:.2f}.'.format(increase, new_salary))
