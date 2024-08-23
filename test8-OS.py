import os

# os.mkdir("D://ww")
# os.rmdir("D://ww")

# ====================================================
'''
'r' 表示只读模式。如果你想要写入文件，可以使用 'w' 模式，如果想要追加内容，可以使用 'a' 模式等。
with open(...) as file : 是使用上下文管理器的方式，确保文件在使用后被正确关闭，即使在处理文件时发生异常也能保证关闭。
'''
# 打开文件（默认为只读模式）
file_path = 'D:/快捷键.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    # 执行文件操作，例如读取文件内容
    file_content = file.read()
    print(file_content)
# 文件在with块结束后会自动关闭，无需显式关闭文件

# -------------

# 关闭文件    文件在with块结束后会自动关闭，无需显式关闭文件
# 另一种方式   可以显式调用文件对象的 close() 方法来关闭文件。相对来说不如 with 语句简洁和安全。
file_path = 'D:/快捷键.txt'
file = open(file_path, 'r', encoding='utf-8')
try:
    # 执行文件操作，例如读取文件内容
    file_content = file.read()
    print(file_content)
finally:
    file.close()


# ====================================================
# 文件读写
# 使用内置的 open 函数来打开文件并写入内容。确保使用适当的模式（例如，'w' 表示写入）。
file_path = 'D:/ww.txt'
# 写入文件
with open(file_path, 'w') as file:
    file.write("Hello, this is some data.")

# -----------------
# 使用 csv 模块来写入CSV格式的文件。
import csv

csv_file_path = 'D:/ww.csv'   # 没有该文件会自动创建
data = [['Name', 'Age', 'Occupation'],
        ['John Doe', 30, 'Engineer'],
        ['Jane Smith', 25, 'Designer']]

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)
# ---------------------------
# 使用内置的 json 模块来写入JSON格式的文件。
import json

json_file_path = 'D:/ww.json'
data = {"name": "John Doe", "age": 30, "occupation": "Engineer"}
with open(json_file_path, 'w') as jsonfile:
    json.dump(data, jsonfile)


# ============================================读取文件==============================
file_path = 'D:/ww.txt'
# 读取文件
with open(file_path, 'r') as file:
    data = file.read()
    print(data)

# -------------------
# 使用 csv 模块来读取CSV格式的文件。

csv_file_path = 'D:/example.csv'

# 读取CSV文件
with open(csv_file_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)

# --------------------
# 使用内置的 json 模块来读取JSON格式的文件。
import json

json_file_path = 'example.json'
# 读取JSON文件
with open(json_file_path, 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data)


# =============================读数据
# readlines 是 Python 中用于读取文件的方法之一，它用于逐行读取文件内容，并将每一行作为字符串存储在一个列表中
with open('file.txt', 'r') as file:
    lines = file.readlines()

'''
'r'表示只读模式。
with 语句可以确保在读取完成后自动关闭文件，不需要显式调用 file.close()。
readlines方法用于读取文件的所有行，并将每一行作为一个字符串存储在列表lines中。
每个列表元素对应文件中的一行文本。你可以使用列表索引来访问特定行，例如lines[0]表示文件的第一行。
'''
# readlines 方法适用于处理包含多行文本的文件，但对于大型文件，可能需要考虑逐行读取而不是将整个文件加载到内存中。这可以通过循环遍历文件对象来实现，而不是使用 readlines。

# ----------------------------
# readline 是 Python 中用于读取文件的方法之一，它用于逐行读取文件内容，并返回文件中的一行作为字符串。以下是对 readline 方法的详细解释：使用 readline 方法的基本语法
with open('file.txt', 'r') as file:
    line1 = file.readline()
    line2 = file.readline()
    line3 = file.readline()

print(line1)  # 输出：Hello, this is line 1.
print(line2)  # 输出：This is line 2.
print(line3)  # 输出：And this is line 3.
# readline 方法用于读取文件的一行，并将该行作为一个字符串存储在变量 line 中。

# 每个 readline 调用都会读取文件的下一行。
# 返回的字符串包含行末尾的换行符 \n。如果不需要换行符，可以使用 strip() 方法去除它。
# 当文件读取完毕后，readline 将返回空字符串 ‘’，因此可以在循环中使用 while line != '' 来逐行读取整个文件。
with open('file.txt', 'r') as file:
    line = file.readline()
    while line != '':        # 这个循环将逐行读取整个文件，直到文件末尾。
        print(line.strip())  # 去除换行符
        line = file.readline()
