#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
WinRAR 密码管理器
用于导出和导入 WinRAR 保存的密码
"""

import os
import sys
import ctypes
import subprocess
from pathlib import Path

# 检查是否以管理员身份运行
def is_admin():
    """检查当前进程是否以管理员身份运行"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# 请求管理员权限
def request_admin():
    """如果未以管理员身份运行，则请求管理员权限"""
    if not is_admin():
        print("正在请求管理员权限...")
        # 使用 ShellExecute 以管理员身份重新运行脚本
        if getattr(sys, 'frozen', False):
            # 如果是打包后的可执行文件
            script_path = sys.executable
            exe_path = script_path
        else:
            # 如果是 Python 脚本
            script_path = os.path.abspath(sys.argv[0])
            exe_path = sys.executable
        
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", exe_path, f'"{script_path}"', None, 1
        )
        sys.exit(0)

# 检查并请求管理员权限
request_admin()

# 确认管理员权限
print("\n确认：当前脚本以管理员身份运行。\n")

# 设置注册表路径
REG_PATH = r"Software\WinRAR\Passwords"
REG_PATH_FULL = r"HKEY_CURRENT_USER\Software\WinRAR\Passwords"

# 获取脚本所在目录（兼容打包后的可执行文件）
def get_script_dir():
    """获取脚本或可执行文件所在目录"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的可执行文件
        return Path(sys.executable).parent.absolute()
    else:
        # 如果是 Python 脚本
        return Path(__file__).parent.absolute()

SCRIPT_DIR = get_script_dir()
BACKUP_FILE = SCRIPT_DIR / "WinRAR_Passwords.reg"

# 检查注册表项是否存在
def test_registry_path():
    """检查注册表项是否存在"""
    try:
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        winreg.CloseKey(key)
        return True
    except FileNotFoundError:
        return False
    except Exception:
        return False

# 导出注册表项
def export_registry_key():
    """导出注册表项到 .reg 文件"""
    try:
        if not test_registry_path():
            print("错误：未找到 Passwords 注册表项。可能是因为从未在 WinRAR 中保存过密码。")
            return False
        
        print("提示：WinRAR 密码是加密存储的，加密与当前 Windows 用户账户相关。")
        print("     在同一台电脑的同一用户账户下导入可以正常使用。")
        print("     跨用户或跨电脑可能无法使用。\n")
        
        # 使用 reg.exe 导出注册表
        result = subprocess.run(
            ["reg.exe", "export", REG_PATH_FULL, str(BACKUP_FILE), "/y"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print(f"注册表项已成功导出到：{BACKUP_FILE}")
            print("\n注意：请妥善保管此文件，它包含您的 WinRAR 密码（已加密）。")
            return True
        else:
            print(f"导出注册表项失败！错误代码：{result.returncode}")
            if result.stderr:
                print(f"错误信息：{result.stderr}")
            return False
    except Exception as e:
        print(f"导出注册表项时发生错误：{str(e)}")
        return False

# 导入注册表项
def import_registry_key():
    """从 .reg 文件导入注册表项"""
    try:
        if not BACKUP_FILE.exists():
            print("备份文件不存在！请先导出注册表项。")
            return False
        
        print("警告：WinRAR 密码是加密存储的，加密与 Windows 用户账户相关。")
        print("     导入后能否使用取决于：")
        print("     ✓ 同一台电脑的同一用户账户：通常可以正常使用")
        print("     ✗ 不同用户账户或不同电脑：可能无法使用")
        print()
        
        confirm = input("确认要导入吗？(y/n): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("已取消导入。")
            return False
        
        # 使用 reg.exe 导入注册表
        result = subprocess.run(
            ["reg.exe", "import", str(BACKUP_FILE)],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("注册表项已成功导入。")
            print("\n提示：请打开 WinRAR 测试密码是否可用。")
            print("     如果密码无法使用，说明加密密钥不匹配（可能是不同用户或电脑）。")
            return True
        else:
            print(f"导入注册表项失败！错误代码：{result.returncode}")
            if result.stderr:
                print(f"错误信息：{result.stderr}")
            return False
    except Exception as e:
        print(f"导入注册表项时发生错误：{str(e)}")
        return False

# 显示菜单
def show_menu():
    """显示主菜单"""
    os.system("cls" if os.name == "nt" else "clear")
    separator = "=" * 50
    print(f"\n{separator}")
    print("  WinRAR 密码管理器")
    print(separator)
    print()
    print("  1. 导出注册表项")
    print("  2. 导入注册表项（文件名为 WinRAR_Passwords.reg）")
    print("  3. 退出")
    print()
    print(separator)
    print()

# 主程序
def main():
    """主程序循环"""
    while True:
        show_menu()
        
        choice = input("请输入选项（1/2/3）：").strip()
        
        if choice == "1":
            print()
            export_registry_key()
            print()
            input("按 Enter 键继续...")
        elif choice == "2":
            print()
            import_registry_key()
            print()
            input("按 Enter 键继续...")
        elif choice == "3":
            print("\n感谢使用！")
            sys.exit(0)
        else:
            print("\n无效的选项！请选择 1、2 或 3。")
            import time
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序已中断。")
        sys.exit(0)
    except Exception as e:
        print(f"\n发生未预期的错误：{str(e)}")
        input("按 Enter 键退出...")
        sys.exit(1)

