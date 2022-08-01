import sys

# ‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.

# 예를 들어, “bdppq”를 거울에 비추면 “pqqbd”처럼 나타날 것이다.



#count_num = int(input())


upsideDown = {
    "b" : "d",
    "d" : "b",
    "p" : "q",
    "q" : "p"   
}
for k,y in upsideDown:
    #키의값이 입력되면 밸류의값인 d 가나오게 하고싶었다. 
    #어제 다이얼문제랑 비슷한거같은데... 구글링을 못하니까 힘들다

 sys.stdin = open("_문자열의거울상.txt")
