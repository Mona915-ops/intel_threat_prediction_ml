# utils.py

import pandas as pd

class PortScanUtils:
    @staticmethod
    def extract_features(df: pd.DataFrame) -> pd.DataFrame:
        """
        Select and clean numeric features from CICIDS2017 dataset.
        """
        df = df.replace([float('inf'), -float('inf')], pd.NA)
        df = df.dropna()

        # Drop non-numeric columns or identifiers
        cols_to_drop = ['Flow ID', 'Source IP', 'Destination IP', 'Timestamp',
                        'SimillarHTTP', 'Source Port', 'Destination Port', 'Protocol']
        df = df.drop(columns=[col for col in cols_to_drop if col in df.columns], errors='ignore')

        numeric_df = df.select_dtypes(include=['number'])

        if 'Label' in df.columns:
            numeric_df['Label'] = df['Label'].values

        return numeric_df
