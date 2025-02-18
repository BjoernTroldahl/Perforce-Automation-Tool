#Default utils 
import sys

#UI
from PySide6.QtWidgets import QApplication, QMainWindow
from Modules.Designer.debug_widget_layout import Ui_Dialog
from PySide6.QtCore import Signal

#Perforce
from Modules.p4_helper import PerforceHelper
from Modules.p4_monitor import PerforceMonitor

class PerforceAutomationApp(QMainWindow):
    log_signal = Signal(str)

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
        self.ui.delete_all_empty_cls_pb.clicked.connect(self.handle_delete_all_empty_cls)
        self.ui.revert_files_from_cl_pb.clicked.connect(self.handle_revert_files_from_cl)
        self.ui.shelve_files_pb.clicked.connect(self.handle_shelve_files)
        self.ui.unshelve_files_pb.clicked.connect(self.handle_unshelve_files)
        self.ui.delete_shelved_pb.clicked.connect(self.handle_delete_shelved_files)
        self.ui.sync_to_latest_pb.clicked.connect(self.handle_sync_to_latest)
        self.ui.submit_pb.clicked.connect(self.handle_submit_cl)
        self.ui.start_monitor_pb.clicked.connect(self.handle_monitor_start)
        self.ui.stop_monitor_pb.clicked.connect(self.handle_monitor_stop)
       
        self.ui.refresh_cls_pb.clicked.connect(self.populate_changelists_cmbx)

        #Connect to Perforce automatically on start-up
        self.handle_p4_connect()
        #Populate the combobox changelists as part of Init as well
        self.populate_changelists_cmbx()

        #Invoke P4 monitor once P4 helper is ready
        self.p4_monitor = PerforceMonitor(self.p4_helper.p4, self.log_signal, 10)
        self.log_signal.connect(self.append_log)

    def populate_changelists_cmbx(self):
        """ Pass data to changelists combobox. """
        self.ui.changelist_cmbx.clear()
        self.ui.changelist_cmbx.addItems(self.p4_helper.get_all_pending_cls_for_ui())

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
            if self.ui.move_to_new_cl_cb.isChecked():
                is_cl_created, cl_number = self.p4_helper.create_new_cl(f"Moving recently marked for edit/add files from {depot_path} to new CL.")
                if is_cl_created:
                    _, log_move = self.p4_helper.move_files_to_cl(depot_path, cl_number)
                    self.append_log(log_move)
        else:
            self.append_log(f"[ERROR] Problem with marking for add and checking out files in {depot_path}: {output_str}")
        self.populate_changelists_cmbx()
    
    def handle_delete_all_empty_cls(self) -> None:
        """ Link between UI action and Perforce Delete all Empty CLs call. """
        _, log_delete_empty_cls = self.p4_helper.delete_all_empty_cls()
        self.append_log(log_delete_empty_cls)
        self.populate_changelists_cmbx()
    
    def handle_revert_files_from_cl(self) -> None:
        """ Link between UI action and Perforce revert files from given pending CL call. """
        changelists_info = self.ui.changelist_cmbx.currentText()
        changelists_id = changelists_info.split(":")[0]
        _, log_revert = self.p4_helper.revert_files_from_cl(changelists_id, self.ui.revert_only_unchanged_cb.isChecked())
        self.append_log(log_revert)

    def handle_shelve_files(self) -> None:
        """ Link between UI action and Perforce shelve files from the given pending CL call. """
        changelists_info = self.ui.changelist_cmbx.currentText()
        changelists_id = changelists_info.split(":")[0]
        _, log_shelve = self.p4_helper.shelve_files_in_cl(changelists_id)
        self.append_log(log_shelve)

    def handle_unshelve_files(self) -> None:
        """ Link between UI action and Perforce un-shelve files from the given pending CL call. """
        changelists_info = self.ui.changelist_cmbx.currentText()
        changelists_id = changelists_info.split(":")[0]
        _, log_unshelve = self.p4_helper.unshelve_files_in_cl(shelve_cl_number=changelists_id,target_cl_number=changelists_id)
        self.append_log(log_unshelve)

    def handle_delete_shelved_files(self) -> None:
        """ Link between UI action and Perforce delete shelved files in the given pending CL call. """
        changelists_info = self.ui.changelist_cmbx.currentText()
        changelists_id = changelists_info.split(":")[0]
        _, log_delete_shelve = self.p4_helper.delete_shelved_files_in_cl(changelists_id)
        self.append_log(log_delete_shelve)
    
    def handle_sync_to_latest(self) -> None:
        """ Link between UI action and Perforce sync files in the given pending depot path call. Also handles file conflicts in case they occur. """
        depot_path = self.ui.depoth_path_le.text()
        _, log_sync = self.p4_helper.sync_to_latest(depot_path)
        self.append_log(log_sync)
        _, log_resolve = self.p4_helper.check_for_file_conflicts(depot_path, self.ui.conflict_accept_local_rb.isChecked())
        self.append_log(log_resolve)

    def handle_submit_cl(self) -> None:
        """ Link between UI action and Perforce submit CL in the given pending CL call. """
        changelists_info = self.ui.changelist_cmbx.currentText()
        changelists_id = changelists_info.split(":")[0]
        _, log_submit = self.p4_helper.submit_cl(changelists_id)
        self.append_log(log_submit)

    def handle_monitor_start(self) -> None:
        """ Link between UI action and Perforce monitor start call. """
        depot_path = self.ui.depoth_path_le.text()
        self.p4_monitor.start_monitoring(depot_path)
        self.append_log(f"Monitoring started in path {depot_path}")

    def handle_monitor_stop(self) -> None:
        """ Link between UI action and Perforce monitor stop call. """
        self.p4_monitor.stop_monitor()
        self.append_log(f"Monitoring stopped.")

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
