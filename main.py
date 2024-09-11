import PyPDF2 as pdf
import csv

def pdfToMatrix(file: str, max_page: int) -> list: 
    i=0
    with open(file, 'rb') as file:
        reader = pdf.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
            i+=1
            if i>=max_page: break

    lines = text.splitlines()
    matrix = [line.split() for line in lines if line.strip()]
    return matrix

def saveToCSV(matrix: list, csv_file: str)-> None:
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in matrix[2:]:
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


pdf_file = "mypdf.pdf"
csv_file = "mycsv.csv"
end_page = 3

matrix = pdfToMatrix(file=pdf_file, max_page=end_page)

saveToCSV(matrix = matrix, csv_file = csv_file)

