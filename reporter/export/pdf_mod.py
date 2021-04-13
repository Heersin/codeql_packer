from reportlab.pdfgen.canvas import Canvas  
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.cidfonts import UnicodeCIDFont  
from reportlab.pdfbase.ttfonts import TTFont 
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
pdfmetrics.registerFont(TTFont('genshin', 'assets/SourceHanSansTC-Normal.ttf'))  
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,Image,Table,TableStyle
import time

class Pdffer:
    def __init__(self):
        # An object to store componets
        self.body = []

        # stylesheet of font
        stylesheet = getSampleStyleSheet()
        self.style = stylesheet['Normal']

    def addMainTitle(self, text, color=0):
        title = f'<para autoLeading="off" fontSize=16 align=center><b><font face="genshin">{text}</font></b><br/><br/><br/></para>'
        self.body.append(Paragraph(title, self.style))

    def addTitle(self, level, text, color=0):
        font_size = str(14 - int(level))
        title = f'<para autoLeading="off" fontSize={font_size} align=left><b><font face="genshin">{text}</font></b><br/><br/><br/></para>'
        self.body.append(Paragraph(title, self.style))

    def addTable(self, head_and_data):
        table_style = [
            ('FONTNAME', (0, 0), (-1, -1), 'genshin'),  # 字体
            ('FONTSIZE', (0, 0), (2, 0), 8),  # 第一行的字体大小
            ('FONTSIZE', (0, 1), (-1, -1), 8),  # 第二行到最后一行的字体大小
            ('ALIGN', (0, 0), (2, 0), 'CENTER'),  # 第一行左右中间对齐
            ('ALIGN', (0, 1), (2, 8), 'LEFT'),  # 第二行到最后一行左右左对齐
            ('VALIGN', (0, 0), (2, 8), 'MIDDLE'),  # 所有表格上下居中对齐
            ('BACKGROUND', (0, 0), (2, 0), colors.lightslategray),  # 设置第一行背景颜色
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.darkslategray),  # 设置表格内文字颜色
            ('GRID', (0, 0), (-1, -1), 0.1, colors.slategray),  # 设置表格框线为灰色，线宽为0.1
        ]

        table_table = Table(head_and_data, style=table_style)
        self.body.append(table_table)
        
    def addPics(self, path, height, width):
        img = Image(path)
        img.drawWidth = width
        img.drawHeight = height
        self.body.append(img)

    def addText(self, text, color=0, size=0):
        text = f'<para autoLeading="off" fontSize=8><font face="genshin" color=darkblue>{text}</font><br/></para>'
        self.body.append(Paragraph(text, self.style))

    def addSpace(self):
        self.body.append(Spacer(240, 10))#添加空白，长度240，宽10

    def generatePdf(self, name):
        doc = SimpleDocTemplate(name)
        doc.build(self.body)


if __name__ == '__main__':
    converter = Pdffer()
    converter.addMainTitle("Test")
    
    # Add pics
    converter.addSpace()
    converter.addPics("assets/test.jpg", 200, 300)

    converter.addTitle(1, "Nice To Meet you")
    
    converter.addText("Today is monday")

    table_data =  [['Year', 'Month', 'Day'],
                  ['2017', '3', '12'],
                  ['2017', '4', '13'],
                  ['2017', '5', '14'],
                  ['2017', '6', '15'],
                  ['2018', '7', '16'],
                  ['2018', '8', '17'],
                  ['2018', '9', '18'],
                  ['2018', '10', '19'],
                  ]

    converter.addTable(table_data)
    
    converter.generatePdf('simple.pdf')
