import pandas as pd

from collections import namedtuple

from .base import BaseReader


class CSVReader(BaseReader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        df = pd.read_csv(self.file_path)
        list_of_column_names = list(df.columns)

        Data = namedtuple('Data', list_of_column_names)

        for index, row in df.iterrows():
            yield Data(*row)
