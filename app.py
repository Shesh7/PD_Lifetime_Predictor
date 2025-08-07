import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import math

# Page configuration
st.set_page_config(
    page_title="Electric Motor Partial Discharge Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

class ElectricMotor_PD_Calculator:
    def __init__(self, runtime, pwm_frequency, mileage, tyre_diameter, axle_transmission_ratio, pole_pairs):
        self.runtime = runtime
        self.pwm_frequency = pwm_frequency
        self.mileage = mileage
        self.tyre_diameter = tyre_diameter
        self.axle_transmission_ratio = axle_transmission_ratio
        self.pole_pairs = pole_pairs
        
    def calculate_number_of_pwm_pulses_over_lift(self):
        """
        Calculate the number of PWM pulses over a lift.
        """
        # convert runtime from hours to seconds
        runtime_seconds = self.runtime * 3600

        # convert pwm frequency from kHz to Hz
        pwm_frequency_hz = self.pwm_frequency * 1000

        return runtime_seconds * pwm_frequency_hz
    
    def calculate_number_of_wheel_revolutions(self):
        """
        Calculate the number of wheel revolutions.
        """
        # convert mileage from km to m
        mileage_m = self.mileage * 1000

        return mileage_m / (self.tyre_diameter * 2 * math.pi)

    def calculate_number_of_electric_motor_revolutions(self):
        """
        Calculate the number of electric motor revolutions.
        """
        self.number_of_wheel_revolutions = self.calculate_number_of_wheel_revolutions()
        return self.number_of_wheel_revolutions * self.axle_transmission_ratio

    def calculate_number_of_phase_changes(self):
        """
        Calculate the number of phase changes.
        """
        self.number_of_electric_motor_revolutions = self.calculate_number_of_electric_motor_revolutions()
        return self.pole_pairs * 2 * self.number_of_electric_motor_revolutions

def create_calculation_chart(pwm_pulses, wheel_revolutions, motor_revolutions, phase_changes):
    """Create a bar chart showing all calculated values"""
    fig = go.Figure(data=[
        go.Bar(
            x=['PWM Pulses', 'Wheel Revolutions', 'Motor Revolutions', 'Phase Changes'],
            y=[pwm_pulses, wheel_revolutions, motor_revolutions, phase_changes],
            text=[f'{pwm_pulses:,.0f}', f'{wheel_revolutions:,.0f}', 
                  f'{motor_revolutions:,.0f}', f'{phase_changes:,.0f}'],
            textposition='auto',
            marker_color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
        )
    ])
    
    fig.update_layout(
        title="Calculation Results Overview",
        xaxis_title="Calculated Values",
        yaxis_title="Count",
        height=400,
        showlegend=False
    )
    
    return fig

def create_parameter_summary_chart(runtime, pwm_freq, mileage, tyre_diameter, axle_ratio, pole_pairs):
    """Create a radar chart showing parameter values"""
    categories = ['Runtime (hrs)', 'PWM Freq (kHz)', 'Mileage (km)', 
                  'Tyre Diameter (m)', 'Axle Ratio', 'Pole Pairs']
    
    values = [runtime, pwm_freq, mileage, tyre_diameter, axle_ratio, pole_pairs]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Parameters',
        line_color='#1f77b4'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) * 1.2]
            )),
        showlegend=False,
        title="Parameter Summary",
        height=400
    )
    
    return fig

