from crowds.kanonymity import ola
from crowds.kanonymity.generalizations import GenRule
from crowds.kanonymity import information_loss
import pandas as pd

##################################
### GENERALIZATION HIERARCHIES ###
##################################

def generalize_age_1(value):
    return '<25' if value < 25 else '25-30' if value < 30 else '30-40' if value < 40 else '>40'

def generalize_age_2(value):
    return '<30' if value < 30 else '30-40' if value < 40 else '>40'

def generalize_age_3(value):
    return '<40' if value < 40 else '>40'

age_hierarchy = [generalize_age_1, generalize_age_2, generalize_age_3]


def generalize_limit_bal1(value):
    return '<50K' if value < 50000 else '50K-140K' if value < 140000 else '140K-240K' if value < 240000 else '>240K'

def generalize_limit_bal2(value):
    return '<75K' if value < 75000 else '75K-200K' if value < 200000 else '>200K'

def generalize_limit_bal3(value):
    return '<140K' if value < 140000 else '>140K'

limit_bal_hierarchy = [generalize_limit_bal1, generalize_limit_bal2, generalize_limit_bal3]


def generalize_educationsmall1(value):
    return 'school' if value in [1, 3] else 'university' if value == 2 else 'others'

def generalize_educationsmall2(value):
    return 'university' if value == 2 else 'non-university'

educationsmall_hierarchy = [generalize_educationsmall1, generalize_educationsmall2]


def generalize_education1(value):
    value = value.strip()

    if value in ['1st 2nd 3rd or 4th grade', '5th or 6th grade', '7th and 8th grade', '9th grade', '10th grade',
                 '11th grade', '12th grade no diploma', 'Less than 1st grade']:
        return "Pre-High School Education"
    elif value == 'High school graduate':
        return "High School Graduate"
    elif value == 'Some college but no degree':
        return "Some College, No Degree"
    elif value in ['Associates degree-academic program', 'Associates degree-occup /vocational']:
        return "Associate's Degree"
    elif value == 'Bachelors degree':
        return "Bachelor's Degree"
    elif value == 'Prof school degree':
        return "Professional Degree"
    elif value == 'Masters degree':
        return "Master's Degree"
    elif value == 'Doctorate degree':
        return "Doctorate Degree"

def generalize_education2(value):
    value = value.strip()

    if value in ['1st 2nd 3rd or 4th grade', '5th or 6th grade', '7th and 8th grade', '9th grade', '10th grade',
                 '11th grade', '12th grade no diploma', 'Less than 1st grade']:
        return "Pre-High School Education"
    elif value == 'High school graduate':
        return "High School Graduate"
    elif value == 'Some college but no degree':
        return "Some College, No Degree"
    elif value == 'Bachelors degree':
        return "Bachelor's Degree"
    elif value in ['Masters degree','Associates degree-academic program', 'Associates degree-occup /vocational',
                   'Prof school degree', 'Doctorate degree']:
        return "other Degree"

def generalize_education3(value):
    value = value.strip()

    if value == 'High school graduate':
        return "High School Graduate"
    elif value == 'Some college but no degree':
        return "Some College, No Degree"
    else:
        return 'some Degree'

education_hierarchy = [generalize_education1, generalize_education2, generalize_education3]


def generalize_bill_amt1(value):
    return '<3500' if value < 3500 else '3500-25000' if value < 25000 else '25000-65000' if value < 65000 else '>65000'

def generalize_bill_amt2(value):
    return '<15000' if value < 15000 else '15000-45000' if value < 45000 else '>45000'

def generalize_bill_amt3(value):
    return '<25000' if value < 25000 else '>25000'

bill_amt_hierarchy = [generalize_bill_amt1, generalize_bill_amt2, generalize_bill_amt3]


def generalize_pay_amt1(value):
    return '<1000' if value < 1000 else '1000-2000' if value < 2000 else '2000-5000' if value < 5000 else '>5000'

def generalize_pay_amt2(value):
    return '<1500' if value < 1500 else '1500-3500' if value < 3500 else '>3500'

def generalize_pay_amt3(value):
    return '<2000' if value < 2000 else '>2000'

pay_amt_hierarchy = [generalize_pay_amt1, generalize_pay_amt2, generalize_pay_amt3]


def generalize_bloodpressure1(value):
    return '<60' if value < 60 else '60-70' if value < 70 else '70-80' if value < 80 else '>80'

def generalize_bloodpressure2(value):
    return '<65' if value < 65 else '65-75' if value < 75 else '>75'

def generalize_bloodpressure3(value):
    return '<70' if value < 70 else '>70'

