from PyPDF4 import PdfFileReader, PdfFileWriter

def encrypt(input,password):
    pdf = PdfFileReader(input)
    writer = PdfFileWriter()
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        writer.addPage(page)
        
    writer.encrypt(password)
    with open('encrypted_' + input, "wb") as output:
        writer.write(output)
        
        
encrypt("cp.pdf",'123456')


def decrypt(input,password):
    pdf = PdfFileReader(input)
    writer = PdfFileWriter()
    pdf.decrypt(password)
    
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        writer.addPage(page)
    
    with open('decrypted_' + input, 'wb') as output:
        writer.write(output)
    
    
decrypt("encrypted_cp.pdf",'123456')