def main():
    # Header with native Streamlit styling
    st.title("⚡ Electric Motor Partial Discharge Calculator")
    st.markdown("---")
    
    # Sidebar navigation using native Streamlit
    with st.sidebar:
        st.header("Navigation")
        selected = st.selectbox(
            "Choose a section:",
            ["Calculator", "About", "Help"],
            index=0
        )
    
    if selected == "Calculator":
        # Main calculator interface
        col1, col2 = st.columns([2, 1])
        
        with col1:
            # Input section with native Streamlit containers
            with st.container():
                st.subheader("📊 Input Parameters")
                
                # Input form
                with st.form("pd_calculator"):
                    col1_input, col2_input = st.columns(2)
                    
                    with col1_input:
                        runtime = st.number_input(
                            "Runtime (hours)", 
                            min_value=0.1, 
                            max_value=10000.0, 
                            value=100.0, 
                            step=1.0,
                            help="Total runtime of the motor in hours"
                        )
                        
                        pwm_frequency = st.number_input(
                            "PWM Frequency (kHz)", 
                            min_value=1.0, 
                            max_value=100.0, 
                            value=20.0, 
                            step=0.1,
                            help="PWM frequency in kilohertz"
                        )
                        
                        mileage = st.number_input(
                            "Mileage (km)", 
                            min_value=0.1, 
                            max_value=1000000.0, 
                            value=5000.0, 
                            step=10.0,
                            help="Total distance traveled in kilometers"
                        )
                    
                    with col2_input:
                        tyre_diameter = st.number_input(
                            "Tyre Diameter (m)", 
                            min_value=0.1, 
                            max_value=2.0, 
                            value=0.6, 
                            step=0.01,
                            help="Diameter of the tyre in meters"
                        )
                        
                        axle_transmission_ratio = st.number_input(
                            "Axle Transmission Ratio", 
                            min_value=0.1, 
                            max_value=100.0, 
                            value=10.0, 
                            step=0.1,
                            help="Transmission ratio between axle and motor"
                        )
                        
                        pole_pairs = st.number_input(
                            "Pole Pairs", 
                            min_value=1, 
                            max_value=20, 
                            value=4, 
                            step=1,
                            help="Number of pole pairs in the motor"
                        )
                    
                    # Calculate button
                    calculate_button = st.form_submit_button("🚀 Calculate Motor Parameters")
        
        with col2:
            # Current parameters display
            st.subheader("📈 Current Parameters")
            
            # Display current parameters using native metrics
            st.metric("Runtime", f"{runtime:.1f} hours")
            st.metric("PWM Frequency", f"{pwm_frequency:.1f} kHz")
            st.metric("Mileage", f"{mileage:.1f} km")
            st.metric("Tyre Diameter", f"{tyre_diameter:.2f} m")
            st.metric("Axle Ratio", f"{axle_transmission_ratio:.1f}")
            st.metric("Pole Pairs", f"{pole_pairs}")
        
        # Calculate and display results
        if calculate_button:
            st.markdown("---")
            
            # Create calculator instance
            calculator = ElectricMotor_PD_Calculator(
                runtime, pwm_frequency, mileage, tyre_diameter, 
                axle_transmission_ratio, pole_pairs
            )
            
            # Calculate all values
            pwm_pulses = calculator.calculate_number_of_pwm_pulses_over_lift()
            wheel_revolutions = calculator.calculate_number_of_wheel_revolutions()
            motor_revolutions = calculator.calculate_number_of_electric_motor_revolutions()
            phase_changes = calculator.calculate_number_of_phase_changes()
            
            # Display results using native Streamlit components
            st.subheader("🎯 Calculation Results")
            
            col1_result, col2_result = st.columns(2)
            
            with col1_result:
                # Main result metrics
                st.metric(
                    "PWM Pulses", 
                    f"{pwm_pulses:,.0f}",
                    delta="Total pulses over lift"
                )
                
                st.metric(
                    "Wheel Revolutions", 
                    f"{wheel_revolutions:,.0f}",
                    delta="Total wheel rotations"
                )
                
                st.metric(
                    "Motor Revolutions", 
                    f"{motor_revolutions:,.0f}",
                    delta="Total motor rotations"
                )
                
                st.metric(
                    "Phase Changes", 
                    f"{phase_changes:,.0f}",
                    delta="Total phase transitions"
                )
            
            with col2_result:
                # Create calculation overview chart
                fig = create_calculation_chart(pwm_pulses, wheel_revolutions, motor_revolutions, phase_changes)
                st.plotly_chart(fig, use_container_width=True)
            
            # Parameter summary chart
            st.markdown("---")
            st.subheader("📊 Parameter Summary")
            
            col1_chart, col2_chart = st.columns(2)
            
            with col1_chart:
                # Create parameter radar chart
                radar_fig = create_parameter_summary_chart(
                    runtime, pwm_frequency, mileage, tyre_diameter, 
                    axle_transmission_ratio, pole_pairs
                )
                st.plotly_chart(radar_fig, use_container_width=True)
            
            with col2_chart:
                # Detailed calculations breakdown
                st.subheader("🔍 Calculation Breakdown")
                
                with st.expander("View Detailed Calculations", expanded=True):
                    st.markdown(f"""
                    **Runtime Conversion:**
                    - Runtime: {runtime:.1f} hours = {runtime * 3600:,.0f} seconds
                    
                    **PWM Frequency Conversion:**
                    - PWM Frequency: {pwm_frequency:.1f} kHz = {pwm_frequency * 1000:,.0f} Hz
                    
                    **Mileage Conversion:**
                    - Mileage: {mileage:.1f} km = {mileage * 1000:,.0f} meters
                    
                    **Wheel Circumference:**
                    - Circumference: {tyre_diameter:.2f} × π = {tyre_diameter * math.pi:.2f} meters
                    
                    **Transmission:**
                    - Axle Ratio: {axle_transmission_ratio:.1f}
                    - Pole Pairs: {pole_pairs}
                    """)
            
            # Formula explanation using native Streamlit components
            st.markdown("---")
            st.subheader("📐 Calculation Formulas")
            
            # Use expander for formula details
            with st.expander("View Formula Details", expanded=True):
                st.markdown("""
                **1. PWM Pulses Over Lift:**
                ```
                PWM Pulses = Runtime (seconds) × PWM Frequency (Hz)
                ```
                
                **2. Wheel Revolutions:**
                ```
                Wheel Revolutions = Mileage (meters) ÷ (Tyre Diameter × π)
                ```
                
                **3. Motor Revolutions:**
                ```
                Motor Revolutions = Wheel Revolutions × Axle Transmission Ratio
                ```
                
                **4. Phase Changes:**
                ```
                Phase Changes = Pole Pairs × 2 × Motor Revolutions
                ```
                """)
                
    elif selected == "About":
        st.subheader("About This Application")
        st.markdown("""
        This application calculates various motor parameters including PWM pulses, wheel revolutions, 
        motor revolutions, and phase changes based on runtime, PWM frequency, mileage, and other 
        motor specifications.
        """)
        
        st.markdown("### Key Features:")
        col1_about, col2_about = st.columns(2)
        
        with col1_about:
            st.markdown("""
            - ✅ Real-time calculation of motor parameters
            - ✅ Visual representation with interactive charts
            - ✅ Comprehensive parameter breakdown
            - ✅ Professional UI with native Streamlit components
            """)
        
        with col2_about:
            st.markdown("""
            - ✅ Detailed calculation formulas
            - ✅ Parameter summary visualization
            - ✅ Responsive design for all devices
            - ✅ Easy-to-use interface
            """)
    
    elif selected == "Help":
        st.subheader("Help & Guidelines")
        
        st.markdown("### How to use this calculator:")
        
        # Use tabs for organized help content
        tab1, tab2, tab3 = st.tabs(["Input Parameters", "Calculation Process", "Result Interpretation"])
        
        with tab1:
            st.markdown("""
            **Input Parameters:**
            
            1. **Runtime (hours)**: Total operating time of the motor (0.1-10,000 hours)
            2. **PWM Frequency (kHz)**: PWM frequency in kilohertz (1-100 kHz)
            3. **Mileage (km)**: Total distance traveled (0.1-100,000 km)
            4. **Tyre Diameter (m)**: Diameter of the tyre in meters (0.1-2.0 m)
            5. **Axle Transmission Ratio**: Ratio between axle and motor (0.1-100)
            6. **Pole Pairs**: Number of pole pairs in the motor (1-20)
            """)
        
        with tab2:
            st.markdown("""
            **Calculation Process:**
            
            1. Enter all required parameters in the input fields
            2. Click the "🚀 Calculate Motor Parameters" button
            3. Review the calculated results and visualizations
            4. Check the detailed breakdown and formulas
            """)
        
        with tab3:
            st.markdown("""
            **Result Interpretation:**
            
            - **PWM Pulses**: Total number of PWM pulses over the entire runtime
            - **Wheel Revolutions**: Total number of wheel rotations based on mileage
            - **Motor Revolutions**: Total motor rotations considering transmission ratio
            - **Phase Changes**: Total phase transitions based on pole pairs and motor revolutions
            """)
        
        st.warning("""
        **Note:** This calculator provides estimates based on the provided parameters. 
        For critical applications, always verify calculations with qualified engineers.
        """)

if __name__ == "__main__":
    main()
