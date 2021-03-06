from random import *

# charList is the list of characters, numbers, and symbols used to create the encryptor key
charList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[',']','}','|',';',':','"','<',',','.','>','?','/']


# Creates a key for encrypting and decrypting
def createEncryptorKey(masterPassword):
  # the four idx's are started at different positions to help the generation of nonmatching keys
  encryptorKey = {}
  idx1 = 3
  idx2 = 13
  idx3 = 7
  idx4 = 11
  # for loop to create a dictionary with with all characters from the charList and their respective keys
  for i in range(len(charList)):
    # while loop will continue to create keys until a unused key is created
    unique = False
    count = 0
    while(unique == False):
      unique = True
      # helps prevent repeat keys
      if idx1 == idx2:
        idx1 += 3
      if idx2 == idx3:
        idx2 += 2
      if idx3 == idx4:
        idx3 += 2
      # moves the idx back into the range of the list
      if idx1 >= len(masterPassword):
        idx1 = 3
      if idx2 >= len(masterPassword):
        idx2 = 13
      if idx3 >= len(masterPassword):
        idx3 = 7
      if idx4 >= len(masterPassword):
        idx4 = 11
      # Checks to see if that key has already been created
      key = masterPassword[idx1] + masterPassword[idx2] + masterPassword[idx3] + masterPassword[idx4]
      if key in encryptorKey:
        unique = False
        count += 1
      else:
        encryptorKey[key] = charList[i]
      # if keys are not unique then count will increase the idx's to help unique key generation
      # while loop will not stop without this
      if count > 5:
        idx1 += 1
      if count > 10:
        idx2 += 1
      if count > 20:
        idx3 += 1
      if count > 30:
        idx4 += 1
      
      idx1 += 1
      idx2 += 1
      idx3 += 1
      idx4 += 1
  return encryptorKey


# Encrypts and decrypts passwords
class Wizard:
  # encrypts the password to be saved in the DB
  def disappear(masterPassword, password):
    encryptorKey = createEncryptorKey(masterPassword)
    dbPassword = ""
    keyList = list(encryptorKey.keys())
    valList = list(encryptorKey.values())
    for i in range(len(password)):
      idx = valList.index(password[i])
      dbPassword += keyList[idx]
    return dbPassword

  # decrypts the password to be seen by the user
  def reappear(masterPassword, dbPassword):
    encryptorKey = createEncryptorKey(masterPassword)
    viewPassword = ""
    keyList = list(encryptorKey.keys())
    valList = list(encryptorKey.values())
    tempVal = ""
    count = 0
    for i in range(len(dbPassword)):
      tempVal += dbPassword[i]
      if count == 3:
        idx = keyList.index(tempVal)
        viewPassword += valList[idx]
        tempVal = ""
        count = 0
        continue
      count += 1
    return viewPassword




# Validates the password
class PasswordChecker:
  def symbolCheck(password):
    symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[',']','}','|',';',':','"','<',',','.','>','?','/']
    symbIdx = 0
    passIdx = 0
    count = 0
    for i in range(len(password)):
      if password[i] in symbols:
        count += 1
    if count > 5:
      return "You can only use 5 symbols"
    if count < 5:
      return "You need to have 5 symbols"

  def numberCheck(password):
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    numIdx = 0
    passIdx = 0
    count = 0
    for i in range(len(password)):
      if password[i] in numbers:
        count += 1
    if count > 5:
      return "You can only use 5 numbers"
    if count < 5:
      return "You need to have 5 numbers"

  def lowerLettersCheck(password):
    lowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    letterIdx = 0
    passIdx = 0
    count = 0
    for i in range(len(password)):
      if password[i] in lowerLetters:
        count += 1
    if count > 5:
      return "You can only use 5 lower case letters"
    if count < 5:
      return "You need to have 5 lower case letters"

  def capLettersCheck(password):
    capLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letterIdx = 0
    passIdx = 0
    count = 0
    for i in range(len(password)):
      if password[i] in capLetters:
        count += 1
    if count > 5:
      return "You can only use 5 upper case letters"
    if count < 5:
      return "You need to have 5 upper case letters"


# Creates a strong password
class Password:
  def create(maxLength):
    password = ""

    chars = [
      ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','[',']','}','|',';',':','"','<',',','.','>','?','/'],
      ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
      ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],
      ['1','2','3','4','5','6','7','8','9','0']
    ]

    for i in range(maxLength):
      charIdx = randint(0, 3)
      idx = randint(0, len(chars[charIdx])-1)
      password += chars[charIdx][idx]

    return password
