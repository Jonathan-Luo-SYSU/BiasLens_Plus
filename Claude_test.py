import os
from cozepy import COZE_CN_BASE_URL
from cozepy import Coze, TokenAuth, Stream, WorkflowEvent, WorkflowEventType  


coze_api_token = ''
coze_api_base = COZE_CN_BASE_URL
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)

workflow_id = '7460925379906584583'

def handle_workflow_iterator(stream: Stream[WorkflowEvent]):
    for event in stream:
        if event.event == WorkflowEventType.MESSAGE:
            print("got message", event.message)
        elif event.event == WorkflowEventType.ERROR:
            print("got error", event.error)
        elif event.event == WorkflowEventType.INTERRUPT:
            handle_workflow_iterator(
                coze.workflows.runs.resume(
                    workflow_id=workflow_id,
                    parameters={
                        "question": question_str
                    },
                    event_id=event.interrupt.interrupt_data.event_id,
                    resume_data="hey",
                    interrupt_type=event.interrupt.interrupt_data.type,
                )
            )

question_str = input("请输入测试数据：")
handle_workflow_iterator(
    coze.workflows.runs.stream(
        workflow_id=workflow_id,
        parameters={
            "question": question_str
        },
    )
)

