import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Bar
from pyvchart.globals import ChartType


TEST_BAR_DATA = [
    {"month": "Monday", "sales": 22},
    {"month": "Tuesday", "sales": 13},
    {"month": "Wednesday", "sales": 25},
    {"month": "Thursday", "sales": 29},
    {"month": "Friday", "sales": 38},
]


class TestBarChart(unittest.TestCase):

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_bar_base(self, fake_writer):
        c = (
            Bar()
            .set_bar_spec()
            .set_data(data=[opts.BaseDataOpts(values=TEST_BAR_DATA)])
            .set_xy_field(
                x_field_name="time",
                y_field_name="value",
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 1000)
        self.assertEqual(c.options.get("type"), ChartType.BAR)
