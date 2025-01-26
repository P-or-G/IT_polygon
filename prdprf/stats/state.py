from typing import Dict, List

import numpy as np
import pandas as pd
import reflex as rx

from prdprf.models import UserInfo

stats_csv = "stats.csv"


class TableState(rx.State):
    users: list[UserInfo] = []

    search_value: str = ""
    sort_value: str = ""
    sort_reverse: bool = False

    total_items: int = 0
    offset: int = 0
    limit: int = 12  # Строки на страницу