# Basic encrypter to save data in the DB
# There are 10 possible encryptions
# Whatever the last number is in the hashed password will determin the encryption key used


class Encrypt:
  def hide(data):
    info = list(data)
    for i in range(len(info)):
      if(info[i] == 'A'):
        info[i] = '0'
      elif(info[i] == 'B'):
        info[i] = 'w'
      elif(info[i] == 'C'):
        info[i] = 'j'
      elif(info[i] == 'D'):
        info[i] = 'G'
      elif(info[i] == 'E'):
        info[i] = 'O'
      elif(info[i] == 'F'):
        info[i] = 'L'
      elif(info[i] == 'G'):
        info[i] = '}'
      elif(info[i] == 'H'):
        info[i] = '4'
      elif(info[i] == 'I'):
        info[i] = '%'
      elif(info[i] == 'J'):
        info[i] = '('
      elif(info[i] == 'K'):
        info[i] = '/'
      elif(info[i] == 'L'):
        info[i] = '>'
      elif(info[i] == 'M'):
        info[i] = 'A'
      elif(info[i] == 'N'):
        info[i] = 'M'
      elif(info[i] == 'O'):
        info[i] = 'I'
      elif(info[i] == 'P'):
        info[i] = 'i'
      elif(info[i] == 'Q'):
        info[i] = 'e'
      elif(info[i] == 'R'):
        info[i] = '+'
      elif(info[i] == 'S'):
        info[i] = '&'
      elif(info[i] == 'T'):
        info[i] = '?'
      elif(info[i] == 'U'):
        info[i] = 'c'
      elif(info[i] == 'V'):
        info[i] = 'o'
      elif(info[i] == 'W'):
        info[i] = 'N'
      elif(info[i] == 'X'):
        info[i] = 'Q'
      elif(info[i] == 'Y'):
        info[i] = '8'
      elif(info[i] == 'Z'):
        info[i] = 'Y'
      elif(info[i] == 'a'):
        info[i] = 'p'
      elif(info[i] == 'b'):
        info[i] = 'l'
      elif(info[i] == 'c'):
        info[i] = 'f'
      elif(info[i] == 'd'):
        info[i] = 'J'
      elif(info[i] == 'e'):
        info[i] = '|'
      elif(info[i] == 'f'):
        info[i] = 'v'
      elif(info[i] == 'g'):
        info[i] = 'u'
      elif(info[i] == 'h'):
        info[i] = 'U'
      elif(info[i] == 'i'):
        info[i] = 't'
      elif(info[i] == 'j'):
        info[i] = 'T'
      elif(info[i] == 'k'):
        info[i] = 'S'
      elif(info[i] == 'l'):
        info[i] = '.'
      elif(info[i] == 'm'):
        info[i] = ','
      elif(info[i] == 'n'):
        info[i] = '"'
      elif(info[i] == 'o'):
        info[i] = '='
      elif(info[i] == 'p'):
        info[i] = '_'
      elif(info[i] == 'q'):
        info[i] = '5'
      elif(info[i] == 'r'):
        info[i] = '3'
      elif(info[i] == 's'):
        info[i] = '1'
      elif(info[i] == 't'):
        info[i] = 'a'
      elif(info[i] == 'u'):
        info[i] = 'b'
      elif(info[i] == 'v'):
        info[i] = 'm'
      elif(info[i] == 'w'):
        info[i] = 'q'
      elif(info[i] == 'x'):
        info[i] = 'p'
      elif(info[i] == 'y'):
        info[i] = 'k'
      elif(info[i] == 'z'):
        info[i] = ';'
      elif(info[i] == '1'):
        info[i] = '*'
      elif(info[i] == '2'):
        info[i] = '^'
      elif(info[i] == '3'):
        info[i] = 's'
      elif(info[i] == '4'):
        info[i] = 'x'
      elif(info[i] == '5'):
        info[i] = '['
      elif(info[i] == '6'):
        info[i] = '`'
      elif(info[i] == '7'):
        info[i] = '!'
      elif(info[i] == '8'):
        info[i] = '#'
      elif(info[i] == '9'):
        info[i] = 'C'
      elif(info[i] == '0'):
        info[i] = 'g'
      elif(info[i] == '~'):
        info[i] = '{'
      elif(info[i] == '`'):
        info[i] = 'R'
      elif(info[i] == '!'):
        info[i] = 'F'
      elif(info[i] == '@'):
        info[i] = '-'
      elif(info[i] == '#'):
        info[i] = '$'
      elif(info[i] == '$'):
        info[i] = 'h'
      elif(info[i] == '%'):
        info[i] = 'y'
      elif(info[i] == '^'):
        info[i] = 'Z'
      elif(info[i] == '&'):
        info[i] = 'n'
      elif(info[i] == '*'):
        info[i] = 'r'
      elif(info[i] == '('):
        info[i] = 'X'
      elif(info[i] == ')'):
        info[i] = 'B'
      elif(info[i] == '-'):
        info[i] = 'D'
      elif(info[i] == '_'):
        info[i] = 'K'
      elif(info[i] == '+'):
        info[i] = 'E'
      elif(info[i] == '='):
        info[i] = '<'
      elif(info[i] == '{'):
        info[i] = 'W'
      elif(info[i] == '['):
        info[i] = '@'
      elif(info[i] == '}'):
        info[i] = '6'
      elif(info[i] == ']'):
        info[i] = ':'
      elif(info[i] == '|'):
        info[i] = 'H'
      elif(info[i] == ':'):
        info[i] = 'z'
      elif(info[i] == ';'):
        info[i] = ']'
      elif(info[i] == '"'):
        info[i] = 'd'
      elif(info[i] == '<'):
        info[i] = '~'
      elif(info[i] == ','):
        info[i] = ')'
      elif(info[i] == '>'):
        info[i] = '7'
      elif(info[i] == '.'):
        info[i] = 'V'
      elif(info[i] == '?'):
        info[i] = '9'
      elif(info[i] == '/'):
        info[i] = '2'
    encryptedString = ""
    for i in range(len(info)):
      encryptedString += info[i]
    return encryptedString

  def discover(data):
    info = list(data)
    for i in range(len(info)):
      if(info[i] == '0'):
          info[i] = 'A'
      elif(info[i] == 'w'):
          info[i] = 'B'
      elif(info[i] == 'j'):
          info[i] = 'C'
      elif(info[i] == 'G'):
          info[i] = 'D'
      elif(info[i] == 'O'):
          info[i] = 'E'
      elif(info[i] == 'L'):
          info[i] = 'F'
      elif(info[i] == '}'):
          info[i] = 'G'
      elif(info[i] == '4'):
          info[i] = 'H'
      elif(info[i] == '%'):
          info[i] = 'I'
      elif(info[i] == '('):
          info[i] = 'J'
      elif(info[i] == '/'):
          info[i] = 'K'
      elif(info[i] == '>'):
          info[i] = 'L'
      elif(info[i] == 'A'):
          info[i] = 'M'
      elif(info[i] == 'M'):
          info[i] = 'N'
      elif(info[i] == 'I'):
          info[i] = 'O'
      elif(info[i] == 'i'):
          info[i] = 'P'
      elif(info[i] == 'e'):
          info[i] = 'Q'
      elif(info[i] == '+'):
          info[i] = 'R'
      elif(info[i] == '&'):
          info[i] = 'S'
      elif(info[i] == '?'):
          info[i] = 'T'
      elif(info[i] == 'c'):
          info[i] = 'U'
      elif(info[i] == 'o'):
          info[i] = 'V'
      elif(info[i] == 'N'):
          info[i] = 'W'
      elif(info[i] == 'Q'):
          info[i] = 'X'
      elif(info[i] == '8'):
          info[i] = 'Y'
      elif(info[i] == 'Y'):
          info[i] = 'Z'
      elif(info[i] == 'p'):
          info[i] = 'a'
      elif(info[i] == 'l'):
          info[i] = 'b'
      elif(info[i] == 'f'):
          info[i] = 'c'
      elif(info[i] == 'J'):
          info[i] = 'd'
      elif(info[i] == '|'):
          info[i] = 'e'
      elif(info[i] == 'v'):
          info[i] = 'f'
      elif(info[i] == 'u'):
          info[i] = 'g'
      elif(info[i] == 'U'):
          info[i] = 'h'
      elif(info[i] == 't'):
          info[i] = 'i'
      elif(info[i] == 'T'):
          info[i] = 'j'
      elif(info[i] == 'S'):
          info[i] = 'k'
      elif(info[i] == '.'):
          info[i] = 'l'
      elif(info[i] == ','):
          info[i] = 'm'
      elif(info[i] == '"'):
          info[i] = 'n'
      elif(info[i] == '='):
          info[i] = 'o'
      elif(info[i] == '_'):
          info[i] = 'p'
      elif(info[i] == '5'):
          info[i] = 'q'
      elif(info[i] == '3'):
          info[i] = 'r'
      elif(info[i] == '1'):
          info[i] = 's'
      elif(info[i] == 'a'):
          info[i] = 't'
      elif(info[i] == 'b'):
          info[i] = 'u'
      elif(info[i] == 'm'):
          info[i] = 'v'
      elif(info[i] == 'q'):
          info[i] = 'w'
      elif(info[i] == 'p'):
          info[i] = 'x'
      elif(info[i] == 'k'):
          info[i] = 'y'
      elif(info[i] == ';'):
          info[i] = 'z'
      elif(info[i] == '*'):
          info[i] = '1'
      elif(info[i] == '^'):
          info[i] = '2'
      elif(info[i] == 's'):
          info[i] = '3'
      elif(info[i] == 'x'):
          info[i] = '4'
      elif(info[i] == '['):
          info[i] = '5'
      elif(info[i] == '`'):
          info[i] = '6'
      elif(info[i] == '!'):
          info[i] = '7'
      elif(info[i] == '#'):
          info[i] = '8'
      elif(info[i] == 'C'):
          info[i] = '9'
      elif(info[i] == 'g'):
          info[i] = '0'
      elif(info[i] == '{'):
          info[i] = '~'
      elif(info[i] == 'R'):
          info[i] = '`'
      elif(info[i] == 'F'):
          info[i] = '!'
      elif(info[i] == '-'):
          info[i] = '@'
      elif(info[i] == '$'):
          info[i] = '#'
      elif(info[i] == 'h'):
          info[i] = '$'
      elif(info[i] == 'y'):
          info[i] = '%'
      elif(info[i] == 'Z'):
          info[i] = '^'
      elif(info[i] == 'n'):
          info[i] = '&'
      elif(info[i] == 'r'):
          info[i] = '*'
      elif(info[i] == 'X'):
          info[i] = '('
      elif(info[i] == 'B'):
          info[i] = ')'
      elif(info[i] == 'D'):
          info[i] = '-'
      elif(info[i] == 'K'):
          info[i] = '_'
      elif(info[i] == 'E'):
          info[i] = '+'
      elif(info[i] == '<'):
          info[i] = '='
      elif(info[i] == 'W'):
          info[i] = '{'
      elif(info[i] == '@'):
          info[i] = '['
      elif(info[i] == '6'):
          info[i] = '}'
      elif(info[i] == ':'):
          info[i] = ']'
      elif(info[i] == 'H'):
          info[i] = '|'
      elif(info[i] == 'z'):
          info[i] = ':'
      elif(info[i] == ']'):
          info[i] = ';'
      elif(info[i] == 'd'):
          info[i] = '"'
      elif(info[i] == '~'):
          info[i] = '<'
      elif(info[i] == ')'):
          info[i] = ','
      elif(info[i] == '7'):
          info[i] = '>'
      elif(info[i] == 'V'):
          info[i] = '.'
      elif(info[i] == '9'):
          info[i] = '?'
      elif(info[i] == '2'):
          info[i] = '/'
    decryptedString = ""
    for i in range(len(info)):
      decryptedString += info[i]
    return decryptedString


