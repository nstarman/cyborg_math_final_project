# 03-zeroth\_order

\`\`\`{r include=FALSE}

## Add a common class name for every chunks

knitr::opts\_chunk$set\(echo = TRUE\) library\(reticulate\) library\(knitr\) opts\_chunk$set\(engine.path = '/Users/nathanielstarkman/miniconda3/bin/python3.7'\)

```text
```{python, echo=F, eval=T}
from src import *
```

## Zeroth-Order Solution

\(@Zaldarriaga1995 \(2.7\)\)

\`\`\`{python, echo=T, eval=T}

## loading

with open\('src/pickled/02.pkl', 'rb'\) as file: vars = pickle.load\(file\)

DeltaTDef = vars\['DeltaTDef'\] DeltaPDef = vars\['DeltaPDef'\]

EqT = vars\['EqT'\] EqP = vars\['EqP'\] EqV = vars\['EqV'\]

aniT0to1 = vars\['aniT0to1'\] tex\_aniT0to1 = vars\['tex\_aniT0to1'\]

```text
Solving Z\&H95 (2.6) at 0th order. The terms on the right go to 0.

```{python}
EqT_O0 = sp.Eq(EqT.lhs.subs(dummyO, 0), 0)
EqP_O0 = sp.Eq(EqP.lhs.subs(dummyO, 0), 0)
EqV_O0 = sp.Eq(EqV.lhs.subs(dummyO, 0), 0)
```

