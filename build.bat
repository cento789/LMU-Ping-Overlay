@echo off
echo ==========================================
echo  LMU Ping Overlay - Build Script
echo  Author: cento789
echo ==========================================
echo.

pip install pyinstaller 2>nul

echo Building LMUPingOverlay.exe ...
pyinstaller --onefile --noconsole --name LMUPingOverlay --version-file version_info.py --icon app_icon.ico --add-data "app_icon.ico;." ping_overlay.py

echo.
if exist dist\LMUPingOverlay.exe (
    echo BUILD SUCCESS: dist\LMUPingOverlay.exe
) else (
    echo BUILD FAILED
)
pause
