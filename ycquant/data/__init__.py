"""数据获取与存储"""

from .fetcher import get_daily, get_index_daily, get_financial
from .processor import clean, align
from .storage import (
    save_raw, load_raw,
    save_processed, load_processed,
    list_raw, has_raw,
    RAW_DIR, PROCESSED_DIR,
)
