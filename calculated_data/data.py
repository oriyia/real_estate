from enum import Enum
import pandas as pd
import numpy as np


class InitialMortgageData(Enum):
    property_value = 2000000
    mortgage_rate = 0.06
    percent_down_payment = 0.15
    monthly_replenishment = 50000


class InitialDepositData(Enum):
    deposit_rate = 10
    monthly_replenishment = 50000
    frequency_capitalization = 12


class GeneralInformation(Enum):
    investment_term_year = 1
    investment_term_month = investment_term_year * 12


pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 3000)