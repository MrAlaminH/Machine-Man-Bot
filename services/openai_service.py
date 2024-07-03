import openai
from config import OPENAI_API_KEY, OPENAI_API_BASE

openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE

async def generate_image(prompt, model_name):
    try:
        response = await openai.Image.acreate(
            model=model_name,
            prompt=prompt,
            n=1,
            size="512x512",
            response_format="url",
        )
        return response['data'][0]['url'] if response['data'] else None
    except Exception as e:
        print(f'Error in generate_image: {e}')
        return None

async def generate_text(messages, model_name):
    try:
        completion = await openai.ChatCompletion.acreate(
            model=model_name,
            messages=messages,
            max_tokens=4096,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return completion.choices[0]['message']['content']
    except Exception as e:
        print(f'Error in generate_text: {e}')
        return None