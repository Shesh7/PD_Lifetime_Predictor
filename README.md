# ⚡ Electric Motor Partial Discharge Calculator

A professional Streamlit application for calculating partial discharge in electric motor stators with a beautiful, modern UI.

## 🚀 Features

- **Interactive Calculator**: Real-time partial discharge calculation based on multiple parameters
- **Beautiful UI**: Modern design with gradient colors and professional styling
- **Visual Results**: Interactive gauge charts and severity indicators
- **Comprehensive Formula**: Detailed explanation of the calculation methodology
- **Responsive Design**: Works on desktop and mobile devices
- **Navigation**: Easy-to-use sidebar navigation with multiple sections

## 📋 Input Parameters

The calculator accepts the following parameters:

1. **Voltage (V)**: Operating voltage of the motor (100V - 10kV)
2. **Frequency (Hz)**: Operating frequency (25-100 Hz)
3. **Capacitance (nF)**: Stator winding capacitance (0.1-100 nF)
4. **Temperature (°C)**: Operating temperature (0-100°C)
5. **Humidity (%)**: Environmental humidity (0-100%)
6. **Insulation Age (years)**: Age of stator insulation (0.1-30 years)

## 🧮 Calculation Formula

The application uses a comprehensive formula that considers multiple factors:

```
Partial Discharge = Base_PD × Temperature_Factor × Humidity_Factor × Age_Factor
```

Where:
- **Base_PD** = Voltage × Frequency × Capacitance × 10⁻⁶
- **Temperature_Factor** = 1 + (Temperature - 25) × 0.02
- **Humidity_Factor** = 1 + (Humidity - 50) × 0.01
- **Age_Factor** = 1 + (Age - 1) × 0.1

## 📊 Severity Levels

The application categorizes results into four severity levels:

- 🟢 **Low (< 100 pC)**: Good insulation condition
- 🟡 **Medium (100-500 pC)**: Moderate PD, monitor closely
- 🟠 **High (500-1000 pC)**: High PD, schedule maintenance
- 🔴 **Critical (> 1000 pC)**: Immediate attention required

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## 📁 Project Structure

```
shesh-thesis/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🎯 Usage Instructions

1. **Navigate to Calculator**: Use the sidebar to select "Calculator"
2. **Enter Parameters**: Fill in the input fields with your motor specifications
3. **Click Calculate**: Press the "🚀 Calculate Partial Discharge" button
4. **Review Results**: Check the calculated PD value and severity level
5. **Interpret Charts**: Use the interactive gauge chart for visual assessment
6. **Follow Recommendations**: Read the severity-based recommendations

## 🔧 Technical Details

### Dependencies
- **streamlit**: Web application framework
- **pandas**: Data manipulation
- **numpy**: Numerical computations
- **plotly**: Interactive charts and visualizations
- **streamlit-option-menu**: Navigation menu component

### Key Functions
- `calculate_partial_discharge()`: Main calculation function
- `calculate_pd_severity()`: Severity level determination
- `create_pd_chart()`: Interactive gauge chart creation

## 🎨 UI Features

- **Gradient Headers**: Beautiful gradient text effects
- **Card-based Layout**: Organized information in styled cards
- **Interactive Charts**: Plotly-based gauge charts
- **Color-coded Results**: Visual severity indicators
- **Responsive Design**: Works on all screen sizes
- **Professional Styling**: Modern CSS with hover effects

## 📚 Additional Information

- **About Section**: Learn more about the application and its features
- **Help Section**: Detailed usage guidelines and parameter explanations
- **Formula Explanation**: Complete breakdown of the calculation methodology

## ⚠️ Important Notes

- This calculator provides estimates based on theoretical models
- For critical applications, always consult with qualified engineers
- Results should be used as part of a comprehensive motor health assessment
- Regular monitoring and maintenance schedules should be followed

## 🤝 Contributing

Feel free to enhance the application by:
- Adding more sophisticated calculation models
- Implementing data export features
- Adding historical data tracking
- Creating additional visualization options

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Streamlit**
