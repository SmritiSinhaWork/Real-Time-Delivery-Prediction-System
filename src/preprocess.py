import pandas as pd

TRAFFIC_MAP = {'low': 1, 'medium': 2, 'high': 3}
WEATHER_MAP = {'clear': 0, 'rainy': 1}

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['traffic_level'] = df['traffic_level'].map(TRAFFIC_MAP)
    df['weather'] = df['weather'].map(WEATHER_MAP)
    return df