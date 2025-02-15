import unittest
from unittest.mock import patch

from pyvchart import options as opts
from pyvchart.charts import LinearProgress
from pyvchart.commons.utils import JsCode
from pyvchart.globals import ChartType


TEST_LINEAR_PROGRESS_DATA = [
    {"type": "Tradition Industries", "value": 0.795, "text": "79.5%"},
    {"type": "Business Companies", "value": 0.25, "text": "25%"},
    {"type": "Customer-facing Companies", "value": 0.065, "text": "6.5%"},
]


class TestLinearProgressChart(unittest.TestCase):

    @patch("pyvchart.render.engine.write_utf8_html_file")
    def test_linear_progress_base(self, fake_writer):
        c = (
            LinearProgress()
            .set_data(
                data=[opts.BaseDataOpts(id_="id0", values=TEST_LINEAR_PROGRESS_DATA)]
            )
            .set_xy_field(x_field_name="value", y_field_name="type")
            .set_linear_progress_spec(
                direction="horizontal",
                corner_radius=20,
                band_width=30,
            )
            .set_global_options(
                series_field="type",
                axes_opts=[
                    opts.AxesBandOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="left",
                            label=opts.AxesLabelOpts(is_visible=True),
                            domain_line=opts.AxesDomainLineOpts(is_visible=False),
                            tick=opts.AxesTickOpts(is_visible=False),
                        )
                    ),
                    opts.AxesLinearOpts(
                        base_axes_opts=opts.BaseAxesOpts(
                            orient="bottom",
                            label=opts.AxesLabelOpts(is_visible=True),
                        ),
                        is_visible=False,
                    ),
                ],
            )
        )
        c.render()
        _, content = fake_writer.call_args[0]
        self.assertGreater(len(content), 1000)
        self.assertEqual(c.options.get("type"), ChartType.LINEAR_PROGRESS)
