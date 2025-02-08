import random

def generate_problem(is_long=False):
    """
    Generates a random math problem for kids, considering order of operations.
    The problem may include addition, subtraction, multiplication, and division.
    Supports integers (including negative numbers).
    """
    # Determine the number of operations (2 or 3 for short, 4 or 5 for long problems)
    num_operations = random.choice([2, 3]) if not is_long else random.choice([4, 5])

    # Generate integers (including negatives)
    def generate_number():
        return random.randint(-10, 10)  # Limit numbers to simpler ranges for clarity

    numbers = [generate_number() for _ in range(num_operations + 1)]

    # Generate operators
    def generate_operator():
        op = random.choice(['+', '-', '*', '/'])  # Removed '**'
        if op == '**':
            return op, random.randint(0, 3)  # Restrict exponents to 0-3 for simplicity
        return op, None

    operations = []
    for _ in range(num_operations):
        op, exponent = generate_operator()
        if op == '**':
            # Replace the next number with the restricted exponent if operator is **
            numbers[len(operations) + 1] = exponent
        operations.append(op)

    # Build the problem string with proper parentheses to enforce operation order
    problem = str(numbers[0])
    for i in range(num_operations):
        if random.choice([True, False]):
            problem = f"({problem} {operations[i]} {numbers[i + 1]})"
        else:
            problem = f"{problem} {operations[i]} {numbers[i + 1]}"

    return problem

def evaluate_problem(problem):
    """
    Evaluates the math problem string and returns the result.
    """
    try:
        return eval(problem)
    except ZeroDivisionError:
        return None

def math_test():
    """
    Runs the math test for kids.
    """
    print("Welcome to the math test! Solve the problems below:")

    score = 0
    problems = []

    # Generate 20 problems, including 5 longer ones
    for i in range(15):
        problems.append(generate_problem(is_long=False))
    for i in range(5):
        problems.append(generate_problem(is_long=True))

    random.shuffle(problems)  # Shuffle the problems to mix long and short ones

    for i, problem in enumerate(problems):
        correct_answer = evaluate_problem(problem)

        # If division by zero occurred, regenerate the problem
        while correct_answer is None:
            problem = generate_problem(is_long=(i >= 15))
            correct_answer = evaluate_problem(problem)

        print(f"Problem {i + 1}: {problem} = ?")

        # Get the user's answer
        try:
            user_answer = float(input("Your answer (rounded to 2 decimal places): "))
            if correct_answer is not None:
                correct_answer = round(float(correct_answer), 2)  # Round the correct answer to 2 decimal places

            if abs(user_answer - correct_answer) < 1e-2:  # Allow small floating-point errors
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer is {correct_answer}")
        except ValueError:
            print(f"Invalid input. The correct answer is {correct_answer}")

    print(f"Your final score is {score}/20. Great job!")

if __name__ == "__main__":
    math_test()

