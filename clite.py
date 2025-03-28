import ply.lex as lex

tokens = [ 'INT' , 'FLOAT']

t_ignore  = ' \t'
digit = r'([0-9])'
underscoredDigit = fr'({digit}+(_{digit}+)*)'
expNotation = fr'([eE][-+]?{underscoredDigit}+)'

floating = fr'({underscoredDigit}+{expNotation})|({underscoredDigit}*\.{underscoredDigit}*{expNotation}?)'
@lex.TOKEN(floating)
def t_FLOAT(t):
  t.value = float(t.value)
  return t

integer = underscoredDigit
@lex.TOKEN(integer)
def t_INT(t):
  t.value = int(t.value.replace("_", ""))
  return t

def getLexer():
  return lex.lex()