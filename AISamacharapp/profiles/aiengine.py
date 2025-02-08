import os
from openai import OpenAI
#import config
from django.conf import settings

github_token=settings.GITHUB_API_KEY
# Load API key from environment variable

# GitHub Developer API configuration
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

client = OpenAI(
    base_url=endpoint,
    api_key=github_token,
)

def generateChatResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "Your name is Karabo. You are a helpful assistant."})

    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)

    response = client.chat.completions.create(
            messages=messages,
            temperature=1.0,
            top_p=1.0,
            max_tokens=1000,
            model=model_name
        )

    try:
        answer = response.choices[0].message.content.replace('\n', '<br>')
    except:
        answer = 'Oops you beat the AI, try a different question, if the problem persists, come back later.'

    return answer