# 🛡️ Trustra — Trust-First AutoML Framework

Automated ML with built-in **fairness**, **drift detection**, **data leakage prevention**, and **audit-ready reporting**.

One `fit()` call. Full trust. Zero surprises.

## ✨ Features
- 🔍 Detects data leakage & duplicates
- ⚖️ Audits fairness (bias in gender, race, etc.)
- 📉 Detects data drift
- 🧠 Auto-trains best model (Optuna + XGBoost/RF)
- 📊 Generates interactive HTML trust report
- 🚀 One-line install: `pip install -e .`

## 🚀 Quick Start
```bash
git clone https://github.com/Devansh-567/Trustra---Trust-First-AutoML-Framework.git
cd Trustra---Trust-First-AutoML-Framework
pip install -e .
python examples/binary_classification.py
