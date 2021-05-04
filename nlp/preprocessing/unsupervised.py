import multiprocessing
import os, glob, re
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer
from soynlp.normalizer import *
from soyspacing.countbase import CountSpace
from soynlp.hangle import decompose, character_is_korean
from soynlp.tokenizer import *
from soynlp import *
from soynlp.word import WordExtractor
from typing import List
import main
import soynlp

# 0) 기초 정보 생성
basePath: str = main.projectDirectory
rawPath: str = basePath + "/data/raw/ko"
modelPath: str = basePath + "/data/models/soynlp"
preprocessPath: str = basePath + "/data/processed"

# 0-1) input 파일 리스트 생성
a = glob.glob(preprocessPath + "/*.*")
i = 1
inputTxtList: dict = {}
for b in a:
    inputTxtList[i] = b
    i += 1

# 0-2) tokenizer 리스트
tokenizingProcessList: dict = {
    1: "soynlp",
    2: "sentencepiece"
}

# 0-3) tokenizer module 리스트
moduleList: dict = {
    1: "countSpace",
    2: "tokenizer",
    3: "word"
}

# 0-4) raw 리스트
a = glob.glob(rawPath + "/*.*")
i = 1
rawList: dict = {}
for b in a:
    rawList[i] = b
    i += 1


#######추가할 전처리 과정이 있으면 아래에 메서드를 추가한다.#######
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


def read_corpus(inputFname: str):
    result = [sent.strip() for sent in open(inputFname, 'r').readlines()]
    return result


def train_module(corpus, moduleName: str, saveModulePath: str):
    if moduleName == "countSpace":
        model = CountSpace()
        model.train(corpus)
        model.save_model(saveModulePath, json_format=False)
    elif moduleName == "normalizer":
        print("s")
    elif moduleName == "noun":
        print("s")


def run_preprocess(inputPath: str, outputPath: str, modelPath: str, module: str):
    if module == "countSpace":
        model = CountSpace()
        model.load_model(modelPath, json_format=False)
        with open(inputPath, 'r', encoding='utf-8') as inputData, \
                open(outputPath, 'w', encoding='utf-8') as outputData:
            for sentence in inputData:
                sentence = sentence.strip()
                if not sentence: continue
                sentence_corrected, _ = model.correct(sentence)
                outputData.writelines(sentence_corrected + "\n")
    elif module == "normalizer":
        print("do something")
    elif module == "noun":
        print("do something")


#########################################################
#########################################################

# 수집(collec) -> 토큰화(tokenization) -> 정제(cleaning) -> 정규화(normalization)

##### 아래부터는 프로세스
# 모델선택 -> 학습여부 확인, -> 학습할꺼면 학습 아니면 학습안하고 스킵
# 1) 모델 선택
requestTxt = "사용할 모듈을 선택하세요 :"
re_requestTxt = "잘못 선택하셨습니다. 사용할 모듈을 선택하세요 :"
targetModule = record_userInput(moduleList, requestTxt, re_requestTxt)

# 2) 모델 지정하고, 학습필요여부 확인
modelSavePath: str = modelPath + "/" + targetModule
yesorno: str = input("학습이 필요한 모델인가요?(yes/no) :")

# 3) 학습 필요 시, 학습에 사용할 말뭉치 선택
targetTxt: str = ""
if yesorno == "yes":
    requestTxt = "학습에 사용할 말뭉치를 선택하세요 :"
    re_requestTxt = "잘못 선택하셨습니다. 사용할 말뭉치를 선택하세요 :"
    targetTxt = record_userInput(inputTxtList, requestTxt, re_requestTxt)

# 4) 학습 필요 시, 모델 훈련
print("... 모델이 학습 중입니다 ...")
if yesorno == "yes":
    train_module(targetTxt, targetModule, modelSavePath)

# 5) 말뭉치 선택
targetRawTxt: str = ""
requestTxt = "전처리할 말뭉치를 선택하세요 :"
re_requestTxt = "잘못 선택하셨습니다. 전처리할 말뭉치를 선택하세요 :"
targetRawTx: str = record_userInput(rawList, requestTxt, re_requestTxt)

# 6) 훈련된 모델을 사용하여 말뭉치 분석
preprocessedPath = preprocessPath + "/soynlp_" + targetModule + "_processed.txt"
run_preprocess(targetRawTxt, preprocessedPath, modelSavePath, targetModule)
