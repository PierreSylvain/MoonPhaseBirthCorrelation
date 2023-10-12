import ephem


def moon_phase(row):
    """Determine the moon phase based on the given date
        :param row: DataFrame row
        :returns: DataFrame row with 2 new columns (moon_phase and moon_emoji)
    """

    # Calculate the date of the previous new moon for the given date
    previous_new_moon = ephem.previous_new_moon(row['DT_DATE'])

    # Calculate the age of the moon by subtracting the date of the previous
    # new moon from the given date
    age_of_moon = (ephem.Date(row['DT_DATE']) - ephem.Date(previous_new_moon))

    # Determine the moon phase based on the age of the moon
    if age_of_moon < 1:
        row['moon_phase'] = "Nouvelle lune"
        row['moon_emoji'] = "🌑"
    elif 1 <= age_of_moon < 3.7:
        row['moon_phase'] = "Premier croissant"
        row['moon_emoji'] = "🌒"
    elif 3.7 <= age_of_moon < 7.4:
        row['moon_phase'] = "Premier quartier"
        row['moon_emoji'] = "🌓"
    elif 7.4 <= age_of_moon < 14.8:
        row['moon_phase'] = "Gibbeuse croissante"
        row['moon_emoji'] = "🌔"
    elif 14.8 <= age_of_moon < 22.1:
        row['moon_phase'] = "Pleine lune"
        row['moon_emoji'] = "🌕"
    elif 22.1 <= age_of_moon < 25.8:
        row['moon_phase'] = "Gibbeuse décroissante"
        row['moon_emoji'] = "🌖"
    elif 25.8 <= age_of_moon < 29.5:
        row['moon_phase'] = "Dernier quartier"
        row['moon_emoji'] = "🌗"
    else:
        row['moon_phase'] = "Dernier croissante"
        row['moon_emoji'] = "🌘"

    return row
