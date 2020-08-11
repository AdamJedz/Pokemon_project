import pandas as pd
import numpy as np
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')


class DataLoader:

    def __init__(self, file_name: str) -> None:

        self.file_name = file_name

    def __str__(self) -> None:
        print(f'DataLoader reads {self.file_name}.csv from Data folder.')

    def __call__(self) -> pd.DataFrame:
        df = self._read_data()
        return df

    def _read_data(self) -> pd.DataFrame:
        df = pd.read_csv(f'../Data/{self.file_name}.csv').drop('Unnamed: 0', axis=1)
        return df


def run_script(file_name: str = 'pokedex') -> pd.DataFrame:
    data_loader = DataLoader(file_name)
    df = data_loader()
    return df


if __name__ == '__main__':
    pd.options.display.max_columns = 999
    df = run_script()
    print(df.head())