'''
readlines 一次性读取整个文件的所有行，并返回一个包含所有行的列表。
readline 逐行读取文件，每次调用返回文件中的一行，适用于处理大型文件，减少内存占用。
readlines 返回包含换行符的每一行，而readline 返回单独的行，需要手动去除换行符。
选择使用哪个方法取决于文件的大小和处理需求。如果文件较小，可以完全装入内存，使用readlines；如果文件较大，可以逐行处理，使用readline。
'''


# =================================================================================
# 文件的相关操作
# Python 文件重命名
# 在重命名文件时，可能会出现各种异常，例如目标文件已存在、没有足够权限等。为了确保程序的健壮性，应该添加异常处理

import os
# 指定要重命名文件的目录
directory = 'path_to_directory'
# 列出目录中的所有文件
files = os.listdir(directory)
# 遍历文件列表并进行重命名
for file in files:
    # 判断是否是文件
    if os.path.isfile(os.path.join(directory, file)):
        # 设定新的文件名
        new_filename = 'new_name'

        # 重命名文件
        try:
            os.rename(
                os.path.join(directory, file),
                os.path.join(directory, new_filename)
            )
            print(f'重命名 {file} 为 {new_filename}')
        except OSError as e:
            print(f'Error renaming {file}: {e}')

# ==================================================================
# 获取当前目录     os.getcwd() 函数来获取当前目录的路径
import os
current_directory = os.getcwd()
print(f'Current directory is: {current_directory}')



# =======================================例题=====================
'''
1. 目录.txt自动清洗
1.1 需要在二级标题所在行最前面空4个格子，一级标题不用
1.2 需要在章和节字的后面加上一个空格
1.3 需要在页码前面加上=>符号
'''
# 获取桌面路径
import os
import re

desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 目标文件路径
file_path = os.path.join(desktop_path, "目录.txt")

# 打开文件并读取内容
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

modified_lines = []
for line in lines:
    # 去除空格
    line = line.replace(" ", "")
    if len(line) == 1:
        continue
    # 使用正则表达式在'章'或'节'后面添加一个空格，仅在后面没有空格的情况下
    line = re.sub(r'(章|节)(?![ ])', r'\1 ', line)
    # 在小数点后添加空格
    line = re.sub(r'(\.\d)', r'\1 ', line)
    if '章' not in line:
        # 二级标题添加4个空格
        line = ' ' * 4 + line
    # 匹配并去除最外层的英文括号
    pattern_en = r'\(([\d\s]+)\)'
    line = re.sub(pattern_en, r'\1', line)
    # 匹配并去除最外层的中文括号及其内部内容（包括除数字和空格以外的字符）
    pattern = r'（([^）]+)）'
    line = re.sub(pattern, r'\1', line)
    # 确保每行只有一个 =>
    if '=>' not in line:
        # 在页码数字前添加 =>（只在行尾）
        line = re.sub(r'(\d+)$', r'=>\1', line)
    # 去除中文汉字和'=>整体符号左边的冗余符号
    pattern = r'([\u4e00-\u9fff]+)[^\w\s]+=>'
    line = re.sub(pattern, r'\1=>', line)
    modified_lines.append(line)
# 将修改后的内容写回文件
with open(file_path, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# ===================================
# 批量修改文件夹下的文件命名   你可以使用 Python 的 os 模块来实现对文件名的批量修改，结合字符串操作来确保文件名中的规定格式。
'''
1.使用 os.listdir 获取目录下的所有文件名，然后遍历这些文件名。
2.通过 os.path.join 构建完整的文件路径，确保路径的正确性。
3.检查文件是否是图片文件（以 .png, .jpg, .jpeg, .gif 结尾的文件），并且文件名中包含下划线。
4.使用 split('_') 分割文件名，确保分割后的第一部分为'00159231127'。
5.构建新文件名，并使用 os.rename 来重命名文件。
'''
import os

# 指定目录路径
directory_path = r'目标文件夹绝对路径'

# 获取目录下所有文件名
files = os.listdir(directory_path)

# 遍历文件
for file_name in files:
    # 构建完整的文件路径
    file_path = os.path.join(directory_path, file_name)

    # 检查文件是否是图片文件，并且文件名中包含下划线
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')) and '_' in file_name:
        # 分割文件名，以下划线为界
        parts = file_name.split('_')

        # 确保分割后的第一部分为'00159231127'
        if parts[0] != '00159231127':
            # 构建新文件名
            new_file_name = '00159231127' + '_' + '_'.join(parts[1:])

            # 构建新文件路径
            new_file_path = os.path.join(directory_path, new_file_name)

            # 重命名文件
            os.rename(file_path, new_file_path)
            print(f'Renamed: {file_name} -&gt; {new_file_name}')














