



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