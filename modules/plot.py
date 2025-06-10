import os
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(
    df: pd.DataFrame,
    column: str,
    output_dir: str = "outputs",
    bins: int = 10
) -> str:
    """
    df[column]의 히스토그램을 그려 PNG로 저장하고,
    파일 경로를 반환합니다.
    """
    # 출력 폴더 준비
    Path(output_dir).mkdir(exist_ok=True)
    filename = f"{column}_hist.png"
    filepath = os.path.join(output_dir, filename)

    # 플롯 생성
    plt.figure()
    df[column].dropna().hist(bins=bins)
    plt.title(f"Histogram of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()

    return filepath

def plot_line(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    output_dir: str = "outputs"
) -> str:
    """
    df[x_col]을 x축, df[y_col]을 y축으로 하는 선그래프를 그려 PNG로 저장하고,
    파일 경로를 반환합니다.
    """
    Path(output_dir).mkdir(exist_ok=True)
    filename = f"{x_col}_vs_{y_col}_line.png"
    filepath = os.path.join(output_dir, filename)

    plt.figure()
    plt.plot(df[x_col], df[y_col], marker="o")
    plt.title(f"{y_col} over {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()
    plt.savefig(filepath)
    plt.close()

    return filepath
