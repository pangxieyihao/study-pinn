import os
import csv
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))


def read_diff():
    hs, fwd, ctr = [], [], []
    with open(os.path.join(base_dir, "diff.csv")) as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            hs.append(float(row[0]))
            fwd.append(float(row[2]))
            ctr.append(float(row[4]))
    return hs, fwd, ctr


def read_integral():
    ns, trap, simp = [], [], []
    with open(os.path.join(base_dir, "intergal_result.csv")) as fp:
        reader = csv.reader(fp)
        next(reader)
        for row in reader:
            ns.append(int(row[0]))
            trap.append(float(row[2]))
            simp.append(float(row[4]))
    return ns, trap, simp


def main():
    hs, fwd, ctr = read_diff()
    ns, trap, simp = read_integral()
    hs_int = [math.pi / n for n in ns]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.loglog(hs, fwd, "o-", label="forward difference")
    ax1.loglog(hs, ctr, "s-", label="central difference")
    ax1.set_xlabel("h")
    ax1.set_ylabel("absolute error")
    ax1.set_title("Differentiation error\nf(x) = sin(x),  x0 = pi/4")
    ax1.grid(True, which="both", linestyle="--", alpha=0.4)
    ax1.legend(loc="best")
    ax1.text(0.05, 0.92, "forward: O(h)", transform=ax1.transAxes)
    ax1.text(0.05, 0.82, "central: O(h^2)", transform=ax1.transAxes)

    ax2.loglog(hs_int, trap, "o-", label="composite trapezoid")
    ax2.loglog(hs_int, simp, "s-", label="composite Simpson")
    ax2.set_xlabel("h = (b - a) / N")
    ax2.set_ylabel("absolute error")
    ax2.set_title("Integration error\nint_0^pi sin(x) dx = 2")
    ax2.grid(True, which="both", linestyle="--", alpha=0.4)
    ax2.legend(loc="best")
    ax2.text(0.05, 0.92, "trapezoid: O(h^2)", transform=ax2.transAxes)
    ax2.text(0.05, 0.82, "Simpson: O(h^4)", transform=ax2.transAxes)

    fig.tight_layout()
    out_path = os.path.join(base_dir, "error_plot.png")
    fig.savefig(out_path, dpi=150)
    print("图已保存：", out_path)


if __name__ == "__main__":
    main()