import PyPDF2 as pdf
import csv

class PDFtoCSV:
    def __init__(self, pdfFilePath: str, pdfPages: int) -> None:
        """
        Generate your .csv curriculum at the same path as your .pdf curriculum

        :param pdfFilePath: absolute or relative path to your .pdf curriculum
        :param pdfPages: the max amount of pages this code will detect
        """
        self.path = pdfFilePath
        self.pages = pdfPages
        self.matrix = []

        self._pdfToMatrix()
        self._saveToCSV()

    def _pdfToMatrix(self) -> None:
        i=0
        with open(self.path, 'rb') as file:
            reader = pdf.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
                i+=1
                if i>=self.pages: break

        lines = text.splitlines()
        self.matrix = [line.split() for line in lines if line.strip()]
    
    def _saveToCSV(self) -> None:
        num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        with open(f"{self.path[:-4]}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            for row in self.matrix[2:]:
                newrow = ['', '', '', '', '', '', '']
                if len(row[0])!=6: continue
                if len(row)<6: continue
                newrow[0] = row[-2] # num
                newrow[1] = row[-3] # periodo
                newrow[2] = row[0] # codigo

                #se tem 2 pré requisitos:
                if row[-5][-1] in num:
                    newrow[3] = " ".join(row[1:-5]) # nome
                    newrow[4] = row[-4] # requisito1
                    newrow[5] = row[-5] # requisito2
                    newrow[6] = row[-1] # horas

                #se tem 1 pré requisito:
                elif row[-4][-1] in num:
                    newrow[3] = " ".join(row[1:-4]) # nome
                    newrow[4] = row[-4] # requisito 1
                    newrow[6] = row[-1] # horas

                #sem pré requisito:
                else:
                    newrow[3] = " ".join(row[1:-3]) # nome
                    newrow[6] = row[-1] # horas
                writer.writerow(newrow)
        print(f".csv saved at {self.path[:-4]}.csv")
        

err = PDFtoCSV("cursocaio.pdf", 3)
