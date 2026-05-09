# Imports
from __future__ import annotations

import numpy as np

from optuna import Trial
from qiskit.circuit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit_ibm_runtime import EstimatorV2


def objective_scipy(
    x: np.ndarray,
    estimator: EstimatorV2,
    qc: QuantumCircuit,
    ising: SparsePauliOp,
    offset: float,
    callback: list = None,
) -> float:
    """

    Args:
        x (np.ndarray):
        estimator: (EstimatorV2):
        qc (QuantumCircuit):
        ising (SparsePauliOp):
        offset (float):

    Returns:
    """

    ansatz = qc.copy()
    params_mapper = {param: value for param, value in zip(ansatz.parameters, x)}
    ansatz = ansatz.assign_parameters(parameters=params_mapper)
    pubs = [(ansatz, ising)]
    estimator_job = estimator.run(pubs=pubs)
    estimator_result = estimator_job.result()
    if not callback is None:
        callback.append(params_mapper)

    obj_val = estimator_result[0].data.evs + offset

    return obj_val


class ObjectiveOptuna:
    """"""

    def __init__(
        self,
        estimator: EstimatorV2,
        qc: QuantumCircuit,
        ising: SparsePauliOp,
        offset: float,
        bounds: tuple = (0, 2 * np.pi),
        callback: list = None,
    ) -> ObjectiveOptuna:
        """

        Args:
            estimator (EstimatorV2):
            qc (QuantumCircuit):
            ising (SparsePauliOp):
            offset (float):
            bounds (tuple, optional): . Defaults to (0, 4*np.pi).

        Returns:
        """
        self.estimator = estimator
        self.qc = qc
        self.ising = ising
        self.offset = offset
        self.bounds = bounds
        self.callback = callback

    def __call__(self, trial: Trial):
        ansatz = self.qc.copy()
        x = [
            trial.suggest_float(f"x[{i}]", self.bounds[0], self.bounds[1])
            for i in range(ansatz.num_parameters)
        ]
        params_mapper = {param: value for param, value in zip(ansatz.parameters, x)}
        ansatz = ansatz.assign_parameters(parameters=params_mapper)
        pubs = [(ansatz, self.ising)]
        estimator_job = self.estimator.run(pubs=pubs)
        estimator_result = estimator_job.result()
        if not self.callback is None:
            self.callback.append(params_mapper)

        obj_val = estimator_result[0].data.evs + self.offset

        return obj_val
