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
                  'Column13' : res.get('thal')}


    for i in user_input:
        if(user_input[i] == None):
            user_input[i] = ''
        else:
            user_input[i] = int(user_input[i])

    user_input_dataframe = pd.DataFrame(user_input, index=[0])

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