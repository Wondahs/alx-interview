#!/usr/bin/python3
def generateParenthesis(n):
    def backtrack(combination, n, openCount, closeCount, result):
        # Base case
        if n == 0 and openCount == 0:
            result.append(combination)
            return

        # Try adding an opening parenthesis
        if n > 0:
            print(combination,"-- N:", "n:", n, "Open:", openCount, "Close:", closeCount)
            print("Adding Opening Bracket")
            backtrack(combination + '(', n - 1, openCount + 1, closeCount, result)

        # Try adding a closing parenthesis (if valid)
        if openCount > 0:
            print(combination,"-- N:", "n:", n, "Open:", openCount, "Close:", closeCount)
            print("Adding Closing Bracket")
            backtrack(combination + ')', n, openCount - 1, closeCount + 1, result)

    result = []
    backtrack('', n, 0, 0, result)
    return result

print(generateParenthesis(3))