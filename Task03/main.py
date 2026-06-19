# ============================================# ============================================
# Project 3: AI Recommendation Logic
# DecodeLabs Industrial Training - Batch 2026
# ============================================

import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# =============================================
# STEP 1: BUILD THE KNOWLEDGE BASE (Dataset)
# Job roles as "items" with their skill tags
# Loaded from raw_skills.csv instead of being hardcoded
# =============================================

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw_skills.csv")


def load_job_roles(csv_path):
    """
    Reads raw_skills.csv and rebuilds the same
    {role_name: skills_string} structure the rest
    of the script expects.
    """
    job_roles = {}

    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # Validate expected columns exist
            if reader.fieldnames is None or \
               "job_role" not in reader.fieldnames or \
               "skills" not in reader.fieldnames:
                raise ValueError(
                    "raw_skills.csv must have 'job_role' and 'skills' columns."
                )

            for row in reader:
                role = row["job_role"].strip()
                skills = row["skills"].strip()
                if role and skills:
                    job_roles[role] = skills

    except FileNotFoundError:
        print(f"ERROR: Could not find '{csv_path}'.")
        print("Make sure raw_skills.csv is in the same folder as main.py.")
        raise SystemExit(1)

    if not job_roles:
        print("ERROR: raw_skills.csv was found but contained no valid rows.")
        raise SystemExit(1)

    return job_roles


job_roles = load_job_roles(CSV_PATH)

# Convert to lists for processing
role_names = list(job_roles.keys())
role_descriptions = list(job_roles.values())

# =============================================
# STEP 2: BUILD THE TF-IDF ENGINE
# Fit on all job role descriptions
# =============================================

vectorizer = TfidfVectorizer()

# Fit and transform all job role descriptions into TF-IDF vectors
role_vectors = vectorizer.fit_transform(role_descriptions)

print("=" * 55)
print("   TECH STACK RECOMMENDER — DecodeLabs")
print("=" * 55)
print(f"Knowledge Base: {len(job_roles)} job roles loaded from raw_skills.csv")
print(f"Vocabulary Size: {len(vectorizer.vocabulary_)} unique skills")
print("=" * 55)

# =============================================
# MAIN RECOMMENDATION LOOP
# =============================================

def get_recommendations(user_skills, top_n=3):
    """
    Takes user skills as a string,
    returns top N matching job roles with scores.
    """

    # --- STEP 3: TRANSFORM USER INPUT using same vectorizer ---
    # CRITICAL: use transform() not fit_transform()
    # The vocabulary must be the same as the job roles
    user_vector = vectorizer.transform([user_skills])

    # --- STEP 4: SCORING — Calculate cosine similarity ---
    # Compare user vector against ALL job role vectors at once
    similarity_scores = cosine_similarity(user_vector, role_vectors)[0]

    # --- STEP 5: SORTING — Rank from highest to lowest ---
    ranked_indices = np.argsort(similarity_scores)[::-1]

    # --- STEP 6: FILTERING — Return only Top-N ---
    results = []
    for i in ranked_indices[:top_n]:
        results.append({
            "role": role_names[i],
            "score": similarity_scores[i],
            "skills": role_descriptions[i]
        })

    return results


# =============================================
# USER INPUT LOOP
# =============================================

while True:

    print("\nEnter your skills to get job role recommendations.")
    print("Type at least 3 skills separated by commas.")
    print("Type 'exit' to quit.\n")

    # --- INGESTION STEP: Collect minimum 3 skills ---
    while True:
        raw_input_str = input("Your Skills: ").strip()

        if raw_input_str.lower() == 'exit':
            break

        # Parse and clean the skills
        skills_list = [s.strip().lower().replace(" ", "_")
                       for s in raw_input_str.split(",")
                       if s.strip()]

        # Cold Start Protection — enforce minimum 3 skills
        if len(skills_list) < 3:
            print(f"  Please enter at least 3 skills. You entered {len(skills_list)}.")
            continue

        break

    if raw_input_str.lower() == 'exit':
        break

    # Join skills back to a single string for TF-IDF
    user_skills_string = " ".join(skills_list)

    print(f"\n  Parsed Skills : {skills_list}")
    print(f"  Searching {len(job_roles)} job roles...\n")

    # --- Get Recommendations ---
    recommendations = get_recommendations(user_skills_string, top_n=3)

    # --- Display Results ---
    print("=" * 55)
    print("   TOP 3 RECOMMENDED JOB ROLES FOR YOU")
    print("=" * 55)

    for rank, rec in enumerate(recommendations, 1):
        score_pct = rec['score'] * 100
        bar_filled = int(rec['score'] * 30)
        bar = "█" * bar_filled + "░" * (30 - bar_filled)

        print(f"\n  #{rank}  {rec['role']}")
        print(f"      Match : {score_pct:.1f}%")
        print(f"      Score : [{bar}]")

        # Show which of user's skills matched
        role_skill_set = set(rec['skills'].split())
        user_skill_set = set(skills_list)
        matched = user_skill_set.intersection(role_skill_set)

        if matched:
            print(f"      Matched Skills : {', '.join(matched)}")
        else:
            print(f"      Matched Skills : Related skills detected")

    print("\n" + "=" * 55)

    # --- Ask to continue ---
    again = input("\nGet another recommendation? (yes / exit): ").strip().lower()
    if again == 'exit' or again == 'no':
        break

print("\nThank you for using Tech Stack Recommender!")
print("=" * 55)
