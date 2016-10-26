from asteval import Interpreter
import sys

# Deleting some node modules that can cause harm
# This is the bare minimum
acceptable_entries = [
    'binop',
    'boolop',
    'compare',
    'expr',
    'module',
    'name',
    'num',
    'str',
    'nameconstant',
    'unaryop',
    # 'try'  # This is needed for Interpreter to be initialized
]

# Deleting entries that are not required.
Interpreter.supported_nodes = tuple(acceptable_entries)

if __name__ == "__main__":
    rules = [
        '( A - B ) == 0',
        '(A + B + C + D + E + F + G + H + I) == J',
        '(A + B + C + D + E + F + G + H) == I',
        '(A + B + C + D + E + F) == G',
        '(A + B + C + D + E) == (F + G + H + I + J)',
        '(A + B + C + D + E) == (F + G + H + I)',
        '(A + B + C + D + E) == F',
        '(A + B + C + D) == (E + F + G + H)',
        '(A + B + C) == (D + E + F)',
        '(A + B) == (C + D + E + F)',
        '(A + B) == (C + D)',
        '(A + B) == (C - D + E - F - G + H + I + J)',
        '(A + B) == C',
        '(A + B) == 0',
        '(A+B+C+D+E) == (F+G+H+I+J)',
        '(A+B+C+D) == (E+F+G+H)',
        '(A+B+C+D)==(E+F+G+H)',
        '(A+B+C)==(D+E+F)',
        '(A+B)==(C+D)',
        '(A+B)==C',
        '(A-B)==C',
        '(A/(B+C))',
        '(B/(C+D))',
        '(G + H) == I',
        '-0.99 <= ((A+B+C)-(D+E+F+G)) <= 0.99',
        '-0.99 <= (A-(B+C)) <= 0.99',
        '-1000.00 <= A <= 0.00',
        '-5000.00 <= A <= 0.00',
        'A < B',
        'A < 7000',
        'A == -(B)',
        'A == C',
        'A == 0',
        'A > 0',
        'A > 0.00',
        'A > 7.00',
        'A <= B',
        'A < -1000.00',
        'A < -5000',
        'A < 0',
        'A==(B+C+D)',
        'A==B',
        'I == (G + H)',
        '0.00 <= A <= 4.00',
        '4.00 < A <= 7.00',
        '0.00 <= A <= 4.00 <= E > D',
        '123E0 > 1000E-1 > 99.0987',
        '123E+0',
        '1000E-1',
        '99.0987',
        'abc',
        '20 % 3',
        '14 // 3',
        '12e2 // 3.7',
        '"a" * 3',
        "('a' * (1+(1+1))) * (1+1)",
        '1 == 2 or A == A',
        'not A and (B+C < E) and G',
        '1 in li',
        '"a1" in di',
        'A is True',
        '"123" in [1,2,3,4]',  # This should throw an error. No lists inside :p
        'True is False',
        'A is None',
        'li.append("123")',
        'A ** 20',
        # Now the real ones
        '__import__("os")',
        '__import__("os").environ',
        '(lambda x:x**2)(2)',
        'm1.__call__',
        'print 123',
        'class mischief:pass'
        ]
    vars_ = {'A': 0, 'B': 1.1, 'C': 2.2, 'D': 3.3, 'E': 4.4, 'F': 5.5, 'G':
             6.6, 'H': 7.7, 'I': 8.8, 'J': 9.9, "abc": 20,
             "li": [1, 2, 3],
             "di": {"a1": "1", "a2": [4, 5, 6]},
             "m1": (lambda : __import__("os"))
             }

    orig_eval = Interpreter()
    # populating the Interpreter
    for k, v in vars_.items():
        orig_eval.symtable[k] = v

    # Validating the results with eval
    for r in rules:
        print("*" * 40)
        print(r)

        try:
            astResp = orig_eval(r)
            if len(orig_eval.error):
                print("Failed - " + orig_eval.error_msg)
            else:
                evalResp = eval(r, vars_)
                if astResp != evalResp:
                    print("FAILURE!!! " + r)
                    print("This should never happen!")
                    sys.exit(1)
        except Exception as e:
            print("Failed for " + r)
            print(e)
