# 先定義標點符號, 正向字, 負向字, hyper-parameter的list
punctuation_list = [' ', '.', ',', ':', ';', '?', '!', "'", '"', '-']
positive = ["GOOD", "BEST", "AWESOME", "EXCELLENT", "WONDERFUL"]
negative = ["BAD", "WORST", "STUPID", "SHAME"]
check_list = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]


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
    global positive_count
    global negative_count
    for i in positive:
        if word == i:
            positive_count += 1
            break
    for i in negative:
        if word == i:
            negative_count += 1
            break


# 每一個hyper-parameter都去算一遍看最好的hyper-parameter以及正確數量
def check_correctness(count, correct, number):
    best = 0
    best_set = 0
    for i in range(7):
        correctness = 0
        for j in range(number):
            if count[j][0] * check_list[i][0] - count[j][1] * check_list[i][1] >= 0:
                judge = 1
            else:
                judge = 0

            if judge == correct[j]:
                correctness += 1
        if correctness > best:
            best = correctness
            best_set = i
    return best_set, best


number = int(input())
count = []
answer = []

# 將整個句子轉成大寫方便判斷是不是正向字或負向字
for i in range(number):
    positive_count = 0
    negative_count = 0
    txt = input().upper()
    string_split(0, txt)
    tmp = []
    tmp.append(positive_count)
    tmp.append(negative_count)
    count.append(tmp)

correct = input().split(',')
for i in range(number):
    correct[i] = int(correct[i])

best_set, correctness = check_correctness(count, correct, number)
print(f'{check_list[best_set][0]},{check_list[best_set][1]},{correctness}')
