"""Chapter 1.

Exploratory Data Analysis.
"""

# # Practical Statistics for Data Scientists (2nd edition)
# # Chapter 1. Exploratory Data Analysis
# > (c) 2020 Peter Bruce, Andrew Bruce, Peter Gedeck

# Import required Python packages.

# !pip install statsmodels wquantiles

# +
from pathlib import Path
from typing import Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import wquantiles
from matplotlib.collections import EllipseCollection
from matplotlib.colors import Normalize
from scipy.stats import trim_mean
from statsmodels import robust

# %matplotlib inline
# -

try:
    import common

    DATA = common.dataDirectory()
except ImportError:
    DATA = Path().resolve() / "data"

# Define paths to data sets. If you don't keep your data in the same directory as the code, adapt the path names.

AIRLINE_STATS_CSV = DATA / "airline_stats.csv"
KC_TAX_CSV = DATA / "kc_tax.csv.gz"
LC_LOANS_CSV = DATA / "lc_loans.csv"
AIRPORT_DELAYS_CSV = DATA / "dfw_airline.csv"
SP500_DATA_CSV = DATA / "sp500_data.csv.gz"
SP500_SECTORS_CSV = DATA / "sp500_sectors.csv"
STATE_CSV = DATA / "state.csv"

# # Estimates of Location
# ## Example: Location Estimates of Population and Murder Rates

# Table 1-2
state = pd.read_csv(STATE_CSV)
print(state.head(8))

# Compute the mean, trimmed mean, and median for Population. For `mean` and `median` we can use the _pandas_ methods of the data frame. The trimmed mean requires the `trim_mean` function in _scipy.stats_.

state = pd.read_csv(STATE_CSV)
print(state["Population"].mean())

print(trim_mean(state["Population"], 0.1))

print(state["Population"].median())

# Weighted mean is available with numpy. For weighted median, we can use the specialised package `wquantiles` (https://pypi.org/project/wquantiles/).

print(state["Murder.Rate"].mean())

print(np.average(state["Murder.Rate"], weights=state["Population"]))

print(wquantiles.median(state["Murder.Rate"], weights=state["Population"]))

# # Estimates of Variability

# Table 1-2
print(state.head(8))

# Standard deviation

print(state["Population"].std())

# Interquartile range is calculated as the difference of the 75% and 25% quantile.

print(state["Population"].quantile(0.75) - state["Population"].quantile(0.25))

# Median absolute deviation from the median can be calculated with a method in _statsmodels_

print(robust.scale.mad(state["Population"]))
print(
    abs(state["Population"] - state["Population"].median()).median()
    / 0.6744897501960817  # noqa: W503
)

# ## Percentiles and Boxplots
# _Pandas_ has the `quantile` method for data frames.

print(state["Murder.Rate"].quantile([0.05, 0.25, 0.5, 0.75, 0.95]))

# _Pandas_ provides a number of basic exploratory plots; one of them are boxplots

# +
ax = (state["Population"] / 1_000_000).plot.box(figsize=(3, 4))
ax.set_ylabel("Population (millions)")

plt.tight_layout()
plt.show()
# -

# ## Frequency Table and Histograms
# The `cut` method for _pandas_ data splits the dataset into bins. There are a number of arguments for the method. The following code creates equal sized bins. The method `value_counts` returns a frequency table.

binnedPopulation = pd.cut(state["Population"], 10)  # noqa: N816
print(binnedPopulation.value_counts())

# +
# Table 1.5
binnedPopulation.name = "binnedPopulation"
df = pd.concat([state, binnedPopulation], axis=1)
df = df.sort_values(by="Population")

groups = []
for group, subset in df.groupby(by="binnedPopulation", observed=False):
    groups.append(
        {
            "BinRange": group,
            "Count": len(subset),
            "States": ",".join(subset.Abbreviation),
        }
    )
print(pd.DataFrame(groups))
# -

# _Pandas_ also supports histograms for exploratory data analysis.

# +
ax = (state["Population"] / 1_000_000).plot.hist(figsize=(4, 4))
ax.set_xlabel("Population (millions)")

plt.tight_layout()
plt.show()
# -

# ## Density Estimates
# Density is an alternative to histograms that can provide more insight into the distribution of the data points. Use the argument `bw_method` to control the smoothness of the density curve.

# +
ax = state["Murder.Rate"].plot.hist(
    density=True,
    xlim=[0, 12],  # type: ignore
    bins=range(1, 12),
    figsize=(4, 4),
)
state["Murder.Rate"].plot.density(ax=ax)
ax.set_xlabel("Murder Rate (per 100,000)")

