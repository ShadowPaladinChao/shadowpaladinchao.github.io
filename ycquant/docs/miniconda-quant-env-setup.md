# 使用 Miniconda 搭建 Python 量化环境

## 1. 安装 Miniconda

### Windows

从 [Miniconda 官网](https://docs.conda.io/en/latest/miniconda.html) 下载 Windows 安装包，双击安装即可。

### Linux / macOS

```bash
# 下载安装脚本（以 Linux x86_64 为例）
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 运行安装
bash Miniconda3-latest-Linux-x86_64.sh

# 重启终端或执行
source ~/.bashrc
```

安装完成后验证：

```bash
conda --version
```

---

## 2. 创建量化专用虚拟环境

```bash
# 创建名为 quant 的 Python 3.10 环境
conda create -n quant python=3.10 -y

# 激活环境
conda activate quant
```

---

## 3. 安装量化核心库

### 数据获取与处理

```bash
pip install numpy pandas
pip install akshare        # A股数据接口
pip install tushare        # 金融数据接口
pip install baostock       # 证券宝数据接口
```

### 技术指标与因子计算

```bash
pip install ta             # 技术分析指标库
pip install ta-lib         # TA-Lib 技术分析（需先安装 C 库，见附录）
```

### 回测框架

```bash
pip install backtrader     # 经典回测框架
pip install zipline-reloaded  # Zipline 回测框架
pip install vnpy           # VeighNa 量化交易框架
```

### 机器学习

```bash
pip install scikit-learn
pip install lightgbm
pip install xgboost
```

### 可视化与工具

```bash
pip install matplotlib
pip install plotly
pip install jupyterlab     # Jupyter Lab
```

---

## 4. 一键安装脚本

将以下内容保存为 `setup_quant_env.sh`（Linux/macOS）或在终端逐行执行：

```bash
# 创建环境
conda create -n quant python=3.10 -y
conda activate quant

# 安装所有依赖
pip install numpy pandas akshare tushare baostock ta backtrader scikit-learn lightgbm xgboost matplotlib plotly jupyterlab
```

---

## 5. 启动 Jupyter Lab

```bash
conda activate quant
jupyter lab
```

浏览器打开 `http://localhost:8888` 即可开始量化研究。

---

## 6. 环境管理常用命令

| 命令 | 说明 |
|------|------|
| `conda info --envs` | 查看所有环境 |
| `conda activate quant` | 激活环境 |
| `conda deactivate` | 退出当前环境 |
| `conda remove -n quant --all` | 删除环境 |
| `conda list` | 查看已安装的包 |
| `pip freeze > requirements.txt` | 导出依赖列表 |
| `pip install -r requirements.txt` | 从文件安装依赖 |

---

## 附录：安装 TA-Lib

TA-Lib 需要先安装 C 语言库：

**Windows**：从 [这里](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib) 下载对应的 `.whl` 文件，然后：

```bash
pip install TA_Lib‑0.4.xx‑cp310‑cp310‑win_amd64.whl
```

**Linux**：

```bash
wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
pip install ta-lib
```

**macOS**：

```bash
brew install ta-lib
pip install ta-lib
```
