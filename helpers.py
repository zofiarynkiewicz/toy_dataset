import random

def has_no_carry(a, b):
    """
    Checking if the addition produces a carry.
    """

    while a > 0 or b > 0:
        if (a % 10) + (b % 10) > 9:
            return False
        a //= 10
        b //= 10
    return True

def generate_two_numbers(n_digits=4):
    """
    Generates two random numbers. We also check if the numbers will require a carry.
    """

    while True:
        a = random.randint(10**(n_digits-1), 10**n_digits - 1)
        b = random.randint(10**(n_digits-1), 10**n_digits - 1)
        if has_no_carry(a, b):
            return a, b


def format_standard(a, b):
    """
    Standard input equation without any fancy format
    """
    return {
        "input": f"{a} + {b} =",
        "output": str(a + b),
        "format": "standard"
    }


def format_spaced(a, b):
    """
    Adding spaces between the digits
    """
    a_spaced = " ".join(list(str(a)))
    b_spaced = " ".join(list(str(b)))
    return {
        "input": f"{a_spaced} + {b_spaced} =",
        "output": str(a + b),
        "format": "spaced"
    }

def format_underscore(a, b):
    """
    Adding the _ separators
    """

    a_with_ = "_".join(str(a))
    b_with_ = "_".join(str(b))
    return {
        "input": f"{a_with_} + {b_with_} =",
        "output": str(a + b),
        "format": "underscore"
    }


def format_10e(a, b):
    """
    Adding the 10e separators
    """

    def to_10e(n):
        digits = str(n)
        tokens = []
        for i, d in enumerate(digits):
            power = len(digits)-i-1
            tokens.append(f"{d} 10e{power}")
        return " ".join(tokens)
    return {
        "input": f"{to_10e(a)} + {to_10e(b)} =",
        "output": str(a + b),
        "format": "10e_based"
    }

def format_leading_zeros(a, b, n_digits= 4):
    """
    Adding padding with zeros
    """
    target_len = n_digits + 2
    a_with_zeros = str(a).zfill(target_len)
    b_with_zeros = str(b).zfill(target_len)
    return {
        "input": f"{a_with_zeros} + {b_with_zeros} =",
        "output": str(a + b),
        "format": "leading_zeros"
    }

def comma_separator(a,b):
    """
    Adding a comma for thousands separator
    """
    return {
        "input": f"{a:,} + {b:,} =",
        "output": str(a+b),
        "format": "comma"
    }