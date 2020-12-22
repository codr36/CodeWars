# My solution
def iq_test(numbers):
    # your code here
    num_list = list(map(lambda num: int(num), numbers.rsplit(" ")))
    even = list()
    odd = list()

    for x in num_list:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    if len(even) == 1:
        odd_one_out = even[0]
    else:
        odd_one_out = odd[0]

    index_of_odd = num_list.index(odd_one_out)
    return index_of_odd + 1

# Best rated solution
def test(numbers):
    # Check out List Comprehensions https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e


print(test("2 4 7 8 10"))
