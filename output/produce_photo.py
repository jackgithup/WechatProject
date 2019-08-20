import pdfkit
from pdf2image import convert_from_path

def produce_pdf():
    options = {
        'page-size': 'Letter',
        'margin-top': '0.00075in',
        'margin-right': '0.00075in',
        'margin-bottom': '0.00075in',
        'margin-left': '0.00075in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    pdfkit.from_file('2.html','out.pdf',options=options)


def produce_photo():
    # images = convert_from_path(filename,outputDir)
    # for index,img in enumerate(images):
    #     img.save('out.png')
    convert_from_path('out.pdf', 300, "output", fmt="JPEG", output_file="essay1", thread_count=1)

if __name__ == '__main__':
    produce_pdf()
    # produce_photo()