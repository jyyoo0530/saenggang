from konlpy.tag import Mecab, Okt, Komoran, Hannanum, Kkma
from konlpy.corpus import kolaw
from threading import Thread
import multiprocessing
import datetime
import glob, json, re
import _jpype
import main
import logging

# 0) 기초 정보 생성
basePath: str = main.projectDirectory
rawPath: str = basePath + "/localdata/raw/ko"
outputPath: str = basePath + "/localdata/processed"

# 0-1) raw 파일 리스트 생성
a = glob.glob(rawPath + "/*.*")
i = 1
corpusList: dict = {}
for b in a:
    corpusList[i] = b
    i += 1

# 0-2) preprocess 명령어 리스트
preprocessList: dict = {
    1: "naverMovieRatings"
}

#######추가할 전처리 과정이 있으면 아래에 메서드를 추가한다.#######
# XX) 메써드들..
def preprocess(inputFname: str, outputFname: str, method: str):
    if method == "naverMovieRatings":
        with open(outputFname, 'w', encoding='utf-8') as output, \
                open(inputFname, 'r', encoding='utf-8') as input:
            next(input)
            for line in input:
                _, sentence, label = line.strip().split("\t")
                if not sentence:
                    continue
                else:
                    output.writelines(sentence + "\n")
    logging.info("전처리(" + method + ")가 완료되었습니다.")
    logging.info("다음 위치에 저장합니다 :")
    logging.info(outputFname)
#########################################################


## !!전처리 프로세스 시작!!
# 1) 분석할 말뭉치 선택
for elem in corpusList:
    print(str(elem) + ": " + corpusList[elem])
targetIdx: int = int(input("사용할 말뭉치를 선택하세요 :"))
if targetIdx in corpusList:
    targetTxt = corpusList[targetIdx]
else:
    for elem in corpusList:
        print(str(elem) + ": " + corpusList[elem])
    targetTxt = input("잘못 선택하셨습니다. 사용할 말뭉치를 선택하세요 :")


# 2) 문서 전처리 과정 실행
logging.info("전처리 과정을 선택하세요")
for elem in preprocessList:
    print(str(elem) + ": " + preprocessList[elem])
targetIdx: int = int(input("사용할 전처리 과정을 선택하세요 :"))
if targetIdx in preprocessList:
    targetPreprocess = preprocessList[targetIdx]
else:
    for elem in preprocessList:
        print(str(elem)+": "+preprocessList[elem])
    targetPreprocess = input("잘못 선택하셨습니다. 사용할 전처리 과정을 선택하세요 :")
outputFname=outputPath+"/naverMovieRatings.txt"
preprocess(targetTxt, outputFname, targetPreprocess)
logging.info("완료 되었습니다.")