plt.tight_layout()
plt.show()
# -

# # Exploring Binary and Categorical Data

# Table 1-6
dfw = pd.read_csv(AIRPORT_DELAYS_CSV)
print(100 * dfw / dfw.values.sum())

# _Pandas_ also supports bar charts for displaying a single categorical variable.

# +
ax = dfw.transpose().plot.bar(figsize=(4, 4), legend=False)
ax.set_xlabel("Cause of delay")
ax.set_ylabel("Count")

plt.tight_layout()
plt.show()
# -

# # Correlation
# First read the required datasets

sp500_sym = pd.read_csv(SP500_SECTORS_CSV)
sp500_px = pd.read_csv(SP500_DATA_CSV, index_col=0)

# +
# Table 1-7
# Determine telecommunications symbols
telecomSymbols = sp500_sym[  # noqa: N816
    sp500_sym["sector"] == "telecommunications_services"
]["symbol"]

# Filter data for dates July 2012 through June 2015
telecom = sp500_px.loc[sp500_px.index >= "2012-07-01", telecomSymbols]
telecom.corr()
print(telecom)
# -

# Next we focus on funds traded on major exchanges (sector == 'etf').

etfs = sp500_px.loc[
    sp500_px.index > "2012-07-01", sp500_sym[sp500_sym["sector"] == "etf"]["symbol"]
]
print(etfs.head())

# Due to the large number of columns in this table, looking at the correlation matrix is cumbersome and it's more convenient to plot the correlation as a heatmap. The _seaborn_ package provides a convenient implementation for heatmaps.

# +
fig, ax = plt.subplots(figsize=(5, 4))
ax = sns.heatmap(
    etfs.corr(),
    vmin=-1,
    vmax=1,
    cmap=sns.diverging_palette(20, 220, as_cmap=True),
    ax=ax,
)

plt.tight_layout()
plt.show()


# -

# The above heatmap works when you have color. For the greyscale images, as used in the book, we need to visualize the direction as well. The following code shows the strength of the correlation using ellipses.


# +
def plot_corr_ellipses(
    data: Union[np.ndarray, pd.DataFrame, list[list[float]]],
    figsize: Optional[tuple[float, float]] = None,
    **kwargs: Union[float, str, tuple[float, ...], None],
) -> plt.Figure:
    """https://stackoverflow.com/a/34558488."""
    m_var = np.array(data)
    if not m_var.ndim == 2:
        raise ValueError("data must be a 2D array")
    fig_2, ax_2 = plt.subplots(  # pylint: disable=W0612
        1, 1, figsize=figsize, subplot_kw={"aspect": "equal"}
    )
    ax_2.set_xlim(-0.5, m_var.shape[1] - 0.5)
    ax_2.set_ylim(-0.5, m_var.shape[0] - 0.5)
    ax_2.invert_yaxis()

    # xy locations of each ellipse center
    indices = np.indices(m_var.shape)
    xy = np.stack(indices[::-1], axis=-1).reshape(-1, 2)

    # set the relative sizes of the major/minor axes according to the strength of
    # the positive/negative correlation
    w_var = np.ones_like(m_var).ravel() + 0.01
    h_var = 1 - np.abs(m_var).ravel() - 0.01
    a_var = 45 * np.sign(m_var).ravel()

    ec = EllipseCollection(
        widths=w_var,
        heights=h_var,
        angles=a_var,
        units="x",
        offsets=xy,
        norm=Normalize(vmin=-1, vmax=1),
        transOffset=ax.transData,
        array=m_var.ravel(),
        **kwargs,
    )
    ax_2.add_collection(ec)

    # if data is a DataFrame, use the row/column names as tick labels
    if isinstance(data, pd.DataFrame):
        ax_2.set_xticks(np.arange(m_var.shape[1]))
        ax_2.set_xticklabels(data.columns, rotation=90)
        ax_2.set_yticks(np.arange(m_var.shape[0]))
        ax_2.set_yticklabels(data.index)

    return ec, ax_2


n_var, ax = plot_corr_ellipses(etfs.corr(), figsize=(5, 4), cmap="bwr_r")
cb = plt.colorbar(n_var, ax=ax)
cb.set_label("Correlation coefficient")

plt.tight_layout()
plt.show()
# -

# ## Scatterplots
# Simple scatterplots are supported by _pandas_. Specifying the marker as `$\u25EF$` uses an open circle for each point.

