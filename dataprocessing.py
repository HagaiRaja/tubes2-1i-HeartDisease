import pandas as pd
import numpy as np

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


    replacer = [54, 1, 4, 130, 225, 0, 0, 140, 0, 1, 2, 0, 3]

    j = 0

    for i in user_input:
        if((i == 'Column1') or (i == 'Column2')):
            if(user_input[i] == '' or user_input[i] == None):
                user_input[i] = np.int64(replacer[j])
            else:
                user_input[i] = np.int64(int(user_input[i]))
        elif((i == 'Column4') or (i == 'Column5') or (i == 'Column6') or (i == 'Column8') or (i == 'Column9') or (i == 'Column10')):
            if(user_input[i] == '' or user_input[i] == None):
                user_input[i] = np.float64(replacer[j])
            else:
                user_input[i] = np.float64(float(user_input[i]))

        else:
            if(user_input[i] == '' or user_input[i] == None):
                user_input[i] = np.uint8(replacer[j])
            else:
                user_input[i] = np.uint8(int(user_input[i]))

        j = j + 1

    user_input_dataframe = pd.DataFrame(user_input, index=[0])


    return(processData(user_input_dataframe))

def processData(datas):
    #Drop 13 dan 12 karena di data train kami tidak digunakan

    #Mendapatkan mean dan modus dari data

    #Melakukan data drop
    del(datas['Column12'])
    del(datas['Column13'])


    datas['Column3_{}'.format(datas['Column3'][0])] = 1
    datas['Column7_{}'.format(datas['Column7'][0])] = 1
    datas['Column11_{}'.format(datas['Column11'][0])] = 1

    datas.drop(['Column3'],axis=1, inplace=True)
    datas.drop(['Column7'],axis=1, inplace=True)
    datas.drop(['Column11'],axis=1, inplace=True)



    return(datas)