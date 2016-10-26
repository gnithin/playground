from parser import Arith
import timeit
from asteval import Interpreter

aeval = Interpreter()
singleTest = "-0.99 <= ((0+1.1+2.2)-(3.3+4.4+5.5+6.6)) <= 0.99"

allVars = {'A': 0, 'B': 1.1, 'C': 2.2, 'D': 3.3, 'E': 4.4, 'F': 5.5, 'G':
           6.6, 'H': 7.7, 'I': 8.8, 'J': 9.9, "abc": 20, }

for k, v in allVars.items():
    aeval.symtable[k] = v

allExamples = [
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
     'not A and (B+C < E) and G'
    ]


def pyparserAllTest():
    arith = Arith(allVars)
    # Just using a simple test right now
    pyparserExec(allExamples, arith)


def evalAllTest():
    evalExec(allExamples, allVars)


def astEvalAllTest():
    astEvalExec(allExamples, allVars)


def pyparserSingleTest():
    arith = Arith(allVars)
    test = 'not A and (B+C < E) and G'
    test = singleTest
    # Just using a simple test right now
    pyparserExec([test], arith)


def evalSingleTest():
    test = 'not A and (B+C < E) and G'
    test = singleTest
    evalExec([test], allVars)


def astEvalSingleTest():
    test = 'not A and (B+C < E) and G'
    test = singleTest
    astEvalExec([test], allVars)


def evalExec(tests, ipVars):
    for test in tests:
        eval(test, ipVars)


def astEvalExec(tests, ipVars):
    for test in tests:
        # ast.literal_eval(test, ipVars)
        aeval(test)


def pyparserExec(tests, arith):
    for test in tests:
        arith.eval(test)

if __name__ == "__main__":
    singleTestNumberRuns = 100
    allTestNumberRuns = 1

    testsList = [
        ["astEvalSingleTest", singleTestNumberRuns],
        ["evalSingleTest", singleTestNumberRuns],
        ["pyparserSingleTest", allTestNumberRuns],
        ["astEvalAllTest", allTestNumberRuns],
        ["evalAllTest", allTestNumberRuns],
        ["pyparserAllTest", allTestNumberRuns]
    ]

    for testItem in testsList:
        print("*" * 10)
        testname = testItem[0]
        numberRuns = testItem[1]

        overallTime = timeit.timeit(
            testname + "()",
            setup="from __main__ import " + testname,
            number=numberRuns)

        avgTime = overallTime/numberRuns

        print("Test name - " + testname)
        print("Number of runs - " + str(numberRuns))
        print("Average time : {}".format(avgTime))
        print("Overall time : {}".format(overallTime))
