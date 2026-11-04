"""Frozen entry point for the packaged CiscoStudy .exe.

PyInstaller bundles the Streamlit app and all dependencies into a single
executable; this module is the thing that runs when the exe is launched. It
starts the Streamlit server in-process and opens the browser.
"""
from __future__ import annotations

import os
import sys
import threading
import time
import webbrowser


def _base_dir() -> str:
    # When frozen by PyInstaller, bundled data is unpacked under sys._MEIPASS.
    if getattr(sys, "frozen", False):
        return sys._MEIPASS  # type: ignore[attr-defined]
    return os.path.dirname(os.path.abspath(__file__))


def _open_browser(url: str, delay: float = 2.5) -> None:
    def _go() -> None:
        time.sleep(delay)
        try:
            webbrowser.open(url)
        except Exception:
            pass
    threading.Thread(target=_go, daemon=True).start()


def main() -> None:
    base = _base_dir()
    # chdir so Streamlit finds .streamlit/config.toml (theme) in the bundle.
    os.chdir(base)
    app_path = os.path.join(base, "app.py")
    port = os.environ.get("CISCOSTUDY_PORT", "8501")

    print("=" * 60)
    print(" CiscoStudy is starting...")
    print(f" Open your browser to:  http://localhost:{port}")
    print(" (a tab should open automatically)")
    print(" Close this window or press Ctrl+C to stop.")
    print("=" * 60, flush=True)

    _open_browser(f"http://localhost:{port}")

    sys.argv = [
        "streamlit", "run", app_path,
        "--server.port", port,
        "--server.headless", "true",          # we open the browser ourselves
        "--server.fileWatcherType", "none",   # no file watching inside a bundle
        "--browser.gatherUsageStats", "false",
    ]
    from streamlit.web import cli as stcli
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
