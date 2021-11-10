from pymarc import MARCReader
import pandas as pd
import os

class ExportCSVData():
    def __init__(self, marcpath="./marctest.txt", csvpath="./ExportCSVData/", csvfilename="out.csv"):
        self.marc = marcpath
        self.csvpath = csvpath
        self.csvname = csvfilename
    
    def read_and_write(self):
        try:
            os.mkdir(self.csvpath)
        except Exception as erro:
            print("Erro na criação do diretório de output do CSV")
            print(erro.__class__())
        else:
            try:
                with open(self.marc, 'rb') as fh:
                    reader = MARCReader(fh)

                    data = {
                        "ISBN" : [],
                        "Titulo" : [], 
                        "Autor" : [],
                        "Editora" : [], 
                        "AnoPublicação" : []
                    }

                    for i in reader:
                        data["ISBN"].append(i.isbn())
                        data["Titulo"].append(i.title())
                        data["Autor"].append(i.author())
                        data["Editora"].append(i.publisher())
                        data["AnoPublicação"].append(i.pubyear())
            except (FileNotFoundError) as erro:
                print("Arquivo não existe")
                print(erro.__class__())
            except Exception as erro:
                print("Erro na leitura do arquivo MARC")
                print(erro.__class__())
            else:
                if self.csvpath[len(self.csvpath)-1] != "/":
                    self.csvpath += "/"
                df = pd.DataFrame(data)
                try:
                    df.to_csv(f"{self.csvpath}{self.csvname}")
                    return df
                except Exception as erro:
                    print("Falha ao escrever CSV")
                    print(erro.__class__())
 
