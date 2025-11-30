#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
打包脚本 - 将 WinRAR_Password_Manager.py 打包成可执行文件
"""

import subprocess
import sys
import os

def check_pyinstaller():
    """检查是否安装了 PyInstaller"""
    try:
        import PyInstaller
        return True
    except ImportError:
        return False

def install_pyinstaller():
    """安装 PyInstaller"""
    print("正在安装 PyInstaller...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    print("PyInstaller 安装完成！\n")

def build_exe():
    """打包可执行文件"""
    script_name = "WinRAR_Password_Manager.py"
    exe_name = "WinRAR_Password_Manager"
    
    if not os.path.exists(script_name):
        print(f"错误：找不到脚本文件 {script_name}")
        return False
    
    print("开始打包...")
    print("=" * 50)
    
    # PyInstaller 打包命令
    cmd = [
        "pyinstaller",
        "--onefile",                    # 打包成单个文件
        "--console",                    # 控制台应用
        "--name", exe_name,             # 可执行文件名称
        "--clean",                      # 清理临时文件
        "--noconfirm",                  # 不询问覆盖
        script_name
    ]
    
    try:
        subprocess.check_call(cmd)
        print("\n" + "=" * 50)
        print("打包完成！")
        print(f"可执行文件位置：dist\\{exe_name}.exe")
        print("\n提示：")
        print("  - 可以将 dist\\{exe_name}.exe 复制到任何 Windows 电脑使用")
        print("  - 不需要安装 Python 环境")
        print("  - 首次运行可能需要管理员权限")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n打包失败：{e}")
        return False
    except Exception as e:
        print(f"\n发生错误：{e}")
        return False

if __name__ == "__main__":
    print("WinRAR 密码管理器 - 打包工具\n")
    
    # 检查并安装 PyInstaller
    if not check_pyinstaller():
        print("未检测到 PyInstaller，需要先安装。")
        install_pyinstaller()
    
    # 开始打包
    if build_exe():
        print("\n打包成功！")
    else:
        print("\n打包失败，请检查错误信息。")
        sys.exit(1)

