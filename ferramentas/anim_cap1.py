# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 1 (equações diferenciais)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from anim_base import *


def _br(v, nd=3):
    return f'{v:.{nd}f}'.replace('.', ',')


def campo(ax, f, xlim, ylim, n=17, cor=CINZA):
    """Desenha o campo de direções de y' = f(x, y) com segmentos de comprimento visual constante."""
    X, Y = np.meshgrid(np.linspace(*xlim, n), np.linspace(*ylim, n))
    S = f(X, Y)
    sx = (xlim[1] - xlim[0]); sy = (ylim[1] - ylim[0])
    U = np.ones_like(S) / sx; V = S / sy; N = np.hypot(U, V); U, V = U / N * sx, V / N * sy
    L = 0.032
    ax.quiver(X, Y, U, V, color=cor, angles='xy', scale_units='xy', scale=1 / L, headwidth=0, headlength=0,
              headaxislength=0, width=0.003, pivot='middle', alpha=0.7)


def _rk(f, x0, y0, x1, n=400):
    xs = np.linspace(x0, x1, n); ys = [y0]; h = xs[1] - xs[0]
    for x in xs[:-1]:
        y = ys[-1]; k1 = f(x, y); k2 = f(x + h / 2, y + h * k1 / 2); k3 = f(x + h / 2, y + h * k2 / 2); k4 = f(x + h, y + h * k3)
        ys.append(y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6)
    return xs, np.array(ys)


def a_campo(path):
    f = lambda x, y: y - x
    fig, ax = plt.subplots(figsize=(6.4, 4.6)); xl, yl = (-1, 5), (-3, 9)
    eixos(ax, xl, yl); campo(ax, f, xl, yl)
    xx = np.linspace(*xl, 300); ax.plot(xx, xx + 1, color=AZUL, lw=2.4, label='$y=x+1$')
    Cs = [-0.3, -0.1, -0.03, 0.03, 0.1, 0.3]; curvas = [ax.plot([], [], color=LARANJA, lw=1.6)[0] for _ in Cs]
    ax.legend(loc='upper left', fontsize=9); N = 50; xs = np.linspace(-1, 5, N)
    def up(i):
        x = xs[:i + 1]
        for c, l in zip(Cs, curvas):
            y = x + 1 + c * np.exp(x); l.set_data(x, np.where((y > yl[0] - 1) & (y < yl[1] + 1), y, np.nan))
        ax.set_title(f"$y'=y-x$:  soluções $y=x+1+Ce^x$   (x = {_br(xs[i], 2)})", fontsize=11)
    salvar(fig, up, N, path)


def a_euler(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); ns = [1, 2, 4, 8, 16, 32, 64]
    xx = np.linspace(0, 1.05, 200)
    def up(i):
        n = ns[i]; ax.cla(); eixos(ax, (-0.02, 1.08), (0.9, 2.85)); ax.plot(xx, np.exp(xx), color=AZUL, lw=2)
        x = np.linspace(0, 1, n + 1); y = (1 + 1 / n) ** np.arange(n + 1)
        ax.plot(x, y, 'o-', color=LARANJA, ms=3, lw=1.5)
        ax.set_title(f'n = {n}:  (1 + 1/n)^n = {_br(y[-1], 4)}   (e ≈ 2,7183)', fontsize=11)
    salvar(fig, up, len(ns), path, fps=2, pausa_final=4)


def a_circulos(path):
    f = lambda x, y: -x / np.where(np.abs(y) < 1e-3, 1e-3, y)
    fig, ax = plt.subplots(figsize=(5.6, 5.0)); xl, yl = (-3.3, 3.3), (-0.3, 3.5)
    eixos(ax, xl, yl); campo(ax, f, xl, yl, n=15); ax.set_aspect('equal')
    Rs = [1, 1.5, 2, 2.5, 3]; ls = [ax.plot([], [], color=LARANJA if r != 2 else AZUL, lw=2)[0] for r in Rs]
    th = np.linspace(np.pi, 0, 60)
    def up(i):
        for r, l in zip(Rs, ls):
            t = th[:i + 1]; l.set_data(r * np.cos(t), r * np.sin(t))
        ax.set_title("$y'=-x/y$:  semicircunferências $y=\\sqrt{K-x^2}$", fontsize=11)
    salvar(fig, up, len(th), path)


