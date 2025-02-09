import P4

class PerforceHelper:
    def __init__(self):
        self.p4 = P4.P4()

    def connect(self) -> tuple[bool, str]:
        """ Atempts to connect to the Perforce server, returns a tuple of status and message. """
        if self.p4.connected():
            return True, "Already connected to Perforce server. Skipping redundant connection request."
        self.p4.connect()
        if self.p4.connected():
            return (True, "Connected to Perforce server.")
        return (False, "Failed to connect to Perforce server.")
    
    def disconnect(self) -> tuple[bool, str]:
        """ Atempts to disconnect from the Perforce server, returns a tuple of status and message. """
        if self.p4.connected():
            self.p4.disconnect()
            return (True, "Disconnected from Perforce server.")
        return (True, "Not connected to Perforce server. Nothing to disconnect.")
    
    def list_files_in_path(self, depot_path:str) -> tuple[bool, list[str]]:
        """List file paths in the specified Perforce depot path.
        Returns a tuple of status and a list of file paths, if succesful. """
        try:
            files = self.p4.run("files", depot_path)
            if files:
                return True, (file["depotFile"] for file in files)
        except P4.P4Exception as e:
            return False, e.value
        
    def mark_for_add_files(self, depot_path:str) -> tuple[bool, str]:
        """Mark for add non-existed in the depot files at the specified location. 
        Returns a tuple of status and log string about checked-out operations."""

        try:
            files_logs = self.p4.run("add", depot_path)
            processed_log = "\n".join(
                            f"Marked for Add file: {file_log['depotFile']}"
                            for file_log in files_logs
                            if isinstance(file_log,dict))
            return True, processed_log
        except P4.P4Exception as e:
            return False, e.value
    
    def checkout_files(self, depot_path:str) -> tuple[bool, str]:
        """Mark on checkout existed files in the depot files at the specified location. 
        Returns a tuple of status and log string about checked-out operations."""

        try:
            files_logs = self.p4.run("edit", depot_path)
            processed_log = "\n".join(
                            f"Checked out file: {file_log['depotFile']}"
                            for file_log in files_logs
                            if isinstance(file_log,dict))
            return True, processed_log
        except P4.P4Exception as e:
            return False, e.value
        
    def mark_for_add_or_checkout(self, depot_path:str) -> tuple[bool, str]:
        """General method to get the files on modifications. 
        Calls mark_for_add_files and checkout_files methods.
        Returns a tuple of status and log string about checked-out operations."""

        result_add, log_add_call = self.mark_for_add_files(depot_path)
        result_checkout, log_checkout_call = self.checkout_files(depot_path)
        return (result_add and result_checkout), "\n".join([log_add_call, log_checkout_call])