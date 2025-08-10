import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather_copy = weather.copy()
    weather_copy['yesterdayDate'] = weather_copy['recordDate'] - pd.Timedelta(days=1)
    merged = weather_copy.merge(
        weather,
        left_on='yesterdayDate',
        right_on='recordDate',
        suffixes=('_today','_yesterday')
    )
    result = merged[merged['temperature_today'] > merged['temperature_yesterday']]
    
    result = result.rename(columns={'id_today':'Id'})
    return result[['Id']]
