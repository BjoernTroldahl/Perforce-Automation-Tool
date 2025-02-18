from P4 import P4Exception
from threading import Thread
import time
from datetime import datetime

class PerforceMonitor: 
    def __init__(self, p4, log_signal, check_interval = 5):
        """Parameters: 
        p4: The Perforce API instance to interact with Perforce.
        log_signal (Signal): a PySide6 Signal used to send log messages to the main application.
        check_interval (int, optional): the interval in seconds between each check for new changelists."""

        self.p4 = p4
        self.log_signal = log_signal
        self.check_interval = check_interval

        self.is_running = False
        self.latest_cl = 0
        self.depot_path = ""
        self.checked_out_files = set()

    def get_latest_changelist(self) -> int:
        """Get initial latest changelist in the depot path specified during start_monitor call."""
        try:
            changes = self.p4.run("changes", "-m", "1", self.depot_path)
            if changes:
                return int(changes[0]['change']) if changes else 0
        except P4Exception as e:
            self.log_signal.emit = f"Error fetching latest changelist to start Monitoring: {e.value}"
            return 0
    
    def track_exclusive_checkouts(self) -> None:
        """Checks for updates regarding exclusive checkouts in the monitored path. """
        #Check out for new exclusive checkouts
        try:
            all_files_info = self.p4.run("fstat", self.depot_path)
            for file_info in all_files_info:
                if "otherLock" in file_info or "ourLock" in file_info:
                    file_path = file_info["depotFile"]
                    if file_path not in self.checked_out_files:
                        self.checked_out_files.add(file_path)
                        self.process_exclusive_checkout_cl_for_log(file_info, True)

            #Check if existing exclusive checkout remains
            files_to_remove = set()
            for file in self.checked_out_files:
                current_file_info = self.p4.run("fstat", file)
                if "otherLock" not in current_file_info[0] and "ourLock" not in current_file_info[0]:
                    files_to_remove.add(file)
                    self.process_exclusive_checkout_cl_for_log(current_file_info[0], False)
            self.checked_out_files -= files_to_remove
        except P4Exception as e:
            self.log_signal.emit = f"Error during checking for exclusive checkout: {e.value}"

    
    def start_monitoring(self, depot_path:str):
        """Starts the monitoring of the given depot path in a separate thread."""
        self.depot_path = depot_path
        self.latest_cl = self.get_latest_changelist()
        self.is_running = True
        monitor_thread = Thread(target=self.run)
        monitor_thread.start()

    def run(self):
        """Core monitoring execution. Should be called within the start_monitoring method using Thread."""
        try:
            while self.is_running:
                results = self.p4.run("changes", "-e", self.latest_cl, self.depot_path)
                if isinstance(results, list):
                    for change in reversed(results):
                        cl_num = int(change['change'])
                        if cl_num > self.latest_cl:
                            self.latest_cl = cl_num
                            self.process_new_cl_data_for_log(change)
                self.track_exclusive_checkouts()
                time.sleep(self.check_interval)
        except P4Exception as e:
            self.log_signal.emit = f"Error during monitoring: {e.value}"
    
    def process_new_cl_data_for_log(self, changelist:dict) -> None:
        """Forms descriptive new submit log message from changelists data and sends it to the log."""
        try:
            cl_number = changelist['change']
            user = changelist['user']
            timestamp = int(changelist['time'])
            date = datetime.fromtimestamp(timestamp)
            formatted_date = date.strftime('%Y-%m-%d %H:%M:%S')
            desc = changelist['desc']
            message = f"[MONITOR] New changelist submitted: \n CL # {cl_number} by {user} on {formatted_date}\n Description: {desc}"
            self.log_signal.emit(message)
        except Exception as e:
            self.log_signal.emit(f"Error during processing new submit CL data for log {e}")
    
    def process_exclusive_checkout_cl_for_log(self, file_info:dict, has_become_locked:bool) -> None:
        """Forms descriptive and exclusive checkout event log message from the changelists data and sends it to the log."""
        try:
            file_path = file_info["depotFile"]
            if has_become_locked:
                user = file_info["actionOwner"]
                message = f"[MONITOR] File {file_path} is now IN exclusive checkout by user {user}."
            else:
                message = f"[MONITOR] File {file_path} is NOT in exclusive checkout anymore."
            self.log_signal.emit(message)
        except Exception as e:
            self.log_signal.emit(f"Error during processing new exclusive checkout event CL data for log {e}")

    def stop_monitor(self) -> None:
        """Stops the monitoring."""
        #For future work, make sure that the thread is properly killed in this method.
        self.is_running = False

