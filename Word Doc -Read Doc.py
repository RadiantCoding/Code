import docx

def ReadDoc(filename):
	doc = docx.Document(filename)
	
	paragraphs = []
	for paragraph in doc.paragraphs:
		if len(paragraph.text)>0:
			paragraphs.append(paragraph.text)
	print(paragraphs)

ReadDoc("table.docx")
