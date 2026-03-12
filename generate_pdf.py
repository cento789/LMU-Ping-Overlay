"""Generate the LMU Ping Overlay PDF User Guide."""

from fpdf import FPDF
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "docs")
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "LMUPingOverlay_UserGuide.pdf")


class Guide(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 8, "LMU Ping Overlay v1.2.2 - User Guide", align="R")
        self.ln(12)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}  |  Author: cento789", align="C")

    def section_title(self, title):
        self.set_font("Helvetica", "B", 14)
        self.set_text_color(0, 120, 0)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(0, 170, 0)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(4)

    def body_text(self, text):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet(self, text, bold_prefix=""):
        self.set_font("Helvetica", "", 11)
        self.set_text_color(30, 30, 30)
        self.cell(8, 6, "-")
        if bold_prefix:
            self.set_font("Helvetica", "B", 11)
            self.write(6, bold_prefix + " ")
            self.set_font("Helvetica", "", 11)
        self.multi_cell(0, 6, text)

    def table_header(self, col1, col2, w1=60):
        self.set_font("Helvetica", "B", 10)
        self.set_fill_color(0, 150, 0)
        self.set_text_color(255, 255, 255)
        self.cell(w1, 7, col1, border=1, fill=True)
        self.cell(0, 7, col2, border=1, fill=True, new_x="LMARGIN", new_y="NEXT")

    def table_row(self, col1, col2, w1=60, bold_first=True):
        if bold_first:
            self.set_font("Helvetica", "B", 10)
        else:
            self.set_font("Helvetica", "", 10)
        self.set_text_color(30, 30, 30)
        self.cell(w1, 7, col1, border=1)
        self.set_font("Helvetica", "", 10)
        self.cell(0, 7, col2, border=1, new_x="LMARGIN", new_y="NEXT")


