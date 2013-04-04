def trampolined_fact(n, k = 1):
    if n == 0:
        return land(k)
    return bounce(trampolined_fact, n-1, k*n)


def fact(n):
    """Returns the factorial of n."""
    return trampoline(trampolined_fact, n)


def trampoline(function, *args):
    """Bounces a function over and over, until we "land" off the trampoline."""
    bouncer = bounce(function, *args)
    while True:
        bouncer = bouncer[1](*bouncer[2])
        if bouncer[0] == 'land':
            return bouncer[1]


def bounce(function, *args):
    """Bounce back onto the trampoline, with an upcoming function call."""
    return ["bounce", function, args]

def land(value):
    """Jump off the trampoline, and land with a value."""
    return ["land", value]
