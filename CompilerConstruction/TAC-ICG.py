import ply.yacc as yacc

# Get the token list from the lexer
from lexer3 import tokens

# Define the grammar rules
def p_statement_assign(p):
    'statement : ID ASSIGN expression EOL'
    p[0] = ('ASSIGN', p[1], p[3])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EQ expression
                  | expression NE expression'''
    p[0] = ('BINOP', p[2], p[1], p[3])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    '''expression : INT
                  | FLOAT
                  | ID'''
    p[0] = ('NUM', p[1])

def p_statement_if(p):
    'statement : IF expression LBRACE statements RBRACE'
    p[0] = ('IF', p[2], p[4])

def p_statement_else(p):
    'statement : IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE'
    p[0] = ('IFELSE', p[2], p[4], p[8])

def p_statement_while(p):
    'statement : WHILE expression LBRACE statements RBRACE'
    p[0] = ('WHILE', p[2], p[4])

def p_statement_print(p):
    'statement : PRINT expression EOL'
    p[0] = ('PRINT', p[2])

def p_statements(p):
    '''statements : statement
                  | statements statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_program(p):
    'statement : statement statement'
    p[0] = (p[1], p[2])

def p_error(p):
    print(f"SyntaxError: Incorrect syntax. Missing token before '{p.value}' on line {p.lineno-1}")

def p_empty(p):
    'empty :'
    pass

# Build parser
parser = yacc.yacc()

def generate_code(node):
    if isinstance(node, tuple):
        op = node[0]
        if op == 'ASSIGN':
            print(node[1], '=', node[2])
        elif op in ['PLUS', 'MINUS', 'MULT', 'DIV', 'LT', 'GT', 'LE', 'GE', 'EQ', 'NE']:
            t1 = generate_code(node[1])
            t2 = generate_code(node[2])
            t3 = 't' + str(temp_count)
            print(t3, '=', t1, op, t2)
            temp_count += 1
            return t3
        elif op == 'IF':
            t1 = generate_code(node[1])
            label1 = 'L' + str(label_count)
            print('if', t1, 'goto', label1)
            label_count += 1
            generate_code(node[2])
            print(label1 + ':')
        elif op == 'ELSE':
            label1 = 'L' + str(label_count)
            label2 = 'L' + str(label_count + 1)
            print('goto', label2)
            label_count += 2
            print(label1 + ':')
            generate_code(node[2])
            print(label2 + ':')
            generate_code(node[4])
        elif op == 'WHILE':
            label1 = 'L' + str(label_count)
            label2 = 'L' + str(label_count + 1)
            print(label1 + ':')
            t1 = generate_code(node[1])
            print('ifFalse', t1, 'goto', label2)
            label_count += 2
            generate_code(node[2])
            print('goto', label1)
            print(label2 + ':')
        elif op == 'PRINT':
            print('print', node[1])
    else:
        return node

# Test parser with sample input
data = '''
    x = 42.4;
    if (x > 40){
    print(x);
    a = 3 + 1 / 5;
    } 
    else {
    print a ;
    }

'''

# Parse the input
result = parser.parse(data)

generate_code(result)

