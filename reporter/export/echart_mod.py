from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Radar
from pyecharts.render import make_snapshot
from pyecharts.charts import Grid
from snapshot_phantomjs import snapshot

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
        print('radar')
           
    def addPie(self, name, pie_data):
        pass

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
        print('bar')

    def renderHtml(self, name):
        self.cur_element.render(name)

    def renderPic(self, name):
        make_snapshot(snapshot, self.cur_element.render(), name)


if __name__ == '__main__':
    echart = Chart()

    y_axis = {
        'name' : 'class',
        'data' : [11, 22, 33]
    }
    x_axis = ['part1', 'part2', 'part3']
    echart.addBar('beta', x_axis, y_axis)

    radar_d = {
        'head' : ['A', 'B', 'C', 'D', 'E', 'F'],
        'data' : [16, 31, 22, 24, 19, 39]
    }
    echart.addRadar('alpha', radar_d)
    echart.renderHtml('new.html')