# Python文件和目录操作

## 1 文件路径 Python中书写文件路径

### 1.1不同系统中的 文件路径示例

```python
"""Windows上的反斜杠以及OS X和Linux上的正斜杠"""

# windows 
"""D:\desktop\test1.txt"""

# linux & mac
"""/desktop/test2.txt"""
```

注意：虽然文件夹名称和文件名在 Windows 和 OS X 上是不区分大小写的，但在 Linux 上是区分大小写的

### 1.2 使用os模块下的join()函数来书写文件路径

```python
import os
newPath = os.path.join('demo', 'exercise')
print(newPath)
```

### 1.3  实现路径和文件名之间的拼接工作

```python
# 1. 将文件名列表中的名称添加到文件夹路径的后面

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    # 实现路径和文件的路径拼接
    print(os.path.join('C:\\demo\\exercise', filename))
```

## 2 当前工作目录

说明：当前所处的文件目录的路径

### 2.1 获取当前工作的目录路径- getcwd()

```python
# 1. 获取当前的工作目录
workDir = os.getcwd()
print(workDir)  # C:\Users\Ammonia\Desktop\My CS Study\Pythonlibrary\005 文件及目录操作
```

### 2.2 跳转到指定的目录 并输出当前路径 - os.chdir()

```python
os.chdir('D:\\chrome_download')
workDir = os.getcwd()
print(workDir)              # D:\chrome_download
```

### 2.3 跳转的目录不存在时 抛出FileNotFoundError

```python
# 3.当要跳转的目录并不存在的时候 会抛出FileNotFoundError
os.chdir('error')
```

## 3 ==相对路径和绝对路径==

### 3.1 相对路径和绝对路径

绝对路径：总是从根文件夹开始，Window 系统中以盘符（C：、D：）作为根文件夹，而 OS X 或者 Linux 系统中以 / 作为根文件夹。

相对路径：指的是文件相对于当前工作目录所在的位置。例如，当前工作目录为 "C:\Windows\System32"，若文件 demo.txt 就位于这个 System32 文件夹下，则 demo.txt 的相对路径表示为 ".\demo.txt"（其中 .\ 就表示当前所在目录）。

#### 3.1.1 当前所在目录和当前所在目录的父目录表示方法

```python
# 当前目录
""".\"""
# 当前目录的上一层目录-父目录的
"""..\"""
```



### 3.2 Python处理绝对路径和相对路径