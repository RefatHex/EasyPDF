import json
import time
from keys import OpenAI_API
from openai import OpenAI
from fpdf import FPDF


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


def writer(dictionary_data, name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)

    for title, text in dictionary_data.items():
        # Title
        title_width = pdf.get_string_width(title)
        page_width = pdf.w
        title_x_pos = ((page_width - title_width) / 4) + title_width
        text = content_generator(get_pdf_content_prompt()+text)
        pdf.set_font('helvetica', size=30)
        pdf.text(title_x_pos, 20, title)

        # Draw a straight line under the title
        pdf.line(10, 28, page_width - 10, 28)

        # Text
        pdf.set_font('helvetica', size=12)
        y_pos = pdf.get_y() + 20
        pdf.set_y(y_pos)
        pdf.multi_cell(0, 10, text=text, border=0, align='L')
        pdf.add_page()
        print("added ")
        time.sleep(1)

    pdf.output(name + ".pdf")


def pdf_generator(text: str):
    Table_of_Contents = content_generator(
        get_table_of_content_prompt() + text)
    dictionary_data = json.loads(Table_of_Contents)
    replaced_text = text.replace(" ", "_")
    writer(dictionary_data, replaced_text)


pdf_generator("Life of an Engineer")
