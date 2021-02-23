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


pd.set_option('display.max_columns', 14)
desired_width = 3000
pd.set_option('display.width', desired_width)


def calculation_income_investment():
    investment_table = pd.DataFrame(columns=['accumulated_amount', 'replenishment', 'increase_percentage',
                                             'increase_percentage_total', 'increase_interest'])
    investment_table.loc[0] = [50000, 50000, 0, 0, 0]
    for x in range(GeneralInformation.investment_term_month.value - 1):
        increase_percentage = investment_table.loc[x].accumulated_amount * \
                              InitialDepositData.deposit_rate.value * 30 / (100 * 365)
        increase_percentage_total = increase_percentage + investment_table.loc[x].increase_percentage_total
        replenishment = investment_table.loc[x].replenishment + InitialDepositData.monthly_replenishment.value
        accumulated_amount = investment_table.loc[x].accumulated_amount + increase_percentage + InitialDepositData.monthly_replenishment.value
        increase_interest = increase_percentage - investment_table.loc[x].increase_percentage
        investment_table.loc[x+1] = [accumulated_amount, replenishment, increase_percentage,
                                     increase_percentage_total, increase_interest]
    return investment_table


df = calculation_income_investment()
print(df)




