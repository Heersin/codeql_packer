from .pdf_mod import Pdffer
from .echart_mod import Chart
from datetime import datetime

class Exporter:
    def __init__(self):
        self.entries = []
        self.classified_entries = {
            'danger' : [],
            'warning' : [],
            'note' : [],
            'style' : [],
            'other' : []
        }
        self.pdf = None
        self.paths = {}
        self.top_list = []
        self.imgs = []
        self.proj_name = ''

    def _calc(self):
        for entry in self.entries:
            level = entry['level']
            path = entry['path']

            # collect levels
            if level in self.classified_entries:
                self.classified_entries[level].append(entry)
            else:
                self.classified_entries['other'].append(entry)
            
            # collect paths
            if path in self.paths:
                self.paths[path] += 1
            else:
                self.paths[path] = 1

        # sort by value
        top_list = [k_name for k_name, v in sorted(self.paths.items(), key=lambda item: item[1])]
        top_list.reverse()
        self.top_list = top_list

    def setData(self, data):
        self.entries = data

    def setProjName(self, name):
        self.proj_name = name

    # analyze data and use pyecharts to generate pics
    def analyzeData(self):
        self._calc()
        py_chart = Chart()

        # prepare radar chart
        score = self.classified_entries
        radar_data = {
            'head' : ['danger', 'warning', 'note', 'style', 'other'],
            'data' : [
                len(score['danger']),
                len(score['warning']),
                len(score['note']),
                len(score['style']),
                len(score['other'])
            ]
        }

        # prepare pie data
        # x -> name, y -> value
        pie_data = []

        for p in self.paths:
            pie_entry = [p, self.paths[p]]
            pie_data.append(pie_entry)

        # render radar
        py_chart.addRadar('Issues Distribution', radar_data)
        radar_path = 'assets/' + self.proj_name + '_radar.png'
        py_chart.renderPic(radar_path)
        self.imgs.append(radar_path)

        # render pie
        py_chart.addPie('Files Statstic', pie_data)
        pie_path = 'assets/' + self.proj_name + '_pie.png'
        py_chart.renderPic(pie_path)
        self.imgs.append(pie_path)

    
    def build_pdf(self):
        proj_name = self.proj_name
        convertor = Pdffer()
        convertor.addMainTitle(f"Code Scan Report-[{proj_name}]")

        # set time
        now = datetime.now()
        time_str = now.strftime("%d/%m/%Y %H:%M:%S")
        convertor.addSubTitle(time_str)

        # Add Aligned Pic
        convertor.addSpace()
        convertor.addTitle(1, "1.Visual")
        if (len(self.imgs) < 2):
            print("[x]Please Analyze Data Once at Least")
            return
        convertor.addAlignedPics(self.imgs[0], self.imgs[1])

        # Top5 vuln 
        convertor.addSpace()
        convertor.addTitle(1, "2.Top Vulnrable Files")
        top_data = []
        # Add header
        top_data.append(['Rank', 'File Path'])
        for i in range(len(self.top_list)):
            tmp = [str(i + 1), self.top_list[i]]
            top_data.append(tmp)
        convertor.addTable(top_data)

        # Add every entry
        convertor.addSpace()
        convertor.addTitle(1, "3.Potential Vulnerabilities")
        c_index = 1

        ## Danger
        convertor.addSpace()
        convertor.addDangerTitle("DANGER")
        for entry in self.classified_entries['danger']:
            convertor.addText(" {}-{}".format(c_index, entry['name']))
            convertor.addText("    -> [Path] : {} (Line) {}".format(entry['path'], entry['pos']))
            convertor.addText("    -> [Message] : {}".format(entry['message']))
            convertor.addSpace()
            c_index += 1

        # Warning
        c_index = 1
        convertor.addSpace()
        convertor.addWarningTitle("WARNING")
        for entry in self.classified_entries['warning']:
            convertor.addText(" {}-{}".format(c_index, entry['name']))
            convertor.addText("    -> [Path] : {} (Line) {}".format(entry['path'], entry['pos']))
            convertor.addText("    -> [Message] : {}".format(entry['message']))
            convertor.addSpace()
            c_index += 1

        c_index = 1
        convertor.addSpace()
        convertor.addNoteTitle("NOTE OR COMMENT")
        for entry in self.classified_entries['note']:
            convertor.addText(" {}-{}".format(c_index, entry['name']))
            convertor.addText("    -> [Path] : {} (Line) {}".format(entry['path'], entry['pos']))
            convertor.addText("    -> [Message] : {}".format(entry['message']))
            convertor.addSpace()
            c_index += 1

        c_index = 1
        convertor.addSpace()
        convertor.addStyleTitle("STYLE ISSUE")
        for entry in self.classified_entries['style']:
            convertor.addText(" {}-{}".format(c_index, entry['name']))
            convertor.addText("    -> [Path] : {} (Line) {}".format(entry['path'], entry['pos']))
            convertor.addText("    -> [Message] : {}".format(entry['message']))
            convertor.addSpace()
            c_index += 1

        c_index = 1
        convertor.addSpace()
        convertor.addOtherTitle("OTHER")
        for entry in self.classified_entries['other']:
            convertor.addText(" {}-{}".format(c_index, entry['name']))
            convertor.addText("    -> [Path] : {} (Line) {}".format(entry['path'], entry['pos']))
            convertor.addText("    -> [Message] : {}".format(entry['message']))
            convertor.addSpace()
            c_index += 1

        convertor.generatePdf('output_test/' + proj_name + '_result.pdf')

    def build(self, proj_name):
        self.proj_name = proj_name
        print("[*]Start Analyze Data ...")
        self.analyzeData()
        print("[*]Building pdf ...")
        self.build_pdf()
