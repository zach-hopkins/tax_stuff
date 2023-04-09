def arizona_state_tax(salary):
    tax_bracket_1 = 28653
    tax_rate_1 = .0255
    tax_rate_2 = .0298

    if salary <= 0:
        return 0
    elif salary <= tax_bracket_1:
        return tax_rate_1 * salary
    else:
        return tax_rate_2 * (salary - tax_bracket_1) + (tax_bracket_1 * tax_rate_1)
    
def federal_tax(salary):
    tax_bracket_1 = 11000
    tax_bracket_2 = 44725
    tax_bracket_3 = 95375
    tax_bracket_4 = 182100
    tax_bracket_5 = 231250
    tax_bracket_6 = 578125
    tax_rate_1 = .10
    tax_rate_2 = .12
    tax_rate_3 = .22
    tax_rate_4 = .24
    tax_rate_5 = .32
    tax_rate_6 = .35
    tax_rate_7 = .37

    max_bracket_1 = tax_bracket_1 * tax_rate_1
    max_bracket_2 = (tax_bracket_2 - tax_bracket_1) * tax_rate_2 + max_bracket_1
    max_bracket_3 = (tax_bracket_3 - tax_bracket_2) * tax_rate_3 + max_bracket_2
    max_bracket_4 = (tax_bracket_4 - tax_bracket_3) * tax_rate_4 + max_bracket_3
    max_bracket_5 = (tax_bracket_5 - tax_bracket_4) * tax_rate_5 + max_bracket_4
    max_bracket_6 = (tax_bracket_6 - tax_bracket_5) * tax_rate_6 + max_bracket_5

    if salary <= 0:
        return 0
    elif salary <= tax_bracket_1:
        return tax_rate_1 * salary
    elif salary <= tax_bracket_2:
        return max_bracket_1 + (salary - tax_bracket_1) * tax_rate_2
    elif salary <= tax_bracket_3:
        return max_bracket_2 + (salary - tax_bracket_2) * tax_rate_3
    elif salary <= tax_bracket_4:
        return max_bracket_3 + (salary - tax_bracket_3) * tax_rate_4
    elif salary <= tax_bracket_5:
        return max_bracket_4 + (salary - tax_bracket_4) * tax_rate_5
    elif salary <= tax_bracket_6:
        return max_bracket_5 + (salary - tax_bracket_5) * tax_rate_6
    else:
        return max_bracket_6 + (salary - tax_bracket_6) * tax_rate_7


def arizona_effective_tax_rate(salary):
    tax_liability = arizona_state_tax(salary)
    taxable_income = salary - 12500  # Standard deduction for single filer
    return tax_liability / taxable_income


#Adjust These
income = 65000
assetExpenses = 25000


salary = income - assetExpenses
federalTax = federal_tax(salary)
stateTax = arizona_state_tax(salary)
effectiveStateTaxRate = stateTax / income
effectiveFederalTaxRate = federalTax / income
totalTax = federalTax + stateTax
totalCash = income - assetExpenses - totalTax
netGained = salary + assetExpenses - totalTax
hypotheticalTaxesWithoutExpenses = federal_tax(income) + arizona_state_tax(income)
hypotheticalSalary = income - hypotheticalTaxesWithoutExpenses
print(f"""Based on your income of ${income:,.0f} and asset purchases totaling ${assetExpenses:,.0f}, your take-home pay pre-taxes would be ${salary:,.0f}. You would have ${salary - totalTax:,.0f} in net take-home pay after taxes of ${totalTax:,.0f}. You would have a net worth of ${netGained:,.0f} (assets + income) at the end of the year. Without the asset purchase strategy, your net worth would have been ${hypotheticalSalary:,.0f} (all towards taxes). By implementing the asset purchase strategy, you increase your net worth by ${netGained - hypotheticalSalary:,.0f}, but you would have ${hypotheticalSalary - totalCash:,.0f} less cash on hand. If you are purchasing assets, you can set your tax witholding to {effectiveStateTaxRate:.2%} for state and {effectiveFederalTaxRate:.2%} for federal""")


