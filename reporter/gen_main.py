from reader.csv_mod import CsvReader
from reader.safri_mod import SafriReader

r = SafriReader()
r.read('/home/heersin/blackhole/codeql/result.sarif')
