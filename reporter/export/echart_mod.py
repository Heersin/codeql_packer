from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Radar
from pyecharts.render import make_snapshot

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
            schema.append(opts.RadarIndicatorItem(name=radar_head[i], max=max_value))
        
        radar.add_schema(schema)
        radar.add(name, radar_data)
        radar.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        radar.set_global_opts(
            legend_opts=opts.LegendOpts(selected_mode="single"),
            title_opts=opts.TitleOpts(title="Radar-单例模式"),
        )

        self.elements.append(radar)
        self.cur_element = radar
           
    def addPie(self, name, pie_data):
        pass

    def addBar(self, name, x, y, reverse=True):
        bar = Bar(init_opts=opts.InitOpts(bg_color='#fff'))
        bar.add_xaxis(x)
        bar.add_yaxis(y)

        if reverse:
            bar.reversal_axis()

        bar.set_series_opts(label_opts=opts.LabelOpts(position="right"))
        bar.set_global_opts(title_opts=opts.TitleOpts(title=name))

        self.elements.append(bar)
        self.cur_element = bar

    def setLayout(self):
        grid = Grid()
        .add(self.elements[0], grid_opts=opts.GridOpts(pos_left="55%"))
        .add(self.elements[1], grid_opts=opts.GridOpts(pos_right="55%"))

        self.cur_element = grid

    def renderHtml(self, name):
        self.cur_element.render(name)

    def renderPic(self, name):
        make_snapshot(snapshot, self.cur_element.render(), name)

