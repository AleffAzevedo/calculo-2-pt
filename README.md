# Cálculo II — edição condensada em português

Adaptação e tradução dos capítulos 4 a 7 de **Calculus Volume 2**, de Gilbert Strang (MIT) e Edwin "Jed" Herman
(University of Wisconsin–Stevens Point), publicado pela OpenStax (Rice University).
Continua o [Cálculo I](https://github.com/AleffAzevedo/calculo-1-pt), onde já estão os capítulos 1 a 3 do original
(integração, aplicações e técnicas de integração). Cada capítulo traz 65 exercícios, com a dificuldade indicada por
pontos (• fácil, •• médio, ••• difícil, •••• desafio) e respostas. Os marcados com ★ têm solução completa e animação
neste repositório.

📘 **[Baixar o PDF](Calculo_II.pdf)**

## Conteúdo

| Capítulo | Tema | Livro | Exercícios resolvidos |
|---|---|---|---|
| 1 | Introdução às equações diferenciais | ✅ | [65 exercícios, 11 resolvidos](exercicios/cap1/README.md) |
| 2 | Sequências e séries | em produção | — |
| 3 | Séries de potências | — | — |
| 4 | Equações paramétricas e coordenadas polares | — | — |

Notação brasileira (sen, tg, arcsen…) e projeto gráfico com a identidade visual da **Nexus BI**
(fonte Barlow Semi Condensed, em `livro/fontes/`, sob a SIL OFL). A marca Nexus BI não é coberta pela licença CC BY-NC-SA.

## Estrutura

```
Calculo_II.pdf         livro compilado
livro/                 fontes LaTeX (calculo2.tex, capN.tex); figuras em TikZ/pgfplots
  exercicios_capN.tex  gerado automaticamente; não edite à mão
exercicios/capN/       soluções (README.md) e animações (anim/*.gif)
ferramentas/
  ex_capN.py           lista de 65 exercícios por capítulo, com respostas
  sol_capN.py          soluções completas dos exercícios ★
  anim_capN.py         animações (matplotlib)
  gerar.py             gera o .tex dos exercícios, os README e as animações
```

## Como compilar

```bash
python3 ferramentas/gerar.py 1          # exercícios + animações do capítulo 1
cd livro && latexmk -xelatex calculo2.tex
```

## Licença e créditos

Este trabalho é uma obra derivada de *Calculus Volume 2*, © 2016 Rice University,
disponível gratuitamente em <https://openstax.org/details/books/calculus-volume-2>,
licenciado sob [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
Esta adaptação (tradução, condensação, figuras redesenhadas, soluções e animações) é
distribuída sob a **mesma licença**, apenas para uso não comercial. Veja [LICENSE](LICENSE).

Esta versão não é endossada pela OpenStax nem pela Rice University. Os nomes e logotipos
OpenStax e Rice University são marcas registradas e não fazem parte da licença.
