# Description
This is a independent project to convert sarif and csv into pdf report, should be refactored as another command line tool

## Target

1. As converter
- convert `csv` format to inner format (table data)
- convert `sarif` format to inner format (table data)
- should support multi result files (concat them)

2. As reporter
- render table data to export a pdf for these data

## QuickStart

### Usage
```
```

### Example
generate by `python gen_main.py`

[scan results of socat project-0](https://github.com/Heersin/codeql_packer/blob/main/reporter/export/output_test/page0.png)

[scan results of socat project-1](https://github.com/Heersin/codeql_packer/blob/main/reporter/export/output_test/page1.png)

## Installation Guide

### Dependency
- This project use `phantomjs` as pyecharts' snapshot engine to convert `html` to `png`, so user should install `phantomjs` first

## Project Structure

### Directories & Files
```
./
├── export
│   ├── assets/          # ttf and images
│   ├── echart_mod.py    # echart module, reuseable (maybe)
│   ├── export.py        # main procedure to generate report for codeql
│   ├── __init__.py
│   ├── output_test/     # a sample output here
│   ├── pdf_mod.py       # pdf module, reuseable (maybe)
│
├── generator.py         # command line settings in the future
├── gen_main.py          # main file
├── reader
│   ├── base_reader.py
│   ├── csv_mod.py
│   ├── __init__.py
│   └── sarif_mod.py
└── README.md

```

### Logic Struct
- reader to read scan results from `csv`/`sarif`/`json-server(WIP)`
- export to organize a report, then generate it
    - pdf_mod : handle pdf related operations
    - echart_mod : handle echarts related operations