#install pyDF2
#pip install PyPDF2

# importing all the required modules
import PyPDF2 
# creating an object 
arquivo = r"C:\Users\gustavo.felix\Downloads/FUNCM10.pdf"
# creating a pdf reader object
ler = PyPDF2.PdfFileReader(arquivo)
pagina = ler.getPage(0)
conteudo = pagina.extractText()
print(conteudo)

# print the number of pages in pdf file
#print(fileReader.numPages)

