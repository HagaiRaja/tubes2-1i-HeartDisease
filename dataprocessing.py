import pandas as pd

def collectData(res):
    user_input = {'Column1' : res.age,
                  'Column2' : res.sex,
                  'Column3' : res.chest-pain,
                  'Column4' : res.rbp,
                  'Column5' : res.sc,
                  'Column6' : res.fbs,
                  'Column7' : res.recg,
                  'Column8' : res.mhra,
                  'Column9' : res.eia,
                  'Column10' : res.stdie,
                  'Column11' : res.pests,
                  'Column12' : res.nomv,
                  'Column13' : res.thal}

    user_input_dataframe = pd.DataFrame.from_dict(user_input)

    return(user_input_dataframe)

def processData(datas):
    #Drop 13 dan 12 karena di data train kami tidak digunakan
    del(datas['Column12'])
    del(datas['Column13'])

    #Mendapatkan mean dan modus dari data
    data_train = pd.read_csv('tubes2_HeartDisease_train.csv')
    changeWithMean = ['Column4', 'Column5', 'Column8', 'Column10']

    #Melakukan data cleansing
    for column in datas:
        if(datas[column] == ''):
            if (column in changeWithMean):
                datas[column] = data_train[column].median()
            else:
                datas[column] = data_train[column].mode()

    #Melakukan data drop
    datas = pd.concat([datas,pd.get_dummies(datas['Column3'], prefix='Column3')],axis=1)
    datas = pd.concat([datas,pd.get_dummies(datas['Column3'], prefix='Column7')],axis=1)
    datas = pd.concat([datas,pd.get_dummies(datas['Column3'], prefix='Column11')],axis=1)

    datas.drop(['Column3'],axis=1, inplace=True)
    datas.drop(['Column7'],axis=1, inplace=True)
    datas.drop(['Column11'],axis=1, inplace=True)

    return(datas)