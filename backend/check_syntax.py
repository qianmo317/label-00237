#!/usr/bin/env python3
"""
语法检查脚本 - 只检查语法，不导入 heavy dependencies
"""
import ast
import sys

def check_syntax(filepath):
    """检查 Python 文件语法"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source = f.read()
        ast.parse(source)
        print(f"✓ {filepath} 语法正确")
        return True
    except SyntaxError as e:
        print(f"✗ {filepath} 语法错误: {e}")
        return False

files_to_check = [
    'src/api/routes.py',
    'src/api/schemas.py'
]

print("=" * 50)
print("语法检查")
print("=" * 50)

all_passed = True
for f in files_to_check:
    if not check_syntax(f):
        all_passed = False

print("=" * 50)
if all_passed:
    print("所有文件语法检查通过 ✓")
    sys.exit(0)
else:
    print("存在语法错误 ✗")
    sys.exit(1)
