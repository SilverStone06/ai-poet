from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#export OPENAI_API_KEY = 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

def poet_content(content) :
    load_dotenv()
    chat_model = ChatOpenAI(api_key = "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")  # api_key 매개변수로 전달

    result = chat_model.invoke(content + "에 대한 시를 써줘.")
    return result
    #print(result)
