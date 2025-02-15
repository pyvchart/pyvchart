import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import RangeColumn
from pyvchart.globals import ChartType


TEST_RANGE_COLUMN_DATA = [
    {"type": "Category One", "min": 76, "max": 100},
    {"type": "Category Two", "min": 56, "max": 108},
    {"type": "Category Three", "min": 38, "max": 129},
    {"type": "Category Four", "min": 58, "max": 155},
    {"type": "Category Five", "min": 45, "max": 120},
    {"type": "Category Six", "min": 23, "max": 99},
    {"type": "Category Seven", "min": 18, "max": 56},
    {"type": "Category Eight", "min": 18, "max": 34},
]


class TestRangeColumnChart(unittest.TestCase):

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_range_column_base(self, fake_writer):
        c = (
            RangeColumn()
            .set_data(data=[opts.BaseDataOpts(values=TEST_RANGE_COLUMN_DATA)])
            .set_range_column_spec(
                direction="horizontal",
                label_opts=opts.LabelOpts(is_visible=True),
            )
            .set_xy_field(x_field_name=["min", "max"], y_field_name="type")
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 1000)
        self.assertEqual(c.options.get("type"), ChartType.RANGE_COLUMN)
