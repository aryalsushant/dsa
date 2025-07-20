"""

"""
def remove_char(s, char):
	if s == "":
		return ""
	if s[0]== char:
		return remove_char(s[1:],char)
	else:
		return s[0]+ remove_char(s[1:], char)

s = "xaxbxc"
char = "x"
print(remove_char(s, char))  # Output: 'abc'
