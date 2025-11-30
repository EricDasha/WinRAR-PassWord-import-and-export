# 打包说明

## 方法一：使用自动打包脚本（推荐）

### Windows 用户
直接双击运行 `build.bat` 文件，脚本会自动：
1. 检查 Python 环境
2. 安装 PyInstaller（如果未安装）
3. 打包成可执行文件

### 手动打包
```bash
# 1. 安装 PyInstaller
pip install pyinstaller

# 2. 打包
python build_exe.py
```

## 方法二：手动使用 PyInstaller

```bash
# 安装 PyInstaller
pip install pyinstaller

# 打包成单个可执行文件
pyinstaller --onefile --console --name WinRAR_Password_Manager WinRAR_Password_Manager.py
```

## 打包选项说明

- `--onefile`: 打包成单个 .exe 文件（推荐）
- `--console`: 显示控制台窗口
- `--name`: 指定生成的可执行文件名称
- `--clean`: 清理临时文件
- `--noconfirm`: 自动覆盖已存在的文件

## 打包后的文件位置

打包完成后，可执行文件位于：
```
dist\WinRAR_Password_Manager.exe
```

## 使用打包后的文件

1. 将 `WinRAR_Password_Manager.exe` 复制到任何 Windows 电脑
2. 双击运行即可（首次运行可能需要管理员权限）
3. **不需要安装 Python 环境**

## 注意事项

- 打包后的文件可能被杀毒软件误报，这是正常现象（PyInstaller 打包的文件经常被误报）
- 如果遇到问题，可以添加 `--add-binary` 参数指定额外的二进制文件
- 文件大小约为 5-10 MB（包含 Python 运行时）

## 高级选项

如果需要更小的文件体积，可以使用 UPX 压缩：

```bash
pip install pyinstaller[encryption]
pyinstaller --onefile --console --upx-dir=path/to/upx WinRAR_Password_Manager.py
```

