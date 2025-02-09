import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from Modules.Designer.debug_widget_layout import Ui_Dialog
from Modules.p4_helper import PerforceHelper

class PerforceAutomationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        #Set up the UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #set up the Perforce helper
        self.p4_helper = PerforceHelper()

        #Connections to widget events
        self.ui.connect_pb.clicked.connect(self.handle_p4_connect)
        self.ui.disconnect_pb.clicked.connect(self.handle_p4_disconnect)
        self.ui.list_files_in_path_pb.clicked.connect(self.handle_list_files_in_path)
        self.ui.checkout_or_add_pb.clicked.connect(self.handle_checkout_or_add_files)

        #Connect to Perforce automatically on start-up
        self.handle_p4_connect()

    def append_log(self, text:str="") -> None: 
        """ Append the given string to the log widget. """
        self.ui.log_pte.appendPlainText("# " * 5)
        self.ui.log_pte.appendPlainText(text)
    
    def handle_p4_connect(self) -> None:
        """ Link between UI action and Perforce connect call. """
        is_success, message = self.p4_helper.connect()
        self.append_log(message)
        self.update_connection_status_color(is_success)

    def handle_p4_disconnect(self) -> None:
        """ Link between UI action and Perforce disconnect call. """
        is_success, message = self.p4_helper.disconnect()
        self.append_log(message)
        self.update_connection_status_color(not is_success)

    def handle_list_files_in_path(self) -> None:
        """ Link between UI action and Perforce list files in depot call. """
        depot_path = self.ui.depoth_path_le.text()
        is_success, path_list = self.p4_helper.list_files_in_path(depot_path)
        if is_success:
            self.append_log("\n".join(path_list))
        else:
            self.append_log(f"[ERROR] Failed to list files in {depot_path}: {path_list[0]}")
    
    def handle_checkout_or_add_files(self) -> None:
        """ Link between UI action and Perforce Mark for Add or Checkout files in depot call. """
        depot_path = self.ui.depoth_path_le.text()
        is_success, output_str = self.p4_helper.mark_for_add_or_checkout(depot_path)
        if is_success:
            self.append_log(output_str)
        else:
            self.append_log(f"[ERROR] Problem with marking for add and checking out files in {depot_path}: {output_str}")

    def update_connection_status_color(self, is_connected) -> None:
        """ Update the color of the connection status indicator. """
        if is_connected:
            self.ui.connection_status_color_lbl.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.ui.connection_status_color_lbl.setStyleSheet("background-color: rgb(255, 0, 0);")
    
    def closeEvent(self, event):
        """Handle the window close event, to ensure proper disconnection from Perforce. """  
        self.handle_p4_disconnect()
        super().closeEvent(event)

if __name__ == "__main__": #Check if the script is being run directly
    app = QApplication(sys.argv)
    window = PerforceAutomationApp()
    window.show()

    sys.exit(app.exec())
