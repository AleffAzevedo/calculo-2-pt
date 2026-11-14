# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 2."""

SOLUCOES = [
dict(id='recorrencia', origem='inspirado no Exemplo 2.2', titulo='Raízes encaixadas',
enunciado=r"""Seja $a_1=\sqrt2$ e $a_{n+1}=\sqrt{2+a_n}$, isto é, $\sqrt2,\ \sqrt{2+\sqrt2},\ \sqrt{2+\sqrt{2+\sqrt2}},\dots$
Mostre que a sequência converge e calcule o limite.""",
resposta=r"""Crescente e limitada por $2$; o limite é $2$.""",
solucao=r"""**Limitada por 2 (indução).** $a_1=\sqrt2<2$. Se $a_n<2$, então $a_{n+1}=\sqrt{2+a_n}<\sqrt4=2$.

**Crescente.** $a_{n+1}>a_n\iff2+a_n>a_n^2\iff(a_n-2)(a_n+1)<0$, verdadeiro para $0<a_n<2$.

**Converge** pelo Teorema da convergência monótona. Seja $L$ o limite. Passando ao limite em $a_{n+1}^2=2+a_n$:
$$L^2=2+L\ \Rightarrow\ L=2\ \ (\text{ou }L=-1,\ \text{impossível, pois }a_n>0).$$

**Valores:** $1{,}4142;\ 1{,}8478;\ 1{,}9616;\ 1{,}9904;\ 1{,}9976;\ 1{,}9994\dots$ A distância a $2$ cai cerca de 4 vezes a cada passo.

**Curiosidade:** $a_n=2\cos\frac{\pi}{2^{n+1}}$ (fórmula do arco metade), o que confirma o limite e a velocidade.

**Animação.** O "diagrama de teia": a partir de $a_1$, sobe-se até a curva $y=\sqrt{2+x}$ e volta-se à reta $y=x$, convergindo para o ponto fixo $(2,2)$.""",
),
dict(id='geometrica', origem='inspirado no Teorema 2.2', titulo='A bola que quica',
enunciado=r"""Uma bola cai de $10$ m e, a cada quique, sobe a $\frac34$ da altura anterior. Qual a distância
total percorrida? E o tempo total, se a queda de uma altura $h$ leva $\sqrt{2h/g}$ ($g=9{,}8$)?""",
resposta=r"""$70$ m; cerca de $19{,}9$ s.""",
solucao=r"""**Distância.** A bola desce $10$, depois sobe e desce $10\cdot\frac34$, depois $10\cdot\big(\frac34\big)^2$, e assim por diante:
$$D=10+2\sum_{n=1}^\infty10\Big(\frac34\Big)^n=10+2\cdot\frac{7{,}5}{1-3/4}=10+60=70\ \text{m}.$$

**Tempo.** Subir ou descer de uma altura $h$ leva $\sqrt{2h/g}$, e a altura do $n$-ésimo quique é $10(3/4)^n$, logo cada tempo é o anterior vezes $r=\sqrt{3/4}\approx0{,}866$. Com $t_0=\sqrt{20/9{,}8}\approx1{,}429$ s:
$$T=t_0+2\sum_{n=1}^\infty t_0r^n=t_0\Big(1+\frac{2r}{1-r}\Big)\approx1{,}429\cdot13{,}93\approx19{,}9\ \text{s}.$$

**Infinitos quiques em tempo finito.** Como os tempos formam uma série geométrica convergente, a bola quica infinitas vezes e para em menos de 20 segundos (no modelo; na prática, efeitos que o modelo ignora param a bola antes).

**Animação.** A bola quica enquanto as somas parciais da distância se aproximam de $70$ m.""",
),
dict(id='harmonica', origem='inspirado na seção 2.2', titulo='A lentidão da série harmônica',
enunciado=r"""Use o teste da integral para mostrar que $\ln(n+1)\le H_n\le1+\ln n$, em que $H_n=1+\frac12+\dots+\frac1n$.
Quantos termos são necessários para $H_n$ passar de $10$?""",
resposta=r"""$12\,367$ termos.""",
solucao=r"""**Retângulos acima da curva:** cada $\frac1k$ é a área de um retângulo de base $[k,k+1]$ que fica acima de $y=\frac1x$:
$$H_n\ \ge\ \int_1^{n+1}\frac{dx}x=\ln(n+1).$$

**Retângulos abaixo da curva:** deslocando para $[k-1,k]$, os retângulos de $\frac12,\dots,\frac1n$ ficam abaixo:
$$H_n-1\ \le\ \int_1^n\frac{dx}x=\ln n.$$

**Divergência confirmada:** $H_n\ge\ln(n+1)\to\infty$.

**Passar de 10:** precisamos de $\ln(n+1)\approx10$, isto é, $n$ da ordem de $e^{10}-1\approx22\,025$ pela cota inferior. A estimativa mais fina $H_n\approx\ln n+\gamma$ (com $\gamma\approx0{,}5772$, a constante de Euler) dá $n\approx e^{10-0{,}5772}\approx12\,367$, e de fato $H_{12\,367}$ é o primeiro acima de $10$.

**Escala:** para passar de $100$ seriam precisos cerca de $1{,}5\times10^{43}$ termos.

**Animação.** As somas parciais (em escala logarítmica de $n$) seguem a reta $\ln n+\gamma$, presas entre as duas cotas.""",
),
dict(id='telescopica', origem='inspirado no Exemplo 2.3', titulo='Telescópica com salto',
enunciado=r"""Calcule $\displaystyle\sum_{n=1}^\infty\frac1{n(n+2)}$.""",
resposta=r"""$\tfrac34$.""",
solucao=r"""**Frações parciais:** $\dfrac1{n(n+2)}=\dfrac12\Big(\dfrac1n-\dfrac1{n+2}\Big)$.

**Soma parcial.** Agora os termos se cancelam *dois a dois de distância*:
$$S_k=\frac12\Big[\Big(1-\tfrac13\Big)+\Big(\tfrac12-\tfrac14\Big)+\Big(\tfrac13-\tfrac15\Big)+\dots+\Big(\tfrac1k-\tfrac1{k+2}\Big)\Big].$$
Sobram os dois primeiros positivos e os dois últimos negativos:
$$S_k=\frac12\Big(1+\frac12-\frac1{k+1}-\frac1{k+2}\Big)\ \xrightarrow{k\to\infty}\ \frac12\cdot\frac32=\frac34 .$$

**Cuidado** com o erro comum de achar que só sobra o primeiro termo: quando o "salto" é 2, sobram dois termos de cada ponta.

**Conferência numérica:** $S_{10}\approx0{,}6629$, $S_{100}\approx0{,}7401$, $S_{1000}\approx0{,}7490$.

**Animação.** Os termos são cancelados aos pares, e o gráfico de $S_k$ se aproxima de $3/4$.""",
),
dict(id='resto_integral', origem='inspirado no Exemplo 2.4', titulo='Estimando $\\sum 1/n^2$',
enunciado=r"""Calcule $S_{10}$ para $\sum\frac1{n^2}$ e use as cotas do resto pelo teste da integral para obter um intervalo para a soma.
Compare com o valor exato $\frac{\pi^2}6$.""",
resposta=r"""$S_{10}\approx1{,}5498$; $1{,}6407\le S\le1{,}6498$; $\frac{\pi^2}6\approx1{,}6449$.""",
solucao=r"""**Soma parcial:** $S_{10}=1+\frac14+\frac19+\dots+\frac1{100}\approx1{,}549768$.

**Cotas do resto** com $f(x)=\frac1{x^2}$:
$$\int_{11}^\infty\frac{dx}{x^2}=\frac1{11}\ \le\ R_{10}\ \le\ \int_{10}^\infty\frac{dx}{x^2}=\frac1{10}.$$

**Intervalo para a soma:**
$$1{,}640677\ \le\ S\ \le\ 1{,}649768 .$$

**Melhor estimativa:** o ponto médio, $1{,}645222$, erra o valor exato $\frac{\pi^2}6=1{,}644934$ por apenas $0{,}0003$, muito melhor que $S_{10}$ sozinha (erro $0{,}095$). Para chegar a esse erro só com somas parciais seriam precisos uns $3000$ termos.

**O valor $\pi^2/6$** (problema de Basileia, resolvido por Euler em 1734) aparece de novo no próximo capítulo.

**Animação.** As somas parciais sobem devagar; a faixa $[S_N+\frac1{N+1},\,S_N+\frac1N]$ estreita-se em torno de $\pi^2/6$.""",
),
dict(id='alternada_erro', origem='inspirado no Teorema 2.8', titulo='Uma alternada que converge depressa',
enunciado=r"""A série $\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n!}$ vale $1-\frac1e$. Quantos termos garantem erro menor que $10^{-4}$?
Compare a soma parcial com o valor exato.""",
resposta=r"""$N=7$; $S_7\approx0{,}632143$ contra $0{,}632121$.""",
solucao=r"""**Hipóteses de Leibniz:** $b_n=\frac1{n!}$ decresce e tende a $0$. ✓

**Cota do erro:** $|R_N|\le b_{N+1}=\frac1{(N+1)!}$. Queremos $(N+1)!>10\,000$: $7!=5040$ não basta, $8!=40\,320$ basta. Logo $N=7$.

**Soma parcial:**
$$S_7=1-\frac12+\frac16-\frac1{24}+\frac1{120}-\frac1{720}+\frac1{5040}\approx0{,}632143 .$$

**Valor exato:** $1-e^{-1}\approx0{,}632121$; o erro real é $2{,}2\times10^{-5}$, abaixo da cota $\frac1{40\,320}\approx2{,}5\times10^{-5}$.

**Sinal do erro:** como paramos num termo positivo, $S_7$ fica *acima* da soma. Em séries alternadas, a soma está sempre entre duas somas parciais consecutivas: $S_6<S<S_7$.

**Contraste** com $\sum\frac{(-1)^{n+1}}n$, que precisa de $10\,000$ termos para o mesmo erro: os fatoriais tendem a zero muito mais depressa.

**Animação.** As somas parciais pulam de um lado para o outro de $1-1/e$, com saltos que encolhem rapidamente.""",
),
dict(id='koch', origem='inspirado na seção 2.2', titulo='O floco de neve de Koch',
enunciado=r"""Partindo de um triângulo equilátero de área $A_0$, a cada etapa cada lado é dividido em três e, sobre o terço
do meio, constrói-se um novo triângulo equilátero para fora. Mostre que o perímetro tende a infinito, mas a área tende a $\frac85A_0$.""",
resposta=r"""Perímetro $3\ell(4/3)^n\to\infty$; área $A_0\big(1+\sum_{n\ge1}\frac{3\cdot4^{n-1}}{9^n}\big)=\frac85A_0$.""",
solucao=r"""**Perímetro.** Cada lado vira 4 segmentos de $\frac13$ do comprimento: o perímetro é multiplicado por $\frac43$ a cada etapa, $P_n=3\ell\big(\frac43\big)^n\to\infty$.

**Área.** Na etapa $n\ge1$:
- número de triângulos novos: um por lado da etapa anterior, $3\cdot4^{n-1}$;
- área de cada um: lado $\frac1{3^n}$ do original, área $\frac{A_0}{9^n}$.

$$A=A_0+\sum_{n=1}^\infty3\cdot4^{n-1}\cdot\frac{A_0}{9^n}=A_0\Big(1+\frac13\sum_{n=1}^\infty\Big(\frac49\Big)^{n-1}\Big)=A_0\Big(1+\frac13\cdot\frac{1}{1-4/9}\Big)=\frac85A_0 .$$

**O paradoxo.** Uma região de área finita cercada por uma curva de comprimento infinito. Não há contradição: a curva fica cada vez mais enrugada dentro de uma região limitada (cabe num círculo).

**Dimensão.** A curva de Koch tem dimensão fractal $\frac{\ln4}{\ln3}\approx1{,}26$: "mais que uma curva, menos que uma superfície".

**Animação.** As cinco primeiras etapas do floco, com o perímetro e a área de cada uma.""",
),
dict(id='rearranjo', origem='inspirado na seção 2.5', titulo='Reordenar muda a soma',
enunciado=r"""Sabendo que $1-\frac12+\frac13-\frac14+\dots=\ln2$, mostre que a reordenação
$1+\frac13-\frac12+\frac15+\frac17-\frac14+\cdots$ (dois positivos, um negativo) tem soma $\frac32\ln2$.""",
resposta=r"""$\tfrac32\ln2\approx1{,}0397$.""",
solucao=r"""**Duas séries conhecidas.**
$$\ln2=1-\tfrac12+\tfrac13-\tfrac14+\tfrac15-\tfrac16+\tfrac17-\tfrac18+\cdots$$
$$\tfrac12\ln2=\phantom{1}\ \ \ \tfrac12\phantom{+\tfrac13}-\tfrac14\phantom{+\tfrac15}+\tfrac16\phantom{+\tfrac17}-\tfrac18+\cdots$$
(a segunda é a primeira multiplicada por $\frac12$, com zeros intercalados, o que não muda a soma).

**Somando termo a termo** (permitido para séries convergentes):
$$\tfrac32\ln2=1+\tfrac13-\tfrac12+\tfrac15+\tfrac17-\tfrac14+\cdots$$
Os $\frac12$ se cancelam, os $-\frac14$ dobram, os $\frac16$ se cancelam… e sobra exatamente a reordenação pedida.

**Os mesmos termos, outra soma.** Isso só é possível porque a convergência é **condicional**: a parte positiva $1+\frac13+\frac15+\cdots$ e a negativa $\frac12+\frac14+\cdots$ divergem separadamente. Riemann mostrou que, reordenando, se obtém *qualquer* número real (ou $\pm\infty$). Com convergência absoluta isso não acontece.

**Conferência:** com 300 000 termos, a soma parcial vale $1{,}039718$, e $\frac32\ln2=1{,}039721$.

**Animação.** As somas parciais das duas ordenações são traçadas lado a lado: uma vai para $\ln2$, a outra para $\frac32\ln2$.""",
),
dict(id='empilhamento', origem='inspirado na seção 2.2', titulo='Empilhando blocos',
enunciado=r"""Blocos de comprimento $1$ são empilhados na borda de uma mesa. Colocando o centro de massa dos $k$ blocos de cima
sobre a borda do bloco $k+1$, o $k$-ésimo bloco (de cima para baixo) avança $\frac1{2k}$. Qual o balanço total com $n$ blocos?
Quantos blocos são precisos para o bloco do topo ficar inteiramente fora da mesa? E para um balanço de $3$?""",
resposta=r"""$\frac12H_n$; $4$ blocos; $227$ blocos.""",
solucao=r"""**Balanço total:** somando os avanços,
$$d_n=\frac12+\frac14+\frac16+\dots+\frac1{2n}=\frac12H_n .$$

**Por que $\frac1{2k}$?** Os $k$ blocos de cima têm centro de massa exatamente sobre a borda do bloco $k+1$. Acrescentando o bloco $k+1$ (centro a $\frac12$ de sua borda), o centro de massa dos $k+1$ blocos se desloca $\frac{1/2}{k+1}$ em relação a essa borda: é o avanço do próximo nível.

**Topo inteiramente fora** ($d_n>1$, ou seja, $H_n>2$): $H_3=1{,}83$, $H_4=2{,}08$. Bastam **4 blocos**.

**Balanço de 3** ($H_n>6$): $n=227$ blocos.

**Sem limite.** Como $H_n\to\infty$, o balanço pode ser tão grande quanto se queira, mas cresce como $\frac12\ln n$: para um balanço de $10$ comprimentos seriam precisos cerca de $2{,}7\times10^8$ blocos.

**Animação.** A pilha cresce de cima para baixo e o balanço total acompanha $\frac12H_n$.""",
),
dict(id='cantor', origem='inspirado na seção 2.2', titulo='O conjunto de Cantor',
enunciado=r"""Do intervalo $[0,1]$ retira-se o terço do meio $(\frac13,\frac23)$; de cada um dos dois intervalos restantes,
retira-se o terço do meio; e assim por diante. Qual o comprimento total retirado?""",
resposta=r"""$1$: o conjunto que sobra tem comprimento total zero.""",
solucao=r"""**Etapa $n$:** retiram-se $2^{n-1}$ intervalos de comprimento $\frac1{3^n}$.

**Comprimento retirado:**
$$\sum_{n=1}^\infty\frac{2^{n-1}}{3^n}=\frac13\sum_{n=1}^\infty\Big(\frac23\Big)^{n-1}=\frac13\cdot\frac1{1-2/3}=1 .$$

**O que sobra.** O conjunto de Cantor tem "comprimento" zero, mas não é vazio nem pequeno: contém $0$, $1$, $\frac13$, $\frac23$, $\frac14$ (!) e, na verdade, tantos pontos quanto o próprio $[0,1]$. São os números cuja expansão na base 3 pode ser escrita só com os dígitos $0$ e $2$; por exemplo, $\frac14=0{,}\overline{02}_3$.

**Após $n$ etapas** sobra $\big(\frac23\big)^n$ do comprimento: depois de 10 etapas, apenas $1{,}7\%$.

**Animação.** As etapas da construção, com o comprimento retirado acumulado se aproximando de $1$.""",
),
dict(id='potencias', origem='inspirado no Teorema 2.2', titulo='Somando $\\sum n/2^n$',
enunciado=r"""Mostre que $\displaystyle\sum_{n=1}^\infty\frac n{2^n}$ converge e calcule a soma usando $S-\frac12S$.
Faça o mesmo para $\displaystyle\sum_{n=1}^\infty\frac{n^2}{2^n}$.""",
resposta=r"""$2$ e $6$.""",
solucao=r"""**Convergência (razão):** $\frac{a_{n+1}}{a_n}=\frac{n+1}{2n}\to\frac12<1$.

**Primeira soma.** Seja $S=\frac12+\frac24+\frac38+\frac4{16}+\cdots$. Então
$$S-\frac12S=\frac12+\frac14+\frac18+\cdots=1\ \Rightarrow\ S=2 .$$
(Deslocando $\frac12S$ uma posição, cada termo $\frac n{2^n}-\frac{n-1}{2^n}=\frac1{2^n}$.)

**Segunda soma.** Seja $T=\sum\frac{n^2}{2^n}$. Do mesmo modo,
$$T-\frac12T=\sum_{n=1}^\infty\frac{n^2-(n-1)^2}{2^n}=\sum\frac{2n-1}{2^n}=2S-1=3\ \Rightarrow\ T=6 .$$

**Conferência:** $S_{20}\approx1{,}99998$; $T_{30}\approx5{,}99999$.

**Ideia geral.** No próximo capítulo, derivando a série geométrica $\sum x^n=\frac1{1-x}$, obtemos $\sum nx^n=\frac x{(1-x)^2}$, que em $x=\frac12$ dá $2$.

**Animação.** As somas parciais de $\sum n/2^n$ e $\sum n^2/2^n$ se aproximam de $2$ e $6$.""",
),
]
