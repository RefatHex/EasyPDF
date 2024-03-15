import json
import time
from keys import OpenAI_API
from openai import OpenAI
import pypdf

client = OpenAI(api_key=OpenAI_API)


def get_table_of_content_prompt() -> str:
    return 'Imagine writing a pdf about a topic using easy and understandable words with no complex words.\n \
            After writing the table of content convert all the content into a dictionary.\n \
            return only the dictionary.\n \
            The topic is \n'


def get_pdf_content_prompt() -> str:
    return 'Write a broad descriptive yet using easy and understandable about this topic -> '


def content_generator(text: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content


def writer(text: str, name: str):
    with open(name+'.pdf') as pdf:
        writer = pypdf.PdfWriter()
        writer.add_attachment(name+'.pdf', text)


def pdf_generator(text: str):
    Table_of_Contents = content_generator(
        get_table_of_content_prompt()+text)
    dictionary_data = json.loads(Table_of_Contents)

    for key, value in dictionary_data.items():
        content = content_generator(get_pdf_content_prompt()+value)
        print(f'Updating pdf. {key}')
        writer(content, text)
        time.sleep(1)


pdf_generator("Life of an Engineer")
