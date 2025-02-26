## GLOBAL VARIABLES

# The k anonymization factor
K_FACTOR = 9

# Weight of the Generalization Information Loss
ALPHA = 1

# Weight of the Structural Information Loss
BETA = 0

# Weight vector for generalization categories
GEN_WEIGHT_VECTORS = {
    'equal': {
        'categorical': {
            'EDUCATION': 1.0/6.0,
        },
        'range': {
            'LIMIT_BAL': 1.0/6.0,
            'PAY_AMT1': 1.0/6.0,
            'BILL_AMT1': 1.0/6.0
        }
    },
    'emph_race': {
        'categorical': {
            'EDUCATION': 0.02
        },
        'range': {
            'LIMIT_BAL': 0.02,
            'PAY_AMT1': 0.02,
            'BILL_AMT1': 0.02
        }
    },
    'emph_age': {
        'categorical': {
            'EDUCATION': 0.02
        },
        'range': {
            'LIMIT_BAL': 0.9,
            'PAY_AMT1': 0.9,
            'BILL_AMT1': 0.9
        }
    }
}

# Chosen weight vector
VECTOR = 'equal'
