from gensim.models import Word2Vec, FastText
from glove import Glove
import main, glob

# 0) 기초 정보 생성
basePath: str = main.projectDirectory
processedPath: str = basePath + "/localdata/processed"
modelPath: str = basePath + "/localdata/models/embedding/word"

# 0) 트레이닝셋 리스트
a = glob.glob(processedPath + "/*.*")
i = 1
trainingSetList: dict = {}
for b in a:
    trainingSetList[i] = b
    i += 1

# 0) 사용가능한 기법 리스트
modelList:dict = {
    1: "Word2Vec",
    2: "FastText",
    3: "Glove",
    4: "Swivel"
}





#########################################################
#########################################################
# XX) 메써드들..
def record_userInput(list2search: dict, diag_requestChoice: str, diag_wrongChoice: str):
    for elem in list2search:
        print(str(elem) + ": " + list2search[elem])
    targetIdx: int = int(input(diag_requestChoice))
    if targetIdx in list2search:
        return list2search[targetIdx]
    else:
        for elem in list2search:
            print(str(elem) + ": " + list2search[targetIdx])
        targetIdx: int = int(input(diag_wrongChoice))
        return list2search[targetIdx]


#########################################################
#########################################################




# 1) 모델 오브젝트 생성 2) 모델 사용처
requestTxt="임베딩에 사용할 모델을 선택하세요 :"
re_requestTxt="잘못 선택하셨습니다. 다시 선택 해주세요 :"
targetModel:str = record_userInput(modelList, requestTxt, re_requestTxt)

#2)