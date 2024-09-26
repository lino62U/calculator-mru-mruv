from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt5.QtCore import Qt  # Import Qt for alignment
from mru import MRU
from mruv import MRUV
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Motion Calculator")
        self.setStyleSheet("background-color: #f0f0f0;")  # Light gray background
        layout = QVBoxLayout()

        self.label = QLabel("Select the type of motion:")
        self.label.setAlignment(Qt.AlignCenter)  # Center the label text
        self.label.setStyleSheet("font-size: 18px; color: #333333;")  # Dark gray text

        # Create buttons with hover effects
        self.button_mru = QPushButton("MRU")
        self.button_mruv = QPushButton("MRUV")
        self.setup_button_style(self.button_mru)
        self.setup_button_style(self.button_mruv)

        # Connect buttons to functions to change windows
        self.button_mru.clicked.connect(self.show_mru_interface)
        self.button_mruv.clicked.connect(self.show_mruv_interface)

        # Create a horizontal layout to center the buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()  # Add stretchable space before the buttons
        button_layout.addWidget(self.button_mru)
        button_layout.addWidget(self.button_mruv)
        button_layout.addStretch()  # Add stretchable space after the buttons

        # Add label and button layout to the main layout
        layout.addStretch()  # Add stretchable space before the label
        layout.addWidget(self.label)
        layout.addLayout(button_layout)
        layout.addStretch()  # Add stretchable space after the button layout

        self.setLayout(layout)

        # Create a stacked widget to switch between interfaces
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self)  # Main screen
        self.mru_interface = MRU(self)
        self.mruv_interface = MRUV(self)
        self.stacked_widget.addWidget(self.mru_interface)
        self.stacked_widget.addWidget(self.mruv_interface)

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

    def show_mru_interface(self):
        self.stacked_widget.setCurrentWidget(self.mru_interface)

    def show_mruv_interface(self):
        self.stacked_widget.setCurrentWidget(self.mruv_interface)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Create the main window
    main_window = MainApp()
    main_window.stacked_widget.show()

    sys.exit(app.exec_())
