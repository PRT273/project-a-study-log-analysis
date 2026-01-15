# src/metrics.py
import pandas as pd

def longest_streak(df: pd.DataFrame) -> int:
    """
    Calculate the longest consecutive study streak (by date).
    """
    dates = (
        df[df["hours"] > 0]["date"]
        .dt.normalize()
        .drop_duplicates()
        .sort_values()
    )

    if dates.empty:
        return 0

    streak = 1
    max_streak = 1

    for i in range(1, len(dates)):
        if (dates.iloc[i] - dates.iloc[i - 1]).days == 1:
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1

    return max_streak

# src/metrics.py
import pandas as pd

def break_days(df: pd.DataFrame) -> pd.Series:
    daily = (
        df.groupby("date")["hours"]
          .sum()
          .reset_index()
    )
    breaks = daily[daily["hours"] == 0]["date"]
    return breaks