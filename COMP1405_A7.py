# ============================================================
#
# Student Name (as it appears on cuLearn): Jeff Jose
# Course Code (for this current semester): COMP1405B
#
# ============================================================
'''
This function will save data on a text file.

@params		file_name, the name of the file to be loaded
@return		an uppercase string containing the data read from the file
'''
def load_text(file_name):
	file_hndl = open(file_name, "r")
	file_data = file_hndl.read()
	file_hndl.close()
	return file_data.upper()

'''
This function will save data to a text file.

@params		file_name, the name of the file to be saved
		file_data, the data to be written to the file
@return		none
'''
def save_text(file_name, file_data):
	file_hndl = open(file_name, "w")
	file_hndl.write(file_data)
	file_hndl.close()
'''
This function will encode the user entered string.

@params		a, the text to be encoded
		b, the alphabet used for the encoding
@return		c, the encoded string
'''
def encode(a, b):
	c = ''
	counter = 0 
	alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	while counter < len(a):
		if (a[counter] not in alphabet_list):
			c = c + a[counter]
		else: 
			for element in range(0, len(alphabet_list)):
				if a[counter] == alphabet_list[element]:
					c = c + (b[element])
		counter = counter + 1
	return(c)
'''
This function will decode the user entered string.

@params		a, the string to be decoded
		b, the alphabet used for decoding
@return		c, the decoded string
'''
def decode(a, b):
	counter = 0
	alphabet_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	c = ''
	while counter < len(a): 
		if (a[counter] not in alphabet_list):
			c = c + a[counter]
		else:
			for element in range(0, len(alphabet_list)):
				if a[counter] == b[element]:
					c = c + alphabet_list[element]
		counter = counter + 1 
	return(c)
'''
This function will shift the alphabet by the integer value inputed.

@params		num, the integer value to shift alphabet
@return		new_alphabet, the shifted alphabet
'''
def caesar_cipher_alphabet(integer):
	new_alphabet=''
	actual_alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for i in range(integer, len(actual_alphabet)):
		new_alphabet=new_alphabet+actual_alphabet[i]
	for j in range (0, integer):
		new_alphabet=new_alphabet+actual_alphabet[j]
	return(new_alphabet)
'''
This function will create a "modified alphabet".

@params		none
@return		a new or unmodified alphabet
'''
def cryptogram_alphabet(): 
	new_alphabet = ''
	count = 0 
	actual_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	modified_list = '' 
	flag = True
	new_alphabet = ''
	print("Input a letter ONCE (any order), then press 'enter' until all 26 letters are\nentered. If an error is made, the Alphabet starting with 'A' will be used.")
	for i in range (0, 26): 
		value = input().upper()
		new_alphabet = new_alphabet + value
	for j in range(0, len(actual_alphabet)):
		flag = True 
		count = 0
		while(count < len(new_alphabet) and flag is True): 
			if (actual_alphabet[j] == new_alphabet[count]):
				if(actual_alphabet[j] not in modified_list): 
					modified_list = modified_list + actual_alphabet[j]
				flag = False
			else: 
                		count = count + 1
	if(modified_list == actual_alphabet):
		result = new_alphabet 
	else:
		result = actual_alphabet
	return(result)
'''
This function will shift the keyword inpuuted to the beginning of the sequence.

@params		num, the integer value to shift alphabet
@return		new_alphabet, the shifted alphabet
'''
def keyword_cipher_alphabet(string_variable):
	actual_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	new_string = string_variable
	new_alphabet = ''
	for i in range(0, len(new_string)):
		for j in range(0, len(actual_alphabet)):
			if(new_string[i] == actual_alphabet[j]):
				actual_alphabet.pop(j)
				break;
	for k in range(0,len(actual_alphabet)):
		new_alphabet = new_alphabet + actual_alphabet[k]
	new_string=new_string + new_alphabet
	return(new_string)
'''
This is the main function, responsible for the user interface.

@params		none
@return		none
'''
def main():
	the_file = input("What file would you like to load?\n")
	text = load_text(the_file)
	option = input("Your options are 'encode', 'decode', 'caesar_cipher_alphabet',\n'cryptogram_alphabet', and 'keyword_cipher_alphabet'.Choose\nONE of the following options my entering it in EXACTLY how it\nis shown in the quotations. Then press 'enter' to continue.\n" ).upper()
	while option not in ['ENCODE', 'DECODE', 'CAESAR_CIPHER_ALPHABET', 'CRYPTOGRAM_ALPHABET', 'KEYWORD_CIPHER_ALPHABET']:
		option = input("- Please type EXACTLY how it is in the quotations. ").upper()
	if option == "ENCODE":
		text = print(encode(text, cryptogram_alphabet()))
	elif option == "DECODE":
		text = print(decode(text, cryptogram_alphabet()))
	elif option == "CAESAR_CIPHER_ALPHABET":
		number = int(input("Enter an integer to for how much to shift alphabet. ")) 
		text = print(caesar_cipher_alphabet(number))
	elif option == "CRYPTOGRAM_ALPHABET":
		text = print(cryptogram_alphabet())
	else:
		keyword = input("Enter your keyword. ")
		text = print(keyword_cipher_alphabet(keyword))
		
main()
