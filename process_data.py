#!/usr/bin/env python3
"""
Data processing script for pollutant breakdown analysis.
Calculates breakdown rate of PAHs in contaminated soil.
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

def main():
    data_path = os.path.join('data', 'experiment.csv')
    if not os.path.exists(data_path):
        print(f"Data file not found: {data_path}")
        return
    
    df = load_data(data_path)
    df = calculate_breakdown_rate(df)
    
    # Save results
    output_path = os.path.join('results', 'breakdown_rates.csv')
    os.makedirs('results', exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")
    print(df.head())

if __name__ == '__main__':
    main()