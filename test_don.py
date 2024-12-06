import pandas as pd
import numpy as np
import pytest
from don import Don

new_don = Don()
update_don = Don()

try:
    new_don.load_data('data.csv')
    update_don.load_data('data.csv')
except FileNotFoundError:
    new_don.load_data('tests/data.csv')
    update_don.load_data('tests/data.csv')