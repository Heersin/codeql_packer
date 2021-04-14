import os
os.chdir("./export")

from reader.csv_mod import CsvReader
from reader.sarif_mod import SarifReader
from export.export import Exporter


r = SarifReader()
r.read('/home/heersin/blackhole/codeql/result.sarif')

#print(os.getcwd())

project_name = "socat"
pdf_factory = Exporter()
pdf_factory.setData(r.get_data())
pdf_factory.build(project_name)
