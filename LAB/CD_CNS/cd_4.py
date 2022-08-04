import re

# s = input("Enter filename : ")
s = 'main.c'
f = open(s, 'r')
text = f.read()

symbols = ['!', '@', '#', '$', '%', '&', '^', '*']
oparators = ['+', '-', '*', '/', '=', '+=', '-=', '==', '<', '>', '<=', '>=']
keywords = ['auto','break', 'case', 'char', 'const', 'continue', 'default', 'do', 
			'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 
			'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 
			'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
delimiters = [' ', '	', '.', ',', '\n', ';', '(', ')', '<', '>', '{', '}', '[', ']']


in_keywords = []
in_spl_symbols = []
in_oparators = []
in_delimiters = []
in_identifiers = []
in_constants = []

tokens = []
isStr = False
isWord = False
isCmt = 0
token = ''

for i in text:
	if i == '/':
		isCmt = isCmt+1

	elif isCmt == 2:
		if i == '\n':
			token = ''
			isCmt = 0
	
	elif i == '"' or i == "'":
		if isStr:
			tokens.append(token)
			token = ''
		isStr = not isStr 

	elif isStr:
		token = token+i
    
	elif i in symbols:
		tokens.append(i)
           
	elif i.isalnum() and not isWord:
		isWord = True
		token = i
    
	elif (i in delimiters) or (i in oparators):
		if token:
			tokens.append(token)
			token = ''
        
		if not (i==' ' or i=='\n' or i=='	'):
			tokens.append(i)

	elif isWord:
		token = token+i


for token in tokens:
	if token in symbols:
		in_spl_symbols.append(token)

	elif token in oparators:
		in_oparators.append(token)

	elif token in keywords:
		in_keywords.append(token)
				
	elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$",token):
		in_identifiers.append(token)
		
	elif token in delimiters:
		in_delimiters.append(token)
		
	else:
		in_constants.append(token)
	
						
print("No of tokens = ", len(tokens))   
print("\nNo. of keywords = ",len(in_keywords))
print(in_keywords);
print("\nNo. of special symbols = ",len(in_spl_symbols))
print(in_spl_symbols);
print("\nNo. of oparators = ",len(in_oparators))
print(in_oparators);
print("\nNo. of identifiers = ",len(in_identifiers))
print(in_identifiers);
print("\nNo. of constants = ",len(in_constants))
print(in_constants);
print("\nNo. of delimiters = ",len(in_delimiters))
print(in_delimiters);
f.close()   