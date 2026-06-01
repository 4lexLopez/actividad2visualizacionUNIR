"""
Preparación y enriquecimiento del dataset causeofdeath.csv
para análisis en Google Looker Studio.
"""

import pandas as pd

import requests

url = (
"https://data360api.worldbank.org/data360/data?DATABASE_ID=WB_HNP&INDICATOR=WB_HNP_SH_STA_OWAD_ZS&TIME_PERIOD=2017&skip=0"
)

data = requests.get(url).json()
records = []

for key in data["value"]:
    records.append({
        "OBS_VALUE": key["OBS_VALUE"],
        "SEX": key["SEX"],
        "TIME_PERIOD": key["TIME_PERIOD"]
    })

life_df = pd.DataFrame(records)
life_df.to_csv(
    "indiceObesidad2017.csv",
    index=False,
    encoding="utf-8-sig"
)

INPUT_FILE = "causeofdeath.csv"

df = pd.read_csv(INPUT_FILE, sep=";")

print("Dimensiones:", df.shape)
print(df.head())

print("\nValores nulos:")
print(df.isnull().sum())

print("\nTipos de datos:")
print(df.dtypes)

df["Value"] = (
    df["Value"]
    .astype(str)
    .str.replace(",", ".", regex=False)
    .astype(float)
)

pivot_df = (
    df.pivot_table(
        index=[
            "Location",
            "Age",
            "Sex",
            "Cause of death or injury"
        ],
        columns="Measure",
        values="Value",
        aggfunc="first"
    )
    .reset_index()
)

pivot_df.columns.name = None

if "Percent of total deaths 2017" in pivot_df.columns:
    top_causes = (
        pivot_df
        .sort_values(
            "Percent of total deaths 2017",
            ascending=False
        )
        .head(10)
    )
    print(top_causes)

if "Deaths annual % change 2010-2017" in pivot_df.columns:
    growing_causes = (
        pivot_df
        .sort_values(
            "Deaths annual % change 2010-2017",
            ascending=False
        )
        .head(10)
    )
    print(growing_causes)

pivot_df.to_csv(
    "cause_of_death_prepared.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Archivo exportado correctamente")
