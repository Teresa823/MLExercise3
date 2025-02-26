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
            'birth_country_mother': 1.0/6.0,
            'marital_stat': 1.0/6.0
        },
        'range': {
            'age': 1.0/6.0
        }
    },
    'emph_race': {
        'categorical': {
            'birth_country_mother': 0.02,
            'marital_stat': 0.02
        },
        'range': {
            'age': 0.02
        }
    },
    'emph_age': {
        'categorical': {
            'birth_country_mother': 0.02,
            'marital_stat': 0.02,
        },
        'range': {
            'age': 0.9
        }
    }
}

# Chosen weight vector
VECTOR = 'equal'
