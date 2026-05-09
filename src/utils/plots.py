import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns


def plot_hamiltonian_expval_heatmap(
    data: np.ndarray, xlabel: str = None, ylabel: str = None, title: str = None
) -> None:
    """"""

    _, ax = plt.subplots()

    sns.heatmap(data=data)
    ax.set_xlabel(r"$\theta_0$" if xlabel is None else xlabel)
    ax.set_ylabel(r"$\theta_1$" if ylabel is None else ylabel)
    ax.set_title("Hamiltonian expectation value heatmap" if title is None else title)

    plt.show()


def plot_hamiltonian_expval_surface(
    x: np.ndarray,
    y: np.ndarray,
    z: np.ndarray,
    xlabel: str = None,
    ylabel: str = None,
    title: str = None,
) -> go.Figure:
    """"""

    data = go.Surface(x=x, y=y, z=z)
    fig = go.Figure(data=data)
    fig.update_layout(
        title_text=(
            "Hamiltonian expectation value landscape" if title is None else title
        ),
        scene=dict(
            xaxis=dict(title={"text": "theta_0" if xlabel is None else xlabel}),
            yaxis=dict(title={"text": "theta_1" if ylabel is None else ylabel}),
            zaxis=dict(title={"text": "<H>"}),
        ),
    )

    return fig


def plot_static_efficient_frontier(
    df_efficient_frontier: pd.DataFrame, df_portfolios: pd.DataFrame = None
) -> None:
    """ """

    _, ax = plt.subplots()

    ax.set_title("Discrete Efficient Frontier")
    ax.plot(
        df_efficient_frontier.portfolio_risk.values,
        df_efficient_frontier.portfolio_return.values,
        linestyle="--",
        marker="o",
        color="black",
        label="Efficient Frontrier",
    )
    if not df_portfolios is None:
        sns.scatterplot(
            data=df_portfolios,
            x="portfolio_risk",
            y="portfolio_return",
            hue="sharpe",
            ax=ax,
        )
    ax.set_xlabel("Risk")
    ax.set_ylabel("Return")

    plt.show()


def plot_interactive_efficient_frontier(
    returns: np.ndarray, risks: np.ndarray, portfolios: list = None
) -> go.Figure:
    """ """

    data = [
        go.Scatter(
            x=risks,
            y=returns,
            mode="markers+lines",
            line=dict(dash="dash"),
            marker=dict(color="black"),
            showlegend=True,
            name="Efficient Frontier",
        )
    ]
    if not portfolios is None:
        data.extend(portfolios)
    fig = go.Figure(data=data)
    fig.update_layout(
        xaxis_title="Risk",
        yaxis_title="Return",
        title_text="Discrete Efficient Frontier",
    )

    return fig
