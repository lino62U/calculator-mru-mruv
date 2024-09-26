from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt  # Import Qt for alignment
from utils import calculate_mru

class MRU(QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.main_app = main_app
        self.setWindowTitle("MRU Calculator")
        self.setStyleSheet("background-color: #f0f0f0;")  # Light gray background
        layout = QVBoxLayout()

        self.label = QLabel("Select what you want to calculate in MRU:")
        self.label.setAlignment(Qt.AlignCenter)  # Center the label text
        self.label.setStyleSheet("font-size: 18px; color: #333333;")  # Dark gray text

        self.combo = QComboBox()
        self.combo.addItems(["Distance", "Speed", "Time"])
        self.combo.currentIndexChanged.connect(self.update_labels)  # Connects to update function for labels

        # Input labels
        self.input1_label = QLabel()
        self.input1 = QLineEdit()
        self.input2_label = QLabel()
        self.input2 = QLineEdit()

        # Formula label
        self.formula_label = QLabel()
        self.formula_label.setAlignment(Qt.AlignCenter)  # Center the formula label

        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)  # Center the result label

        self.button_calculate = QPushButton("Calculate")
        self.setup_button_style(self.button_calculate)
        self.button_calculate.clicked.connect(self.calculate_mru)

        self.button_back = QPushButton("Back to Main Menu")
        self.setup_button_style(self.button_back)
        self.button_back.clicked.connect(self.go_back)

        # Adding widgets to the layout
        layout.addWidget(self.label)
        layout.addWidget(self.combo)
        layout.addWidget(self.input1_label)
        layout.addWidget(self.input1)
        layout.addWidget(self.input2_label)
        layout.addWidget(self.input2)
        layout.addWidget(self.formula_label)  # Add formula label
        layout.addWidget(self.button_calculate)
        layout.addWidget(self.result_label)
        layout.addWidget(self.button_back)

        self.setLayout(layout)
        self.update_labels()  # Call to set initial labels and formula

    def setup_button_style(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;  /* Green */
                color: white; 
                font-size: 16px; 
                padding: 10px;
                border: none; 
                border-radius: 5px; 
            }
            QPushButton:hover {
                background-color: #45a049;  /* Darker green */
            }
        """)

    def update_labels(self):
        """Update input labels and show corresponding formula based on selection."""
        option = self.combo.currentText()
        if option == "Distance":
            self.input1_label.setText("Enter speed (m/s):")
            self.input2_label.setText("Enter time (s):")
            self.formula_label.setText("Formula: S = v * t\n(S = Distance in meters, v = Speed in m/s, t = Time in seconds)")
        elif option == "Speed":
            self.input1_label.setText("Enter distance (m):")
            self.input2_label.setText("Enter time (s):")
            self.formula_label.setText("Formula: v = S / t\n(v = Speed in m/s, S = Distance in meters, t = Time in seconds)")
        elif option == "Time":
            self.input1_label.setText("Enter distance (m):")
            self.input2_label.setText("Enter speed (m/s):")
            self.formula_label.setText("Formula: t = S / v\n(t = Time in seconds, S = Distance in meters, v = Speed in m/s)")

    def calculate_mru(self):
        option = self.combo.currentText()
        try:
            # Get user input values
            input1 = float(self.input1.text())
            input2 = float(self.input2.text())
            # Call MRU calculation function
            result = calculate_mru(option, input1, input2)
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Please enter valid numerical values.")

    def go_back(self):
        self.main_app.stacked_widget.setCurrentWidget(self.main_app)
