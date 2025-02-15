import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import Gauge
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType

TEST_GAUGE_DATA = [{"type": "目标A", "value": 0.6}]


class TestGaugeChart(unittest.TestCase):

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_gauge_base(self, fake_writer):
        c = (
            Gauge()
            .set_data(data=[opts.BaseDataOpts(id_="id0", values=TEST_GAUGE_DATA)])
            .set_gauge_spec(
                category_field="type",
                value_field="value",
                outer_radius=0.8,
                inner_radius=0.5,
                start_angle=-180,
                end_angle=0,
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 1000)
        self.assertEqual(c.options.get("type"), ChartType.GAUGE)
