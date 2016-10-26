from pyparsing import Word, nums, alphas, alphanums, Combine, oneOf, Optional, \
    opAssoc, operatorPrecedence, QuotedString, Keyword, ParserElement

# ParserElement.enablePackrat()


class EvalConstant():
    "Class to evaluate a parsed constant or variable"
    def __init__(self, tokens):
        self.value = tokens[0]
    def eval(self, vars_):
        vars_.setdefault("True", True)
        vars_.setdefault("False", False)
        if self.value in vars_:
            return vars_[self.value]
        elif len(self.value) > 1 and (self.value[0], self.value[-1]) in [ ("'", "'"), ('"', '"') ]:
            return self.value[1:-1]
        else:
            try:
                return int( self.value )
            except:
                return float(self.value)

class EvalSignOp():
    "Class to evaluate expressions with a leading + or - sign"
    def __init__(self, tokens):
        self.sign, self.value = tokens[0]
    def eval(self, vars_):
        mult = {'+':1, '-':-1}[self.sign]
        return mult * self.value.eval( vars_ )

def operatorOperands(tokenlist):
    "generator to extract operators and operands in pairs"
    it = iter(tokenlist)
    while 1:
        try:
            o1 = next(it)
            o2 = next(it)
            yield ( o1, o2 )
        except StopIteration:
            break

class EvalMultOp():
    "Class to evaluate multiplication and division expressions"
    def __init__(self, tokens):
        self.value = tokens[0]
    def eval(self, vars_ ):
        prod = self.value[0].eval( vars_ )
        for op,val in operatorOperands(self.value[1:]):
            if op == '*':
                prod *= val.eval( vars_ )
            if op == '/':
                prod /= val.eval( vars_ )
            if op == '//':
                prod //= val.eval( vars_ )
            if op == '%':
                prod %= val.eval( vars_ )
        return prod

class EvalAddOp():
    "Class to evaluate addition and subtraction expressions"
    def __init__(self, tokens):
        self.value = tokens[0]
    def eval(self, vars_ ):
        sum = self.value[0].eval( vars_ )
        for op,val in operatorOperands(self.value[1:]):
            if op == '+':
                sum += val.eval( vars_ )
            if op == '-':
                sum -= val.eval( vars_ )
        return sum

class EvalComparisonOp():
    "Class to evaluate comparison expressions"
    opMap = {
        "<" : lambda a,b : a < b,
        "<=" : lambda a,b : a <= b,
        ">" : lambda a,b : a > b,
        ">=" : lambda a,b : a >= b,
        "==" : lambda a,b : a == b,
        "!=" : lambda a,b : a != b,
        'in' : lambda a,b : a in b,
        "not in" : lambda a,b : a not in b,
        "is" : lambda a,b : a is b,
        "is not" : lambda a,b : a is not b,
        }
    def __init__(self, tokens):
        self.value = tokens[0]
    def eval(self, vars_ ):
        val1 = self.value[0].eval( vars_ )
        for op,val in operatorOperands(self.value[1:]):
            fn = self.opMap[op]
            val2 = val.eval( vars_ )
            if not fn(val1,val2):
                break
            val1 = val2
        else:
            return True
        return False

class EvalBoolOp():
    "Class to evaluate and and or expressions"
    def __init__(self, tokens):
        self.value = tokens[0]
    def eval(self, vars_ ):
        sum = self.value[0].eval( vars_ )
        for op,val in operatorOperands(self.value[1:]):
            if op == 'and':
                sum = sum and val.eval( vars_ )
            if op == 'or':
                sum = sum or val.eval( vars_ )
        return sum

class EvalBoolNot():
    "Class to evaluate expressions with a not"
    def __init__(self, tokens):
        self.sign, self.value = tokens[0]
    def eval(self, vars_):
        return not self.value.eval( vars_ )


class Arith():
    # define the parser
    integer = Word(nums)
    real = ( Combine(Word(nums) + Optional("." + Word(nums))
                     + oneOf("E e") + Optional( oneOf('+ -')) + Word(nums))
             | Combine(Word(nums) + "." + Word(nums))
             )

    TRUE = Keyword("True")
    FALSE = Keyword("False")

    variable = Combine(Word(alphas + "_", exact=1) + Optional(Word(alphanums + '_')))
    operand = real | integer | variable | \
              TRUE | FALSE | \
              QuotedString('"', escChar = '\\', unquoteResults=False) | QuotedString("'", escChar = '\\', unquoteResults=False)

    signop = oneOf('+ -')
    multop = oneOf('* / // %')
    plusop = oneOf('+ -')
    comparisonop = oneOf(['<', '<=', '>', '>=', '==', '!=', '<>', 'not in', 'in', 'is not', 'is'])
    booland = oneOf('and')
    boolor = oneOf('or')
    boolnot = oneOf('not')

    # use parse actions to attach EvalXXX constructors to sub-expressions
    operand.setParseAction(EvalConstant)
    arith_expr = operatorPrecedence(operand,
        [(signop, 1, opAssoc.RIGHT, EvalSignOp),
         (multop, 2, opAssoc.LEFT, EvalMultOp),
         (plusop, 2, opAssoc.LEFT, EvalAddOp),
         (comparisonop, 2, opAssoc.LEFT, EvalComparisonOp),
        (boolnot, 1, opAssoc.RIGHT, EvalBoolNot),
        (booland, 2, opAssoc.LEFT,  EvalBoolOp),
        (boolor, 2, opAssoc.LEFT, EvalBoolOp),
         ])

    def __init__( self, vars_={} ):
        self.vars_ = vars_

    def setvars( self, vars_ ):
        self.vars_ = vars_

    def setvar( var, val ):
        self.vars_[ var ] = val

    def eval( self, strExpr ):
        ret = self.arith_expr.parseString( strExpr, parseAll=True)[0]
        result = ret.eval( self.vars_ )
        return result

if __name__=='__main__':
    def main():
        # sample expressions posted on comp.lang.python, asking for advice
        # in safely evaluating them
        rules=[
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
        vars_={'A': 0, 'B': 1.1, 'C': 2.2, 'D': 3.3, 'E': 4.4, 'F': 5.5, 'G':
               6.6, 'H':7.7, 'I':8.8, 'J':9.9, "abc": 20, }

        # define tests from given rules
        tests = []
        for t in rules:
            tests.append( (t, eval(t,vars_)) )

        # copy vars_ to EvalConstant lookup dict
        arith = Arith( vars_ )
        for test,expected in tests:
            result = arith.eval( test )
            print( test, expected == result )
            # print( ret )
            if expected != result:
                print("*" * 60 )

    main()
