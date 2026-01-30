from dataclasses import dataclass
from typing import Dict, Any

import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)


@dataclass
class EvalResult:
    metrics: Dict[str, Any]
    cm : np.ndarray
    fpr: np.ndarray
    tpr: np.ndarray
    thresholds: np.ndarray


def evaluate_binary(y_true, y_pred, y_proba) -> EvalResult:
    acc = accuracy_score(y_true, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true, y_pred, average="binary", zero_division=0
    )

    cm = confusion_matrix(y_true, y_pred)

    auc = roc_auc_score(y_true, y_proba)
    fpr, tpr, thresholds = roc_curve(y_true, y_proba)

    metrics = {
        "accuracy": acc,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "roc_auc": auc,
    }
    return EvalResult(metrics=metrics, cm=cm, fpr=fpr, tpr=tpr, thresholds=thresholds)