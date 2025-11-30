# WinRAR 密码导入导出工具

一个用于备份和恢复 WinRAR 保存密码的实用工具。支持导出和导入 WinRAR 密码注册表项，方便在不同电脑或重装系统后恢复密码。

## ✨ 功能特性

- 🔐 **导出密码**：将 WinRAR 保存的密码导出为注册表文件
- 📥 **导入密码**：从备份文件恢复 WinRAR 密码
- 🛡️ **自动权限管理**：自动检测并请求管理员权限
- 💻 **跨平台支持**：提供 Python 脚本和打包后的 Windows 可执行文件
- ⚠️ **安全提示**：详细说明密码加密机制和使用限制

## 📋 系统要求

- Windows 操作系统
- Python 3.6+（如果使用 Python 脚本）
- 管理员权限（用于访问注册表）

## 🚀 快速开始

### 方法一：使用可执行文件（推荐）

1. 从 [Releases](https://github.com/EricDasha/WinRAR-PassWord-import-and-export/releases) 下载 `WinRAR_Password_Manager.exe`
2. 双击运行（首次运行需要管理员权限）
3. 按照菜单提示操作

### 方法二：使用 Python 脚本

1. 确保已安装 Python 3.6+
2. 下载 `WinRAR_Password_Manager.py`
3. 运行脚本：
   ```bash
   python WinRAR_Password_Manager.py
   ```

## 📖 使用说明

### 导出密码

1. 运行程序，选择选项 `1`
2. 程序会自动导出 WinRAR 密码到 `WinRAR_Passwords.reg` 文件
3. 请妥善保管此文件（包含加密的密码数据）

### 导入密码

1. 确保 `WinRAR_Passwords.reg` 文件在同一目录
2. 运行程序，选择选项 `2`
3. 确认导入操作
4. 打开 WinRAR 测试密码是否可用

## ⚠️ 重要提示

### 密码加密机制

WinRAR 的密码是**加密存储**的，加密与 Windows 用户账户相关：

- ✅ **可以使用**：同一台电脑的同一用户账户
- ❌ **可能无法使用**：不同用户账户或不同电脑

### 使用场景

- ✅ 备份当前用户的 WinRAR 密码
- ✅ 重装系统后恢复密码（同一用户账户）
- ❌ 跨电脑迁移密码（加密密钥不同）

### 安全建议

- 备份文件包含加密的密码数据，请妥善保管
- 不要将备份文件分享给他人
- 导入后请测试密码是否可用

## 🔨 从源码构建

### 自动打包（推荐）

Windows 用户可以直接运行：
```bash
build.bat
```

### 手动打包

1. 安装 PyInstaller：
   ```bash
   pip install pyinstaller
   ```

2. 打包可执行文件：
   ```bash
   pyinstaller --onefile --console --name WinRAR_Password_Manager WinRAR_Password_Manager.py
   ```

3. 可执行文件位于 `dist\WinRAR_Password_Manager.exe`

详细说明请参考 [README_BUILD.md](README_BUILD.md)

## 📁 项目结构

```
.
├── WinRAR_Password_Manager.py    # Python 主程序
├── build_exe.py                  # 打包脚本
├── build.bat                     # Windows 一键打包脚本
├── README.md                     # 项目说明（本文件）
├── README_BUILD.md               # 打包说明
└── LICENSE                       # MIT 许可证
```

## 🛠️ 技术栈

- **Python 3.6+**
- **PyInstaller**（用于打包）
- **Windows Registry API**（通过 reg.exe）

## 📝 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## ⚡ 常见问题

### Q: 导入后密码无法使用？

A: 这通常是因为加密密钥不匹配。WinRAR 密码加密与用户账户相关，只有在同一用户账户下才能正常使用。

### Q: 打包后的 exe 被杀毒软件报毒？

A: 这是 PyInstaller 打包文件的常见误报。可以添加白名单或使用源码运行。

### Q: 支持其他压缩软件的密码吗？

A: 目前仅支持 WinRAR。其他软件（如 7-Zip、WinZip）的密码存储方式不同。

## 📞 联系方式

如有问题或建议，请提交 [Issue](https://github.com/EricDasha/WinRAR-PassWord-import-and-export/issues)。

---

⭐ 如果这个项目对你有帮助，请给个 Star！
