def fizz_buzz(n : int) -> None:
    """
    it is a Fizzbuzz game
    :param n: it has number to check the conditions
    :return: None
    """
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 5 == 0:
        print("buzz")
    elif n % 3 == 0:
        print("fizz")

for i in range(1, 100):
    fizz_buzz(i)