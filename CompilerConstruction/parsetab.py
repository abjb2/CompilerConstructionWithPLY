
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIV ELSE EOL EQ FLOAT GE GT ID IF INT LBRACE LE LPAREN LT MINUS MULT NE PLUS PRINT RBRACE RPAREN WHILEstatement : ID ASSIGN expression EOLexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression MULT expression\n                  | expression DIV expression\n                  | expression LT expression\n                  | expression GT expression\n                  | expression LE expression\n                  | expression GE expression\n                  | expression EQ expression\n                  | expression NE expressionexpression : LPAREN expression RPARENexpression : INT\n                  | FLOAT\n                  | IDstatement : IF expression LBRACE statements RBRACEstatement : IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACEstatement : WHILE expression LBRACE statements RBRACEstatement : PRINT expression EOLstatements : statement\n                  | statements statementstatement : statement statementempty :'
    
_lr_action_items = {'ID':([0,1,3,4,5,6,7,9,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,44,45,46,47,49,50,51,],[2,2,12,12,12,2,12,12,2,12,12,12,12,12,12,12,12,12,12,2,-19,-1,2,2,2,-16,2,-18,2,2,-17,]),'IF':([0,1,6,16,28,29,30,31,32,44,45,46,47,49,50,51,],[3,3,3,3,3,-19,-1,3,3,3,-16,3,-18,3,3,-17,]),'WHILE':([0,1,6,16,28,29,30,31,32,44,45,46,47,49,50,51,],[4,4,4,4,4,-19,-1,4,4,4,-16,4,-18,4,4,-17,]),'PRINT':([0,1,6,16,28,29,30,31,32,44,45,46,47,49,50,51,],[5,5,5,5,5,-19,-1,5,5,5,-16,5,-18,5,5,-17,]),'$end':([1,6,29,30,45,47,51,],[0,-22,-19,-1,-16,-18,-17,]),'ASSIGN':([2,],[7,]),'LPAREN':([3,4,5,7,9,17,18,19,20,21,22,23,24,25,26,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'INT':([3,4,5,7,9,17,18,19,20,21,22,23,24,25,26,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'FLOAT':([3,4,5,7,9,17,18,19,20,21,22,23,24,25,26,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'RBRACE':([6,29,30,31,32,44,45,46,47,50,51,],[-22,-19,-1,45,-20,47,-16,-21,-18,51,-17,]),'LBRACE':([8,10,11,12,13,33,34,35,36,37,38,39,40,41,42,43,48,],[16,-13,-14,-15,28,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,49,]),'PLUS':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[17,-13,-14,-15,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-12,]),'MINUS':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[18,-13,-14,-15,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-12,]),'MULT':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[19,-13,-14,-15,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-12,]),'DIV':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[20,-13,-14,-15,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-12,]),'LT':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[21,-13,-14,-15,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-12,]),'GT':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[22,-13,-14,-15,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-12,]),'LE':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[23,-13,-14,-15,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-12,]),'GE':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[24,-13,-14,-15,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-12,]),'EQ':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[25,-13,-14,-15,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-12,]),'NE':([8,10,11,12,13,14,15,27,33,34,35,36,37,38,39,40,41,42,43,],[26,-13,-14,-15,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-12,]),'EOL':([10,11,12,14,15,33,34,35,36,37,38,39,40,41,42,43,],[-13,-14,-15,29,30,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,]),'RPAREN':([10,11,12,27,33,34,35,36,37,38,39,40,41,42,43,],[-13,-14,-15,43,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,]),'ELSE':([45,],[48,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,1,6,16,28,31,32,44,46,49,50,],[1,6,6,32,32,46,6,46,6,32,46,]),'expression':([3,4,5,7,9,17,18,19,20,21,22,23,24,25,26,],[8,13,14,15,27,33,34,35,36,37,38,39,40,41,42,]),'statements':([16,28,49,],[31,44,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> ID ASSIGN expression EOL','statement',4,'p_statement_assign','TAC-ICG.py',8),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','TAC-ICG.py',12),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','TAC-ICG.py',13),
  ('expression -> expression MULT expression','expression',3,'p_expression_binop','TAC-ICG.py',14),
  ('expression -> expression DIV expression','expression',3,'p_expression_binop','TAC-ICG.py',15),
  ('expression -> expression LT expression','expression',3,'p_expression_binop','TAC-ICG.py',16),
  ('expression -> expression GT expression','expression',3,'p_expression_binop','TAC-ICG.py',17),
  ('expression -> expression LE expression','expression',3,'p_expression_binop','TAC-ICG.py',18),
  ('expression -> expression GE expression','expression',3,'p_expression_binop','TAC-ICG.py',19),
  ('expression -> expression EQ expression','expression',3,'p_expression_binop','TAC-ICG.py',20),
  ('expression -> expression NE expression','expression',3,'p_expression_binop','TAC-ICG.py',21),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','TAC-ICG.py',25),
  ('expression -> INT','expression',1,'p_expression_number','TAC-ICG.py',29),
  ('expression -> FLOAT','expression',1,'p_expression_number','TAC-ICG.py',30),
  ('expression -> ID','expression',1,'p_expression_number','TAC-ICG.py',31),
  ('statement -> IF expression LBRACE statements RBRACE','statement',5,'p_statement_if','TAC-ICG.py',35),
  ('statement -> IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE','statement',9,'p_statement_else','TAC-ICG.py',39),
  ('statement -> WHILE expression LBRACE statements RBRACE','statement',5,'p_statement_while','TAC-ICG.py',43),
  ('statement -> PRINT expression EOL','statement',3,'p_statement_print','TAC-ICG.py',47),
  ('statements -> statement','statements',1,'p_statements','TAC-ICG.py',51),
  ('statements -> statements statement','statements',2,'p_statements','TAC-ICG.py',52),
  ('statement -> statement statement','statement',2,'p_program','TAC-ICG.py',60),
  ('empty -> <empty>','empty',0,'p_empty','TAC-ICG.py',67),
]
