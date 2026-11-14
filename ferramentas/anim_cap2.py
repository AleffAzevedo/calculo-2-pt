# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 2 (sequências e séries)."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from anim_base import *


def _br(v, nd=4):
    return f'{v:.{nd}f}'.replace('.', ',')


def _somas(path, termos, alvo, titulo, ylim, nmax=None, alvo_txt=None, cor=LARANJA, fps=6):
    S = np.cumsum(termos); N = len(S); ks = np.arange(1, N + 1)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    def up(i):
        ax.cla(); eixos(ax, (0, N + 1), ylim); ax.axhline(alvo, color=CINZA, ls='--', lw=1)
        ax.plot(ks[:i + 1], S[:i + 1], '-', color=cor, lw=1); ax.plot(ks[:i + 1], S[:i + 1], 'o', color=AZUL, ms=3.5)
        ax.set_xlabel('k'); ax.set_title(f'{titulo}   S_{i + 1} = {_br(S[i])}   (soma {alvo_txt or _br(alvo)})', fontsize=10)
    salvar(fig, up, N, path, fps=fps, pausa_final=12)


def a_recorrencia(path):
    fig, ax = plt.subplots(figsize=(5.6, 5.0)); xx = np.linspace(0, 2.6, 300)
    a = [np.sqrt(2)]
    for _ in range(7): a.append(np.sqrt(2 + a[-1]))
    pts = [(a[0], 0)]
    for k in range(len(a) - 1): pts += [(a[k], a[k + 1]), (a[k + 1], a[k + 1])]
    def up(i):
        ax.cla(); eixos(ax, (0, 2.6), (0, 2.6)); ax.set_aspect('equal')
        ax.plot(xx, np.sqrt(2 + xx), color=AZUL, lw=2, label=r'$y=\sqrt{2+x}$'); ax.plot(xx, xx, color=CINZA, lw=1, label='$y=x$')
        P = np.array(pts[:i + 1]); ax.plot(P[:, 0], P[:, 1], color=LARANJA, lw=1.4); ax.plot([2], [2], 'o', color=TINTA)
        k = min(i // 2, len(a) - 1); ax.legend(loc='upper left', fontsize=9)
        ax.set_title(f'a_{k + 1} = {_br(a[k], 5)}  →  2', fontsize=11)
    salvar(fig, up, len(pts), path, fps=3, pausa_final=6)


def a_geometrica(path):
    g = 9.8; h0 = 10; r = 0.75; nq = 40
    seg = []; t = 0
    for k in range(nq):
        h = h0 * r ** k; tq = np.sqrt(2 * h / g)
        if k == 0: seg.append((t, tq, h, 'desce')); t += tq
        else: seg.append((t, 2 * tq, h, 'quica')); t += 2 * tq
    T = t; ts = np.linspace(0, T, 140)
    def altura(tt):
        for (t0, d, h, tipo) in seg:
            if t0 <= tt <= t0 + d:
                if tipo == 'desce': return h - 0.5 * g * (tt - t0) ** 2
                v = np.sqrt(2 * g * h); s = tt - t0; return v * s - 0.5 * g * s * s
        return 0
    tf = np.linspace(0, T, 20000); hf = np.array([altura(x) for x in tf])
    Df = np.concatenate([[0], np.cumsum(np.abs(np.diff(hf)))]); dist = lambda tt: np.interp(tt, tf, Df)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 4.0), gridspec_kw={'width_ratios': [1, 2]})
    def up(i):
        tt = ts[i]; a1.cla(); a2.cla()
        a1.set_xlim(-1, 1); a1.set_ylim(-0.3, 10.8); a1.set_xticks([]); a1.axhline(0, color=TINTA)
        a1.plot([0], [altura(tt)], 'o', color=LARANJA, ms=14); a1.set_title(f't = {_br(tt, 1)} s', fontsize=10)
        eixos(a2, (0, T + 1), (0, 75)); a2.axhline(70, color=CINZA, ls='--', lw=1)
        d = [dist(x) for x in ts[:i + 1]]; a2.plot(ts[:i + 1], d, color=LARANJA, lw=2)
        a2.set_xlabel('t (s)'); a2.set_title(f'distância percorrida = {_br(d[-1], 1)} m  (total 70 m)', fontsize=10)
    salvar(fig, up, len(ts), path, fps=12)


