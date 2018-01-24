import re
import pyperclip

text = str(pyperclip.paste())

phoneNumber_regex = re.compile(r'\+*\d{2}-\d{10}')
email_regex = re.compile(r'''(
	[._%+-a-zA-z0-9]+
	@
	[a-zA-z0-9.-]+
	\.[a-zA-Z]{2,4}
	)''', re.VERBOSE)


phone_list = []
email_list = []
for numbers in phoneNumber_regex.findall(text):
	phone_list.append(numbers)

for email in email_regex.findall(text):
	email_list.append(email)

print(email_list)
print(phone_list)


