from wordcloud import WordCloud
from konlpy.tag import Twitter
from collections import Counter
import json
import nltk
from nltk import regexp_tokenize
text = open('result copy.txt', encoding='utf8').read()
pattern = r'''(?x) [A-Za-z]+'''
tokens_en = regexp_tokenize(text, pattern)
en = nltk.Text(tokens_en)

counts = Counter(dict(en.vocab()))
tags = counts.most_common(1000)

# print(tokens_en)
print(list(map(lambda x: x[0], tags)))

for i in tags:
    print(i[1], i[0])

# open('rr1.txt', 'w', encoding='utf8').write(
#     json.dumps(dicten.vocab(), ensure_ascii=False, indent=4))

exit()

# open으로 txt파일을 열고 read()를 이용하여 읽는다.


twitter = Twitter()

# twitter함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag = []
sentences_tag = twitter.pos(text)

noun_adj_list = []

# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for word, tag in sentences_tag:
    if tag in ['Noun', 'Adjective']:
        noun_adj_list.append(word)


# 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(10000)

# open('rr.txt', 'w', encoding='utf8').write(
#     json.dumps(tags, ensure_ascii=False, indent=4))

# tags = json.load(open('rr.txt', 'r', encoding='utf8'))

# # WordCloud를 생성한다.
# # 한글을 분석하기위해 font를 한글로 지정해주어야 된다. macOS는 .otf , window는 .ttf 파일의 위치를
# # 지정해준다. (ex. '/Font/GodoM.otf')
# wc = WordCloud(font_path='malgun.ttf',
#                background_color="black", max_font_size=60)
# cloud = wc.generate_from_frequencies(dict(tags))


# # 생성된 WordCloud를 test.jpg로 보낸다.
# cloud.to_file('test.jpg')
