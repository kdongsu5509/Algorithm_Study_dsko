import re

text = 'Hello123World'

# 숫자를 찾는 정규 표현식
pattern = re.compile(r'\d+')

# 주어진 문자열에서 숫자를 찾아냅니다.
matches = pattern.findall(text)

# 매칭된 숫자들을 출력합니다.
print(matches)