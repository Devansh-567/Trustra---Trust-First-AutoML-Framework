# examples/binary_classification.py
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from trustra import TrustRA  # ✅ Updated import

X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
X = pd.DataFrame(X, columns=[f"feature_{i}" for i in range(10)])
y = pd.Series(y, name="target")
X["gender"] = pd.Categorical(np.random.choice([0, 1], size=len(X)))

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

model = TrustRA(target="target", sensitive_features=["gender"], timeout=60)
model.fit(X_train, y_train, X_val, y_val)

print("✅ First 5 predictions:", model.predict(X_val)[:5])
