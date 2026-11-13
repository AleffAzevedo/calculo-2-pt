# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 1."""

SOLUCOES = [
dict(id='campo', origem='inspirado na Figura 1.1', titulo='Um campo que espalha as soluções',
enunciado=r"""Para $y'=y-x$, esboce o campo de direções, encontre a solução geral e mostre que só uma
solução não se afasta da reta $y=x+1$. Compare $y(0)=1$ e $y(0)=1{,}1$ em $x=5$.""",
resposta=r"""$y=x+1+Ce^x$; só $C=0$; $y(5)=6$ contra $y(5)\approx20{,}8$.""",
solucao=r"""**Linear.** Na forma padrão, $y'-y=-x$, com $\mu=e^{-x}$:
$$(e^{-x}y)'=-xe^{-x}\ \Rightarrow\ e^{-x}y=(x+1)e^{-x}+C\ \Rightarrow\ y=x+1+Ce^{x}.$$

**A reta especial.** Com $C=0$, $y=x+1$: de fato $y'=1=(x+1)-x$. ✓ No campo, os segmentos sobre essa reta têm inclinação exatamente $1$, a da própria reta.

**Instabilidade.** Para $C\neq0$, o termo $Ce^x$ cresce sem limite: acima da reta ($C>0$) as soluções sobem cada vez mais rápido; abaixo ($C<0$), despencam. Uma diferença minúscula na condição inicial vira uma diferença enorme:
- $y(0)=1$: $C=0$, $y(5)=6$;
- $y(0)=1{,}1$: $C=0{,}1$, $y(5)=6+0{,}1e^5\approx20{,}8$.

**Contraste** com $y'=x-y$ (Figura 1.1): lá o fator é $e^{-x}$ e todas as soluções convergem para a reta. O sinal do coeficiente de $y$ decide se o campo junta ou espalha as soluções.

**Animação.** As soluções partem de valores iniciais próximos e seguem o campo, afastando-se da reta $y=x+1$.""",
),
dict(id='euler', origem='inspirado no Exemplo 1.4', titulo='Euler e o número $e$',
enunciado=r"""Aplique o método de Euler a $y'=y$, $y(0)=1$, em $[0,1]$ com $n$ passos de tamanho $h=\frac1n$.
Mostre que a aproximação de $y(1)$ é $\big(1+\frac1n\big)^n$ e calcule-a para $n=1,2,4,10,100$.""",
resposta=r"""$2;\ 2{,}25;\ 2{,}441;\ 2{,}594;\ 2{,}705$, tendendo a $e\approx2{,}718$.""",
solucao=r"""**Um passo:** $y_{k+1}=y_k+h\,y_k=(1+h)\,y_k$. Começando em $y_0=1$, depois de $n$ passos:
$$y_n=(1+h)^n=\Big(1+\frac1n\Big)^n .$$

**Valores:**

| $n$ | $(1+1/n)^n$ | erro |
|---|---|---|
| 1 | 2 | 0,718 |
| 2 | 2,25 | 0,468 |
| 4 | 2,4414 | 0,277 |
| 10 | 2,5937 | 0,125 |
| 100 | 2,7048 | 0,0135 |

A solução exata é $y=e^x$, então $y(1)=e$. O limite $\lim(1+\frac1n)^n=e$ (visto no capítulo 3 do Cálculo I) aparece aqui como a convergência do método de Euler.

**Ordem do erro.** De $n=10$ para $n=100$ o erro cai cerca de 10 vezes: erro proporcional a $h$, como esperado para o método de Euler. Para ganhar uma casa decimal é preciso dez vezes mais passos, por isso existem métodos melhores (Runge–Kutta).

**Animação.** As poligonais de Euler com $1,2,4,\dots,64$ passos se aproximam de $y=e^x$; o valor final se aproxima de $e$.""",
),
dict(id='circulos', origem='inspirado no Exemplo 1.5', titulo='Soluções que acabam',
enunciado=r"""Resolva $y'=-\dfrac xy$, $y(0)=2$. Em que intervalo a solução existe? O que acontece nas pontas?""",
resposta=r"""$y=\sqrt{4-x^2}$, para $-2<x<2$; a inclinação tende a $\mp\infty$ nas pontas.""",
solucao=r"""**Separando:** $y\,dy=-x\,dx\Rightarrow\frac{y^2}2=-\frac{x^2}2+C\Rightarrow x^2+y^2=K$.

As soluções são **arcos de circunferência** centrados na origem. Com $y(0)=2$, $K=4$ e, como $y>0$ no ponto inicial, ficamos com a metade de cima:
$$y=\sqrt{4-x^2}.$$

**Intervalo.** A equação exige $y\neq0$. A solução existe em $-2<x<2$; quando $x\to\pm2$, $y\to0$ e $y'=-x/y\to\mp\infty$: a tangente fica vertical e a solução não pode continuar como função de $x$.

**Lição.** Uma equação com coeficientes bem comportados ($-x/y$ é simples) pode ter soluções que existem só num intervalo limitado, mesmo sem nenhuma "explosão": a curva simplesmente dá a volta.

**Campo de direções.** Os segmentos são perpendiculares ao raio (inclinação $-x/y$ contra $y/x$ do raio): o campo "gira" em torno da origem.

**Animação.** As semicircunferências de raios $1$ a $3$ são traçadas seguindo o campo de direções.""",
),
dict(id='resfriamento', origem='inspirado na seção 1.3', titulo='A hora da morte',
enunciado=r"""Um corpo é encontrado a $30$\textdegree C numa sala a $20$\textdegree C; uma hora depois está a
$28$\textdegree C. Supondo a lei de Newton e temperatura de $37$\textdegree C no momento da morte, há quanto tempo
ocorreu a morte quando o corpo foi encontrado?""",
resposta=r"""Cerca de $2{,}38$ h, isto é, $2$ h $23$ min.""",
solucao=r"""**Modelo:** $T'=k(T-20)\Rightarrow T(t)=20+(T_0-20)e^{kt}$.

**$k$ pelas duas medições.** Contando o tempo a partir do achado: $T=30$ e, uma hora depois, $28$. Então
$$\frac{28-20}{30-20}=e^{k}\Rightarrow k=\ln0{,}8\approx-0{,}2231\ \text{h}^{-1}.$$

**Voltando no tempo.** Seja $t_m<0$ o instante da morte, com $T(t_m)=37$:
$$37-20=(30-20)e^{kt_m}\Rightarrow t_m=\frac{\ln1{,}7}{k}=\frac{0{,}5306}{-0{,}2231}\approx-2{,}38\ \text{h}.$$

A morte ocorreu cerca de **2 h 23 min antes** de o corpo ser encontrado.

**Conferência:** de $37$ a $30$, a diferença para o ambiente vai de $17$ a $10$; com fator $0{,}8$ por hora, $17\cdot0{,}8^{2{,}38}\approx10$. ✓

**Limitações.** O modelo supõe sala a temperatura constante e corpo homogêneo; na prática a perícia usa curvas corrigidas, mas a ideia é a mesma.

**Animação.** A curva $T(t)$ é traçada desde a morte; os dois pontos medidos ficam marcados e o tempo decorrido é indicado.""",
),
dict(id='logistica', origem='inspirado no Exemplo 1.6', titulo='Resolvendo a logística',
enunciado=r"""Resolva $P'=rP\big(1-\frac PK\big)$, $P(0)=P_0$, por separação de variáveis e frações parciais.
Para $r=0{,}2311$, $K=4000$ e $P_0=900$, quando a população cresce mais rápido?""",
resposta=r"""$P=\dfrac{KP_0e^{rt}}{K-P_0+P_0e^{rt}}$; em $t=\frac1r\ln\frac{K-P_0}{P_0}\approx5{,}35$ anos, com $P=2000$.""",
solucao=r"""**Separando:** $\displaystyle\int\frac{K\,dP}{P(K-P)}=\int r\,dt$.

**Frações parciais:** $\dfrac{K}{P(K-P)}=\dfrac1P+\dfrac1{K-P}$. Integrando:
$$\ln P-\ln(K-P)=rt+C\ \Rightarrow\ \frac{P}{K-P}=Ae^{rt},\qquad A=\frac{P_0}{K-P_0}.$$

**Isolando $P$:** $P=(K-P)Ae^{rt}\Rightarrow P(1+Ae^{rt})=KAe^{rt}$, e multiplicando por $K-P_0$:
$$P(t)=\frac{KP_0e^{rt}}{K-P_0+P_0e^{rt}} .$$

**Crescimento máximo.** $P'=rP-\frac rKP^2$ é uma parábola em $P$, máxima em $P=\frac K2$. Isso acontece quando $Ae^{rt}=1$:
$$t^*=\frac1r\ln\frac{K-P_0}{P_0}=\frac{\ln(3100/900)}{0{,}2311}\approx5{,}35\ \text{anos},$$
com $P=2000$ e taxa $P'=\frac{rK}4\approx231$ cervos por ano.

**Simetria.** A curva logística é simétrica em relação ao ponto de inflexão: o tempo para ir de $P_0$ a $K/2$ é o mesmo que de $K/2$ até $K-P_0$.

**Animação.** Várias curvas logísticas (com $P_0$ diferentes) são traçadas sobre o campo de direções; o ponto de inflexão aparece em $P=2000$.""",
),
dict(id='queda', origem='inspirado no Exemplo 1.8', titulo='Velocidade terminal',
enunciado=r"""Um paraquedista cai com $v'=9{,}8-0{,}2v$, $v(0)=0$ (SI). Encontre $v(t)$, a distância percorrida
$s(t)$ e quanto tempo leva para atingir $95\%$ da velocidade terminal.""",
resposta=r"""$v=49(1-e^{-0{,}2t})$; $s=49t-245(1-e^{-0{,}2t})$; $t=5\ln20\approx15$ s.""",
solucao=r"""**Velocidade (linear):** $v'+0{,}2v=9{,}8$, $\mu=e^{0{,}2t}$:
$$(e^{0{,}2t}v)'=9{,}8e^{0{,}2t}\Rightarrow v=49+Ce^{-0{,}2t},\quad v(0)=0\Rightarrow v(t)=49\big(1-e^{-0{,}2t}\big).$$

**Velocidade terminal:** $49$ m/s ($\approx176$ km/h), o equilíbrio $v'=0\iff v=9{,}8/0{,}2$.

**Distância:** $s(t)=\int_0^tv=49t-245\big(1-e^{-0{,}2t}\big)$.

**95% da terminal:** $1-e^{-0{,}2t}=0{,}95\Rightarrow t=5\ln20\approx15{,}0$ s, quando já se caiu $s\approx49\cdot15-245\cdot0{,}95\approx502$ m.

**Sem resistência** ($v=9{,}8t$) a velocidade de 49 m/s seria atingida em 5 s; a resistência faz a aproximação ser assintótica.

**Animação.** A velocidade cresce e se aproxima da reta $v=49$; ao lado, a posição do paraquedista desce.""",
),
dict(id='colheita', origem='inspirado na seção 1.4', titulo='Logística com colheita',
enunciado=r"""Uma população de peixes segue $P'=0{,}4P\big(1-\frac P{1000}\big)-60$ (pesca constante de 60 por ano).
Encontre e classifique os equilíbrios. O que acontece se $P(0)=150$? Qual a maior pesca sustentável?""",
resposta=r"""$P\approx183{,}8$ (instável) e $P\approx816{,}2$ (estável); com $P(0)=150$ a população se extingue; pesca máxima $100$ por ano.""",
solucao=r"""**Equilíbrios:** $0{,}4P-0{,}0004P^2-60=0\iff P^2-1000P+150\,000=0$:
$$P=\frac{1000\pm\sqrt{400\,000}}2\approx183{,}8\ \text{ou}\ 816{,}2 .$$

**Sinal de $P'$** (parábola voltada para baixo em $P$): negativo abaixo de $183{,}8$, positivo entre as raízes, negativo acima de $816{,}2$. Logo:
- $816{,}2$ é **estável** (as soluções vizinhas convergem para ele);
- $183{,}8$ é **instável**: um limiar.

**$P(0)=150$:** abaixo do limiar, $P'<0$ e continua negativo: a população cai até zero em tempo finito. A pesca, que era tolerável para uma população grande, extingue uma pequena.

**Pesca máxima sustentável.** Com pesca $H$, os equilíbrios existem se $0{,}4P(1-P/1000)=H$ tem solução, e o máximo do lado esquerdo é $\frac{rK}4=\frac{0{,}4\cdot1000}4=100$. Para $H>100$ não há equilíbrio e a população sempre se extingue.

**Animação.** As soluções partem de vários $P(0)$; as que começam acima de $183{,}8$ sobem ou descem até $816$, e as de baixo despencam.""",
),
dict(id='mistura', origem='inspirado na seção 1.3', titulo='Mistura com volume variável',
enunciado=r"""Um tanque tem $100$ L de água pura. Entra salmoura com $0{,}5$ kg/L a $3$ L/min e sai a mistura a
$2$ L/min. Encontre o sal $u(t)$ e a concentração quando o volume dobrar.""",
resposta=r"""$u=\tfrac12(100+t)-\dfrac{500\,000}{(100+t)^2}$; em $t=100$: $87{,}5$ kg, concentração $0{,}4375$ kg/L.""",
solucao=r"""**Volume:** $V(t)=100+t$ (entra 3, sai 2).

**Balanço de sal:** entra $0{,}5\cdot3=1{,}5$ kg/min; sai $2\cdot\frac{u}{V}$:
$$u'+\frac{2}{100+t}\,u=1{,}5 .$$
Agora a equação é linear com coeficiente **variável**, não separável.

**Fator integrante:** $\mu=e^{\int\frac2{100+t}dt}=(100+t)^2$:
$$\big((100+t)^2u\big)'=1{,}5(100+t)^2\Rightarrow(100+t)^2u=\tfrac12(100+t)^3+C .$$
Com $u(0)=0$: $C=-\tfrac12\cdot10^6$, logo
$$u(t)=\frac{100+t}2-\frac{500\,000}{(100+t)^2}.$$

**Quando $V=200$** ($t=100$): $u=100-12{,}5=87{,}5$ kg, concentração $\frac{87{,}5}{200}=0{,}4375$ kg/L.

**Longo prazo:** a concentração $u/V=\frac12-\frac{500\,000}{(100+t)^3}\to0{,}5$ kg/L, a da salmoura que entra (se o tanque não transbordar antes).

**Animação.** O nível do tanque sobe e a cor da mistura se intensifica; ao lado, a concentração se aproxima de $0{,}5$.""",
),
dict(id='bernoulli', origem='inspirado na seção 1.5', titulo='Uma equação de Bernoulli',
enunciado=r"""Resolva $y'+y=y^2$ com a substituição $v=\frac1y$. Descreva as soluções com $y(0)=\tfrac13$, $y(0)=1$ e $y(0)=2$.""",
resposta=r"""$y=\dfrac1{1+Ce^x}$; tende a $0$, fica em $1$, e explode em $x=\ln2$, respectivamente.""",
solucao=r"""**Substituição.** Com $v=\frac1y$, $v'=-\frac{y'}{y^2}$. Dividindo a equação por $-y^2$:
$$-\frac{y'}{y^2}-\frac1y=-1\ \Rightarrow\ v'-v=-1,$$
que é **linear**.

**Resolvendo:** $\mu=e^{-x}$, $(e^{-x}v)'=-e^{-x}$, $e^{-x}v=e^{-x}+C$, $v=1+Ce^x$. Logo
$$y=\frac1{1+Ce^x}\quad(\text{e também }y\equiv0).$$

**Casos:**
- $y(0)=\frac13$: $C=2$, $y=\frac1{1+2e^x}\to0$;
- $y(0)=1$: $C=0$, $y\equiv1$, um equilíbrio (instável);
- $y(0)=2$: $C=-\frac12$, $y=\frac1{1-e^x/2}$, que **explode** quando $e^x=2$, isto é, em $x=\ln2\approx0{,}69$.

**Equilíbrios:** $y'=y^2-y=y(y-1)$: $0$ estável e $1$ instável, coerente com os três casos.

**Bernoulli em geral:** $y'+p\,y=q\,y^n$ vira linear com $v=y^{1-n}$.

**Animação.** As três soluções são traçadas; a de $y(0)=2$ dispara rumo à assíntota $x=\ln2$.""",
),
dict(id='ortogonais', origem='inspirado na seção 1.3', titulo='Trajetórias ortogonais',
enunciado=r"""Encontre as curvas que cortam todas as parábolas $y=Cx^2$ em ângulo reto.""",
resposta=r"""As elipses $x^2+2y^2=K$.""",
solucao=r"""**Equação da família.** De $y=Cx^2$, $y'=2Cx$; eliminando $C=\frac y{x^2}$:
$$y'=\frac{2y}{x}.$$

**Ortogonais.** Em cada ponto, a inclinação da curva ortogonal é o oposto do inverso:
$$y'=-\frac{x}{2y}.$$

**Separando:** $2y\,dy=-x\,dx\Rightarrow y^2=-\frac{x^2}2+c$, ou seja,
$$x^2+2y^2=K,$$
uma família de **elipses** centradas na origem, com eixo maior horizontal (semieixos $\sqrt K$ e $\sqrt{K/2}$).

**Conferência num ponto:** em $(1,1)$, a parábola $y=x^2$ tem inclinação $2$ e a elipse $x^2+2y^2=3$ tem inclinação $-\frac12$; o produto é $-1$. ✓

**Onde aparece:** linhas de campo e equipotenciais, linhas de fluxo e curvas de nível são sempre famílias ortogonais.

**Animação.** As parábolas e as elipses são desenhadas alternadamente, formando uma malha de ângulos retos.""",
),
dict(id='torricelli', origem='inspirado na seção 1.3', titulo='Esvaziando um tanque',
enunciado=r"""Pela lei de Torricelli, o nível de um tanque cilíndrico que esvazia por um furo no fundo satisfaz
$h'=-0{,}1\sqrt h$ ($h$ em m, $t$ em min). Com $h(0)=4$, encontre $h(t)$, o tempo para esvaziar e o tempo
para o nível cair à metade.""",
resposta=r"""$h=(2-0{,}05t)^2$; esvazia em $40$ min; metade do nível em $\approx11{,}7$ min.""",
solucao=r"""**Separando:** $\frac{dh}{\sqrt h}=-0{,}1\,dt\Rightarrow2\sqrt h=-0{,}1t+C$, e com $h(0)=4$, $C=4$:
$$\sqrt h=2-0{,}05t\ \Rightarrow\ h(t)=(2-0{,}05t)^2 .$$

**Esvaziamento:** $h=0$ em $t=40$ min (depois disso, $h\equiv0$).

**Metade do nível** ($h=2$): $\sqrt2=2-0{,}05t\Rightarrow t=\frac{2-\sqrt2}{0{,}05}\approx11{,}7$ min.

**Por que tão rápido?** A vazão é proporcional a $\sqrt h$: com o tanque cheio a água sai com mais pressão. A primeira metade da altura cai em $11{,}7$ min; a segunda leva os $28{,}3$ min restantes.

**Unicidade.** Em $h=0$ a função $\sqrt h$ não tem derivada limitada; por isso, voltando no tempo, não dá para saber *quando* um tanque vazio foi esvaziado (infinitas soluções terminam em $h=0$).

**Animação.** O nível do tanque desce ao lado do gráfico de $h(t)$, uma parábola que toca o eixo em $t=40$.""",
),
]
