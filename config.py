# Configuration file for Electric Motor Partial Discharge Calculator

# Default parameter values
DEFAULT_PARAMETERS = {
    'voltage': 400.0,
    'frequency': 50.0,
    'capacitance': 10.0,
    'temperature': 25.0,
    'humidity': 50.0,
    'insulation_age': 5.0
}

# Parameter ranges
PARAMETER_RANGES = {
    'voltage': {'min': 100.0, 'max': 10000.0, 'step': 50.0},
    'frequency': {'min': 25.0, 'max': 100.0, 'step': 1.0},
    'capacitance': {'min': 0.1, 'max': 100.0, 'step': 0.1},
    'temperature': {'min': 0.0, 'max': 100.0, 'step': 1.0},
    'humidity': {'min': 0.0, 'max': 100.0, 'step': 1.0},
    'insulation_age': {'min': 0.1, 'max': 30.0, 'step': 0.5}
}

# Severity thresholds (in pC)
SEVERITY_THRESHOLDS = {
    'low': 100,
    'medium': 500,
    'high': 1000,
    'critical': float('inf')
}

# Factor coefficients
FACTOR_COEFFICIENTS = {
    'temperature_base': 25.0,
    'temperature_factor': 0.02,
    'humidity_base': 50.0,
    'humidity_factor': 0.01,
    'age_base': 1.0,
    'age_factor': 0.1,
    'base_multiplier': 1e-6
}

# UI Configuration
UI_CONFIG = {
    'page_title': "Electric Motor Partial Discharge Calculator",
    'page_icon': "⚡",
    'layout': "wide",
    'initial_sidebar_state': "expanded"
}

# Chart Configuration
CHART_CONFIG = {
    'gauge_height': 400,
    'gauge_max_value': 1500,
    'colors': {
        'low': 'lightgreen',
        'medium': 'yellow',
        'high': 'orange',
        'critical': 'red'
    }
}
