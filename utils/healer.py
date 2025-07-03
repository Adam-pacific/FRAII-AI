def analyze_and_heal(df):
    fixes = []
    for col in df.columns:
        nulls = df[col].isnull().sum()
        if nulls > 0:
            fixes.append(f"Column '{col}' has {nulls} missing. Fill with mean or Unknown?")
    return fixes

def apply_fix(df, col):
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(df[col].mean())
    else:
        df[col] = df[col].fillna("Unknown")
    return df
