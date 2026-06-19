# Iris Flower Classification using K-Nearest Neighbors (KNN) 🌸

A supervised learning project that trains a machine learning model to classify Iris flowers into one of three species — **Setosa**, **Versicolor**, or **Virginica** — based on their physical measurements. Built as **Project 2** of the DecodeLabs Industrial Training Program (Batch 2026).

This project marks the shift from hardcoded, rule-based logic to **Supervised Learning**: instead of writing `if/else` rules, the model is given historical, labeled data and learns the decision boundary between classes on its own.

---

## 📖 Project Description

The goal of this project is to build, train, and validate a basic classification model using a small, well-known dataset — the **Iris benchmark dataset**. The system takes four numerical flower measurements as input and predicts which of the three Iris species the flower belongs to, using the **K-Nearest Neighbors (KNN)** algorithm.

This is a foundational machine learning exercise that demonstrates the complete supervised learning pipeline: loading data, preprocessing, splitting, training, predicting, and evaluating — the same pipeline used in real-world production ML systems, just at a smaller, interpretable scale.

---

## 🎯 Key Learning Outcomes

By completing this project, the following skills are demonstrated:

- Loading and exploring a structured dataset
- Understanding the difference between **features** (inputs) and **labels** (outputs)
- Splitting data into **training** and **testing** sets correctly (with shuffling, to avoid order bias)
- Applying **feature scaling** so that all measurements contribute fairly to distance calculations
- Training a classification model using the **scikit-learn** `fit → predict` workflow
- Evaluating a model properly — going beyond raw accuracy into **confusion matrices**, **precision**, **recall**, and **F1 score**
- Recognizing the difference between **overfitting** and **underfitting** via the K value

---

## ✨ Features

- Loads the classic Iris dataset directly via `sklearn.datasets.load_iris()`
- Scales features using `StandardScaler` for fair distance-based comparison
- Splits data into training and testing sets using `train_test_split`
- Trains a `KNeighborsClassifier` to classify flowers into 3 species
- Predicts species for unseen test data
- Evaluates model performance with a confusion matrix, accuracy, precision, recall, and F1 score
- Simple, readable, single-script implementation — easy to extend or experiment with

---

## 🔄 Project Workflow

The project follows the **Input → Process → Output (IPO)** framework:

```
INPUT                    PROCESS                      OUTPUT
─────                    ───────                      ──────
Iris Dataset      →      Train-Test Split       →      Confusion Matrix
Feature Scaling          KNN Algorithm                 F1 Score
```

### Step-by-step pipeline:

1. **Load the Data** — Import the Iris dataset (150 samples, 3 balanced classes, 4 features each: sepal length, sepal width, petal length, petal width).
2. **Scale the Features** — Apply `StandardScaler` to normalize all features to mean = 0, variance = 1. This prevents features with larger numeric ranges from dominating the distance calculation that KNN relies on.
3. **Split the Data** — Shuffle and split the dataset into a **training set** (used to "teach" the model) and a **test set** (kept hidden, used only to validate performance).
4. **Train the Model** — Instantiate a `KNeighborsClassifier` and call `.fit(X_train, y_train)` so the model "memorizes" the training data points and their labels.
5. **Predict** — Call `.predict(X_test)` to classify the unseen test samples based on the majority vote of their **K nearest neighbors**.
6. **Evaluate** — Compare predictions against the true labels using a confusion matrix and metrics like accuracy, precision, recall, and F1 score — because in imbalanced or sensitive datasets, accuracy alone can be misleading.

---

## 🧠 Concepts Covered

