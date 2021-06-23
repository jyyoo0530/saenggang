from Korpora import Korpora
import os


rawDataList = Korpora.corpus_list()
for key in rawDataList:
    print(key, ": ", rawDataList[key])

target=input("저장할 말 뭉치를 위에서 고르세요: ")
Korpora.fetch(target)
print(os.system("mv ~/Korpora/"+target+"/*.txt ~/PycharmProjects/ginger/localdata/raw/ko/raw"+target+".txt"))
print(os.system("rm -rf ~/Korpora/*"))