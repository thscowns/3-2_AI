import math
import re

pDic ={}    # postive로 나온 word를  {word: 개수} 로 저장하는 dictionary
nDic = {}   # negative로 나온 word를  {word: 개수} 로 저장하는 dictionary
pos_num = 0 # positive인 review의 개수를 저장하는 변수
neg_num = 0 # negative인 review의 개수를 저장하는 변수
pos_word_num = 0    #positive인 review에서 나온 모든 word 개수의 합을 저장하는 변수
neg_word_num = 0    #negative인 review에서 나온 모든 word 개수의 합을 저장하는 변수

def learning() :
    global pDic,nDic,pos_num,neg_num,pos_word_num,neg_word_num
    f = open("ratings_train.txt",'rt',encoding ='UTF8')
    total = 0
    line = f.readline()
    #for i in range(1000):
    while True:
        line = f.readline()
        total += 1
        if not line : break
        count_word(line)
        print(total)
    #print(pos_num,neg_num)
    for n in pDic.values():
        pos_word_num += n
    for n in nDic.values():
        neg_word_num += n
    #print(pos_word_num,neg_word_num)

'''
pDic, nDic을 채우기위한 함수
'''
def count_word(line):
    global pDic,nDic,pos_num,neg_num
    doc = line.split("\t")
    #word = doc[1].split(" ")   # line을 띄어쓰기로 나눈 list
    p = doc[2][0]
    word = re.findall(r"[\w']+",doc[1]) # line 을 모든 특수문자에 대해 나눈 list
    if (p == '1'):
        pos_num += 1
    else :
        neg_num += 1
    for i in word :
        if (p == '1'):
            if i in pDic:
                pDic[i] += 1
            else :
                pDic[i] = 1
        else :
            if i in nDic:
                nDic[i] += 1
            else :
                nDic[i] = 1
    #print(p)

def test(path) :
    global pDic,nDic
    f = open(path,'rt',encoding ='UTF8')

    f2 = open("ratings_result.txt",'w',encoding ='UTF8')
    line = f.readline()
    f2.writelines(line)
    #for i in range(1000):
    #sum = 0
    n = 0
    while True:
        line = f.readline()
        if not line : break
        n += 1
        line =line.rstrip('\n')+ valid(line)+'\n'
        f2.writelines(line)
        #print(valid(line))
        #sum += valid(line)
    #print(sum,n)

def valid(line):
    global pos_num,neg_num,pos_word_num,neg_word_num
    doc = line.split("\t")
    #word = doc[1].split(" ")
    word = re.findall(r"[\w']+", doc[1]) # line을 모든 특수문자로 나눈 list
    p = pos_num/(pos_num + neg_num) #
    #print(word)
    prob_P = math.log(p)
    prob_N = math.log(1-p)
    for i in word:
        a = 1
        b = 1
        if i in pDic :
            a = pDic[i]
        if i in nDic:
            b = nDic[i]
        prob_P += math.log(a / pos_word_num)
        prob_N += math.log(b / pos_word_num)
        '''if (a!=0 and b!=0):                      word가 pDic,nDic 둘중 한개라도 한번도 나오지 않은 단어였다면
            prob_P += math.log(a / pos_word_num)    계산하지 않는다.
            prob_N += math.log(b / pos_word_num)'''
        #print(prob_P,prob_N,doc[2])
    '''if((prob_N <= prob_P and doc[2][0] == '1') or (prob_N > prob_P and doc[2][0] == '0')):
        return 1
    else :
        return 0
    '''
    if (prob_P >= prob_N) :
        return '1'
    else :
        return '0'




learning()
test("ratings_test.txt")
