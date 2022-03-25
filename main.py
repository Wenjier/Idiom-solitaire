import pypinyin
import turtle as t
import draw
from solvtion import solitaire

if __name__ == "__main__":
    word = "山崩地裂"
    firstPinyin = pypinyin.pinyin(word)[len(word) - 1][0]
    firstHanzi = word[len(word)-1]
    words = solitaire(firstPinyin,firstHanzi)
    words.insert(0, word)    
    draw.drawAll(words)
    t.done()
 