import pandas as pd

def collectData(res):

    user_input = {'Column1' : res.get('age'),
                  'Column2' : res.get('sex'),
                  'Column3' : res.get('chest-pain'),
                  'Column4' : res.get('rbp'),
                  'Column5' : res.get('sc'),
                  'Column6' : res.get('fbs'),
                  'Column7' : res.get('recg'),
                  'Column8' : res.get('mhra'),
                  'Column9' : res.get('eia'),
                  'Column10' : res.get('stdie'),
                  'Column11' : res.get('pests'),
                  'Column12' : res.get('nomv'),
                  'Column13' : res.get('thal'),
                  'Column3_1' : 0,
                  'Column3_2' : 0,
                  'Column3_3' : 0,
                  'Column3_4' : 0,
                  'Column7_0' : 0,
                  'Column7_1' : 0,
                  'Column7_2' : 0,
                  'Column11_1' : 0,
                  'Column11_2' : 0,
                  'Column11_3' : 0}
    print(user_input)


    for i in user_input:
        if((i == 'Column1') or (i == 'Column2') or (i == 'Column3')):
            if(user_input[i] != ''):
                user_input[i] = int(user_input[i])

    user_input_dataframe = pd.DataFrame(user_input, index=[0])


    return(processData(user_input_dataframe))

def processData(datas):
    #Drop 13 dan 12 karena di data train kami tidak digunakan

    #Mendapatkan mean dan modus dari data
    data_train = pd.read_csv('tubes2_HeartDisease_train.csv')
    replacer = processTrain(data_train)
    print(replacer)



    #Melakukan data cleansing
    j = 0
    for i in datas:
        if (datas[i].empty):
            if (type(replacer[i]) != str):
                datas[i] = replacer[j].item()
            else:
                datas[i] = replacer[j]

        j = j + 1


    #Melakukan data drop
    del(datas['Column12'])
    del(datas['Column13'])
    print(datas)


    c3 = int(datas['Column3'])
    c7= int(datas['Column7'])
    c11 = int(datas['Column11'])

    datas['Column3_{}'.format(c3)] = 1
    datas['Column7_{}'.format(c7)] = '1'
    datas['Column11_{}'.format(c11)] = '1'

    datas.drop(['Column3'],axis=1, inplace=True)
    datas.drop(['Column7'],axis=1, inplace=True)
    datas.drop(['Column11'],axis=1, inplace=True)



    return(datas)


def dropNanOnCol(df, colName) :
    listDel = []
    for index, row in df.iterrows():
        if (row[colName] == "?") :
            listDel.append(index)
    return df.drop(listDel)

def countNanRow(df, rowNum) :
    count = 0
    for column in df :
        if (df.loc[rowNum][column] == "?") :
            count += 1
    return count


def processTrain(data_train):
    threshold = 8

    listDel = []
    for index, row in data_train.iterrows():
        if (countNanRow(data_train, index) > threshold) :
            listDel.append(index)

    data_train_clean = data_train.drop(listDel)


    replacer = []

    changeWithMean = ['Column4', 'Column5', 'Column8', 'Column10', 'Column12']
    for column in data_train_clean:
        cleanData = dropNanOnCol(data_train_clean, column)
        if (column in changeWithMean) :
            replacer.append(cleanData.median()[column])
        #         replacer.append(np.asarray(cleanData.loc[:,column], dtype=np.float).mean())
        else :
            replacer.append(cleanData.mode()[column])

    # special case
    replacer[10] = replacer[10][0]

    return(replacer)