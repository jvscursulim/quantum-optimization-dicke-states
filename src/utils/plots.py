import numpy as np
import plotly.graph_objects as go


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


def plot_interactive_sharpe_ratio_surface(
    returns: np.ndarray, risks: np.ndarray, sharpes: np.ndarray, portfolios: list = None
) -> go.Figure:
    """ """

    data = [
        go.Scatter3d(
            x=risks,
            y=returns,
            z=sharpes,
            mode="markers+lines",
            line=dict(dash="dash"),
            marker=dict(color="black", size=3),
            showlegend=True,
            name="Efficient Frontier",
        ),
        go.Surface(
            x=np.linspace(risks.min(), risks.max(), 101),
            y=np.linspace(returns.min(), returns.max(), 101),
            z=np.zeros(101),
            colorscale="gray",
            opacity=0.3,
            showscale=False,
        )
    ]
    if not portfolios is None:
        data.extend(portfolios)
    fig = go.Figure(data=data)
    fig.update_layout(
        scene=dict(
            xaxis=dict(title="Risk"),
            yaxis=dict(title="Return"),
            zaxis=dict(title="Sharpe Ratio"),
        ),
        title_text="Discrete Efficient Frontier",
    )

    return fig