| Concept | Description |
|---|---|
| **Supervised Learning** | Teaching a model using labeled historical data instead of writing manual rules |
| **Feature Scaling** | Normalizing numeric ranges (`StandardScaler`) so no single feature dominates distance-based calculations |
| **Train-Test Split** | Dividing data so the model is evaluated on data it has never seen, simulating real-world generalization |
| **K-Nearest Neighbors (KNN)** | A "proximity principle" algorithm — a new data point is classified by majority vote among its K closest neighbors in feature space |
| **Choosing K** | Small K (e.g. K=1) risks overfitting to noise; large K (e.g. K=100) risks underfitting/over-generalizing. The "elbow point" on an error-rate curve indicates a good K |
| **Confusion Matrix** | A table of True Positives, False Positives, False Negatives, and True Negatives — used to diagnose *how* a model is wrong, not just *whether* it's wrong |
| **Precision vs. Recall** | Precision favors trustworthiness (few false alarms); Recall favors sensitivity (few missed detections). Trade-offs depend on the use case |
| **F1 Score** | The harmonic mean of precision and recall — useful when you need a single balanced metric |
| **Accuracy Mirage** | In imbalanced datasets, high accuracy can hide poor performance on minority classes — a key reason to look beyond accuracy alone |

---

## 🛠️ Requirements / Tech Stack

- **Python 3.9+**
- **scikit-learn** — dataset loading, preprocessing, KNN model, evaluation metrics
- **numpy** — numerical operations
- **uv** — fast Python package & project manager (used instead of pip/venv/poetry)
- **VS Code** — development environment

---

## 📦 Installation

### Prerequisites
- [Python 3.9+](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) installed

Install uv (if not already installed):

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Clone the repository

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### Install dependencies

If a `pyproject.toml` already exists in the project, simply sync:

```bash
uv sync
```

If starting fresh, add the required packages:

```bash
uv add scikit-learn numpy
```

---

## 📁 Project Structure

```
.
├── main.py          # Core script: data loading, scaling, training, prediction, evaluation
├── pyproject.toml    # Project metadata & dependencies (managed by uv)
├── uv.lock           # Locked dependency versions
└── README.md         # You are here
```

---

## 🚀 Getting Started

Once dependencies are installed, run the project with:

```bash
uv run main.py
```

This will:
1. Load the Iris dataset
2. Scale the features
3. Split into training/test sets
4. Train the KNN classifier
5. Generate predictions on the test set
6. Print evaluation metrics (confusion matrix, accuracy, precision, recall, F1 score)

---

## 💡 Sample Usage

**Core model workflow** (the heart of `main.py`):

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# 4. Instantiate & train the model
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# 5. Predict
predictions = model.predict(X_test)

# 6. Evaluate
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
```

**Expected output (example):**
```
Confusion Matrix:
[[10  0  0]
 [ 0  9  1]
 [ 0  0 10]]

              precision    recall  f1-score   support
      setosa       1.00      1.00      1.00        10
  versicolor       1.00      0.90      0.95        10
   virginica       0.91      1.00      0.95        10

    accuracy                           0.97        30
```

> Actual numbers will vary slightly depending on `random_state` and the chosen value of `K`.

---

## 🛣️ Future Improvements

- [ ] Experiment with different values of K and plot the error-rate curve to find the optimal K (the "elbow")
- [ ] Compare KNN against other classification algorithms (Decision Trees, Logistic Regression, SVM)
- [ ] Add cross-validation instead of a single train-test split for more robust evaluation
- [ ] Visualize decision boundaries and the confusion matrix using matplotlib/seaborn
- [ ] Test the trained model against a completely new, unseen dataset
- [ ] Extend the pipeline toward more complex domains — e.g. moving from tabular data to computer vision (CNNs)

---

## ✅ Conclusion

This project demonstrates the complete, fundamental pipeline behind every supervised learning system: turning raw, labeled data into a model capable of making informed predictions on new, unseen inputs. By mastering the Iris classification pipeline — scaling, splitting, training, predicting, and evaluating — this project builds the foundation needed to tackle more advanced classification problems and algorithms in the future.

Built as part of the **DecodeLabs Industrial Training Kit — Batch 2026, Project 2: Data Classification Using AI**.

📍 Greater Lucknow, India · 🌎 [decodelabs.tech](https://www.decodelabs.tech)
