from fpdf import FPDF


def writer(name, title, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('helvetica', size=12)

    # Title
    title_width = pdf.get_string_width(title)
    page_width = pdf.w
    title_x_pos = ((page_width - title_width) / 4)+title_width

    pdf.set_font('helvetica', size=30)
    pdf.text(title_x_pos, 20, title)

    # Draw a straight line under the title
    pdf.line(10, 28, page_width - 10, 28)

    # Text
    pdf.set_font('helvetica', size=12)
    y_pos = pdf.get_y() + 20
    pdf.set_y(y_pos)
    pdf.multi_cell(0, 10, text=text, border=0, align='L')
    pdf.output(name + ".pdf")


# Example usage:
writer("example", "Sample Title",
       "This is a sample text for demonstration purposes.")
