import random
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QTextEdit, QComboBox
from PyQt5.QtGui import QPixmap, QIcon, QDesktopServices
from PyQt5.QtCore import Qt, QUrl

class FakeTradingBot(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("One Minute Trading Bot")
        self.setGeometry(100, 100, 600, 300)  # Adjusted window size to medium height

        # Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout(central_widget)

        # Currency selector
        self.currency_selector = QComboBox(self)
        self.currency_selector.addItems(["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "NZD", "CNY", "INR"])
        self.currency_selector.setStyleSheet("""
            background-color: #333333;
            color: #ffffff;
            font-size: 14px;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        """)
        self.currency_selector.currentIndexChanged.connect(self.currency_changed)
        self.layout.addWidget(self.currency_selector)

        # Chat display for fake trading messages (result list with padding and border)
        self.chat_box = QTextEdit(self)
        self.chat_box.setReadOnly(True)
        self.chat_box.setStyleSheet("""
            background-color: #1c1c1c;
            color: #f0f0f0;
            font-size: 14px;
            font-family: 'Arial', sans-serif;
            border: 2px solid #444444;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 20px;
            height: 300px;  /* Adjust height for better visibility of messages */
        """)
        self.layout.addWidget(self.chat_box)

        # Trade recommendation display
        self.recommendation_label = QLabel("Trade Recommendation: ", self)
        self.recommendation_label.setStyleSheet("""
            color: #ffffff;
            font-size: 16px;
            padding: 15px;
            background-color: #333333;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 2px solid #444444;
        """)
        self.layout.addWidget(self.recommendation_label)

        # Button to trigger a new trade signal
        self.trade_button = QPushButton("Generate Trade Signal", self)
        self.trade_button.setIcon(QIcon('trade_icon.png'))  # Add custom trade icon
        self.trade_button.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px;
            border-radius: 15px;
            border: none;
            width: 250px;
            margin-bottom: 20px;  /* Add margin to create space below the button */
        """)
        self.trade_button.clicked.connect(self.generate_signal)
        self.layout.addWidget(self.trade_button)

        # Performance tracker with padding and border
        self.performance_label = QLabel("Balance: $1000 | Wins: 0 | Losses: 0", self)
        self.performance_label.setStyleSheet("""
            color: #ffffff;
            font-size: 16px;
            padding: 15px;
            background-color: #333333;
            border-radius: 10px;
            margin-bottom: 20px;
            border: 2px solid #444444;
        """)
        self.layout.addWidget(self.performance_label)

        # Footer with clickable link
        self.footer_label = QLabel("Made by <a href='https://github.com/Mdbaizidtanvir'>Mdbaizidtanvir</a>", self)
        self.footer_label.setOpenExternalLinks(True)
        self.footer_label.setAlignment(Qt.AlignCenter)
        self.footer_label.setStyleSheet("""
            color: #ffffff;
            font-size: 14px;
            padding: 10px;
            background-color: #333333;
            border-radius: 10px;
            margin-top: 20px;
        """)
        self.layout.addWidget(self.footer_label)

        # Initialize fake stats
        self.balance = 1000
        self.wins = 0
        self.losses = 0
        self.selected_currency = "USD"  # Default currency is USD

    def currency_changed(self):
        """Update the selected currency."""
        self.selected_currency = self.currency_selector.currentText()
        self.update_performance()  # Update balance display with the new currency

    def generate_signal(self):
        """Generates a random buy/sell signal and recommends it."""
        signal_type = random.choice(["buy", "sell"])
        recommendation_message = f"Trade Recommendation: {signal_type.capitalize()}"
        self.recommendation_label.setText(recommendation_message)
        self.display_message(f"New Signal: {signal_type.capitalize()}", "white")

        # Simulate trade outcome after a short delay
        self.process_trade(signal_type)

    def process_trade(self, signal_type):
        """Simulate processing the trade."""
        # Simulate a random outcome (win/loss)
        trade_outcome = random.choice(["win", "lose"])
        outcome_message = f"{signal_type.capitalize()} Signal: {trade_outcome.capitalize()}"

        # Update performance stats based on the outcome
        if trade_outcome == "win":
            self.balance += 100  # Simulate win gain
            self.wins += 1
            outcome_message += f" | Balance: {self.selected_currency} {self.balance}"
            message_color = "green"  # Green for win
        else:
            self.balance -= 100  # Simulate loss
            self.losses += 1
            outcome_message += f" | Balance: {self.selected_currency} {self.balance}"
            message_color = "red"  # Red for loss

        self.display_message(outcome_message, message_color)
        self.update_performance()

        # Simulate some delay and reset the signal display
        time.sleep(2)
        self.display_message(f"Signal: {signal_type.capitalize()} processed.\n", "yellow")

    def display_message(self, message, color):
        """Display message in the chat box with specific color and padding."""
        padded_message = f"<div style='padding: 10px;'>{message}</div>"
        self.chat_box.append(f"<font color='{color}'>{padded_message}</font>")

    def update_performance(self):
        """Update the performance label with current stats."""
        self.performance_label.setText(f"Balance: {self.selected_currency} {self.balance} | Wins: {self.wins} | Losses: {self.losses}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    bot = FakeTradingBot()
    bot.show()
    sys.exit(app.exec_())
