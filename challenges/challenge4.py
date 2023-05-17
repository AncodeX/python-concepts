# Es primo entre 1 - 100

def in_print():
    for i in range(1, 101):
        if is_prime(i):
            print(i, end=" ")

def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

# Invirtiendo cadenas

def reverse(text):
    reverse_text = ""
    for index in range(1, len(text)+1):
        reverse_text += text[-index]
    
    return reverse_text

print(reverse())