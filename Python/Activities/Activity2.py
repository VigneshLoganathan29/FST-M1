num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("You picked an odd number.")
else:
    print("You picked an even number.")


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1