# ============================================
# Project 2: Data Classification Using AI
# DecodeLabs Industrial Training - Batch 2026
# ============================================

# --- IMPORTS ---
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score
import pandas as pd

# --- STEP 1: LOAD DATA ---
iris = load_iris()
X = iris.data
y = iris.target
print(f"Dataset: {X.shape[0]} samples, {X.shape[1]} features, {len(iris.target_names)} classes")
print(f"Classes: {iris.target_names}\n")

# --- STEP 2: TRAIN-TEST SPLIT (split BEFORE scaling) ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

# --- STEP 3: FEATURE SCALING (fit on train only) ---
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --- STEP 4: TRAIN KNN MODEL ---
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
print("Model trained successfully!\n")

# --- STEP 5: PREDICT ---
predictions = model.predict(X_test)

# --- STEP 6: EVALUATE ---
print("=== CONFUSION MATRIX ===")
print(confusion_matrix(y_test, predictions))

print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, predictions, target_names=iris.target_names))

f1 = f1_score(y_test, predictions, average='weighted')
print(f"=== WEIGHTED F1 SCORE: {f1:.4f} ===")

# --- TEST ON A CUSTOM NEW FLOWER ---
import numpy as np
new_flower = np.array([[5.1, 3.5, 1.4, 0.2]])  # measurements you choose
new_flower_scaled = scaler.transform(new_flower)
prediction = model.predict(new_flower_scaled)
print(f"\nCustom flower prediction: {iris.target_names[prediction[0]]}")
