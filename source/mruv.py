from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from utils import calculate_mruv

class MRUV(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setWindowTitle("MRUV Calculator")
        layout = QVBoxLayout()

        self.label = QLabel("Select what you want to calculate in MRUV:")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.combo = QComboBox()
        self.combo.addItems(["Distance (Δx)", "Final Velocity (Vf)", "Time (Δt)", 
                             "Acceleration (α)", "Initial Velocity (Vi)"])

        # Input labels
        self.input1_label = QLabel()
        self.input1 = QLineEdit()
        self.input2_label = QLabel()
        self.input2 = QLineEdit()
        self.input3_label = QLabel()
        self.input3 = QLineEdit()

        # Formula label
        self.formula_label = QLabel()

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        
        self.button_calculate = QPushButton("Calculate")
        self.button_calculate.setStyleSheet(self.button_style())
        self.button_calculate.clicked.connect(self.calculate_mruv)

        self.button_back = QPushButton("Back to Main Menu")
        self.button_back.setStyleSheet(self.button_style())
        self.button_back.clicked.connect(self.go_back)

        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.input1_label)
        layout.addWidget(self.input1)
        layout.addWidget(self.input2_label)
        layout.addWidget(self.input2)
        layout.addWidget(self.input3_label)
        layout.addWidget(self.input3)
        layout.addWidget(self.formula_label)  # Add formula label
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.result_label)
        layout.addWidget(self.button_back)

        self.setLayout(layout)
        self.update_labels()  # Initial call to set labels and formulas

        self.combo.currentIndexChanged.connect(self.update_labels)  # Connect to update function for labels

    def button_style(self):
        """Define the button style with hover effects."""
        return """
        QPushButton {
            background-color: #4CAF50;  /* Green */
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #45a049;  /* Darker green */
        }
        QPushButton:pressed {
            background-color: #388e3c;  /* Even darker green */
        }
        """

    def update_labels(self):
        """Update input labels and show corresponding formula based on selection."""
        option = self.combo.currentText()
        if option == "Distance (Δx)":
            self.input1_label.setText("Enter Initial Velocity (Vi in m/s):")
            self.input2_label.setText("Enter Time (Δt in s):")
            self.input3_label.setText("Enter Acceleration (α in m/s²):")
            self.formula_label.setText("Formula: Δx = Vi * Δt + 0.5 * α * (Δt²)\n"
                                        "(Δx = Distance, Vi = Initial Velocity, "
                                        "Δt = Time, α = Acceleration)")
        elif option == "Final Velocity (Vf)":
            self.input1_label.setText("Enter Initial Velocity (Vi in m/s):")
            self.input2_label.setText("Enter Time (Δt in s):")
            self.input3_label.setText("Enter Acceleration (α in m/s²):")
            self.formula_label.setText("Formula: Vf = Vi + α * Δt\n"
                                        "(Vf = Final Velocity, Vi = Initial Velocity, "
                                        "α = Acceleration, Δt = Time)")
        elif option == "Time (Δt)":
            self.input1_label.setText("Enter Distance (Δx in m):")
            self.input2_label.setText("Enter Initial Velocity (Vi in m/s):")
            self.input3_label.setText("Enter Acceleration (α in m/s²):")
            self.formula_label.setText("Formula: Δt = (Vf - Vi) / α\n"
                                        "(Δt = Time, Vf = Final Velocity, Vi = Initial Velocity, "
                                        "α = Acceleration)")
        elif option == "Acceleration (α)":
            self.input1_label.setText("Enter Final Velocity (Vf in m/s):")
            self.input2_label.setText("Enter Initial Velocity (Vi in m/s):")
            self.input3_label.setText("Enter Time (Δt in s):")
            self.formula_label.setText("Formula: α = (Vf - Vi) / Δt\n"
                                        "(α = Acceleration, Vf = Final Velocity, "
                                        "Vi = Initial Velocity, Δt = Time)")
        elif option == "Initial Velocity (Vi)":
            self.input1_label.setText("Enter Final Velocity (Vf in m/s):")
            self.input2_label.setText("Enter Time (Δt in s):")
            self.input3_label.setText("Enter Acceleration (α in m/s²):")
            self.formula_label.setText("Formula: Vi = Vf - α * Δt\n"
                                        "(Vi = Initial Velocity, Vf = Final Velocity, "
                                        "α = Acceleration, Δt = Time)")

    def calculate_mruv(self):
        option = self.combo.currentText()
        try:
            # Get user input values and convert to float
            input1 = float(self.input1.text())
            input2 = float(self.input2.text())
            input3 = float(self.input3.text())
            # Call MRUV calculation function
            result = calculate_mruv(option, input1, input2, input3)
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Please enter valid numerical values.")

    def go_back(self):
        self.main_app.stacked_widget.setCurrentWidget(self.main_app)
