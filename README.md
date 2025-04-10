# iompyplotstyle


The `iompyplotstyle` package provides Matplotlib styles following the [IOM Data Visualization Guidelines](https://iomint.sharepoint.com/sites/DTMStandards/SitePages/VISUALIZE.aspx), ensuring that charts are professional and brand-compliant. The purpose of this package is to simplify and expedite the chart creation process using Matplotlib custom stylesheets. This package can be used within Microsoft Fabric for [Visualisation Notebook](https://learn.microsoft.com/en-us/fabric/data-engineering/notebook-visualization)

## Getting started
The easiest way to install the `iompyplotstyle` package is by using pip:

```bash
# to install the latest PyPI release
pip install iompyplotstyle

# to install the latest Github commit
pip install git+https://github.com/iom/iompyplotstyle
```

The pip installation will automatically download and store all Matplotlib custom style files (*.mplstyle) in the appropriate local directory on your computer.

## Use the styles
`iompyplotstyle` is the base style of this package. It provides basic styles for chart elements such as color, font, font size, and position. To use the base style, you can simply call it from your local style directory after importing the `Matplotlib` library.

```python
import matplotlib.pyplot as plt
plt.style.use('iompyplotstyle')
```

Once the base style is applied, you can add a specific style related to the type of chart you want to create by combining two styles together:

```python
import matplotlib.pyplot as plt
plt.style.use('iompyplotstyle','column')
```

In this case, the 'column' style will add some parameters to the base style 'iompyplotstyle' to align all chart element styles with a standard IOM-style column chart.

You can find the full list of styles based on chart types below:
- `area`
- `bar`
- `bubble`
- `column`
- `connected_scatterplot`
- `donut`
- `dotplot`
- `heatmap`
- `histogram`
- `line`
- `linecolumn`
- `lollipop`
- `map`
- `pie`
- `population_pyramid`
- `scatterplot`
- `slope`
- `streamgraph`
- `treemap`