def generate():
    pdf = Guide()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # ── Title ────────────────────────────────────────────────────────────────
    pdf.ln(20)
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(0, 150, 0)
    pdf.cell(0, 15, "LMU Ping Overlay", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "User Guide", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_font("Helvetica", "", 12)
    pdf.cell(0, 8, "Version 1.2.2", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, "Author: cento789", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 6,
        "A lightweight, fully transparent network latency (ping) overlay for "
        "Le Mans Ultimate. Displays real-time ping, packet loss and jitter "
        "directly over the game screen, automatically detecting the server you "
        "are connected to.", align="C")

    # ── Features ─────────────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("1. Features")
    features = [
        ("Real-time ping display", "updated every 1-10 seconds (configurable)"),
        ("Auto-detect LMU server", "reads active TCP/UDP connections to find the game server IP"),
        ("LMU REST API support", "uses localhost:6397 API when LMU is running for enhanced accuracy"),
        ("Ping smoothing", "moving average over the last N samples to reduce noise"),
        ("Packet loss %", "tracks failed pings and shows the loss percentage"),
        ("Jitter display", "standard deviation of recent pings shown as +/-Xms"),
        ("Blink alert", "text blinks when ping exceeds the 'bad' threshold"),
        ("Dynamic color", "green / yellow / red based on configurable thresholds"),
        ("Fully transparent", "only the text is visible; background is fully transparent"),
        ("Always on top", "stays visible over fullscreen and borderless games"),
        ("Click-through mode", "mouse events pass through the overlay in-game"),
        ("Draggable", "left-click and drag to reposition anywhere on screen"),
        ("Snap to corner", "one-click positioning to any of the 4 screen corners"),
        ("Font selector", "choose from 9 fonts (Consolas, Arial, Segoe UI, etc.)"),
        ("Font size & opacity", "adjustable to fit any HUD layout"),
        ("Text shadow", "drop shadow for readability on bright backgrounds"),
        ("DPI-aware", "crisp text on HiDPI and 4K monitors"),
        ("System tray", "minimizes to the notification area after start"),
        ("Global hotkey", "Ctrl+Shift+H to toggle visibility in-game"),
        ("Persistent settings", "all preferences and position saved automatically"),
    ]
    for bold, text in features:
        pdf.bullet(text, bold_prefix=bold)

    # ── Installation ─────────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("2. Installation")
    pdf.body_text(
        "No installation required. LMU Ping Overlay is a portable, standalone .exe file.\n\n"
        "Steps:\n"
        "1. Download LMUPingOverlay.exe\n"
        "2. Place it in any folder (e.g. your LMU tools folder)\n"
        "3. Double-click to run\n\n"
        "Note: On first launch, Windows SmartScreen may show a warning. "
        "Click 'More info' then 'Run anyway' to proceed.\n\n"
        "No administrator rights are required. Settings are stored in your user profile."
    )

    # ── Settings Window ───────────────────────────────────────────────────────
    pdf.section_title("3. Settings Window")
    pdf.body_text(
        "When you launch the application, a dark-themed settings window appears. "
        "It is organized in three tabs: Display, Ping and Position. "
        "A live preview at the bottom updates as you change settings."
    )

    # Display tab
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 150, 0)
    pdf.cell(0, 8, "Tab: Display", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(30, 30, 30)
    pdf.ln(1)
    pdf.table_header("Setting", "Description")
    display_rows = [
        ("Font",           "Font family (Consolas, Arial, Segoe UI, Verdana, etc.)"),
        ("Font size",      "Text size in pixels (10 to 60)"),
        ("Opacity",        "Overall transparency from 20% to 100%"),
        ("Show 'PING:'",   "Whether to include the 'PING:' label prefix in the text"),
        ("Shadow",         "Dark drop shadow behind the text for readability"),
        ("Dynamic color",  "Enable green/yellow/red color based on latency"),
        ("Colors",         "Click Good/Warn/Bad buttons to open a color picker"),
    ]
    for c1, c2 in display_rows:
        pdf.table_row(c1, c2)

    pdf.ln(5)

    # Ping tab
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 150, 0)
    pdf.cell(0, 8, "Tab: Ping", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(30, 30, 30)
    pdf.ln(1)
    pdf.table_header("Setting", "Description")
    ping_rows = [
        ("Auto-detect",    "Detect the LMU game server IP automatically (recommended)"),
        ("Fallback target","IP or hostname to ping when auto-detect is off or fails"),
        ("Interval (sec)", "How often to send a ping packet (1 to 10 seconds)"),
        ("Smoothing",      "Number of recent pings to average for stable display (1-10)"),
        ("Warn (ms)",      "Threshold above which the ping turns yellow"),
        ("Bad (ms)",       "Threshold above which the ping turns red"),
        ("Show loss %",    "Display packet loss percentage alongside ping (e.g. | 2%)"),
        ("Show jitter +/-","Display ping jitter as standard deviation (e.g. +/-8)"),
        ("Blink on bad",   "Blink the overlay text when ping exceeds the bad threshold"),
    ]
    for c1, c2 in ping_rows:
        pdf.table_row(c1, c2)

    pdf.ln(5)

    # Position tab
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 150, 0)
    pdf.cell(0, 8, "Tab: Position", new_x="LMARGIN", new_y="NEXT")
    pdf.set_text_color(30, 30, 30)
    pdf.ln(1)
    pdf.body_text(
        "Four large buttons (Top-Left, Top-Right, Bot-Left, Bot-Right) let you snap "
        "the overlay to a screen corner when clicking START. The same snap actions are "
        "also available at any time from the system tray icon context menu."
    )

    pdf.ln(2)
    pdf.body_text("Click the green START button to launch the overlay and minimize to tray.")

    # ── In-Game Controls ──────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("4. In-Game Controls")
    pdf.body_text("Once the overlay is running, you can interact with it without leaving the game:")
    pdf.ln(2)
    pdf.table_header("Action", "How", w1=55)
    controls = [
        ("Move overlay",       "Left-click and drag (position is saved immediately)"),
        ("Hide / Show",        "Press Ctrl+Shift+H"),
        ("Click-through ON/OFF","Right-click the tray icon > Click-through"),
        ("Snap to corner",     "Right-click tray icon > Snap TL / TR / BL / BR"),
        ("Quit",               "Right-click tray icon > Quit"),
    ]
    for c1, c2 in controls:
        pdf.table_row(c1, c2, w1=55)

    pdf.ln(6)
    pdf.section_title("5. Click-Through Mode")
    pdf.body_text(
        "By default the overlay intercepts mouse clicks (so you can drag it). "
        "Once you have positioned it, enable Click-Through mode from the tray menu "
        "so that all mouse events pass directly to the game window underneath.\n\n"
        "To move the overlay again:\n"
        "1. Open the tray icon context menu\n"
        "2. Disable Click-Through\n"
        "3. Drag the overlay to its new position\n"
        "4. Re-enable Click-Through"
    )

    # ── Auto-Detect Server ────────────────────────────────────────────────────
    pdf.section_title("6. Auto-Detect Server")
    pdf.body_text(
        "When 'Auto-detect' is enabled, the overlay looks for the game server in "
        "two ways (tried in order):\n\n"
        "1. LMU REST API (localhost:6397) - reads session info directly from the game. "
        "This is the most accurate method and works only while LMU is running.\n\n"
        "2. netstat inspection - scans active TCP/UDP connections of the LMU process "
        "and finds the most common public IP address. This works for any game session "
        "including online practice, qualifying and races.\n\n"
        "The detection method used is shown in the system tray tooltip:\n"
        "   Ping: 42 ms | Loss: 0% | Jitter: +/-5 ms -> 1.2.3.4 (API)\n"
        "   Ping: 42 ms | Loss: 0% | Jitter: +/-5 ms -> 1.2.3.4 (netstat)\n\n"
        "If LMU is not running or no server is found, the overlay falls back to the "
        "configured 'Fallback target' (default: 8.8.8.8)."
    )

    # ── Display Format ────────────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("7. Display Format")
    pdf.body_text("The overlay text format depends on which options are enabled:")
    pdf.ln(1)
    pdf.set_font("Courier", "B", 11)
    pdf.set_text_color(0, 150, 0)
    examples = [
        ("Show label + loss",         "PING: 42 ms | 0%"),
        ("Show label + jitter + loss", "PING: 42 ms +/-5 | 0%"),
        ("No label + loss",            "42 ms | 0%"),
        ("No label, no extras",        "42 ms"),
        ("Timeout / no reply",         "PING: --- ms | 100%"),
    ]
    for desc, sample in examples:
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(60, 60, 60)
        pdf.cell(75, 6, desc)
        pdf.set_font("Courier", "B", 10)
        pdf.set_text_color(0, 180, 0)
        pdf.cell(0, 6, sample, new_x="LMARGIN", new_y="NEXT")

    pdf.ln(4)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(30, 30, 30)
    pdf.body_text(
        "Color thresholds (with Dynamic color enabled):\n"
        "  - Green: ping < Warn threshold\n"
        "  - Yellow: ping >= Warn threshold\n"
        "  - Red: ping >= Bad threshold\n\n"
        "When Blink is enabled, the text alternates on/off every 300ms "
        "while the ping is in the red zone."
    )

    # ── System Tray ───────────────────────────────────────────────────────────
    pdf.section_title("8. System Tray")
    pdf.body_text(
        "After pressing START, the application minimizes to the Windows system tray. "
        "A small signal-bars icon appears near the clock.\n\n"
        "Right-click the tray icon for the following options:"
    )
    pdf.ln(1)
    pdf.table_header("Menu item", "Action", w1=70)
    tray_rows = [
        ("LMU Ping Overlay v1.2.2", "Version label (not clickable)"),
        ("Show/Hide (Ctrl+Shift+H)", "Toggle overlay visibility"),
        ("Click-through: OFF/ON",    "Enable or disable mouse click-through"),
        ("Snap TL - Top-left",       "Move overlay to top-left corner"),
        ("Snap TR - Top-right",      "Move overlay to top-right corner"),
        ("Snap BL - Bot-left",       "Move overlay to bottom-left corner"),
        ("Snap BR - Bot-right",      "Move overlay to bottom-right corner"),
        ("Quit",                     "Close the application and save settings"),
    ]
    for c1, c2 in tray_rows:
        pdf.table_row(c1, c2, w1=70)

    # ── Settings Persistence ──────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("9. Settings Persistence")
    pdf.body_text(
        "All settings are saved automatically and restored on the next launch. "
        "The position is also saved immediately after every drag or snap action.\n\n"
        "Saved settings include:\n"
        "- Font family, size\n"
        "- Colors (good, warn, bad)\n"
        "- Opacity\n"
        "- Ping interval, target, auto-detect\n"
        "- Smoothing, warn/bad thresholds\n"
        "- Show loss / jitter / label / shadow toggles\n"
        "- Blink alert toggle\n"
        "- Overlay position (X, Y)\n\n"
        "Settings are stored in:\n"
        "   %APPDATA%\\LMUPingOverlay\\settings.json\n\n"
        "To reset all settings to defaults, delete this file."
    )

    # ── Tips ──────────────────────────────────────────────────────────────────
    pdf.section_title("10. Tips for Le Mans Ultimate")
    pdf.bullet(
        "Run LMU in Borderless Windowed mode for the best overlay compatibility.",
        bold_prefix="Display mode:")
    pdf.bullet(
        "Position the overlay in a corner that does not overlap with the LMU HUD "
        "(brake bias, fuel, tyre temps). The Position tab or tray snap options make "
        "this quick and easy.",
        bold_prefix="Positioning:")
    pdf.bullet(
        "Enable text shadow if racing on tracks with bright environments (e.g. "
        "Le Mans at midday) for better text readability.",
        bold_prefix="Readability:")
    pdf.bullet(
        "Enable Click-Through mode once the overlay is in place so you do not "
        "accidentally interact with it during a race.",
        bold_prefix="Click-Through:")
    pdf.bullet(
        "Set Warn to 60ms and Bad to 120ms as a starting point. Adjust based on "
        "your typical connection quality.",
        bold_prefix="Thresholds:")
    pdf.bullet(
        "Set Smoothing to 3-5 to filter out single spike reads without adding "
        "too much lag to the display.",
        bold_prefix="Smoothing:")
    pdf.bullet(
        "Use Ctrl+Shift+H to quickly hide the overlay during replays or menus.",
        bold_prefix="Quick hide:")
    pdf.bullet(
        "The LMU REST API detection (localhost:6397) is more reliable than netstat. "
        "It works automatically when LMU is running - no configuration required.",
        bold_prefix="Auto-detect:")

    # ── Command line ──────────────────────────────────────────────────────────
    pdf.ln(4)
    pdf.section_title("11. Command Line")
    pdf.body_text("You can check the application version from the command line:")
    pdf.set_font("Courier", "", 11)
    pdf.cell(0, 7, "  LMUPingOverlay.exe --version", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.ln(2)
    pdf.body_text('Output: "LMU Ping Overlay v1.2.2 by cento789"')

    # ── Building from Source ──────────────────────────────────────────────────
    pdf.add_page()
    pdf.section_title("12. Building from Source")
    pdf.body_text("Requirements: Python 3.10+")
    pdf.ln(1)
    pdf.body_text("Install dependencies:")
    pdf.set_font("Courier", "", 10)
    pdf.cell(0, 6, "  pip install pyinstaller pystray Pillow keyboard fpdf2",
             new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)
    pdf.set_font("Helvetica", "", 11)
    pdf.body_text("Build command:")
    pdf.set_font("Courier", "", 9)
    pdf.multi_cell(0, 5,
        "  pyinstaller --onefile --noconsole --name LMUPingOverlay\n"
        "    --version-file version_info.py\n"
        "    --icon app_icon.ico\n"
        "    --add-data \"app_icon.ico;.\"\n"
        "    ping_overlay.py")
    pdf.ln(3)
    pdf.set_font("Helvetica", "", 11)
    pdf.body_text(
        "The built executable will appear in the dist/ folder.\n\n"
        "To regenerate this PDF:\n"
        "  python generate_pdf.py"
    )

    # ── Save ──────────────────────────────────────────────────────────────────
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pdf.output(OUTPUT_FILE)
    print(f"PDF generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate()
