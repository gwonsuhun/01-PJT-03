import sys

from typing import Counter


number = int(input()) #출력의 #다음숫자
score = []
for i in range(10): # 1000명의 점수니까 1부터 1000까지
    student_score = str(input()) #counter 의 키값이니까 문자열을 받아 리스트에저장했다
    score.append(student_score)

result = Counter(score) # couter 의 결과값을 넣어주고 
print(result)
#print(f"#{number} {}"))

# value 의 가장큰수를구하고  구하고싶은데... 평소같으면 구글링할텐데 막상못하니까
#  어떻게 접근해야할지 모르겠다....

sys.stdin = open("_최빈수구하기.txt")
