# Open and read a page from a pdf file
# Write page one from the file to a new pdf file
import PyPDF2

f = open('resources/Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)

page_one = pdf_reader.getPage(0)

page_one_text = page_one.extractText()

print(page_one_text)
f.close()
f = open('resources/Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfWriter()
print(type(first_page))
pdf_writer.addPage(first_page)
pdf_output = open('Some_Brand_New_doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()