def a_resfriamento(path):
    k = np.log(0.8); tm = np.log(1.7) / k
    T = lambda t: 20 + 10 * np.exp(k * t)
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); ts = np.linspace(tm, 4, 60)
    def up(i):
        ax.cla(); eixos(ax, (tm - 0.3, 4.2), (15, 40)); ax.axhline(20, color=CINZA, ls='--', lw=1)
        t = ts[:i + 1]; ax.plot(t, T(t), color=AZUL, lw=2)
        ax.plot([tm], [37], 'o', color=LARANJA, ms=8); ax.annotate('morte: 37 °C', (tm, 37), (tm + 0.2, 38.2), fontsize=9)
        if ts[i] >= 0: ax.plot([0], [30], 'o', color=TINTA); ax.annotate('achado: 30 °C', (0, 30), (0.15, 32), fontsize=9)
        if ts[i] >= 1: ax.plot([1], [28], 'o', color=TINTA); ax.annotate('1 h depois: 28 °C', (1, 28), (1.15, 29.5), fontsize=9)
        ax.set_xlabel('t (h), com t = 0 no achado'); ax.set_title(f'T(t) = 20 + 10·0,8^t   morte em t ≈ {_br(tm, 2)} h', fontsize=11)
    salvar(fig, up, len(ts), path)


def a_logistica(path):
    r, K = 0.2311, 4000
    P = lambda t, p0: K * p0 * np.exp(r * t) / (K - p0 + p0 * np.exp(r * t))
    fig, ax = plt.subplots(figsize=(6.6, 4.4)); xl, yl = (0, 30), (0, 5600)
    p0s = [100, 300, 900, 2000, 5500]; ts = np.linspace(0, 30, 60); ti = np.log(3100 / 900) / r
    def up(i):
        ax.cla(); eixos(ax, xl, yl); campo(ax, lambda t, p: r * p * (1 - p / K), xl, yl, n=15)
        ax.axhline(K, color=CINZA, ls='--', lw=1); t = ts[:i + 1]
        for p0 in p0s: ax.plot(t, P(t, p0), color=AZUL if p0 == 900 else LARANJA, lw=2 if p0 == 900 else 1.4)
        if ts[i] >= ti: ax.plot([ti], [2000], 's', color=TINTA, ms=7); ax.annotate('inflexão (P = 2000)', (ti, 2000), (ti + 1, 1500), fontsize=9)
        ax.set_xlabel('t (anos)'); ax.set_title(f'Logística, r = 0,2311, K = 4000   (P₀ = 900 em branco)', fontsize=11)
    salvar(fig, up, len(ts), path)


def a_queda(path):
    v = lambda t: 49 * (1 - np.exp(-0.2 * t)); s = lambda t: 49 * t - 245 * (1 - np.exp(-0.2 * t))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 4.2), gridspec_kw={'width_ratios': [3, 1]}); ts = np.linspace(0, 25, 60)
    def up(i):
        a1.cla(); a2.cla(); t = ts[:i + 1]
        eixos(a1, (0, 26), (0, 55)); a1.axhline(49, color=CINZA, ls='--', lw=1); a1.plot(t, v(t), color=LARANJA, lw=2)
        a1.plot(t, 9.8 * t, color=CINZA, lw=1, ls=':'); a1.set_xlabel('t (s)'); a1.set_title(f'v = {_br(v(ts[i]), 1)} m/s  (terminal 49)', fontsize=10)
        a2.set_xlim(-1, 1); a2.set_ylim(-1000, 50); a2.set_xticks([]); a2.plot([0], [-s(ts[i])], 'v', color=AZUL, ms=12)
        a2.set_title(f'caiu {s(ts[i]):.0f} m', fontsize=10); a2.axhline(0, color=TINTA, lw=0.8)
    salvar(fig, up, len(ts), path)


def a_colheita(path):
    f = lambda t, p: 0.4 * p * (1 - p / 1000) - 60
    fig, ax = plt.subplots(figsize=(6.6, 4.4)); xl, yl = (0, 25), (0, 1100)
    p0s = [60, 120, 170, 200, 300, 600, 1000]; sols = [_rk(f, 0, p, 25, 300) for p in p0s]; N = 60
    def up(i):
        ax.cla(); eixos(ax, xl, yl); campo(ax, f, xl, yl, n=15)
        ax.axhline(816.2, color=AZUL, lw=1.5); ax.axhline(183.8, color=AZUL, lw=1.5, ls='--')
        k = int((i + 1) / N * 300)
        for (t, p) in sols:
            pp = np.where(p > 0, p, np.nan); ax.plot(t[:k], pp[:k], color=LARANJA, lw=1.5)
        ax.text(0.5, 840, 'estável ≈ 816', fontsize=9); ax.text(0.5, 205, 'limiar ≈ 184 (instável)', fontsize=9)
        ax.set_xlabel('t (anos)'); ax.set_title("P' = 0,4P(1 − P/1000) − 60", fontsize=11)
    salvar(fig, up, N, path)


