# src/features.py
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, FunctionTransformer
from sklearn.impute import SimpleImputer

def _clip(X):
    """Clip values between -3 and 3"""
    return X.clip(-3, 3)

def build_numeric_preprocess():
    """
    Prétraitement amélioré :
    - imputation médiane
    - standardisation
    - clipping ([-3, 3])
    """
    return Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("clip", FunctionTransformer(_clip)),
    ])
