from lxml import html
import requests

word = 'sword'
soundsLike = 'ken'
url = 'https://www.merriam-webster.com/dictionary/' + word + '#examples/'
page = requests.get(url)
tree = html.fromstring(page.content)
#This will create a list of sentences:
sentences = tree.xpath('//span[@class="ex-sent  t no-aq sents"]/text()')
wordInSentence = tree.xpath('//em[@class="mw_t_it"]/text()')
cleanedSentences = []
firstPart = []
secondPart = []
for x in sentences:
    x = x.replace('\n', '')
    x = x.strip()
    cleanedSentences.append(x)

print(cleanedSentences)


for y in cleanedSentences:
    if cleanedSentences.index(y) is 0:
        firstPart.append(y)
    elif cleanedSentences.index(y) % 2 is 0:
        firstPart.append(y)
    else:
        secondPart.append(y)

print(firstPart)
print(wordInSentence)
print(secondPart)

for z in range(0, len(cleanedSentences) - 1):
    #print(soundsLike + ' ' + str(wordInSentence[z]) + ' ' + str(secondPart[z]))
    #print(str(firstPart[z]) + ' ' + str(wordInSentence[z]) + ' ' + soundsLike)
    #print(cleanedSentences[z] + ' ' + str(wordInSentence[z]) + ' ' + cleanedSentences[z+1])
    alpha = (soundsLike + ' ' + str(wordInSentence[z]) + ' ' + cleanedSentences[z + 1])
    print(alpha)
    beta = (cleanedSentences[z] + ' ' + str(wordInSentence[z]) + ' ' + soundsLike)
    if beta[0].isupper() is True:
        print(beta)