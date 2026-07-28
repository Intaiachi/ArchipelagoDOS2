import os
from pathlib import Path
import Utils

import settings


class DOS2Settings(settings.Group):
    class RootDirectory(settings.UserFolderPath):
        """
        Locates the Osiris Data folder in the DOS2DE folder in documents.
        This is used by both the client and game to communicate with one another.
        """

        description = "DOS2 communication directory"

        def browse(self, **kwargs):
            from Utils import messagebox
            
            messagebox(
                "DOS2 communication directory",
                "Please select the DOS2 Osiris Data folder.\nThis will be in something like \"Documents\\Larian Studios\\Divinity Original Sin 2 Definitive Edition\\\" or equivilent.\nIf it is not there, refer to the setup guide before continuing.",
            )
            result = super().browse(**kwargs)
            path = Path(result)
            if(path.name == "Osiris Data"):
                return result
            else:
                Utils.messagebox("Error", "Comm file directory is incorrect!", error = True)

    root_directory: RootDirectory = RootDirectory(
        "error"
    )