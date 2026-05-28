# %%

# Paket für Bearbeitung von Tabellen
import pandas as pd
import numpy as np

# Paket
## zuvor !pip install plotly
## ggf. auch !pip install nbformat
import plotly.express as px


def read_my_csv():
    # Einlesen eines Dataframes
    ## "\t" steht für das Trennzeichen in der txt-Datei (Tabulator anstelle von Beistrich)
    ## header = None: es gibt keine Überschriften in der txt-Datei
    df = pd.read_csv("data/ekg_data/01_Ruhe.txt", sep="\t", header=None)

    # Setzt die Columnnames im Dataframe
    df.columns = ["Messwerte in mV", "Zeit in ms"]

    # Gibt den geladen Dataframe zurück
    return df


# power original
# heartrate
# %%


def read_activity_csv():
    df = pd.read_csv("data/activities/activity.csv")
    df
    # noch auswählen welche daten ich genau brauch
    df["time in seconds"] = np.arange(len(df))
    df["time_in_minutes"] = df["time in seconds"] / 60
    return df


def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    fig = px.line(df.head(2000), x="Zeit in ms", y="Messwerte in mV")
    return fig


def make_power_hr_plot(df):

    fig = px.line(df, x="time_in_minutes", y=["PowerOriginal", "HeartRate"])
    return fig


def add_zones(df, hr_max):
    df["zone1"] = df["HeartRate"] < 120
    df["zone2"] = (df["HeartRate"] > 130) & (
        df["HeartRate"] < 150
    )  # gibt ein bool array aus!!!
    df["zone3"]
    df["zone4"]
    df["zone5"]


# %% Test

# df = read_my_csv()
# fig = make_plot(df)

# fig.show()

# %%
if __name__ == "__main__":
    # ekg_df = read_my_csv()
    # print(ekg_df.head())

    # ekg_fig = make_plot(ekg_df)
    # ekg_fig.show

    # zum testen
    df_activity = read_activity_csv()

    print(df_activity.head())
    pow_hr_figure = make_power_hr_plot(df_activity)
    pow_hr_figure.show()

    # df_activity["heartRate"] < 100
