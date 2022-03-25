import regex
import pypinyin
import random
def solitaire(firstPinyin,firstHanzi):
    pinyin = r'\b[a-z]*[āáǎàōóǒòêēéěèīíǐìūúǔùǖǘǚǜüńňǹɑɡ]+[a-z]*\b'
    characters = r"\p{han}+(，?\p{han})+"
    words = []
    f = open("chengyu_utf8.txt", encoding='utf-8')
    lines = f.readlines()
    i = 0
    while i < (len(lines)):
        line = random.choice(lines)
        #findall()方法用于在整个字符串中搜索所有符合正则表达式的字符串，并以列表的形式返回。
        pinyinList = regex.findall(pinyin, line) 
        #search()方法找到行首的成语并添加到words组里 
        word = regex.search(characters, line).group()
        if not pinyinList:
            i += 1
            continue
        firstChar = pinyinList[0]
        lastChar = pinyinList[len(pinyinList) - 1]
        firstChinese = word[0]
        lastChinese =word[len(word) - 1]
        if (firstChar == firstPinyin and firstChinese != firstHanzi and word not in words):
            words.append(word)
            firstPinyin = lastChar
            firstHanzi = lastChinese
            i = -1
        i += 1
        if (len(words) >= 10):
            break
    words.append("接龙完成")
    return words

if __name__ == "__main__":
    word = "山崩地摧"
    firstPinyin = pypinyin.pinyin(word)[len(word) - 1][0]
    firstHanzi = word[len(word)-1]
    words = solitaire(firstPinyin,firstHanzi)
    words.insert(0, word)
    print(words)