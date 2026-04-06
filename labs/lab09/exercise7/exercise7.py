import pandas as pd


def promotion_candidates(filename):
    df = pd.read_csv(filename)

    avg_performance = round(df["PerformanceScore"].mean() , 1)
    min_years = 2
    candidates_df = df[
        (df['PerformanceScore'] > avg_performance) &
        (df['YearsOfService'] >= min_years)
    ]
    
    candidate_names = set(candidates_df['EmployeeName'])
    
    return {
        "average_performance": avg_performance,
        "min_years_required": min_years,
        "candidate_count": len(candidate_names),
        "candidate_names": candidate_names
    }


result = promotion_candidates("labs/lab09/data/employees.csv")
print(result)