def a_harmonica(path):
    ns = np.unique(np.round(np.logspace(0, 4.2, 90)).astype(int)); H = np.cumsum(1 / np.arange(1, ns[-1] + 1))
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); xx = np.logspace(0, 4.2, 200)
    def up(i):
        ax.cla(); ax.set_xscale('log'); ax.set_xlim(1, 2e4); ax.set_ylim(0, 11); ax.grid(alpha=0.12)
        ax.plot(xx, np.log(xx + 1), color=CINZA, ls='--', lw=1, label='ln(n+1)'); ax.plot(xx, 1 + np.log(xx), color=CINZA, ls=':', lw=1, label='1 + ln n')
        n = ns[:i + 1]; ax.plot(n, H[n - 1], 'o-', color=LARANJA, ms=3, lw=1.2, label='$H_n$'); ax.legend(loc='upper left', fontsize=9)
        ax.set_xlabel('n (escala log)'); ax.set_title(f'n = {ns[i]}:  H_n = {_br(H[ns[i] - 1], 3)}   (passa de 10 em n = 12 367)', fontsize=10)
    salvar(fig, up, len(ns), path, fps=10)


def a_telescopica(path):
    _somas(path, [1 / (n * (n + 2)) for n in range(1, 31)], 0.75, r'$\sum 1/(n(n+2))$', (0, 0.85), alvo_txt='3/4')


def a_resto_integral(path):
    Ns = list(range(1, 41)); S = np.cumsum([1 / n ** 2 for n in range(1, 41)]); v = np.pi ** 2 / 6
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    def up(i):
        ax.cla(); eixos(ax, (0, 41), (0.95, 1.75)); ax.axhline(v, color=CINZA, ls='--', lw=1)
        n = np.array(Ns[:i + 1]); s = S[:i + 1]
        ax.fill_between(n, s + 1 / (n + 1), s + 1 / n, color=LARANJA, alpha=0.5, lw=0)
        ax.plot(n, s, 'o', color=AZUL, ms=3)
        ax.set_xlabel('N'); ax.set_title(f'N = {Ns[i]}: S_N = {_br(s[-1])};  soma em [{_br(s[-1] + 1 / (Ns[i] + 1))}; {_br(s[-1] + 1 / Ns[i])}]', fontsize=10)
    salvar(fig, up, len(Ns), path, fps=6)


def a_alternada_erro(path):
    from math import factorial
    _somas(path, [(-1) ** (n + 1) / factorial(n) for n in range(1, 11)], 1 - np.exp(-1), r'$\sum(-1)^{n+1}/n!$', (0.45, 1.05), alvo_txt='1 − 1/e ≈ 0,6321', fps=2)


def _koch(p, q, n):
    if n == 0: return [p]
    p, q = np.array(p), np.array(q); d = (q - p) / 3; a = p + d; b = p + 2 * d
    c = a + np.array([[0.5, -np.sqrt(3) / 2], [np.sqrt(3) / 2, 0.5]]) @ d
    return _koch(p, a, n - 1) + _koch(a, c, n - 1) + _koch(c, b, n - 1) + _koch(b, q, n - 1)


def a_koch(path):
    V = [np.array([0, 0]), np.array([0.5, np.sqrt(3) / 2]), np.array([1, 0])]
    fig, ax = plt.subplots(figsize=(5.6, 5.4)); N = 6
    def up(n):
        ax.cla(); ax.set_aspect('equal'); ax.axis('off'); ax.set_xlim(-0.25, 1.25); ax.set_ylim(-0.45, 1.05)
        pts = []
        for k in range(3): pts += _koch(V[k], V[(k + 1) % 3], n)
        P = np.array(pts + [pts[0]]); ax.add_patch(Polygon(P, fc=LARANJA, alpha=0.55, ec=AZUL, lw=0.8))
        per = 3 * (4 / 3) ** n; area = 1 + sum(3 * 4 ** (k - 1) / 9 ** k for k in range(1, n + 1))
        ax.set_title(f'etapa {n}:  perímetro = {_br(per, 2)}·ℓ   área = {_br(area, 4)}·A₀  (→ 1,6)', fontsize=10)
    salvar(fig, up, N, path, fps=1, pausa_final=3)


