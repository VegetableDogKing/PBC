# 先定義標點符號, 正向字, 負向字的list
punctuation_list = [' ', '.', ',', ':', ';', '?', '!', "'", '"', '-']
positive = ["GOOD", "BEST", "AWESOME", "EXCELLENT", "WONDERFUL"]
negative = ["BAD", "WORST", "STUPID", "SHAME"]


# 定義sting_split這個function來切割句子
# 利用空格以及.,:;?!'"-來切割
# 這邊運用到遞迴因為在切割完後會放入一個list, 要一個一個字看過去能不能再切割
# 直到所有標點符號都看完後再去看每一個字是不是情緒字詞
def string_split(n, word):
    if n <= 9:
        word = word.split(punctuation_list[n])
        for i in word:
            string_split(n+1, i)
    else:
        emotion_judge(word)


# 判斷當前的字是正向字還是負向字
def emotion_judge(word):
    global positive_point
    global negative_point
    for i in positive:
        if word == i:
            positive_point += 1
            break
    for i in negative:
        if word == i:
            negative_point += 1
            break


number = int(input())
answer = []

# 將整個句子轉成大寫方便判斷是不是正向字或負向字
for i in range(number):
    positive_point = 0
    negative_point = 0
    txt = input().upper()
    string_split(0, txt)
    total = positive_point - negative_point
    answer.append(total)

# 輸出答案
for i in range(number):
    if i == 0:
        print(answer[i], end="")
    else:
        print(f',{answer[i]}', end="")
