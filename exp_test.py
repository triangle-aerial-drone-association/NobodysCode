import random


def generate_exponent_problem():
    """
    Generates a random math problem involving exponentiation with base 2, 3, 4, 5, or 10,
    and either multiplication or division, with the result expressed as an exponent.
    """
    bases = [2, 3, 4, 5, 10]
    operations = ['*', '/']

    # Randomly select a base and an operation
    base = random.choice(bases)
    operation = random.choice(operations)

    # If the operation is division, ensure the result is an integer
    if operation == '/':
        exponent = random.randint(1, 4)  # Exponent up to 4
        result = base ** exponent
    else:
        exponent = random.randint(1, 4)  # Exponent up to 4
        result = base * (base ** (exponent - 1))  # Ensure result is in exponential form

    return base, operation, exponent, result


def math_test_exponents():
    """
    Runs the math test focusing on exponent operations.
    """
    print("Welcome to the exponent math test! Solve the problems below:")

    score = 0
    problems = []

    # Generate 10 problems
    for _ in range(10):
        base, operation, exponent, result = generate_exponent_problem()

        if operation == '/':
            problem = f"{base ** exponent} / {base ** (exponent - 1)} = ?"
        else:
            problem = f"{base} * {base ** (exponent - 1)} = ?"

        problems.append((problem, result))

    random.shuffle(problems)  # Shuffle the problems

    for i, (problem, correct_answer) in enumerate(problems):
        print(f"Problem {i + 1}: {problem}")

        # Get the user's answer
        try:
            user_answer = input("Your answer (in exponent form, e.g., 2^3): ")
            if user_answer:
                # Validate if the user answer is in the correct exponent form
                base, exp = user_answer.split('^')
                user_base = int(base)
                user_exponent = int(exp)

                if user_base == correct_answer and user_exponent == correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong. The correct answer is {correct_answer}^{correct_answer}")
            else:
                print(f"Invalid input. The correct answer is {correct_answer}^{correct_answer}")
        except ValueError:
            print(f"Invalid input. The correct answer is {correct_answer}^{correct_answer}")

    print(f"Your final score is {score}/10. Great job!")


if __name__ == "__main__":
    math_test_exponents()