def a_rearranjo(path):
    K = 60; a = np.cumsum([(-1) ** (n + 1) / n for n in range(1, K + 1)])
    termos = []; o, e = 1, 2
    while len(termos) < K: termos += [1 / o, 1 / (o + 2), -1 / e]; o += 4; e += 2
    b = np.cumsum(termos[:K]); ks = np.arange(1, K + 1)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    def up(i):
        ax.cla(); eixos(ax, (0, K + 1), (0.3, 1.45))
        ax.axhline(np.log(2), color=AZUL, ls='--', lw=1); ax.axhline(1.5 * np.log(2), color=LARANJA, ls='--', lw=1)
        ax.plot(ks[:i + 1], a[:i + 1], 'o-', color=AZUL, ms=2.5, lw=0.8, label='1 − 1/2 + 1/3 − …  → ln 2')
        ax.plot(ks[:i + 1], b[:i + 1], 'o-', color=LARANJA, ms=2.5, lw=0.8, label='1 + 1/3 − 1/2 + …  → (3/2) ln 2')
        ax.legend(loc='lower right', fontsize=9); ax.set_xlabel('termos somados'); ax.set_title('Os mesmos termos, outra ordem, outra soma', fontsize=11)
    salvar(fig, up, K, path, fps=8)


def a_empilhamento(path):
    N = 12; fig, ax = plt.subplots(figsize=(6.6, 4.6))
    def up(n):
        ax.cla(); ax.set_aspect('equal'); ax.axis('off'); n = n + 1
        ax.set_xlim(-2.2, 3.2); ax.set_ylim(-0.6, N * 0.32 + 0.5)
        ax.add_patch(Rectangle((-2.2, -0.6), 2.2, 0.6, fc='#4A4A4A', ec=TINTA))  # mesa: borda em x = 0
        # posições: bloco k (k=1 topo) com borda direita em sum_{j=k}^{n} 1/(2j)
        right = [sum(1 / (2 * j) for j in range(k, n + 1)) for k in range(1, n + 1)]
        for k in range(n, 0, -1):
            y = (n - k) * 0.32
            ax.add_patch(Rectangle((right[k - 1] - 1, y), 1, 0.3, fc=LARANJA if k == 1 else AZUL, alpha=0.9 if k == 1 else 0.35, ec=TINTA, lw=0.6))
        ax.plot([0, 0], [-0.6, n * 0.32 + 0.3], color=CINZA, ls=':', lw=1)
        ax.set_title(f'{n} blocos: balanço = H_n/2 = {_br(right[0], 3)}', fontsize=11)
    salvar(fig, up, N, path, fps=2, pausa_final=6)


def a_cantor(path):
    fig, ax = plt.subplots(figsize=(6.6, 4.2)); N = 7
    def up(n):
        ax.cla(); ax.axis('off'); ax.set_xlim(-0.02, 1.02); ax.set_ylim(-N - 0.5, 1.2)
        ints = [(0.0, 1.0)]
        for k in range(n + 1):
            for (a, b) in ints: ax.add_patch(Rectangle((a, -k), b - a, 0.45, fc=AZUL if k < n else LARANJA, ec='none', alpha=0.85))
            ints = [x for (a, b) in ints for x in ((a, a + (b - a) / 3), (b - (b - a) / 3, b))]
        ret = 1 - (2 / 3) ** n
        ax.set_title(f'etapa {n}: retirado = {_br(ret, 4)}   (→ 1)', fontsize=11)
    salvar(fig, up, N, path, fps=1, pausa_final=3)


def a_potencias(path):
    K = 30; n = np.arange(1, K + 1); S1 = np.cumsum(n / 2.0 ** n); S2 = np.cumsum(n ** 2 / 2.0 ** n)
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    def up(i):
        ax.cla(); eixos(ax, (0, K + 1), (0, 6.6)); ax.axhline(2, color=AZUL, ls='--', lw=1); ax.axhline(6, color=LARANJA, ls='--', lw=1)
        ax.plot(n[:i + 1], S1[:i + 1], 'o-', color=AZUL, ms=3, lw=1, label=r'$\sum n/2^n\to2$')
        ax.plot(n[:i + 1], S2[:i + 1], 'o-', color=LARANJA, ms=3, lw=1, label=r'$\sum n^2/2^n\to6$')
        ax.legend(loc='lower right', fontsize=9); ax.set_xlabel('k')
        ax.set_title(f'k = {i + 1}:  {_br(S1[i])}  e  {_br(S2[i])}', fontsize=11)
    salvar(fig, up, K, path, fps=6)


ANIM = {'recorrencia': a_recorrencia, 'geometrica': a_geometrica, 'harmonica': a_harmonica, 'telescopica': a_telescopica,
        'resto_integral': a_resto_integral, 'alternada_erro': a_alternada_erro, 'koch': a_koch, 'rearranjo': a_rearranjo,
        'empilhamento': a_empilhamento, 'cantor': a_cantor, 'potencias': a_potencias}