blood_pressure_hierarchy = [generalize_bloodpressure1, generalize_bloodpressure2, generalize_bloodpressure3]


def generalize_insulin1(value):
    return '<5' if value < 5 else '5-25' if value < 25 else '25-130' if value < 130 else '>130'

def generalize_insulin2(value):
    return '<10' if value < 10 else '10-75' if value < 75 else '>75'

def generalize_insulin3(value):
    return '<20' if value < 20 else '>20'

insulin_hierarchy = [generalize_insulin1, generalize_insulin2, generalize_insulin3]


def generalize_marital_1(value):
    value = value.strip()

    if value == 'Never married':
        return 'Never married'
    elif value == 'Divorced':
        return 'Divorced'
    elif value == 'Separated':
        return 'Separated'
    elif value in ['Married-civilian spouse present', 'Married-A F spouse present', 'Married - spouse absent']:
        return 'Married'
    elif value == 'Widowed':
        return 'Widowed'
    else:
        return 'Unknown'

def generalize_marital_2(value):
    value = value.strip()

    if value in ['Never married', 'Separated', 'Divorced']:
        return 'Single'
    elif value in ['Married-civilian spouse present', 'Married-A F spouse present', 'Married - spouse absent']:
        return 'Married'
    elif value == 'Widowed':
        return 'Widowed'
    else:
        return 'Unknown'

def generalize_marital_3(value):
    value = value.strip()

    if value in ['Married-civilian spouse present', 'Married-A F spouse present', 'Married - spouse absent']:
        return 'Married'
    else:
        return 'Not-Married'

marital_hierarchy = [generalize_marital_1, generalize_marital_2, generalize_marital_3]

def generalize_country_1(value):
    value = value.strip()
    if value == 'United-States':
        return 'United-States'
    elif value in ['Canada', 'Mexico', 'Puerto-Rico']:
        return 'North America'
    elif value in ['England', 'Ireland', 'France', 'Germany', 'Portugal']:
        return 'Western Europe'
    elif value in ['Poland', 'Hungary', 'Yugoslavia']:
        return 'Eastern Europe'
    elif value in ['Italy', 'Spain', 'Greece']:
        return 'Southern Europe'
    elif value in ['Vietnam', 'Philippines', 'Cambodia', 'Laos', 'Thailand']:
        return 'Southeast Asia'
    elif value in ['China', 'Japan', 'South Korea', 'Taiwan', 'Hong Kong']:
        return 'East Asia'
    elif value in ['India']:
        return 'South Asia'
    elif value in ['Cuba', 'Dominican-Republic', 'Jamaica', 'Puerto-Rico']:
        return 'Caribbean'
    elif value in ['Ecuador', 'Peru', 'Panama']:
        return 'South America'
    else:
        return 'Unknown'

def generalize_country_2(value):

    if pd.isna(value):
        return 'unknown'

    value = value.strip()
    if value == 'United-States':
        return 'United-States'
    elif value in ['Mexico', 'Canada', 'Puerto-Rico', 'Outlying-U S (Guam USVI etc)']:
        return 'North America'
    elif value in ['Columbia', 'England', 'Poland', 'Ireland', 'Italy', 'Yugoslavia', 'Portugal', 'Germany', 'France', 'Scotland', 'Greece', 'Holand-Netherlands']:
        return 'Europe'
    elif value in ['Vietnam', 'Taiwan', 'Philippines', 'China', 'Japan', 'South Korea', 'Cambodia', 'Hong Kong', 'Laos', 'Thailand', 'India']:
        return 'Asia'
    elif value in ['Cuba', 'Dominican-Republic', 'El-Salvador', 'Nicaragua', 'Puerto-Rico', 'Jamaica', 'Ecuador', 'Peru', 'Honduras']:
        return 'Central/South America'
    else:
        return 'Unknown'

def generalize_country_3(value):
    if pd.isna(value):
        return 'unknown'

    value = value.strip()
    if value == 'United-States':
        return 'United-States'
    else:
        return 'not US'

country_hierarchy = [generalize_country_1, generalize_country_2, generalize_country_3]

############################
### PIMA Indian Diabetes ###
############################

# Load data
PID_training = pd.read_csv('data/PID_train.csv', sep=",")
PID_test = pd.read_csv('data/PID_test.csv', sep=",")

# Convert to correct data types
PID_training['Outcome'] = PID_training['Outcome'].astype('category')
PID_test['Outcome'] = PID_test['Outcome'].astype('category')

# Generalization rules
generalization_rules_PID = {
    'Age': GenRule(age_hierarchy),
    'BloodPressure': GenRule(blood_pressure_hierarchy),
    'Insulin': GenRule(insulin_hierarchy)
}

