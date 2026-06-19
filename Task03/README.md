# AI Recommendation System

A beginner-friendly Artificial Intelligence project that recommends items based on user preferences using similarity matching techniques. This project demonstrates the core concepts behind recommendation systems used by platforms such as Netflix, YouTube, Spotify, and Amazon.

---

## Project Description

This project implements a simple content-based recommendation system. The system collects user preferences, compares them with predefined item attributes, calculates similarity scores, and recommends the most relevant items.

The primary objective is to understand how recommendation systems work before moving to advanced Machine Learning and Deep Learning recommendation engines.

### Key Learning Outcomes

- User Preference Modeling
- Vector Mapping
- Similarity Calculation
- Recommendation Ranking
- Pattern Matching
- Content-Based Filtering
- Basic AI Recommendation Logic

---

## Features

- Accepts user preferences as input
- Matches preferences against available items
- Calculates similarity scores
- Ranks recommendations by relevance
- Displays top recommendations
- Handles invalid and empty input
- Beginner-friendly implementation
- Easy to extend with additional items and categories

---

## Project Workflow

```text
User Input
    ↓
Preference Processing
    ↓
Vector Mapping
    ↓
Similarity Calculation
    ↓
Ranking
    ↓
Recommendation Generation
    ↓
Display Results
```


---

## Requirements / Teck Stack

- Python 3.x
- scikit-learn — TfidfVectorizer and cosine_similarity
- UV Package Manager
- Visual Studio Code (Recommended)

---

## Installation

### Clone Repository

```bash
git clone <repository-url>

```

### Create Virtual Environment

```bash
uv venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```




## Getting Started

Prerequisites

Python 3.9+
uv installed


Install uv (if you don't have it):

bash# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

1. Clone the repository

git clone <repo>
cd <repo-folder-name>

2. Sync dependencies

uv reads pyproject.toml / uv.lock and sets up an isolated virtual environment automatically:

uv sync

3. Run the project

uv run main.py

This launches the recommender — you'll be prompted to enter your skills, and the script will return the Top-N recommended job roles ranked by similarity score.
---


## Sample Usage

 ### Input:

python["Python", "Cloud Computing", "Automation"]

### Process:


Skills are mapped into the TF-IDF vector space built from all job roles' skill sets.
Cosine similarity is computed between the user vector and each job role vector.


### Output:

Top 3 Recommended Career Paths:
1. DevOps Engineer     — Score: 0.91
2. Cloud Architect     — Score: 0.84
3. SysAdmin            — Score: 0.68

---


### Project Structure

```
project03
│
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

---

## Future Improvements

- User Rating System
- Weighted Similarity Scores
- Cosine Similarity
- TF-IDF Based Matching
- Machine Learning Recommendation Engine
- Collaborative Filtering
- Embedding-Based Recommendations
- Database Integration
- Web Interface with Streamlit
- Personalized Recommendation History

---

## Concepts Covered

- Artificial Intelligence Fundamentals
- Recommendation Systems
- Similarity Matching
- Vector Representation
- Content-Based Filtering
- Data Structures
- Ranking Algorithms
- User Preference Modeling
- Error Handling
- Python Programming

---

## Conclusion

This project introduces the foundational concepts behind recommendation systems. Instead of predicting classes like traditional Machine Learning classifiers, the system recommends relevant items by comparing user preferences with item attributes using similarity logic.

It serves as an excellent stepping stone toward advanced recommendation engines, Machine Learning, embeddings, and Generative AI systems.