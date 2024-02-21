'''
Ćwiczenie 2
Załóżmy, że pracujesz nad klasą o nazwie FileUtils. Potrzebujesz zaimplementować statyczną 
metodę o nazwie file_extension(), która zwraca rozszerzenie podanej nazwy pliku. Zdefiniuj 
wymaganą metodą statyczną przy użyciu dekoratora @staticmethod. Ta metoda powinna przyjmować
jeden argument (filename - nazwę pliku) i zwracać rozszerzenie pliku (tj. część nazwy pliku 
po kropce). Jeśli w nazwie pliku nie ma kropki, metoda powinna zwrócić pusty ciąg znaków ''.

Przetestuj swoją implementację, wywołując metodę file_extension() z poniższymi nazwami 
plików drukując wyniki do konsoli:

'file.txt'
'document.pdf'
'no_extension'
'image.png'

Oczekiwany wynik:
txt
pdf
 
png
'''

class FileUtils:
    @staticmethod
    def file_extension(filename):
        if '.' not in filename:
            return ''
        return filename.split('.')[-1]
 
 
print(FileUtils.file_extension('file.txt'))
print(FileUtils.file_extension('document.pdf'))
print(FileUtils.file_extension('no_extension'))
print(FileUtils.file_extension('image.png'))