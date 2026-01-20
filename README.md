# mlops-ml-project (baseline)

Mini-projet ML avec versioning Git - Atelier DevOps & MLOps

## Installation

```bash
python3 -m venv .venv
# Activer le venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

## Entraînement

```bash
PYTHONPATH=. python3 scripts/train.py
```

## Évaluation

```bash
PYTHONPATH=. python3 scripts/evaluate.py
```

## Artefacts

Après l'entraînement et l'évaluation, les artefacts suivants sont générés dans `artifacts/`:

- `artifacts/model.joblib` - Modèle entraîné (pipeline complet)
- `artifacts/metrics.json` - Métriques de performance (accuracy, F1-macro)
- `artifacts/confusion_matrix.png` - Matrice de confusion visualisée
- `artifacts/report.json` - Rapport détaillé de classification

## Structure du projet

```
mlops-ml-project/
├── README.md
├── requirements.txt
├── config/
│   └── train.yaml          # Configuration de l'entraînement
├── src/
│   ├── __init__.py
│   ├── data.py             # Chargement des données
│   ├── features.py         # Prétraitement
│   └── model.py            # Construction du modèle
├── scripts/
│   ├── train.py            # Script d'entraînement
│   └── evaluate.py         # Script d'évaluation
├── tests/
│   └── test_config.py      # Tests
├── notebooks/              # Notebooks Jupyter
├── data/                   # Données (non versionnées)
└── artifacts/              # Artefacts ML (non versionnés)
```

## Dataset

Par défaut, le projet utilise le dataset **Iris** de scikit-learn pour garantir la reproductibilité sans dépendance externe.

## Configuration

La configuration se trouve dans `config/train.yaml`:
- Type de données (iris ou csv)
- Paramètres de split (test_size, random_state)
- Paramètres du modèle (Logistic Regression)
