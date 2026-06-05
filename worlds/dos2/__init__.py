from worlds.LauncherComponents import Component, Type, components, launch

from .World import DOS2World as DOS2World

def launch_client(*args: str) -> None:
    from .DOS2Client import launch_dos2_client
    launch(launch_dos2_client, name = "Divinity Original Sin 2 Client", args = args)
components.append(
    Component(
        "Divinity Original Sin 2 Client",
        func = launch_client,
        game_name = "Divinity Original Sin 2",
        component_type = Type.CLIENT,
        supports_uri = True
    )
)