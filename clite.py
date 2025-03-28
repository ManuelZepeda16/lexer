import ply.lex as lex

tokens = [ 'INT' , 'FLOAT']

t_ignore  = ' \t'
digit = r'([0-9])'
expNotation = r'([eE][-+]?[0-9]+)'

floating = fr'({digit}+{expNotation})|({digit}*\.{digit}*{expNotation}?)'
@lex.TOKEN(floating)
def t_FLOAT(t):
  t.value = float(t.value)
  return t

integer = fr'{digit}+(_{digit}+)*'
@lex.TOKEN(integer)
def t_INT(t):
  t.value = int(t.value.replace("_", ""))
  return t

def getLexer():
  return lex.lex()