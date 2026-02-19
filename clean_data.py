import pandas as pd


df=pd.read_csv("GlobalWeatherRepository.csv")

print("original shape :",df.shape)

print(df.head())


df=df.drop_duplicates()

print("new shape :",df.shape)

print("Missing Values : ",df.isnull().sum())

df.fillna(df.mean(numeric_only=True),inplace=True)


if "temperature_celsius" in df.columns:
    df = df[(df["temperature_celsius"] > -50) & (df["temperature_celsius"] < 60)]



df.columns = df.columns.str.lower().str.replace(" ", "_")

df.to_csv("cleaned_weather.csv", index=False)

print("Cleaned Shape:", df.shape)