import os
import pandas as pd

def cmdfile(csvdf, server, cmdfile="yazcommands.txt", marcdump="out.marc", outdir="./MARCOut/", base=""):

        # Cria o diretório de Output para o código se não existir
        try:
            os.mkdir(outdir)
        except Exception:
            pass

        # Lista de comandos para abrir conexão        
        open_cmds = [
            f"open {server}\n",
            f"base {base}\n", 
            f"set_marcdump {outdir}{marcdump}\n"
        ]

        finds = []
        for i in csvdf["ISBN"]:
            finds.append(f"f @attr 1=7 {i}\n")

        stdin = f"{outdir}{cmdfile}"

        # Cria o arquivo de stdin para o yaz-client
        try:
            os.system(f"touch {stdin}")
        except Exception:
            pass

        with open(stdin, "wb") as file:
            for i in open_cmds:
                file.write(i.encode())
            for i in finds:
                file.write(i.encode())
        
        return outdir, stdin

class PyYazClient():
    
    def __init__(self, csv="./cat1.csv", server="162.214.168.248:9998/bib", base=""):
        self.csv = csv
        self.server = server
        self.csvdf = pd.read_csv(self.csv)
        self.csvdf.columns = ["ISBN", "DataImpressão", "Exemplares"]
        self.base = base
    
    def installyaz():
        os.system("sudo apt install yaz-client")

    def getmarcs(self):
        s = cmdfile(csvdf=self.csvdf, server=self.server, base = self.base)
        os.system(f"yaz-client < {s[1]} > {s[0]}yazout.txt 2> {s[0]}yazerror.txt")

