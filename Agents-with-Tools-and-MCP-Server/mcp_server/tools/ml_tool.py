"""
Machine Learning Recommendation Tool
"""

def recommend_ml_model(problem: str) -> str:

    problem = problem.lower()

    if "predict" in problem:
        return "Recommended Model: Linear Regression"

    elif "classify" in problem:
        return "Recommended Model: Random Forest Classifier"

    elif "cluster" in problem:
        return "Recommended Model: K-Means Clustering"

    return "Recommended Model: Decision Tree"