import pandas as pd


def load_country_data(filepaths: dict) -> pd.DataFrame:
    frames = []
    for country, path in filepaths.items():
        df = pd.read_csv(path)
        df["Country"] = country
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def get_summary_stats(df: pd.DataFrame, metrics: list):
    return df.groupby("Country")[metrics].agg(["mean", "median", "std"]).round(2)
