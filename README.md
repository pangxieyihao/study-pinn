# study-pinn

研究生学习计划实验仓库：**传统数值计算 · PDE 求解 · 优化算法 → 物理信息神经网络（PINNs）**

• 能够从PDE强形式推导离散格式或弱形式，并解释离散变量、边界条件和数值通量的含义。
• 能够独立实现常见算法的核心部分，而不只是调用现成软件包；允许用SciPy做结果交叉验证。
• 能够用解析解、制造解（MMS）或高精度参考解验证程序，并报告误差、收敛阶、稳定性和计
算成本。
• 能够实现GD、SGD、Momentum、Adam、Newton、BFGS/L-BFGS、Gauss–Newton和Levenberg
Marquardt 的基本版本。
• 能够完成一个PINN基线程序，并与传统数值方法进行公平比较。
每周统一提交规范
• 代码：一个可独立运行的目录，包含README、环境依赖、运行命令、参数说明和随机种子。
• 报告：建议3–6 页，至少包含问题定义、方法推导、参数设置、结果图、误差表、失败案例和
结论。
• 结果：保存原始数据（CSV/NPZ）、图片（PNG/PDF）和运行日志；图中必须标注坐标、单
位、网格/步长及误差定义。
• 验收：导师随机指定一个参数或网格，让学生现场运行并解释结果；不能只展示预先生成的图
片。
• 原创实现：每个主题至少有一个核心算法由学生自己编写；可另外用 SciPy/PyTorch 对照验
证。
建议统一代码仓库结构
graduate-numerics/
week01_error/
src/ results/ report.pdf README.md
week02_linear/
week16_pinn_compare/
environment.yml
requirements.txt
报告中的误差指标建议统一：离散相对L2 误差E2=∥unum−uref∥2/∥uref∥2；最大误差 E∞ =
maxi |unum −uref|；实验收敛阶 p = log(Eh/Eh/2)/log2



