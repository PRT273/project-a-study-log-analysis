from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from src.validate import validate_data
from src.metrics import longest_streak, break_days


def project_root() -> Path:
    # src/main.py -> project root
    return Path(__file__).resolve().parents[1]


def load_data(root: Path) -> pd.DataFrame:
    csv_path = root / "Data" / "study_log.csv"
    df = pd.read_csv(csv_path)

    # basic normalization (keep consistent with your notebook)
    df["date"] = pd.to_datetime(df["date"])
    return df


def ensure_dirs(root: Path) -> Path:
    fig_dir = root / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)
    return fig_dir


def plot_subject_breakdown(df: pd.DataFrame, fig_dir: Path) -> Path:
    subject_hours = (
        df.groupby("subject")["hours"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(6, 4))
    subject_hours.plot(kind="bar")
    plt.title("Total Study Hours by Subject")
    plt.ylabel("Hours")
    plt.tight_layout()

    out = fig_dir / "subject_breakdown.png"
    plt.savefig(out)
    plt.close()
    return out


def plot_daily_trend(df: pd.DataFrame, fig_dir: Path) -> Path:
    daily_hours = (
        df.groupby("date")["hours"]
        .sum()
        .sort_index()
    )

    plt.figure(figsize=(6, 4))
    daily_hours.plot(marker="o")
    plt.title("Daily Study Time Trend")
    plt.ylabel("Hours")
    plt.xlabel("Date")
    plt.tight_layout()

    out = fig_dir / "daily_trend.png"
    plt.savefig(out)
    plt.close()
    return out


def main() -> None:
    root = project_root()
    fig_dir = ensure_dirs(root)

    df = load_data(root)
    validate_data(df)

    # metrics
    ls = longest_streak(df)
    breaks = break_days(df)

    # plots
    p1 = plot_subject_breakdown(df, fig_dir)
    p2 = plot_daily_trend(df, fig_dir)

    print("✅ Analysis complete.")
    print(f"- Longest study streak (days): {ls}")
    print(f"- Break days (no study): {[d.date() for d in breaks]}")
    print(f"- Saved figures: {p1.name}, {p2.name}")


if __name__ == "__main__":
    main()