def a_mistura(path):
    u = lambda t: (100 + t) / 2 - 5e5 / (100 + t) ** 2
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 4.2), gridspec_kw={'width_ratios': [1, 2]}); ts = np.linspace(0, 100, 50)
    def up(i):
        a1.cla(); a2.cla(); t = ts[i]; V = 100 + t; c = u(t) / V
        a1.set_xlim(0, 1); a1.set_ylim(0, 220); a1.set_xticks([]); a1.set_ylabel('volume (L)')
        a1.add_patch(Rectangle((0.15, 0), 0.7, V, fc=LARANJA, alpha=0.15 + 1.2 * c)); a1.add_patch(Rectangle((0.15, 0), 0.7, 210, fill=False, ec=TINTA))
        a1.set_title(f'V = {V:.0f} L', fontsize=10)
        tt = ts[:i + 1]; eixos(a2, (0, 105), (0, 0.55)); a2.axhline(0.5, color=CINZA, ls='--', lw=1)
        a2.plot(tt, u(tt) / (100 + tt), color=LARANJA, lw=2); a2.set_xlabel('t (min)')
        a2.set_title(f'concentração = {_br(c, 4)} kg/L   (sal {_br(u(t), 1)} kg)', fontsize=10)
    salvar(fig, up, len(ts), path)


def a_bernoulli(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); xl, yl = (-1, 3), (-0.5, 4)
    xs = np.linspace(-1, 3, 70)
    sol = [(2, lambda x: 1 / (1 + 2 * np.exp(x)), LARANJA), (0, lambda x: 1 + 0 * x, AZUL), (-0.5, lambda x: np.where(x < np.log(2), 1 / (1 - np.exp(x) / 2), np.nan), LARANJA)]
    def up(i):
        ax.cla(); eixos(ax, xl, yl); campo(ax, lambda x, y: y * y - y, xl, yl, n=15); ax.axvline(np.log(2), color=CINZA, ls='--', lw=1)
        x = xs[:i + 1]
        for c, g, cor in sol:
            y = g(x); y = np.where((y > yl[0] - 1) & (y < yl[1] + 1), y, np.nan); ax.plot(x, y, color=cor, lw=2)
        ax.set_title("$y'+y=y^2$:  $y=1/(1+Ce^x)$;  explosão em x = ln 2", fontsize=11)
    salvar(fig, up, len(xs), path)


def a_ortogonais(path):
    fig, ax = plt.subplots(figsize=(6.0, 5.0)); ax.set_aspect('equal'); xx = np.linspace(-3, 3, 300)
    Cs = [-2, -1, -0.5, -0.2, 0.2, 0.5, 1, 2]; Ks = [0.5, 1.5, 3, 5, 7.5]; N = len(Cs) + len(Ks)
    def up(i):
        ax.cla(); eixos(ax, (-3, 3), (-2.4, 2.4), grade=False); ax.set_aspect('equal')
        for c in Cs[:min(i + 1, len(Cs))]: ax.plot(xx, c * xx ** 2, color=AZUL, lw=1.4)
        th = np.linspace(0, 2 * np.pi, 200)
        for k in Ks[:max(0, i + 1 - len(Cs))]: ax.plot(np.sqrt(k) * np.cos(th), np.sqrt(k / 2) * np.sin(th), color=LARANJA, lw=1.8)
        ax.set_title('parábolas $y=Cx^2$ e elipses $x^2+2y^2=K$', fontsize=11)
    salvar(fig, up, N, path, fps=3, pausa_final=6)


def a_torricelli(path):
    h = lambda t: np.clip(2 - 0.05 * t, 0, None) ** 2
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 4.2), gridspec_kw={'width_ratios': [1, 2]}); ts = np.linspace(0, 45, 60)
    def up(i):
        a1.cla(); a2.cla(); t = ts[i]
        a1.set_xlim(0, 1); a1.set_ylim(0, 4.4); a1.set_xticks([]); a1.set_ylabel('h (m)')
        a1.add_patch(Rectangle((0.15, 0), 0.7, h(t), fc=LARANJA, alpha=0.6)); a1.add_patch(Rectangle((0.15, 0), 0.7, 4.2, fill=False, ec=TINTA))
        a1.set_title(f'h = {_br(h(t), 2)} m', fontsize=10)
        tt = ts[:i + 1]; eixos(a2, (0, 46), (0, 4.4)); a2.plot(tt, h(tt), color=AZUL, lw=2); a2.axhline(2, color=CINZA, ls=':', lw=1)
        a2.set_xlabel('t (min)'); a2.set_title('h = (2 − 0,05t)²: vazio em t = 40 min', fontsize=10)
    salvar(fig, up, len(ts), path)


ANIM = {'campo': a_campo, 'euler': a_euler, 'circulos': a_circulos, 'resfriamento': a_resfriamento,
        'logistica': a_logistica, 'queda': a_queda, 'colheita': a_colheita, 'mistura': a_mistura,
        'bernoulli': a_bernoulli, 'ortogonais': a_ortogonais, 'torricelli': a_torricelli}
