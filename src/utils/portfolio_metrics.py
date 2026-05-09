import numpy as np


def calculate_portfolio_return(
    x: np.ndarray, weights: np.ndarray, assets_returns: np.ndarray
) -> float:
    """ """

    return assets_returns @ (x * weights)


def calculate_portfolio_risk(
    x: np.ndarray, weights: np.ndarray, covariance_matrix: np.ndarray
) -> float:
    """ """

    return np.sqrt((x * weights).T @ covariance_matrix @ (x * weights))


def calculate_portfolio_sharpe_ratio(
    x: np.ndarray,
    weights: np.ndarray,
    assets_returns: np.ndarray,
    covariance_matrix: np.ndarray,
    return_risk_free: float = 0.0375,
) -> float:
    """ """

    portfolio_return = calculate_portfolio_return(
        x=x, weights=weights, assets_returns=assets_returns
    )
    portfolio_risk = calculate_portfolio_risk(
        x=x, weights=weights, covariance_matrix=covariance_matrix
    )

    return (portfolio_return - return_risk_free) / portfolio_risk
