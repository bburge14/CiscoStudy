# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec that bundles CiscoStudy (Streamlit app + engine + content)
into a single self-contained Windows executable: dist/CiscoStudy.exe.

Build (on Windows):   pyinstaller --noconfirm --clean CiscoStudy.spec
"""
from PyInstaller.utils.hooks import collect_all, copy_metadata

datas, binaries, hiddenimports = [], [], []

# Streamlit and the libraries it loads dynamically at runtime need their data
# files, binaries and submodules pulled in explicitly.
for pkg in [
    "streamlit", "pandas", "numpy", "pyarrow", "altair", "pydeck", "tornado",
    "watchdog", "blinker", "click", "rich", "cachetools", "tenacity", "toml",
    "validators", "packaging", "pympler", "git",
]:
    try:
        d, b, h = collect_all(pkg)
        datas += d
        binaries += b
        hiddenimports += h
    except Exception:
        pass

# Streamlit (and friends) read their version via importlib.metadata, which needs
# the dist-info to be bundled.
for pkg in [
    "streamlit", "altair", "pandas", "numpy", "pyarrow", "click", "rich",
    "blinker", "cachetools", "tenacity", "toml", "validators", "watchdog",
    "gitpython", "pydeck", "tornado", "packaging", "protobuf", "pillow",
    "requests", "pympler",
]:
    try:
        datas += copy_metadata(pkg)
    except Exception:
        pass

# The application itself (served by Streamlit from the bundle root).
datas += [
    ("Home.py", "."),
    ("ui_common.py", "."),
    ("views", "views"),
    ("studyengine", "studyengine"),
    ("data", "data"),
    (".streamlit", ".streamlit"),
]

a = Analysis(
    ["launcher.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports + ["studyengine", "ui_common"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pytest", "_pytest", "tkinter"],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="CiscoStudy",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    runtime_tmpdir=None,
    console=True,              # keep a console so the learner sees status + can Ctrl+C
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
