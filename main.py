from keys import OpenAI_API
from openai import OpenAI
import pypdf


client = OpenAI(api_key=OpenAI_API)


def get_prompt() -> str:
    return 'Imagine writing a pdf about a topic using easy and understandable words with no complex words.\n \
            After writing the table of content convert all the content into a dictonary .\n \
            return only the dictionary.\
            The topic is \n'


def table_of_content_generator(text: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": get_prompt()+text}
        ]
    )
    return response.choices[0].message.content


def pdf_generator():
    Table_of_Contents = table_of_content_generator("Life of an Engineer")

    
