from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Radar
from pyecharts.charts import Pie
from pyecharts.render import make_snapshot
from pyecharts.charts import Grid
from snapshot_phantomjs import snapshot
import os

from pyecharts.faker import Faker

class Chart:
    def __init__(self):
        self.elements = []
        self.cur_element = None
    
    def addRadar(self, name, radar_data_dict):
        radar = Radar()

        radar_data = radar_data_dict['data']
        radar_head = radar_data_dict['head']
        
        item_cnt = len(radar_data)
        max_value = max(radar_data)

        schema = []
        for i in range(item_cnt):
            schema.append(opts.RadarIndicatorItem(name=radar_head[i], max_=max_value))
        
        radar.add_schema(schema)
        radar.add(name, [radar_data])
        radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        radar.set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title=name),
        )

        self.elements.append(radar)
        self.cur_element = radar
        print('[*]Radar Analyzing ...')
           
    def addPie(self, name, pie_data):
        pie = Pie()
        pie.add(
                name,
                pie_data,
                radius=["30%", "75%"],
                center="50%",
                rosetype="area",
        )
        pie.set_series_opts(label_opts=opts.LabelOpts(is_show=True, formatter='{b}-{c}' ))

        self.elements.append(pie)
        self.cur_element = pie
        print("[*]Pie Analyzing ...")


    def addBar(self, name, x, y, reverse=True):
        bar = Bar(init_opts=opts.InitOpts(bg_color='#fff'))
        bar.add_xaxis(x)
        bar.add_yaxis(y['name'], y['data'])

        if reverse:
            bar.reversal_axis()

        bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
        bar.set_global_opts(title_opts=opts.TitleOpts(title=name))

        self.elements.append(bar)
        self.cur_element = bar

    def renderHtml(self, name):
        self.cur_element.render(name)

    def renderPic(self, name):
        make_snapshot(snapshot, self.cur_element.render(), name, is_remove_html=True)
        print(f"[*]Generate A snapshot in {name}")


if __name__ == '__main__':
    echart = Chart()

    y_axis = {
        'name' : 'class',
        'data' : [11, 0, 0]
    }

    y_axis2 = {
        'name' : 'class',
        'data' : [0, 22, 0]
    }
    x_axis = ['part1', 'part2', 'part3']
    echart.addBar('beta', x_axis, y_axis)

    radar_d = {
        'head' : ['A', 'B', 'C', 'D', 'E', 'F'],
        'data' : [16, 31, 22, 24, 19, 39]
    }

    pie_d = [[k, v] for k, v in zip(radar_d['head'], radar_d['data'])]
    #echart.addRadar('alpha', radar_d)
    echart.addPie('test', pie_d)
    echart.renderHtml('new.html')
    #echart.renderPic('assets/right.png')