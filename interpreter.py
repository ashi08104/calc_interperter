def get_paired_parenthes_pos(s, left_paren_pos):
    """Get left_paren_pos's paired parenthes in s.
    If no parenthes pos found or unpair parenthes included, an error will be
    thrown.
    """
    assert(s)
    assert(s[left_paren_pos] == '(')

    def get_paired_parenthes_pos_help(start_pos):
        try:
            next_p = start_pos + 1
            # If () case
            if s[next_p] == ')':
                return next_p
            # if ((... case
            elif s[next_p] == '(':
                return get_paired_parenthes_pos_help(
                    get_paired_parenthes_pos_help(next_p))
            # if (abc... case
            else:
                return get_paired_parenthes_pos_help(next_p)
        except IndexError:
            raise Exception("Unmatched parenthes found.")

    return get_paired_parenthes_pos_help(left_paren_pos)

def str2tk(s):
    """break the string into tokens
    e.g. "(33+2)" -> ["(", "33", "+", "2", ")"]"""

    if not s:
        return []
    elif s[0].isdigit():
        dig_len = 1
        while dig_len < len(s) and s[dig_len].isdigit():
            dig_len += 1
        return [s[:dig_len]] + str2tk(s[dig_len:])
    elif s[0].isspace():
        return str2tk(s[1:])
    else:
        return [s[0]] + str2tk(s[1:])

class AstNode(object):
    def __init__(self, token=""):
        self.token = token
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left
        right = self.right
        if not left:
            left = "N"
        if not right:
            right = "N"
        return "[{}:{} {}]".format(self.token,
                                   left,
                                   right)

def parser(exps):
    """Parse following grammar and return the AST:
       E->n
       E->(E OP E)
       OP-> one of +, -, *, /
    Input is list of tokens: ["(", "33", "+", "2", ")"]
    """
    if exps[0].isdigit():
        # case of E->n
        return AstNode(exps[0])
    elif exps[0] == "(":
        # case of E->(E+E)
        # Look forward one element.
        ast = AstNode()
        if exps[1] == "(":
            pos = get_paired_parenthes_pos(exps, 1)
            ast.left = parser(exps[1:pos + 1])
            # Extract operation.
            ast.token = exps[pos + 1]
            # Exclude last ")".
            ast.right = parser(exps[pos + 2:-1])
            return ast
        else:
            # It is digit.
            ast.left = AstNode(exps[1])
            ast.token = exps[2]
            ast.right = parser(exps[3:])
            return ast

def str2ast(s):
    return parser(str2tk(s))

def eval_help(ast):
    """ Evaluate ast to result.
    """
    # The terminal node, which is None.
    # This would not happen. Because every terminal node must be the leaf of
    # number node and number just return number.
    # if not ast:
    #     return 0

    # Number node, just return number.
    if ast.token.isdigit():
        return int(ast.token)
    # Varies opeartions.
    # TODO is there a simpler solution?:
    # return eval_help(ast.left) (translate2opeartion(ast.token)) eval_help(ast.right)
    elif ast.token == "+":
        return eval_help(ast.left) + eval_help(ast.right)
    elif ast.token == "-":
        return eval_help(ast.left) - eval_help(ast.right)
    elif ast.token == "*":
        return eval_help(ast.left) * eval_help(ast.right)
    elif ast.token == "/":
        return eval_help(ast.left) / eval_help(ast.right)

def evaluate(s):
    return eval_help(str2ast(s))

if __name__ == "__main__":
    pass
