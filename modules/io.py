from pathlib import Path
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """
    주어진 CSV 파일을 DataFrame으로 읽어 반환합니다.
    파일이 없거나 파싱 오류 시 예외를 발생시킵니다.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {path}")

    try:
        df = pd.read_csv(p)
    except pd.errors.ParserError as e:
        raise pd.errors.ParserError(f"CSV ParserError: {e}")
    except Exception as e:
        raise RuntimeError(f"CSV 읽기 중 알 수 없는 오류 발생: {e}")

    return df