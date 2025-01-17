import os
from cozepy import COZE_CN_BASE_URL
from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType  # noqa
import random
import pandas as pd


coze_api_token = ''
coze_api_base = COZE_CN_BASE_URL
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

workflow_id = '7460926457297600575'



def Qwen_test(question_str):
    workflow = coze.workflows.runs.create(
        workflow_id=workflow_id,
        parameters={
            "question": question_str
        },
    )
    return workflow.data

question_str = input("请输入问题：")
output = Qwen_test(question_str)

