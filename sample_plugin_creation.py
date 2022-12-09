# Import necessary libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from email import message
from email.policy import default

# Define the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the main window
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set the window title and size
        self.setWindowTitle('Python Plugin')
        self.resize(300, 300)
        
        # Create an action for the plugin
        pluginAction = QAction('Filter Emails', self)
        pluginAction.triggered.connect(self.filterEmails)
        
        # Add the action to the menu bar
        self.menuBar().addAction(pluginAction)
        
    def filterEmails(self):
        # Open the email file
        with open('emails.txt', 'rb') as f:
            # Parse the email messages
            messages = message.from_bytes(f.read(), policy=default)
            for msg in messages:
                # Filter the emails by sender and subject
                if msg['from'] == 'john@example.com' and 'Important' in msg['subject']:
                    print('Email from John with subject "Important":')
                    print(msg.get_body())
                    print()

# Create an instance of the application and main window
app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()

# Run the main event loop
sys.exit(app.exec_())





#####################version 2#########
# Import necessary libraries
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QDialog, QFormLayout, QLineEdit, QDialogButtonBox
from email import message
from email.policy import default

# Define the settings dialog class
class SettingsDialog(QDialog):
    def __init__(self):
        # Initialize the settings dialog
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set the dialog title and size
        self.setWindowTitle('Filter Settings')
        self.resize(300, 150)
        
        # Create the form layout and input fields
        layout = QFormLayout()
        self.senderField = QLineEdit()
        self.subjectField = QLineEdit()
        layout.addRow('Sender:', self.senderField)
        layout.addRow('Subject:', self.subjectField)
        
        # Create the button box
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        
        # Add the layout and button box to the dialog
        layout.addWidget(buttons)
        self.setLayout(layout)

# Define the main window class
class MainWindow(QMainWindow):
    def __init__(self):
        # Initialize the main
