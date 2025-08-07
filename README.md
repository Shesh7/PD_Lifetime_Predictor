# ⚡ Electric Motor Parameter Calculator

A professional Streamlit application for calculating various motor parameters including PWM pulses, wheel revolutions, motor revolutions, and phase changes with a beautiful, modern UI.

## 🚀 Features

- **Interactive Calculator**: Real-time motor parameter calculation based on multiple inputs
- **Beautiful UI**: Modern design with native Streamlit components
- **Visual Results**: Interactive charts and parameter visualizations
- **Comprehensive Calculations**: Detailed breakdown of all motor parameters
- **Responsive Design**: Works on desktop and mobile devices
- **Navigation**: Easy-to-use sidebar navigation with multiple sections

## 📋 Input Parameters

The calculator accepts the following parameters:

1. **Runtime (hours)**: Total operating time of the motor (0.1-10,000 hours)
2. **PWM Frequency (kHz)**: PWM frequency in kilohertz (1-100 kHz)
3. **Mileage (km)**: Total distance traveled (0.1-100,000 km)
4. **Tyre Diameter (m)**: Diameter of the tyre in meters (0.1-2.0 m)
5. **Axle Transmission Ratio**: Ratio between axle and motor (0.1-100)
6. **Pole Pairs**: Number of pole pairs in the motor (1-20)

## 🧮 Calculation Formulas

The application uses comprehensive formulas to calculate motor parameters:

### 1. PWM Pulses Over Lift
```
PWM Pulses = Runtime (seconds) × PWM Frequency (Hz)
```

### 2. Wheel Revolutions
```
Wheel Revolutions = Mileage (meters) ÷ (Tyre Diameter × π)
```

### 3. Motor Revolutions
```
Motor Revolutions = Wheel Revolutions × Axle Transmission Ratio
```

### 4. Phase Changes
```
Phase Changes = Pole Pairs × 2 × Motor Revolutions
```

## 📊 Calculated Results

The application provides four key calculated values:

- **PWM Pulses**: Total number of PWM pulses over the entire runtime
- **Wheel Revolutions**: Total number of wheel rotations based on mileage
- **Motor Revolutions**: Total motor rotations considering transmission ratio
- **Phase Changes**: Total phase transitions based on pole pairs and motor revolutions

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation Steps

1. **Clone or download the project files**

2. **Create and activate a virtual environment** (recommended):
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

### Alternative: Using Existing Virtual Environment

If you have an existing virtual environment, you can use it:

```bash
# Activate your existing virtual environment
source /path/to/your/venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📁 Project Structure

```
shesh-thesis/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── config.py          # Configuration settings
└── README.md          # This file
```

## 🎯 Usage Instructions

1. **Navigate to Calculator**: Use the sidebar to select "Calculator"
2. **Enter Parameters**: Fill in the input fields with your motor specifications
3. **Click Calculate**: Press the "🚀 Calculate Motor Parameters" button
4. **Review Results**: Check the calculated values and visualizations
5. **Explore Charts**: Use the interactive charts for visual assessment
6. **View Details**: Check the detailed breakdown and formulas

## 🔧 Technical Details

### Dependencies
- **streamlit**: Web application framework
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **plotly**: Interactive charts and visualizations

### Key Classes
- `ElectricMotor_PD_Calculator`: Main calculation class with methods for:
  - `calculate_number_of_pwm_pulses_over_lift()`
  - `calculate_number_of_wheel_revolutions()`
  - `calculate_number_of_electric_motor_revolutions()`
  - `calculate_number_of_phase_changes()`

### Key Functions
- `create_calculation_chart()`: Bar chart for calculated values
- `create_parameter_summary_chart()`: Radar chart for input parameters

## 🎨 UI Features

- **Native Streamlit Components**: Clean, professional interface
- **Interactive Charts**: Plotly-based visualizations
- **Responsive Layout**: Works on all screen sizes
- **Professional Styling**: Modern design with proper spacing
- **Expandable Sections**: Detailed information in collapsible sections

## 📚 Additional Information

- **About Section**: Learn more about the application and its features
- **Help Section**: Detailed usage guidelines and parameter explanations
- **Formula Explanation**: Complete breakdown of the calculation methodology

## 🔍 Calculation Breakdown

The application provides detailed step-by-step calculations:

- **Runtime Conversion**: Hours to seconds
- **PWM Frequency Conversion**: kHz to Hz
- **Mileage Conversion**: km to meters
- **Wheel Circumference**: Based on tyre diameter
- **Transmission Calculations**: Motor to wheel ratios

## ⚠️ Important Notes

- This calculator provides estimates based on the provided parameters
- For critical applications, always verify calculations with qualified engineers
- Results should be used as part of a comprehensive motor analysis
- Regular monitoring and maintenance schedules should be followed

## 🤝 Contributing

Feel free to enhance the application by:
- Adding more sophisticated calculation models
- Implementing data export features
- Adding historical data tracking
- Creating additional visualization options
- Improving the calculation accuracy

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit**
