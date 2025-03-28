import ply.lex as lex

tokens = [ 'INT' , 'FLOAT']

t_ignore  = ' \t'

def t_FLOAT(t):
  r'[0-9]*\.[0-9]*'
  t.value = float(t.value)
  return t
  
def t_INT(t):
  r'[0-9]+(_[0-9]+)*'
  t.value = int(t.value.replace("_", ""))
  return t

def getLexer():
  return lex.lex()