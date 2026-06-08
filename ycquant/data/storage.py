"""本地数据存储层
使用 Parquet 格式读写数据，按类别存放在 data/raw/ 和 data/processed/ 下。
"""

from pathlib import Path
import pandas as pd

# 项目根目录 → data/
DATA_DIR = Path(__file__).resolve().parent
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# 确保目录存在
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
(RAW_DIR / "stock").mkdir(exist_ok=True)
(RAW_DIR / "index").mkdir(exist_ok=True)
(RAW_DIR / "financial").mkdir(exist_ok=True)


def save_raw(df: pd.DataFrame, name: str, category: str = "stock"):
    """保存原始数据为 Parquet

    Args:
        df: 数据 DataFrame
        name: 文件名（不含扩展名），如 '000001'
        category: 类别目录，stock / index / financial
    """
    filepath = RAW_DIR / category / f"{name}.parquet"
    df.to_parquet(filepath, index=True)
    print(f"[storage] 原始数据已保存: {filepath}")


def load_raw(name: str, category: str = "stock") -> pd.DataFrame | None:
    """加载原始数据

    Args:
        name: 文件名（不含扩展名）
        category: 类别目录

    Returns:
        DataFrame，文件不存在则返回 None
    """
    filepath = RAW_DIR / category / f"{name}.parquet"
    if filepath.exists():
        return pd.read_parquet(filepath)
    return None


def save_processed(df: pd.DataFrame, name: str):
    """保存清洗后的数据"""
    filepath = PROCESSED_DIR / f"{name}.parquet"
    df.to_parquet(filepath, index=True)
    print(f"[storage] 处理后数据已保存: {filepath}")


def load_processed(name: str) -> pd.DataFrame | None:
    """加载清洗后的数据"""
    filepath = PROCESSED_DIR / f"{name}.parquet"
    if filepath.exists():
        return pd.read_parquet(filepath)
    return None


def list_raw(category: str = "stock") -> list[str]:
    """列出某类已缓存的数据名称"""
    dir_path = RAW_DIR / category
    if not dir_path.exists():
        return []
    return sorted([f.stem for f in dir_path.glob("*.parquet")])


def has_raw(name: str, category: str = "stock") -> bool:
    """检查某数据是否已缓存"""
    return (RAW_DIR / category / f"{name}.parquet").exists()
