import ply.lex as lex
import re

tokens = (
    'FUNC', # D
    'NUMBER', # D
    'PLUS', # D
    'MINUS', # D
    'GREATER', # D 
    'LESS', # D
    'TIMES', # D
    'DIVIDE', # D
    'LOOP', # D
    'FUNCTION',
    'PROGRAM',
    'VARIABLES', # D
    'EQUAL', 
    'CAST',
    'BRACKETS_O',
    'BRACKETS_C',
    'CBRACKETS_O',
    'CBRACKETS_C',
    'RBRACKETS_O',
    'RBRACKETS_C',
    'END_OF_LINE',
    'LIST',
    'COMMENT', 
    'MULTI_COMMENT', 
    'COMMA'
)

t_FUNC = r' \w+(?=[\{\(])' 
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_FUNCTION = r'function'
t_PROGRAM = r'program'
t_VARIABLES = r' \w+(?=\[)*'
t_GREATER = r'>'
t_LESS = r'<'
t_EQUAL = r'='
t_BRACKETS_O = r'\(' 
t_BRACKETS_C = r'\)' 
t_CBRACKETS_O = r'\{' 
t_CBRACKETS_C = r'\}' 
t_RBRACKETS_O = r'\[' 
t_RBRACKETS_C = r'\]'
t_END_OF_LINE = r'\;'
t_LIST = r'\[.*,*\]'
t_COMMENT = r'//.*'
t_MULTI_COMMENT = r'/\*[\s\S]*?\*/'
t_COMMA = r'\,'




def t_NUMBER(t) : 
    r'\d+'
    t.value = int(t.value)
    return t

def t_LOOP(t):
    r'for|while'
    return t

def t_CAST(t) : 
    r'int|float|double|bool|char|string|long'
    return t


def t_error(t):
    if re.match(r'[ \t\n]', t.value[0]) == None:
      print(f"Unspecified token {t.value[0]}")
    t.lexer.skip(1)


example1 = '''
/* factorial.p
-- 2023-03-20 
-- by jcr
*/

int i;

// Função que calcula o factorial dum número n
function fact(n){
  int res = 1;
  while res > 1 {
    res = res * n;
    res = res - 1;
  }
}

// Programa principal
program myFact{
  for i in [1..10]{
    print(i, fact(i));
  }
}
'''


example2 = '''
/* max.p: calcula o maior inteiro duma lista desordenada
-- 2023-03-20 
-- by jcr
*/
int i = 10, a[10] = {1,2,3,4,5,6,7,8,9,10};
// Programa principal
program myMax{
  int max = a[0];
  for i in [1..9]{
    if max < a[i] {
      max = a[i];
    }
  }
  print(max);
}
'''

lexer = lex.lex()
lexer.input(example1)

print("\n\n\n")
print("EXAMPLE 1")
print("\n\n")


while tok := lexer.token():
    print(tok)


print("\n\n\n")
print("EXAMPLE 2")
print("\n\n")


lexer.input(example2)

while tok := lexer.token():
    print(tok)