# soil-pollutant-analysis
Analysis of pollutant breakdown in contaminated soil using environmental microbiology

## Overview
This repository contains scripts for analyzing pollutant breakdown rates in contaminated soil, with a focus on polycyclic aromatic hydrocarbons (PAHs). The main script `process_data.py` processes experimental data to calculate and normalize breakdown rates based on soil moisture content.

## Analysis Parameters

### Breakdown Rate Calculation
The breakdown rate is calculated as the fractional reduction in pollutant concentration over time:

```
breakdown_rate = (initial_concentration - final_concentration) / initial_concentration
```

Where:
- `initial_concentration`: pollutant concentration at the start of the experiment (column `pollutant_concentration_initial`)
- `final_concentration`: pollutant concentration at the end of the experiment (column `pollutant_concentration_final`)

### Soil Moisture Normalization
Soil moisture content significantly influences microbial activity and thus pollutant breakdown rates. To account for this, a moisture correction is applied:

```
corrected_breakdown_rate = breakdown_rate × (soil_moisture_pct / reference_moisture)
```

Where:
- `soil_moisture_pct`: measured soil moisture percentage (column `soil_moisture_pct`)
- `reference_moisture`: optimal soil moisture level, default set to 30%

This linear correction assumes that microbial activity scales proportionally with soil moisture up to the optimal level. The correction factor adjusts the raw breakdown rate to a value that would be expected under reference moisture conditions.

## Usage
1. Place your experimental data in `data/experiment.csv` with the required columns.
2. Run `python process_data.py`.
3. Results are saved in `results/breakdown_rates.csv`.

## Dependencies
- pandas
- numpy