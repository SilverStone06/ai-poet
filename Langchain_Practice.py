from langchain_openai import ChatOpenAI

def poem_content(content) :
    
    chat_model = ChatOpenAI()  # api_key 매개변수로 전달

    result = chat_model.invoke(content + "에 대한 시를 써줘.")
    return result