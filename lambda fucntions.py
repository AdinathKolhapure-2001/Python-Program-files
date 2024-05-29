# Anonymous function = Lambda function -> A function which has no name

# syntax: lambda <input args> : <return statement>

g = lambda x : 3 * x + 1

print(g(3))


# lambda function with multiple inputs

full_name = lambda fn, ln : fn.strip().title() + " " + ln.strip().title()

print(full_name("   Harry   ", "POtTer"))


# use lambda function to sort based on a key

hollywood_actors = [
    "Tom Hanks",
    "Leonardo DiCaprio",
    "Meryl Streep",
    "Brad Pitt",
    "Angelina Jolie",
    "Denzel Washington",
    "Jennifer Lawrence",
    "Robert Downey Jr.",
    "Scarlett Johansson",
    "Johnny Depp"
]


hollywood_actors.sort(key = lambda name : name.split(" ")[-1].lower())

print(hollywood_actors)



# Function to build another function

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x : a * x ** 2 + b * x + c

f = build_quadratic_function(2, 3, -5)

print(f(0))

print(f(1))

print(f(2))

print(build_quadratic_function(3, 0, 1)(2))




