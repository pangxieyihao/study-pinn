# Week01：数值微分与数值积分的误差实验

Python 科学计算与数值误差入门实验：用差分公式近似导数、用复合求积公式计算积分，
观察截断误差、舍入误差与收敛阶。

## 文件清单

| 文件 | 说明 |
|------|------|
| `week01_diff.py` | 实验 1：前向/中心差分求 f′(π/4)，h = 10⁻¹ … 10⁻⁸ |
| `week01_integral.py` | 实验 2：复合梯形 / Simpson 计算 ∫₀^π sin x dx，N = 4 … 64 |
| `week01_plot.py` | 读取两个 CSV，绘制 log–log 误差图 `error_plot.png` |
| `week01_report.pdf` | 实验报告：截断误差推导 + 误差先降后升的解释 + 结果图表 |
| `error_plot.png` | 双子图 log–log 误差图（左：差分；右：积分） |
| `diff.csv` / `intergal_result.csv` | 运行后自动生成的原始数据 |

## 环境要求

- 实验 1、2：Python 3.6+，仅标准库（`math` / `csv` / `os`）
- 画图脚本：需额外安装 `matplotlib`（`pip install matplotlib`）

## 运行方式

```bash
# 1. 实验 1：差分求导（输出每个 h 的近似值与误差，生成 diff.csv）
python week01_diff.py

# 2. 实验 2：数值积分（输出每个 N 的近似值与误差，生成 intergal_result.csv）
python week01_integral.py

# 3. 绘制 log–log 误差图（需先运行前两步生成 CSV，输出 error_plot.png）
python week01_plot.py
```

三个脚本按顺序运行；CSV 与图片均保存在脚本所在目录。

## 结果摘要

- 前向差分：截断误差 O(h)，实测收敛阶 ≈ 1.002
- 中心差分：截断误差 O(h²)，实测收敛阶 ≈ 2.000；h ≈ 10⁻⁵ 时误差最小（1.4×10⁻¹¹），
  之后因舍入误差回升（V 形曲线），与理论最优步长 ε^(1/3) 一致
- 复合梯形：误差 O(h²)，实测 ≈ 2.003
- 复合 Simpson：误差 O(h⁴)，实测 ≈ 4.024；N = 64 时误差 6.5×10⁻⁸

详细推导与讨论见 `week01_report.pdf`。
