import main, glob, re, datetime
from konlpy.tag import Okt, Mecab, Hannanum, Kkma, Komoran

# 0) 기초 정보 생성
basePath = main.projectDirectory

timestampNow = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
preprocessedPath = basePath + "/localdata/preprocessed"
processedPath = basePath + "/localdata/processed"
modelPath = basePath + "/localdata/models"

# 0-1) input 파일 리스트 생성
a = glob.glob(preprocessedPath + "/*.*")
i = 1
inputTxtList: dict = {}
for b in a:
    inputTxtList[i] = b
    i += 1

# 0-2) 실행할 모델 리스트 생성
modelList: dict = {
    1: "okt",
    2: "mecab",
    3: "hannanum",
    4: "kkma",
    5: "komoran"
}
# 0-2-1) 모델별 전처리기능 리스트
oktModuleList: dict = {
    1: "pos",
    2: "nouns",
    3: "morphs",
    4: "phrases",
    5: "normalize"
}
mecabModuleList: dict = {
    1: "pos",
    2: "morphs",
    3: "nouns"
}
hannanumModuleList: dict = {
    1: "analyze",
    2: "pos",
    3: "nouns",
    4: "morphs"
}
kkmaModuleList: dict = {
    1: "nouns",
    2: "pos",
    3: "morphs",
    4: "sentences"
}
komoranModuleList: dict = {
    1: "pos",
    2: "nouns",
    3: "morphs"
}


#######추가할 전처리 과정이 있으면 아래에 메서드를 추가한다.#######
#########################################################
# XX) 메써드들..
def get_tokenizer(targetModel: str):
    global tokenizer
    if targetModel == "komoran":
        tokenizer = Komoran()
    elif targetModel == "okt":
        tokenizer = Okt()
    elif targetModel == "mecab":
        tokenizer = Mecab()
    elif targetModel == "hannanum":
        tokenizer = Hannanum()
    elif targetModel == "kkma":
        tokenizer = Kkma()
    return tokenizer


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


def preprocess_morph(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    def post_processing(tokens):
        results = []
        for token in tokens:
            # 숫자에 공백을 주어서 띄우기
            processed_token = [el for el in re.sub(r"(\d)", r" \1 ", token).split(" ") if len(el) > 0]
            results.extend(processed_token)
        return results

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "okt":
                tokens = tokenizer.morphs(sentence)
            elif targetModel == "mecab":
                tokens = tokenizer.morphs(sentence)
            elif targetModel == "hannanum":
                tokens = tokenizer.morphs(sentence)
            elif targetModel == "kkma":
                tokens = tokenizer.morphs(sentence)
            elif targetModel == "komoran":
                tokens = tokenizer.morphs(sentence)
            tokenized_sent = ' '.join(post_processing(tokens))
            outputData.writelines(tokenized_sent + '\n')


def preprocess_pos(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "okt":
                tokens = tokenizer.pos(sentence)
            elif targetModel == "mecab":
                tokens = tokenizer.pos(sentence)
            elif targetModel == "hannanum":
                tokens = tokenizer.pos(sentence)
            elif targetModel == "kkma":
                tokens = tokenizer.pos(sentence)
            elif targetModel == "komoran":
                tokens = tokenizer.pos(sentence)
            for items in tokens:
                outputData.write(' '.join(str(s) for s in items) + '\n')


def preprocess_nouns(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "okt":
                tokens = tokenizer.nouns(sentence)
            elif targetModel == "mecab":
                tokens = tokenizer.nouns(sentence)
            elif targetModel == "hannanum":
                tokens = tokenizer.nouns(sentence)
            elif targetModel == "kkma":
                tokens = tokenizer.nouns(sentence)
            elif targetModel == "komoran":
                tokens = tokenizer.nouns(sentence)
            for items in tokens:
                outputData.write(' '.join(str(s) for s in items) + '\n')

def preprocess_phrases(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "okt":
                tokens = tokenizer.phrases(sentence)
            for items in tokens:
                outputData.write(' '.join(str(s) for s in items) + '\n')

def preprocess_normalize(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "okt":
                tokens = tokenizer.normalize(sentence)
            for items in tokens:
                outputData.write(' '.join(str(s) for s in items) + '\n')

def preprocess_analyze(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "hannanum":
                tokens = tokenizer.analyze(sentence)
            for items in tokens:
                outputData.write(' '.join(str(s) for s in items) + '\n')

def preprocess_sentences(targetModel: str, targetTxt: str, outputTxt: str):
    tokenizer = get_tokenizer(targetModel)

    with open(targetTxt, 'r', encoding='utf-8') as inputData, \
            open(outputTxt, 'w', encoding='utf-8') as outputData:
        for line in inputData:
            sentence = line.replace('\n', '').strip()
            if targetModel == "kkma":
                tokens = tokenizer.sentences(sentence)
            for items in tokens:
                outputData.write(' '.join(str(s) for s in items) + '\n')

#########################################################
#########################################################


##### 아래부터는 프로세스
# 모델선택 -> 학습여부 확인, -> 학습할꺼면 학습 아니면 학습안하고 스킵
# 1) 모델 선택
requestTxt = "사용할 모델을 선택하세요 :"
re_requestTxt = "잘못 선택하셨습니다. 사용할 모델을 선택하세요 :"
targetModel: str = record_userInput(modelList, requestTxt, re_requestTxt)

# 2) 모듈 선택
targetModule: str = ""
requestTxt = "사용할 모듈을 선택하세요 :"
re_requestTxt = "잘못 선택하셨습니다. 사용할 모듈을 선택하세요 :"
if targetModel == "okt":
    targetModule = record_userInput(oktModuleList, requestTxt, re_requestTxt)
elif targetModel == "mecab":
    targetModule = record_userInput(mecabModuleList, requestTxt, re_requestTxt)
elif targetModel == "hannanum":
    targetModule = record_userInput(hannanumModuleList, requestTxt, re_requestTxt)
elif targetModel == "kkma":
    targetModule = record_userInput(kkmaModuleList, requestTxt, re_requestTxt)
elif targetModel == "komoran":
    targetModule = record_userInput(komoranModuleList, requestTxt, re_requestTxt)

# 2) 전처리할 텍스트 선택
requestTxt = "전처리를 시행할 말뭉치를 선택하세요 :"
re_requestTxt = "잘못 선택하셨습니다. 말뭉치를 다시 선택하세요 :"
targetTxt = record_userInput(inputTxtList, requestTxt, re_requestTxt)

# 3) 전처리 시행
print("")
outputTxt = processedPath + "/" + targetModel + "_" + targetModule + "_" + timestampNow + ".txt"
if targetModule == "pos":
    preprocess_pos(targetModel, targetTxt, outputTxt)
elif targetModule == "nouns":
    preprocess_nouns(targetModel, targetTxt, outputTxt)
elif targetModule == "morphs":
    preprocess_morph(targetModel, targetTxt, outputTxt)
elif targetModule == "phrases":
    preprocess_phrases(targetModel, targetTxt, outputTxt)
elif targetModule == "normalize":
    preprocess_normalize(targetModel, targetTxt, outputTxt)
elif targetModule == "analyze":
    preprocess_analyze(targetModel, targetTxt, outputTxt)
elif targetModule == "sentences":
    preprocess_sentences(targetModel, targetTxt, outputTxt)
