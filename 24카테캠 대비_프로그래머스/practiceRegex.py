import re

#re.compile(pattern, flag = 0)

#re.search(patter, string, flags)

#re.match(pattern, string, flags)

#re.findall(pattern, string, flag)

#re. sub(pattern, repl, string, count, flags)


pattern = re.compile(r'\w\b+@\w+\.\w+\b')
test_Text = " asdfkasd fdsafsa dongs@naver.com"

email = pattern.findall(test_Text)

for em in email:
    print(em)