PID_training_anonymous = ola.anonymize(PID_training, k=10, generalization_rules=generalization_rules_PID,
                             info_loss=information_loss.dm_star_loss)


###################
### CREDIT CARD ###
###################

import importlib
from crowds.kanonymity import ola
importlib.reload(ola)

# Load data
credit_training = pd.read_csv('data/CCD_train.csv', sep=",")
credit_test = pd.read_csv('data/CCD_test.csv', sep=",")

# Convert to correct data types
credit_training['SEX'] = credit_training['SEX'].astype('category')
credit_training['EDUCATION'] = credit_training['EDUCATION'].astype('category')
credit_training['MARRIAGE'] = credit_training['MARRIAGE'].astype('category')
credit_training['default_payment_next_month'] = credit_training['default_payment_next_month'].astype('category')

credit_test['SEX'] = credit_test['SEX'].astype('category')
credit_test['EDUCATION'] = credit_test['EDUCATION'].astype('category')
credit_test['MARRIAGE'] = credit_test['MARRIAGE'].astype('category')
credit_test['default_payment_next_month'] = credit_test['default_payment_next_month'].astype('category')

# Generalization rules
generalization_rules_CCD = {
    'LIMIT_BAL': GenRule(limit_bal_hierarchy),
    'EDUCATION': GenRule(educationsmall_hierarchy),
    'BILL_AMT1': GenRule(bill_amt_hierarchy),
    'PAY_AMT1' : GenRule(pay_amt_hierarchy)
}

credit_training_anonymous = ola.anonymize(credit_training, k=10, generalization_rules=generalization_rules_CCD,
                             info_loss=information_loss.dm_star_loss)


#####################
### Census Income ###
#####################

import importlib
from crowds.kanonymity import ola
importlib.reload(ola)

# Load data
KDD_training = pd.read_csv('data/KDD_train.csv', sep=",")
KDD_test = pd.read_csv('data/KDD_test.csv', sep=",")

# Generalization rules
generalization_rules_KDD = {
    'age': GenRule(age_hierarchy),
    'marital_stat': GenRule(marital_hierarchy),
    'birth_country_mother': GenRule(country_hierarchy),
    'education' : GenRule(education_hierarchy)
}

KDD_training_anonymous = ola.anonymize(KDD_training, k=160, generalization_rules=generalization_rules_KDD,
                             info_loss=information_loss.dm_star_loss)

#################
### TEST SETS ###
#################

# apply same generalization to test set

def apply_generalization(value, generalization_level, hierarchy):
    return hierarchy[generalization_level - 1](value)

def generalize_test_data(test_data, generalization_levels, generalization_hierarchies):
    for column, level in generalization_levels.items():
        hierarchy = generalization_hierarchies[column]
        test_data[column] = test_data[column].apply(lambda x: apply_generalization(x, level, hierarchy))

    return test_data

# Generalization hierarchies
generalization_hierarchies = {
    'Age': age_hierarchy,
    'BloodPressure': blood_pressure_hierarchy,
    'Insulin': insulin_hierarchy,
    'LIMIT_BAL': limit_bal_hierarchy,
    'EDUCATION': educationsmall_hierarchy,
    'BILL_AMT1': bill_amt_hierarchy,
    'PAY_AMT1' : pay_amt_hierarchy,
    'age': age_hierarchy,
    'education': education_hierarchy,
    'birth_country_mother': country_hierarchy,
    'marital_stat': marital_hierarchy
}

generalization_levels_PID = PID_training_anonymous[1]
generalization_levels_credit = credit_training_anonymous[1]
generalization_levels_KDD = KDD_training_anonymous[1]

PID_test_anonymous = generalize_test_data(PID_test, generalization_levels_PID, generalization_hierarchies)
credit_test_anonymous = generalize_test_data(credit_test, generalization_levels_credit, generalization_hierarchies)
KDD_test_anonymous = generalize_test_data(KDD_test, generalization_levels_KDD, generalization_hierarchies)


# Save anonymized training and test sets
PID_training_anonymous[0].to_csv('data/PID_train_GT.csv', index=False)
PID_test_anonymous.to_csv('data/PID_test_GT.csv', index=False)

credit_training_anonymous[0].to_csv('data/CCD_train_GT.csv', index=False)
credit_test_anonymous.to_csv('data/CCD_test_GT.csv', index=False)

KDD_training_anonymous[0].to_csv('data/KDD_train_GT.csv', index=False)
KDD_test_anonymous.to_csv('data/KDD_test_GT.csv', index=False)