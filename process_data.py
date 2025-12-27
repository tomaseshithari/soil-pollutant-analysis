#!/usr/bin/env python3
"""
Data processing script for pollutant breakdown analysis.
Calculates breakdown rate of PAHs in contaminated soil.
Now includes soil moisture normalization.
"""

import pandas as pd
import numpy as np
import os

def load_data(data_path):
    """Load experimental data from CSV file."""
    df = pd.read_csv(data_path)
    return df

def calculate_breakdown_rate(df):
    """
    Calculate breakdown rate based on initial and final concentrations.
    Assumes columns: pollutant_concentration_initial, pollutant_concentration_final
    """
    df['breakdown_rate'] = (df['pollutant_concentration_initial'] - df['pollutant_concentration_final']) / df['pollutant_concentration_initial']
    return df

def normalize_by_moisture(df, reference_moisture=30.0):
    """
    Normalize breakdown rate based on soil moisture percentage.
    
    Parameters:
    - df: DataFrame with columns 'breakdown_rate' and 'soil_moisture_pct'
    - reference_moisture: optimal soil moisture percentage (default 30%)
    
    Returns:
    - DataFrame with added column 'corrected_breakdown_rate'
    """
    # Simple linear correction: rate * (moisture / reference)
    # Ensure no division by zero
    if reference_moisture <= 0:
        raise ValueError("reference_moisture must be positive")
    
    df['corrected_breakdown_rate'] = df['breakdown_rate'] * (df['soil_moisture_pct'] / reference_moisture)
    return df

def main():
    data_path = os.path.join('data', 'experiment.csv')
    if not os.path.exists(data_path):
        print(f"Data file not found: {data_path}")
        return
    
    df = load_data(data_path)
    df = calculate_breakdown_rate(df)
    df = normalize_by_moisture(df, reference_moisture=30.0)
    
    # Save results
    output_path = os.path.join('results', 'breakdown_rates.csv')
    os.makedirs('results', exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
    print(df.head())

if __name__ == '__main__':
    main()