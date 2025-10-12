from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Group
from rich import box
from rich.box import Box   
from rich.progress import Progress, BarColumn, TextColumn


console = Console()

vined_border = "🌿"


def show_intro():
    title = Text(f"🌴🌴🌴🌴🌴 Welcome to Stranglethorn Vale! 🌴🌴🌴🌴🌴", style="bold italic underline green")
    body = Text(
        (
            "You awaken in the depths of the jungle, the air thick with humidity and the cries of unseen creatures.\n"
            "Your head throbs — the last thing you remember is the storm that tore your raft apart.\n\n"
            "Around you, the towering palms whisper in the wind. To the north, you hear rushing water — "
            "perhaps the river that nearly claimed your life. To the east, faint smoke rises... "
            "and with it, the unsettling rhythm of drums.\n\n"
            "You are unarmed and alone. Somewhere out there, predators watch from the shadows.\n"
            "You push aside the ferns and step into a small clearing…"
        ), 
            style="green",
    )
    panel = Panel.fit(
        body,
        box=box.DOUBLE,
        title=title,
        border_style="green",
        padding=(1, 2),
    )
    console.print(panel)

def show_location(location):
    header = Text(f"🌴 {location.name} 🌴", style="bold underline green")

    desc = Text(location.description, style="italic green")
    
    title = Text("\nExits:", style="bold green")

    exits_table = Table(title=title, show_header=False, box=box.ASCII, style="green")
    if location.exits:
        for direction, dest in location.exits.items():
            exits_table.add_row(f"[bold green]{direction}[/bold green] → {dest.name}")
    else:
        exits_table.add_row("[dim]No exits[/dim]")

    group = Group(desc, exits_table)

    
    panel = Panel.fit(
        group,
        title=header,
        border_style="green",
        padding=(1, 2),
    )

    console.print(panel)

def show_items(location):
    items_table = Table(title="Items Nearby", show_header=False, box=box.ASCII)
    if hasattr(location, "items") and location.items:
        for item in location.items:
            items_table.add_row(f"🪶 [yellow]{item.name}[/yellow]")
    else:
        items_table.add_row(f"[dim]No items here[/dim]")
    console.print(items_table)

def enemy_info(location):
    if hasattr(location, "enemy") and location.enemy:
        enemy_panel = Panel(
            f"⚔ [red]{location.enemy.name}[/red] — HP: {location.enemy.health}",
            title="Enemy Nearby",
            border_style="red",
            padding=(0, 2)
        )
        console.print(enemy_panel)


def show_movement(direction, location_name):
    text = Text(f"\nYou move {direction} to the {location_name}.", style="green italic")    
    panel = Panel.fit(
        text,
        border_style="green",
    )
    console.print(panel)

def show_combat_intro(enemy):
    header = Text("⚔️   COMBAT  ⚔️", style = "bright_red")
    body = f"A wild {enemy.name} attacks you"
    panel = Panel.fit(
        body,
        title=header,
        border_style="bright_red"
    )
    console.print(panel)

