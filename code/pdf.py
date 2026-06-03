from pypdf import PdfWriter, PdfReader

reader1 = PdfReader("Time Table.pdf")
reader2 = PdfReader("Enrollment.pdf")

writer = PdfWriter()

writer.append(reader1)
writer.append(reader2)

writer.write(open("Merged.pdf", "wb"))