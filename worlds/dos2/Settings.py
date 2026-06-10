import os

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
                "Please select the DOS2 Osiris Data folder.\nThis will be in something like Documents\\Larian Studios\\Divinity Original Sin 2 Definitive Edition\\ or equivilent.\nIf it is not there, refer to the setup guide before continuing",
            )
            return super().browse(**kwargs)

    root_directory: RootDirectory = RootDirectory(
        os.path.join("Documents", "Larian Studios", "Divinity Original Sin 2 Definitive Edition", "Osiris Data")
    )