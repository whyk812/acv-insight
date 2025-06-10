from pathlib import Path
import pandas as pd

def compute_stats(df: pd.DataFrame) -> dict:
    """
    DataFrame의 각 숫자형 컬럼에 대해
    평균, 표준편차, 최솟값, 최댓값을 계산하여
    {컬럼명: { 'mean':…, 'std':…, 'min':…, 'max':… }, …} 형태로 반환합니다.
    """
    