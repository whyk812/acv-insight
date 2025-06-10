import os
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import os
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(df: pd.DataFrame, column: str, bins: int = 30, output_dir: str = "outputs") -> str:
    """
    Plots a histogram for the specified column of the DataFrame and saves it as a PNG.

    Parameters:
    - df: pandas DataFrame containing the data.
    - column: Column name to plot.
    - bins: Number of bins for the histogram.
    - output_dir: Directory to save the plot.

    Returns:
    - Filepath of the saved histogram image.
    """
    # Prepare output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Plot histogram
    plt.figure()
    df[column].dropna().plot.hist(bins=bins)
    plt.title(f"Histogram of '{column}'")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()

    # Save the figure
    filename = f"{column}_histogram.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()

    return filepath

def plot_line(df: pd.DataFrame, x_col: str, y_col: str, output_dir: str = "outputs") -> str:
    """
    Plots a line graph of y_col vs x_col of the DataFrame and saves it as a PNG.

    Parameters:
    - df: pandas DataFrame containing the data.
    - x_col: Column name for x-axis.
    - y_col: Column name for y-axis.
    - output_dir: Directory to save the plot.

    Returns:
    - Filepath of the saved line graph image.
    """
    # Prepare output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Plot line graph
    plt.figure()
    plt.plot(df[x_col], df[y_col], marker="o")
    plt.title(f"{y_col} over {x_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.tight_layout()

    # Save the figure
    filename = f"{x_col}_vs_{y_col}_line.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath)
    plt.close()

    return filepath
