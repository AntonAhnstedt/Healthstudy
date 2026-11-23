import numpy as np
from scipy import stats

def calc_disease(df):
    """Räknar ut antalet och andelen sjuka"""
    df_sick = len(df[df["disease"] == 1])
    
    df_sick_prob = df["disease"].value_counts(normalize=True)
    df_sick_prob.index = ["Nej", "Ja"]
    return df_sick, df_sick_prob

def calc_bp_ci(df):
    """Räknar ut konfidensintervallet för blodtrycket"""
    df_bp = df["systolic_bp"]
    df_bp_mean = np.mean(df_bp)
    df_bp_std = np.std(df_bp, ddof=1)
    n = len(df_bp)

    se = df_bp_std / np.sqrt(n)
    t_val = stats.t.ppf(0.975, df=n-1)

    lower = df_bp_mean - t_val * se
    upper = df_bp_mean + t_val * se
    return lower, upper