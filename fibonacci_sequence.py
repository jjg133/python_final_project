# Write a piece of code to create a Fibonacci sequence using the iterative method.
list = [1, 2, 3]
for x in range(0,150):
    new_value = list[-1] + list[-2]
    list.append(new_value)
print(list)

# Write a piece of code to create a Fibonacci sequence using the recursion meth
def fibonacci_sequence(list, max_limit):
    if max_limit < 0:
        print("error")
    elif list[-1] + list[-2] < max_limit:
        new_value = list[-1] + list[-2]
        list.append(new_value)
        fibonacci_sequence(list, max_limit)
    else:
        print("Fibonacci Seuquence: ")
        print(list)

list = [1, 2]
fibonacci_sequence(list, 23)
