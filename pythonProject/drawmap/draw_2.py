from pyecharts.charts import Line
from pyecharts.options import TitleOpts,ToolboxOpts
line = Line()

line.add_xaxis(["中国", "美国", "日本"])
line.add_yaxis("gdp", [30.5, 20, 5.5])

line.set_global_opts(
    title_opts=TitleOpts(title='GDP'),
    toolbox_opts=ToolboxOpts(is_show=True),
)

line.render()