# Encryptor Key
      # 'A' = '0'
      # 'B' = 'w'
      # 'C' = 'j'
      # 'D' = 'G'
      # 'E' = 'O'
      # 'F' = 'L'
      # 'G' = '}'
      # 'H' = '4'
      # 'I' = '%'
      # 'J' = '('
      # 'K' = '/'
      # 'L' = '>'
      # 'M' = 'A'
      # 'N' = 'M'
      # 'O' = 'I'
      # 'P' = 'i'
      # 'Q' = 'e'
      # 'R' = '+'
      # 'S' = '&'
      # 'T' = '?'
      # 'U' = 'c'
      # 'V' = 'o'
      # 'W' = 'N'
      # 'X' = 'Q'
      # 'Y' = '8'
      # 'Z' = 'Y'
      # 'a' = 'P'
      # 'b' = 'l'
      # 'c' = 'f'
      # 'd' = 'J'
      # 'e' = '|'
      # 'f' = 'v'
      # 'g' = 'u'
      # 'h' = 'U'
      # 'i' = 't'
      # 'j' = 'T'
      # 'k' = 'S'
      # 'l' = '.'
      # 'm' = ','
      # 'n' = '"'
      # 'o' = '='
      # 'p' = '_'
      # 'q' = '5'
      # 'r' = '3'
      # 's' = '1'
      # 't' = 'a'
      # 'u' = 'b'
      # 'v' = 'm'
      # 'w' = 'q'
      # 'x' = 'p'
      # 'y' = 'k'
      # 'z' = ';'
      # '1' = '*'
      # '2' = '^'
      # '3' = 's'
      # '4' = 'x'
      # '5' = '['
      # '6' = '`'
      # '7' = '!'
      # '8' = '#'
      # '9' = 'C'
      # '0' = 'g'
      # '~' = '{'
      # '`' = 'R'
      # '!' = 'F'
      # '@' = '-'
      # '#' = '$'
      # '$' = 'h'
      # '%' = 'y'
      # '^' = 'Z'
      # '&' = 'n'
      # '*' = 'r'
      # '(' = 'X'
      # ')' = 'B'
      # '-' = 'D'
      # '_' = 'K'
      # '+' = 'E'
      # '=' = '<'
      # '{' = 'W'
      # '[' = '@'
      # '}' = '6'
      # ']' =':'
      # '|' = 'H'
      # ':' = 'z'
      # ';' = ']'
      # '"' = 'd'
      # '<' = '~'
      # ',' = ')'
      # '>' = '7'
      # '.' = 'V'
      # '?' = '9'
      # '/' = '2'