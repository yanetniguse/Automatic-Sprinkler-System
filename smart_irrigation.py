import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSlider, QPushButton
from PyQt5.QtCore import Qt

#Main application window for the Smart Irrigation System. It provides a user interface to simulate sensor inputs and get watering recommendations.
class IrrigationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Smart Irrigation System')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()#main layout for the application
        
        # Labels and sliders for soil moisture input
        self.soil_label = QLabel('Soil Moisture (%): 50')
        layout.addWidget(self.soil_label)
        self.soil_slider = QSlider(Qt.Horizontal)
        self.soil_slider.setMinimum(0)
        self.soil_slider.setMaximum(100)
        self.soil_slider.setValue(50)
        self.soil_slider.valueChanged.connect(self.update_soil) #connect slider to update function
        layout.addWidget(self.soil_slider)
        
        # Labels and sliders for temperature input
        self.temp_label = QLabel('Temperature (°C): 25')
        layout.addWidget(self.temp_label)
        self.temp_slider = QSlider(Qt.Horizontal)
        self.temp_slider.setMinimum(-10)
        self.temp_slider.setMaximum(50)
        self.temp_slider.setValue(25)
        self.temp_slider.valueChanged.connect(self.update_temp)
        layout.addWidget(self.temp_slider)
        
        # Labels and sliders for humidity input
        self.humidity_label = QLabel('Humidity (%): 50')
        layout.addWidget(self.humidity_label)
        self.humidity_slider = QSlider(Qt.Horizontal)
        self.humidity_slider.setMinimum(0)
        self.humidity_slider.setMaximum(100)
        self.humidity_slider.setValue(50)
        self.humidity_slider.valueChanged.connect(self.update_humidity)
        layout.addWidget(self.humidity_slider)
        
        # Button to analyze and provide recommendation
        self.button = QPushButton('Analyze & Recommend')
        self.button.clicked.connect(self.analyze)
        layout.addWidget(self.button)
        
        # Label to display watering recommendation
        self.result_label = QLabel('Watering Recommendation:')
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def update_soil(self, value):
        """Update soil moisture label based on slider value."""
        self.soil_label.setText(f'Soil Moisture (%): {value}')
    
    def update_temp(self, value):
        """Update temperature label based on slider value."""
        self.temp_label.setText(f'Temperature (°C): {value}')
    
    def update_humidity(self, value):
        """Update humidity label based on slider value."""
        self.humidity_label.setText(f'Humidity (%): {value}')
    
    def analyze(self):
        """Analyze the input values and determine the watering recommendation."""
        soil = self.soil_slider.value()
        temp = self.temp_slider.value()
        humidity = self.humidity_slider.value()
        
        # Decision logic for irrigation recommendation
        if soil < 30:
            recommendation = "High Watering Needed!" 
        elif 30 <= soil < 60:
            recommendation = "Moderate Watering Required."
        else:
            recommendation = "No Watering Needed."
        
        # Adjust recommendation based on temperature and humidity conditions
        if temp > 35 and humidity < 40:
            recommendation += " Increase watering due to high heat."
        elif temp < 10:
            recommendation += " Reduce watering to prevent overwatering in cold."
        
        self.result_label.setText(f'Watering Recommendation: {recommendation}')

if __name__ == '__main__':
    # Create the application instance
    app = QApplication(sys.argv)
    ex = IrrigationApp()
    ex.show()
    sys.exit(app.exec_())
