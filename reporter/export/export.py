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

    def setData(self, pack_data):
        self.entries = pack_data['data']
    
    def build(self, proj_name):
        self._calc()
        convertor = Pdffer()
        convertor.addMainTitle(f"Code Scan Report-[{proj_name}]")

        # set time
        now = datetime.now()
        time_str = now.strftime("%d/%m/%Y %H:%M:%S")
        convertor.addSubTitle(time_str)

        # Add Aligned Pic
        convertor.addSpace()
        convertor.addTitle(1, "1.Visual")
        convertor.addAlignedPics('assets/left.png', 'assets/right.png')

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

        convertor.generatePdf('output_test/sample_result.pdf')
