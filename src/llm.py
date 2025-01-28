import os
from litellm import completion

def main():    
    os.environ["GEMINI_API_KEY"] = ""
    messages1 = [{"role": "user", "content": "What is Chat Gpt ?"}]
    model1="gemini/gemini-2.0-flash-exp"

    response = completion(model=model1, messages=messages1)


    print(response['choices'][0]['message']['content'])
