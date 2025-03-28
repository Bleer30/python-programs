def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes = ""
    results = ""

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."

        num1, operator, num2 = parts

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2
        first_line += num1.rjust(width) + "    "
        second_line += operator + num2.rjust(width - 1) + "    "
        dashes += "-" * width + "    "

        if show_answers:
            result = str(eval(problem))
            results += result.rjust(width) + "    "

    arranged_problems = f"{first_line.rstrip()}\n{second_line.rstrip()}\n{dashes.rstrip()}"
    if show_answers:
        arranged_problems += f"\n{results.rstrip()}"

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
