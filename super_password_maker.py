import hashlib
'''
Super password maker using sha256
1) this app changes some sha256 chars of yor key
'''
User_key= input("Enter your Key: ")

def get_lenth():
	global lenth
	lenth= int(input("Enter lenth of your password (max lenth is 64)"))
	

	if lenth<=8 or lenth>64:
		print("lenth should greater than 8")
		get_lenth()
	elif lenth== None:
		lenth=64	

def func1(Key):

	global sha256_key

	Key= str(Key)

	sha256_key= hashlib.sha256()

	sha256_key.update(Key.encode("utf-8"))	

	sha256_key= str(sha256_key.hexdigest())
	#ascii is correct but we cant use it for variable's name

	#this ascii number is our "for" loop range
	ascy_for= ord(sha256_key[0])

	salt_list= "!%()?†‰Õ{®^&*®µ>ÿ¥™£Æíá|Ö$~}_<€Ø-æ+ßþ@#œ"

	for i in range(ascy_for):

		int_of_i= i
		
		mod_i_10= i % 10

		i= str(i)

		half_of_ascy= ascy_for/2

		#after this line is incomprehensible:)
		if int_of_i <= half_of_ascy:
			pass_index= (ord(i[-1])) % 10
			salt_index= (ord(i[-1])) % 10
			sha256_key = sha256_key.replace(sha256_key[pass_index], salt_list[salt_index])
		else :
			pass_index= ((ord(i[0]))**mod_i_10) % 10
			salt_index= ((ord(i[0]))**mod_i_10) % 10
			sha256_key = sha256_key.replace(sha256_key[-1*pass_index], salt_list[-1*salt_index])

		#return sha256_key
get_lenth()
func1(User_key)

print(sha256_key[:lenth])