\`\`\`{python, echo=FALSE} tex\_EqT\_O0 = sp.latex\(EqT\_O0\).replace\('=', '&='\) tex\_EqP\_O0 = sp.latex\(EqP\_O0\).replace\('=', '&='\) tex\_EqV\_O0 = sp.latex\(EqV\_O0\).replace\('=', '&='\)

```text
\begin{align}
    `r py$tex_EqT_O0` & (\#eq:O0T) \\
    `r py$tex_EqP_O0` & (\#eq:O0P) \\
    `r py$tex_EqV_O0` & (\#eq:O0Vb)
\end{align}

We have already derived Z\&H95's relation $`r py$tex_aniT0to1`$ above -- the middle equation of his (2.8) -- in \@ref(eq:aniT0to1). Recall that this is true order-by-order, so the 0th order form is 

```{python}
# temp = aniT0to1.subs(DT_a_0, DT_a_0.my_eval(l=0))
aniT0to1_O0 = aniT0to1.subs(dummyO, 0)
```

\`\`\`{python, echo=F} tex\_aniT0to1\_O0 = sp.latex\(aniT0to1\_O0\)

```text
\begin{equation}
    `r py$tex_aniT0to1_O0`.
    (\#eq:O0aniT0to1)
\end{equation}

Rearranging \@ref(eq:O0Vb), we find Z\&H95 (2.7a):

```{python}
ZH2p7a = sp.Eq(DT_0_1, sp.solve(EqV_O0, DT_0_1)[0])
```

\`\`\`{python, echo=FALSE} tex\_ZH2p7a = sp.latex\(ZH2p7a\)

```text
\begin{equation}
  `r py$tex_ZH2p7a`
  (\#eq:O0Zaldarriaga2p7a)
\end{equation}

Now looking at \@ref(eq:O0P), expanding order-by-order

```{python}
alltemp = sp.expand(EqP_O0.lhs)
tempRHS = EqP_O0.rhs

# l=0
temp = alltemp.subs(DP_0, DP_0.my_eval(l=0, fullsub=False))
temp = sp.collect(temp, LgP(0), evaluate=False)[LgP(0)]  # collect powers of LgP(0)
temp = temp.subs(LgP(0), 1)
EqP_O0_l0 = sp.Eq(2 * tempRHS, 2 * temp)

# l=1
temp = alltemp.subs(DP_0, DP_0.my_eval(l=1, fullsub=False))
temp = sp.collect(temp, LgP(1), evaluate=False)[LgP(1)]  # collect powers of LgP(1)
EqP_O0_l1 = sp.Eq(tempRHS / 3, temp / 3)

# l=2
temp = alltemp.subs(DP_0, DP_0.my_eval(l=2, fullsub=False))
temp = sp.collect(temp, LgP(2), evaluate=False)[LgP(2)]  # collect powers of LgP(2)
EqP_O0_l2 = sp.Eq(2 * tempRHS, 2 * temp)

# l>=3
temp = alltemp.subs(DP_0, DP_0.my_eval(l=lge3, fullsub=False)).subs(l, lge3)
temp_exp = sp.collect(temp, LgP(lge3), evaluate=False)[LgP(lge3)]  # collect powers of LgP(>=3)
EqP_O0_lge3 = sp.Eq(tempRHS / (2*lge3 + 1), temp_exp / (2*lge3 + 1))
# just confirming
if sp.collect(temp, LgP(4), evaluate=False).get(LgP(4), False) is not False:
  raise Exception()
```

\`\`\`{python, echo=FALSE} tex\_EqP\_O0\_l0 = sp.latex\(EqP\_O0\_l0\).replace\('=', '&='\) tex\_EqP\_O0\_l1 = sp.latex\(EqP\_O0\_l1\).replace\('=', '&='\) tex\_EqP\_O0\_l2 = sp.latex\(EqP\_O0\_l2\).replace\('=', '&='\) tex\_EqP\_O0\_lge3 = sp.latex\(EqP\_O0\_lge3.subs\(3, l\)\).replace\('=', '&='\)

```text
\begin{align}
    `r py$tex_EqP_O0_l0` & (\ell=0) (\#eq:O0Pl0) \\
    `r py$tex_EqP_O0_l1` & (\ell=1) (\#eq:O0Pl1) \\
    `r py$tex_EqP_O0_l2` & (\ell=2) (\#eq:O0Pl2) \\
    `r py$tex_EqP_O0_lge3` & (\ell \geq 3) (\#eq:O0Plge3)
\end{align}

Substituting \@ref(eq:O0Pl0) into \@ref(eq:O0Pl2).

```{python}
temp = sp.Eq(EqP_O0_l0.lhs - EqP_O0_l2.lhs, EqP_O0_l0.rhs - EqP_O0_l2.rhs)  # \@ref(eq:O0Pl0)- \@ref(eq:O0Pl2)
O0PT2toP2 = sp.Eq(DP_0_2, sp.solve(temp, DP_0_2)[0])
```

\`\`\`{python, echo=FALSE} tex\_O0PT2toP2 = sp.latex\(O0PT2toP2\)

```text
\begin{equation}
    `r py$tex_O0PT2toP2`
    (\#eq:O0PT2toP2)
\end{equation}

Substitute \@ref(eq:O0PT2toP2) into \@ref(eq:O0Pl0).

```{python}
temp = EqP_O0_l0.subs(O0PT2toP2.lhs, O0PT2toP2.rhs)  # sub
O0PT2toP0 = sp.Eq(DP_0_0, sp.solve(temp, DP_0_0)[0])  # solve
```

\`\`\`{python, echo=FALSE} tex\_O0PT2toP0 = sp.latex\(O0PT2toP0\)

```text
\begin{equation}
    `r py$tex_O0PT2toP0`
    (\#eq:O0PT2toP0)
\end{equation}

These equations will prove inconsistent when analyzing the expansion of \@ref(eq:O0T). Expanding \@ref(eq:O0T) now,

```{python}
alltemp = sp.expand(EqT_O0.lhs)
tempRHS = EqT_O0.rhs

# l=0
temp = alltemp.subs(DT_0, DT_0.my_eval(l=0, fullsub=False))
temp = sp.collect(temp, LgP(0), evaluate=False).get(LgP(0), False)  # collect powers of LgP(0)
if temp is False:
    EqT_O0_l0 = sp.Eq(tempRHS, 0)
else:
    raise Exception(str(temp))

# l=1
temp = alltemp.subs(DT_0, DT_0.my_eval(l=1, fullsub=False))
temp = sp.collect(temp, LgP(1), evaluate=False)[LgP(1)]  # collect powers of LgP(1)
EqT_O0_l1 = sp.Eq(tempRHS, temp)

# l=2
temp = alltemp.subs(DT_0, DT_0.my_eval(l=2, fullsub=False))
temp = sp.collect(temp, LgP(2), evaluate=False)[LgP(2)]  # collect powers of LgP(2)
EqT_O0_l2 = sp.Eq(2 * tempRHS, 2 * temp)

# l>=3
temp = alltemp.subs(DT_0, DT_0.my_eval(l=lge3, fullsub=False)).subs(l, lge3)
temp_exp = sp.collect(temp, LgP(lge3), evaluate=False)[LgP(lge3)]  # collect powers of LgP(l>=3)
EqT_O0_lge3 = sp.Eq(tempRHS / (2*lge3 + 1), temp_exp / (2*lge3 + 1))
# just confirming
if sp.collect(temp, LgP(4), evaluate=False).get(LgP(4), False) is not False:
  raise Exception()
```

\`\`\`{python, echo=FALSE} tex\_EqT\_O0\_l0 = sp.latex\(EqT\_O0\_l0\).replace\('=', '&='\) tex\_EqT\_O0\_l1 = sp.latex\(EqT\_O0\_l1\).replace\('=', '&='\) tex\_EqT\_O0\_l2 = sp.latex\(EqT\_O0\_l2\).replace\('=', '&='\) tex\_EqT\_O0\_lge3 = sp.latex\(EqT\_O0\_lge3\).replace\('=', '&='\)

```text
\begin{align}
    &`r py$tex_EqT_O0_l0` \quad \text{$\Delta^{(0)}_{T0}$ is a free parameter.} & (\ell = 0) (\#eq:O0Tl0) \\
    `r py$tex_EqT_O0_l1` & \text{see (4.4)} \quad (\ell=1) \\
    `r py$tex_EqT_O0_l2` & (\ell=2) (\#eq:O0Tl2) \\
    `r py$tex_EqT_O0_lge3` & (\ell \geq 3)  (\#eq:O0Tlge3)
\end{align}


Combining \@ref(eq:O0Tl2) with \@ref(eq:O0Pl2).

```{python}
temp = sp.Eq(EqT_O0_l2.lhs - EqP_O0_l2.lhs, EqT_O0_l2.rhs - EqP_O0_l2.rhs)
O0T2P2 = sp.Eq(DP_0_2, sp.solve(temp, DP_0_2)[0])
```

\`\`\`{python, echo=F} tex\_O0T2P2 = sp.latex\(O0T2P2\)

```text
\begin{equation}
    `r py$tex_O0T2P2`
    (\#eq:O0T2P2)
\end{equation}

Comparing this with \@ref(eq:O0PT2toP2) we see the incompatibility of the two equations. Therefore,

```{python}
tempLHS = O0T2P2.lhs - O0PT2toP2.lhs
tempRHS = O0T2P2.rhs - O0PT2toP2.rhs
O0T2sol = sp.Eq(sp.Rational(4,3)*tempRHS, sp.Rational(4,3)*tempLHS)

# and subbing into P equation
O0P2sol = O0T2P2.subs(sp.solve(O0T2sol, DT_0_2, dict=True)[0])
```

\`\`\`{python, echo=F} tex\_O0T2sol = sp.latex\(O0T2sol\).replace\('=', '&='\) tex\_O0P2sol = sp.latex\(O0P2sol\).replace\('=', '&='\)

```text
\begin{align}
    `r py$tex_O0T2sol` & (\#eq:O0T2sol) \\
    `r py$tex_O0P2sol` & (\#eq:O0P2sol)
\end{align}

Substituting this into \@ref(eq:O0PT2toP0) we again see the incompatibility of the two equations. Therefore,

```{python}
O0P0sol = O0PT2toP0.subs(sp.solve(O0T2sol, DT_0_2, dict=True)[0])
```

\`\`\`{python, echo=F} tex\_O0P0sol = sp.latex\(O0P0sol\)

```text
\begin{equation}
    `r py$tex_O0P0sol`
\end{equation}

Putting all these relations together we get Z\&H95 (2.7),

```{python}
# ZH2p7a already done
if (
    (sp.solve(O0P0sol, DP_0_0)[0] == 0)
    & (sp.solve(EqP_O0_l1, DP_0_1)[0] == 0)
    & (sp.solve(O0P2sol, DP_0_2)[0] == 0)
    & (sp.solve(EqP_O0_lge3, DP_0_ge3)[0] == 0)
):
    O0Psol = sp.Eq(DP_0, 0)

if (
    (sp.solve(O0T2sol, DT_0_2)[0] == 0)
    & (sp.solve(EqT_O0_lge3, DT_0_ge3)[0] == 0)
):
    O0Tsol = sp.Eq(DT_0.subs(dummyL, lge2), 0)
```

\`\`\`{python, echo=F} tex\_O0Tsol = sp.latex\(O0Tsol\) tex\_O0Psol = sp.latex\(O0Psol\)

```text
\begin{align}
    `r py$tex_ZH2p7a` \quad , \quad `r py$tex_O0Psol` \quad , \quad `r py$tex_O0Tsol`
\end{align}

<!-- \begin{align} -->
<!--     \mathbf{\Delta^{(0)}_{T1} = \frac{1}{3}V_b^{(0)}} \quad , \quad \mathbf{\Delta^{(0)}_{P} = 0} \quad , \quad \mathbf{\Delta^{(0)}_{T\ell} = 0 \, , \, \ell \geq 2} -->
<!-- \end{align} -->


- - -

```{python, echo=T}

vars['aniT0to1_O0'] = aniT0to1_O0
vars['tex_aniT0to1_O0'] = tex_aniT0to1_O0

vars['O0Tsol'] = {DT_0: DT_0.doit(i=l).subs(sp.oo, 1).doit()}

with open('src/pickled/03.pkl', 'wb') as file:
    pickle.dump(vars, file)
```

