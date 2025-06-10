from pathlib import Path
import pandas as pd

def compute_stats(df: pd.DataFrame) -> dict:
    """
    DataFrame의 각 숫자형 컬럼에 대해
    평균, 표준편차, 최솟값, 최댓값을 계산하여
    {컬럼명: { 'mean':…, 'std':…, 'min':…, 'max':… }, …} 형태로 반환합니다.
    """
    stats = {}
    numeric_cols = df.select_dtypes(include="number").columns

    for col in numeric_cols:
        col_data = df[col].dropna()
        stats[col] = {
            "mean": col_data.mean(),
            "std": col_data.std(),
            "min": col_data.min(),
            "max": col_data.max(),
        }
    return stats