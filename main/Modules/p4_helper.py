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
    
    def create_new_cl(self, description:str = "") -> tuple[bool, str]:
        """Creates the new changelist and (optional) sets the custom description.
        Returns a tuple of status and CL number (string) created."""
        try:
            cl_spec = self.p4.run("change", "-o")[0]
            cl_spec["Description"] = f"[AUTOMATED] {description}"
            self.p4.input = cl_spec
            cl = self.p4.run("change", "-i")
            cl_number = cl[0].split()[1]
            return True, cl_number
        except P4.P4Exception as e:
            return False, e.value
    
    def move_files_to_cl(self, depot_path:str, cl_number:str) -> tuple[bool, str]:
        """Moves the files from the given depot path to the specified CL number.
        Returns a tuple of status and string message for log output created."""
        try:
            file_logs = self.p4.run("reopen", "-c", cl_number, depot_path)
            log = "\n".join(
                f"Moved to CL {cl_number} file: {file_log['depotFile']}"
                for file_log in file_logs
            )
            return True, log
        except P4.P4Exception as e:
            return False, e.value
        
    def delete_all_empty_cls(self) -> tuple[bool, str]:
        """Identifies all empty Changelists and deletes them for the current client.
        Returns a tuple of Status and log string message of processed results."""

        try:
            changelists = self.p4.run("changes", "-c", self.p4.client, "-s", "pending")
            deleted_cl_ids = []
            for cl in changelists:
                cl_id = cl['change']
                opened_files = self.p4.run("opened", "-c", cl_id)
                if not opened_files:
                    self.p4.run("change", "-d", cl_id)
                    deleted_cl_ids.append(cl_id)
            if deleted_cl_ids:
                log = "\n".join(
                    f"Deleted empty Changelist in ID {cl_id}"
                    for cl_id in deleted_cl_ids
                    )
            else:
                log = "No empty CLs to delete."
            return True, log
        except P4.P4Exception as e:
            return False, e.value
        
    def revert_files_from_cl(self, cl_number:str, only_unchanged:bool = False) -> tuple[bool, str]:
        """Reverts files from the given pending Changelists.
        Returns a tuple of Status and log string message of processed results."""

        try:
            if only_unchanged:
                revert_result = self.p4.run("revert", "-a","-c", cl_number, "//...")
            else:
                revert_result = self.p4.run("revert", "-c", cl_number, "//...")
            if revert_result:
                log = "\n".join(
                        f"File {result['depotFile']} was reverted from CL {cl_number}"
                        for result in revert_result
                        )
            else:
                log = f"No files were reverted from CL {cl_number} with option 'Revert only unchanged' set to {only_unchanged}"
            return True, log
        except P4.P4Exception as e:
            return False, e.value
        
    def shelve_files_in_cl(self, cl_number:str) -> tuple[bool, str]:
        """Shelves all files in the specified pending Changelist.
        Returns a tuple of Status and log string message of processed results."""
        try:
            shelve_result = self.p4.run("shelve", "-c", cl_number)
            log = "\n".join(
                        f"File {result['depotFile']} was shelved in CL {cl_number}"
                        for result in shelve_result
                        )
            return True, log
        except P4.P4Exception as e:
            return False, e.value
        
    def unshelve_files_in_cl(self, shelve_cl_number:str, target_cl_number:str=None) -> tuple[bool, str]:
        """Un-shelves all files from the specified Changelist to a target Changelist.
        If no target CL is specified, the files will be un-shelved in the same CL where they were kept.
        Returns a tuple of Status and log string message of processed results."""
        try:
            target_cl_number = target_cl_number or shelve_cl_number
            unshelve_result = self.p4.run("unshelve", "-s", shelve_cl_number, "-f", "-c", target_cl_number)
            if isinstance(unshelve_result[0], dict):   
                log = "\n".join(
                            f"Shelved File {result['depotFile']} was un-shelved from CL {shelve_cl_number} to CL {target_cl_number}"
                            for result in unshelve_result
                            )
            else:
                log = "\n".join(unshelve_result)
            return True, log
        except P4.P4Exception as e:
            return False, e.value
    
    def delete_shelved_files_in_cl(self, shelve_cl_number:str) -> tuple[bool, str]:
        """Delete shelved files in the specified pending Changelist.
        Returns a tuple of Status and log string message of processed results."""
        try:
            shelve_delete_result = self.p4.run("shelve", "-d", "-c", shelve_cl_number)
            return True, shelve_delete_result[0]
        except P4.P4Exception as e:
            return False, e.value
    
    def sync_to_latest(self, depot_path:str) -> tuple[bool, str]:
        """Syncronizes all files in the specified depot path to their latest revision.
        Returns a tuple of Status and log string message of processed results."""
        try:
            sync_result = self.p4.run("sync", depot_path)
            if isinstance(sync_result[0], dict):   
                log = "\n".join(
                            f"File {result['depotFile']} was {result['action']} to revision #{result['rev']}"
                            for result in sync_result
                            )
            else:
                log = "\n".join(sync_result)
            return True, log
        except P4.P4Exception as e:
            return False, e.value
    
    def check_for_file_conflicts(self, depot_path:str, should_accept_target:bool) -> tuple[bool, str]:
        """Checks if there are file conflicts in the given depot path and if so, evokes a resolving method.
        Returns a tuple of Status and log string message of processed results."""
        try:
            resolve_preview = self.p4.run("resolve", "-n", depot_path)
            conflicts = [file['fromFile'] for file in resolve_preview]
            if conflicts:
                return self.resolve_file_conflicts(conflicts, should_accept_target)
            return True, f"No conflicts found for the depot path {depot_path}"
        except  P4.P4Exception as e:
            return False, e.value
    
    def resolve_file_conflicts(self, files_with_conflicts:list[str], should_accept_target:bool) -> tuple[bool, str]:
        """Resolves each file conflict with the specififed option.
        Returns a tuple of Status and log string message of processed results."""
        resolve_choice = "-ay" if should_accept_target else "-at"
        try:
            for file_path in files_with_conflicts:
                self.p4.run("resolve", resolve_choice, file_path)
            log = "\n".join(
                    f"Resolved conflict for file {file_path} with choice {resolve_choice}"
                    for file_path in files_with_conflicts
                    )
            return True, log
        except  P4.P4Exception as e:
            return False, e.value
    
    def submit_cl(self, cl_number:str) -> tuple[bool, str]:
        """Submits all files in the given changelists.
        Returns a tuple of Status and log string message of processed results."""
        try:
            submit_result = self.p4.run("submit", "-c", cl_number)
            log = "\n".join(f"File {result['depotFile']} was submitted in CL {cl_number}"
                    for result in submit_result
                    if result.get("depotFile"))
            return True, log
        except  P4.P4Exception as e:
            return False, e.value

    def get_all_pending_cls_for_ui(self) -> list[str]:
        """Supportive UI method to prepare data for the combobox."""
        changelists = self.p4.run("changes", "-c", self.p4.client, "-s", "pending")
        cl_id_desc = [f"{cl['change']}: {cl['desc']}"
                      for cl in changelists]
        return cl_id_desc