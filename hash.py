import hashlib
def compare(a,b):
    a == b
myText = 'Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação.'

SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

print("\"" +myText + "\" - " + SHA256 + " - " + MD5)
sha = 'b2ff0457c8c20ccd84e20cd72f06c08140b8ea472d6a6848a5c291319bf9e4a8'
md = '0288b32001adf2f237ba8410f8415e50'
print("SHA256 " + compare(SHA256,sha))
print("MD5 " + compare(MD5,md))