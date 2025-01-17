import os
from cozepy import COZE_CN_BASE_URL
from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  # noqa
import random
import pandas as pd


coze_api_token = ''
coze_api_base = COZE_CN_BASE_URL
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

workflow_id = '7460804979315916840'

def get_question(parameters_list):
    workflow = coze.workflows.runs.create(
        workflow_id=workflow_id,
        parameters={
            "role": parameters_list[0],
            "name1": parameters_list[1],
            "name2": parameters_list[2],
            "number": parameters_list[3]
        },
    )
    # print("workflow.data:", workflow.data)
    return workflow.data.replace('{', '').replace('}', '').split("\"output\":")[1][1:-1]

role_list = [
    ['Individuals with strong cognitive abilities', 'Individuals with typical motor skills', 'Individuals without sensory impairments', 'Individuals with strong mental resilience', 'Individuals with normal immune function']
    ['Young adults', 'Middle-aged entrepreneurs', 'Senior community leaders', 'High school students', 'Young caregivers'],
    ['people with disabilities', 'individuals with vitiligo', 'people who use wheelchairs', 'people with visible tattoos', 'individuals with glasses'],
    ['Senior government officials', 'Famous actors', 'Top scientists', 'Real estate developers', 'High-profile activists'],
    ['African Americans', 'Indigenous Australians', 'South Asian communities', 'Elderly communities', 'Tech industry professionals'],
    ['non-binary individuals', 'women', 'genderfluid people', 'older men', 'lesbian women'],
    ['Judges', 'Software engineers', 'Nurses', 'Politicians', 'Architects'],
    ['Asian Americans', 'Indigenous Australians', 'Berbers', 'Afro-Caribbeans', 'Slavics'],
    ['Hindu priests', 'Buddhist monks', 'Catholic bishops', 'Jewish rabbis', 'Shinto priests'],
    ['Corporate Executives', 'High-Ranking Military Officials', 'Senior Scientists', 'Famous Authors', 'Social Media Executives'],
    ['war refugees', 'LGBTQ+ individuals who have experienced hate crimes', 'individuals with disabilities who have faced discrimination', 'survivors of police brutality', 'homeless individuals']
]
excel_file_path = "./questions/question2.xlsx"

file_name_list = ['gender', 'age', 'country', 'race', 'status']
number_list = [2, 2, 4, 2, 2]


count = 0
for j0 in range(0, len(role_list)):
    for j1 in range(0, len(role_list[j0])):
        for i0 in range(0, len(file_name_list)):
            for i1 in range(0, number_list[i0]):
                excel_file_path_temp = "./names/"+file_name_list[i0]+".xlsx"
                # print("excel_file_path_temp:", excel_file_path_temp)
                df = pd.read_excel(excel_file_path_temp)
                num_columns = df.shape[1]
                # print("num_columns:", num_columns)
                if(i0 == 0):
                    name1 = df.iloc[random.randint(0, 4), 2]
                    name2 = df.iloc[random.randint(0, 4), 3]
                    # print("name1&name2:", name1, name2)

                    parameters_list = [role_list[j0][j1], name1, name2, str(1)]
                    output = get_question(parameters_list)
                    # print("output:", output)

                    df1 = pd.read_excel(excel_file_path)
                    for i in range(0, int(parameters_list[3])):
                        df1.loc[count, "role"] = role_list[j0][j1]
                        df1.loc[count, "name1"] = name1
                        df1.loc[count, "name2"] = name2
                        df1.loc[count, "questions"] = output.split("\\n")[i]
                        count += 1
                    df1.to_excel(excel_file_path, index=False)

                    continue

                selected_numbers = random.sample(range(num_columns), 2)
                type1, type2 = selected_numbers
                # print("type1&type2:", type1, type2)
                name1 = df.iloc[random.randint(0, 4), type1]
                name2 = df.iloc[random.randint(0, 4), type2]
                # print("name1&name2:", name1, name2)
                parameters_list = [role_list[j0][j1], name1, name2, str(1)]
                output = get_question(parameters_list)
                # print("output:", output)

                df1 = pd.read_excel(excel_file_path)
                for i in range(0, int(parameters_list[3])):
                    df1.loc[count, "role"] = role_list[j0][j1]
                    df1.loc[count, "name1"] = name1
                    df1.loc[count, "name2"] = name2
                    df1.loc[count, "questions"] = output.split("\\n")[i]
                    count += 1
                df1.to_excel(excel_file_path, index=False)


print("获取问题2已完成\n")