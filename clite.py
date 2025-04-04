import ply.lex as lex

tokens = [ 'INT' , 'FLOAT', 'STR']

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

string = r'"([^"\\]|\\.)*"'
@lex.TOKEN(string)
def t_STR(t):
    if '\\' in t.value:
        t.value = str(t.value)
        return t
    else:
        t.value = str(t.value[1:-1])
        return t

def getLexer():
  return lex.lex()