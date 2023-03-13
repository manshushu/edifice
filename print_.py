name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")


name = "John"
age = 30
print("My name is", name, "and I am", age, "years old.")


name = "John"
age = 25
print("My name is %s and I am %d years old" % (name, age))


def test_output_string():
    name = "John"
    age = 30
    output = f"My name is {name} and I am {age} years old."
    assert name in output and str(age) in output


def test_output_commas_vs_fstring():
    name = "John"
    age = 30
    fstring_output = f"My name is {name} and I am {age} years old."
    commas_output = "My name is", name, "and I am", age, "years old."
    assert ''.join(commas_output) == fstring_output


def test_output_pf_vs_fstring():
    name = "John"
    age = 25
    fstring_output = f"My name is {name} and I am {age} years old."
    pf_output = "My name is %s and I am %d years old" % (name, age)
    assert pf_output == fstring_output


def add_numbers(a, b):
    assert isinstance(a, int), "a must be an integer"
    assert isinstance(b, int), "b must be an integer"
    return a + b

result = add_numbers(10, 20)
print(result)  # output: 30

result = add_numbers(10, '20')  # this line will raise an AssertionError with the message "b must be an integer"
