from reader.csv_mod import CsvReader
from reader.sarif_mod import SarifReader

r = SarifReader()
r.read('/home/heersin/blackhole/codeql/result.sarif')