# +
ax = telecom.plot.scatter(x="T", y="VZ", figsize=(4, 4), marker="$\u25ef$")
ax.set_xlabel("ATT (T)")
ax.set_ylabel("Verizon (VZ)")
ax.axhline(0, color="grey", lw=1)
ax.axvline(0, color="grey", lw=1)

plt.tight_layout()
plt.show()
# -

ax = telecom.plot.scatter(x="T", y="VZ", figsize=(4, 4), marker="$\u25ef$", alpha=0.5)
ax.set_xlabel("ATT (T)")
ax.set_ylabel("Verizon (VZ)")
ax.axhline(0, color="grey", lw=1)
print(ax.axvline(0, color="grey", lw=1))

# # Exploring Two or More Variables
# Load the kc_tax dataset and filter based on a variety of criteria

kc_tax = pd.read_csv(KC_TAX_CSV)
kc_tax0 = kc_tax.loc[
    (kc_tax.TaxAssessedValue < 750000)
    & (kc_tax.SqFtTotLiving > 100)  # noqa: W503
    & (kc_tax.SqFtTotLiving < 3500),  # noqa: W503
    :,
]
print(kc_tax0.shape)

# ## Hexagonal binning and Contours
# ### Plotting numeric versus numeric data

# If the number of data points gets large, scatter plots will no longer be meaningful. Here methods that visualize densities are more useful. The `hexbin` method for _pandas_ data frames is one powerful approach.

# +
ax = kc_tax0.plot.hexbin(
    x="SqFtTotLiving", y="TaxAssessedValue", gridsize=30, sharex=False, figsize=(5, 4)
)
ax.set_xlabel("Finished Square Feet")
ax.set_ylabel("Tax Assessed Value")

plt.tight_layout()
plt.show()
# -

# ## Two Categorical Variables
# Load the `lc_loans` dataset

lc_loans = pd.read_csv(LC_LOANS_CSV)

# Table 1-8(1)
crosstab = lc_loans.pivot_table(
    index="grade", columns="status", aggfunc=len, margins=True
)
print(crosstab)

# Table 1-8(2)
# fmt: off
df = crosstab.copy().loc["A":"G", :].astype(float)  # type: ignore[misc]
df.loc[:, "Charged Off":"Late"] = (  # type: ignore[misc]
    df.loc[:, "Charged Off":"Late"].div(df["All"], axis=0)  # type: ignore[misc]
)
df["All"] = df["All"] / sum(df["All"])
perc_crosstab = df
print(perc_crosstab)
# fmt: on

# ## Categorical and Numeric Data
# _Pandas_ boxplots of a column can be grouped by a different column.

# +
airline_stats = pd.read_csv(AIRLINE_STATS_CSV)
airline_stats.head()
ax = airline_stats.boxplot(by="airline", column="pct_carrier_delay", figsize=(5, 5))
ax.set_xlabel("")
ax.set_ylabel("Daily % of Delayed Flights")
plt.suptitle("")

plt.tight_layout()
plt.show()
# -

# _Pandas_ also supports a variation of boxplots called _violinplot_. l

# +
fig, ax = plt.subplots(figsize=(5, 5))
sns.violinplot(
    data=airline_stats,
    x="airline",
    y="pct_carrier_delay",
    ax=ax,
    inner="quartile",
    color="white",
)
ax.set_xlabel("")
ax.set_ylabel("Daily % of Delayed Flights")

plt.tight_layout()
plt.show()
# -

# ## Visualizing Multiple Variables

# +
# fmt: off
zip_codes = [98188, 98105, 98108, 98126]
kc_tax_zip = kc_tax0.loc[kc_tax0.ZipCode.isin(zip_codes), :]
kc_tax_zip


def hexbin(  # type: ignore[explicit-any]
    x_var: Union[np.ndarray, pd.Series, list[float]],
    y_var: Union[np.ndarray, pd.Series, list[float]],
    color: str,
    **kwargs: object,
) -> None:
    """Draw a hexagonal binning plot of two numeric variables."""
    cmap = sns.light_palette(color, as_cmap=True)
    plt.hexbin(x_var, y_var, gridsize=25, cmap=cmap, **kwargs)


g_var = sns.FacetGrid(kc_tax_zip, col="ZipCode", col_wrap=2)
g_var.map(
    hexbin, 
    "SqFtTotLiving", 
    "TaxAssessedValue", 
    extent=[0, 3500, 0, 700000],
)
g_var.set_axis_labels("Finished Square Feet", "Tax Assessed Value")
g_var.set_titles("Zip code {col_name:.0f}")

plt.tight_layout()
plt.show()
# fmt: on
