@echo off
chcp 65001 >nul
echo WinRAR 密码管理器 - 打包工具
echo.

REM 检查 Python 是否安装
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误：未检测到 Python，请先安装 Python 3.6 或更高版本
    pause
    exit /b 1
)

echo 正在检查并安装 PyInstaller...
python -m pip install pyinstaller --quiet

echo.
echo 开始打包...
echo ========================================

python build_exe.py

if errorlevel 1 (
    echo.
    echo 打包失败！
    pause
    exit /b 1
)

echo.
echo 打包完成！可执行文件在 dist 文件夹中
pause

