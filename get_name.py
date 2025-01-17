import os
from cozepy import COZE_CN_BASE_URL
from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  # noqa
import random
import pandas as pd


coze_api_token = ''
coze_api_base = COZE_CN_BASE_URL
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

workflow_id = '7459469705595011112'


# type_list = ['men_in_Chinese', 'women_in_Chinese', 'men_in_Americans', 'women_in_Americans'] 
# type_list = ['1940-1960 in Americans', '1960-1980 in Americans', '1980-2000 in Americans', '2000-2020 in Americans'] 
# type_list = ['Britons', 'Frenchman', 'Germans', 'Russians', 'American', 'Chinese', 'Japanese', 'Koreans', 'Thais ', 'Indians', 'South Africans', 'Iranians', 'Saudis', 'Brazilians']
# type_list = ['white people', 'black people', 'yellow people']
# type_list = ['white people', 'black people', 'yellow people']
type_list = ['celebrity', 'famous villains in history']

			

type_list_str = ""
for i in range(0, len(type_list)-1):
    type_list_str += type_list[i] + ","
type_list_str += type_list[len(type_list)-1]

print("type_list_str:", type_list_str)


def get_name(type_list_str):
    workflow = coze.workflows.runs.create(
        workflow_id=workflow_id,
        parameters={
            "list": type_list_str
        },
    )

    # print("workflow.data", workflow.data.split("```json")[1].split("```")[0])
    return workflow.data.split("```json")[1].split("```")[0].replace("\\n", "").replace("\\", "")


output = get_name(type_list_str)
print("output:", output)



import pandas as pd
# excel_file_path = "C:/Users/12740/Desktop/names/gender.xlsx"
# excel_file_path = "C:/Users/12740/Desktop/names/age.xlsx"
# excel_file_path = "C:/Users/12740/Desktop/names/country.xlsx"
# excel_file_path = "C:/Users/12740/Desktop/names/race.xlsx"
excel_file_path = "C:/Users/12740/Desktop/names/status.xlsx"



df = pd.read_excel(excel_file_path)

count = output.count("Type names")
for i in range(0, count):
    for j in range(0, 5):
        df.iloc[j, i] = output.split("Type names")[i+1].split(",")[j+1].split(":")[1].split("\"")[1]

df.to_excel(excel_file_path, index=False)



print("获取姓名已完成\n")