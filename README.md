# Moon Phase and Birth Correlation

## Description

This project aims to analyze and debunk the widely-held belief that lunar phases influence birth rates.
Using a dataset from Statbel combined with the ephem library and statistical analysis, we explore whether
there is a correlation between moon phases and daily birth counts.

## Data

The data used in this project includes:

- The date
- Number of births on that date
- Moon phase on that date
- Moon Emoji

Data Source: [StatBel](https://statbel.fgov.be/sites/default/files/files/opendata/bevolking/Geboorte/TF_BIRTHS.zip)

The moon phases used in this analysis are computed using the `ephem` Python library.

## Methodology

### Data exploration to understand the distribution of births across lunar phases.

| Index | DT_DATE    | MS_NUM_BIRTHS | moon_phase       | moon_emoji |
|------:|------------|--------------:|------------------|------------|
|     0 | 1992-01-01 |           219 | Dernier quartier | 🌗         |
|     1 | 1992-01-02 |           331 | Dernier quartier | 🌗         |
|     2 | 1992-01-03 |           420 | Dernier quartier | 🌗         |
|     3 | 1992-01-04 |           282 | Dernier quartier | 🌗         |
|     4 | 1992-01-05 |           252 | Nouvelle lune    | 🌑         |

| moon_phase            | Mean birth |
|-----------------------|------------|
| Dernier croissante    | 305.774194 |   
| Dernier quartier      | 326.302622 |  
| Gibbeuse croissante   | 327.135288 | 
| Gibbeuse décroissante | 328.247167 | 
| Nouvelle lune         | 326.799479 | 
| Pleine lune           | 327.502678 | 
| Premier croissant     | 325.645472 | 
| Premier quartier      | 327.458657 | 

### Hypothesis testing (ANOVA) to determine if birth averages vary significantly across different lunar phases.
 - f-value: 0.13819272173295818
 - p-value: 0.9834565625981031

## Results

We have stated the following assumptions:
$$H_0$$: There is no correlation between moon phases and births.
$$H_1$$: There is a correlation between moon phases and births.

To test these hypotheses, we performed an ANOVA test, which compares the means of several groups.

Results:

F-value: 0.1381
p-value: 0.9834

**The ANOVA test showed no significant difference in birth counts across lunar phases.**

> There's no evidence supporting the belief that lunar phases influence birth rates.

## How to Run the Code

First download the dataset from StatBel website.

````shell
$ pip install -r requirements.txt
$ cd src
$ python main.py
````

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

A big thank you to Lucile who inspired me for this project. I hope you changed your beliefs.