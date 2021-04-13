from .pdf_mod import Pdffer
from .echart_mod import Chart

class Exporter:
    def __init__(self):
        self.entries = []
        self.scores = {}
        self.pdf = None

    def _calc(self):
        for entry in self.entries:
            level = entry['level']

            if level in self.scores:
                self.scores[level] += 1
            else:
                self.scores[level] = 0

    def setData(self, pack_data):
        self.entries = pack_data['data']
    
    def build(self):
        self._calc()
        convertor = Pdffer()
        convertor.addMainTitle("Code Scan Report")

        # Add Aligned Pic
        convertor.addSpace()
        convertor.addTitle(1, "1.Visual")
        convertor.addAlignedPics('assets/left.png', 'assets/right.png')

        # Top5 vuln 
        convertor.addSpace()
        convertor.addTitle(1, "2.Top Scan")
        top_data = [
            ["Rank", "Filename"],
            ["1", "xio.c"],
            ["2", "ssl.c"],
            ["3", "cap.c"],
            ["4", "xxname.c"],
            ["5", "xeport.c"]]
        convertor.addTable(top_data)

        # Add every entry
        convertor.addSpace()
        convertor.addTitle(1, "3.Vulnerabilities")

        for entry in self.entries:
            convertor.addText(" {}-{}".format(entry['level'], entry['name']))
            convertor.addText("    -> [Path] : {} [Position]{}".format(entry['path'], entry['pos']))
            convertor.addText("    -> [Message] : {}".format(entry['message']))
            convertor.addSpace()

        convertor.generatePdf('output_test/sample_result.pdf')
