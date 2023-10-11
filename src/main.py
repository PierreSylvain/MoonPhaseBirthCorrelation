from modules.moon_phase import moon_phase
import pandas as pd
import scipy.stats as stats

if __name__ == "__main__":

    # Load data
    df = pd.read_csv("../data/TF_BIRTHS.txt", sep="|")

    # Convert the 'DT_DATE' column to a standard date format
    df['DT_DATE'] = pd.to_datetime(df['DT_DATE'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    # Apply the moon_phase function to each row in the DataFrame
    df = df.apply(moon_phase, axis=1)
    print(df)

    # Group the DataFrame by moon phase and calculate the average number of births for each phase
    mean_births_per_moon_phase = df.groupby("moon_phase")["MS_NUM_BIRTHS"].mean()
    print(mean_births_per_moon_phase)

    # Perform an Analysis of Variance (ANOVA) to test if the average number of births differs
    # significantly across the different moon phases
    f_value, p_value = stats.f_oneway(
        df["MS_NUM_BIRTHS"][df["moon_phase"] == "Gibbeuse croissante"],
        df["MS_NUM_BIRTHS"][df["moon_phase"] == "Gibbeuse décroissante"],
        df["MS_NUM_BIRTHS"][df["moon_phase"] == "Nouvelle lune"],
        df["MS_NUM_BIRTHS"][df["moon_phase"] == "Pleine lune"],
        df["MS_NUM_BIRTHS"][df["moon_phase"] == "Premier croissant"],
        df["MS_NUM_BIRTHS"][df["moon_phase"] == "Premier quartier"]
    )
    print(f"f-value: {f_value}")
    print(f"p-value: {p_value}")

    # Save modified DataFrame to a new CSV file
    df.to_csv("../data/BIRTHS_MOON_PHASE.csv", index=False)
