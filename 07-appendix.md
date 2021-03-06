# 07-appendix

\`\`\`{r include=FALSE} knitr::opts\_chunk$set\(echo = TRUE\) library\(reticulate\) library\(knitr\) opts\_chunk$set\(engine.path = '/Users/nathanielstarkman/miniconda3/bin/python3.7'\)

```text
```{python echo=FALSE, eval=TRUE}
from src import *
```

## Appendix

### Legendre Products <a id="app:legendre_products"></a>

It's useful to note that the product $\rm{P}_{2} \rm{P}_{\ell}$, can easily be expressed as a linear combination of $\rm{P}_{\ell+2}$, $\rm{P}_{\ell}$, and $\rm{P}\_{\ell-2}$.  
We derive the coefficients:

\begin{equation} \mu \rm{P}_{\ell} = \frac{l+1}{2l+1} \rm{P}_{\ell+1} + \frac{l}{2l+1}\rm{P}_{\ell-1}  
\end{equation} Applying this again, \begin{eqnarray} \mu^2 \rm{P}_{\ell} &=& \frac{l+1}{2l+1} \left\( \frac{l+2}{2l+3} \rm{P}_{\ell+2} + \frac{l+1}{2l+3}\rm{P}_{\ell} \right\) \ &&\,+ \frac{l}{2l+1}\left\( \frac{l}{2l-1} \rm{P}_{\ell} + \frac{l-1}{2l-1}\rm{P}_{\ell-2} \right\) \nonumber \ &=& \frac{\(l+2\)\(l+1\)}{\(2l+3\)\(2l+1\)}\rm{P}_{\ell+2} + \frac{1}{2l+1}\left\(\frac{\(l+1\)^2}{2l+3} + \frac{l^2}{2l-1}\right\) \rm{P}_{\ell} \nonumber\ &&\,+ \frac{l\(l-1\)}{\(2l+1\)\(2l-1\)}\rm{P}_{\ell-2}\nonumber\ &=& \frac{\(l+2\)\(\ell+1\)}{\(2\ell+3\)\(2\ell+1\)}\rm{P}_{\ell+2} + \frac{2\ell^2 + 2\ell - 1}{\(2\ell+3\)\(2\ell-1\)}\rm{P}_{\ell} \nonumber\ &&\,+ \frac{\ell\(\ell-1\)}{\(2\ell+1\)\(2\ell-1\)}\rm{P}_{\ell-2}\nonumber \end{eqnarray}

use \begin{eqnarray} \rm{P}_{2}\rm{P}_{\ell} &=& \frac{1}{2}\(3\mu^2-1\)\rm{P}_{\ell}\ &=& a_\ell^+\rm{P}_{\ell+2} + a_\ell^0\rm{P}_{\ell} + a_\ell^-\rm{P}\_{\ell-2} \nonumber \end{eqnarray}

Therefore \begin{eqnarray} a_\ell^+ &=& \frac{3}{2}\frac{\(\ell+2\)\(\ell+1\)}{\(2\ell+3\)\(2\ell+1\)} \ a_\ell^0 &=& \frac{\ell\(\ell+1\)}{\(2\ell+3\)\(2\ell-1\)} \ a\_\ell^- &=& \frac{3}{2}\frac{\ell\(\ell-1\)}{\(2\ell+1\)\(2\ell-1\)} \end{eqnarray}

Similarly for the $b's$

\begin{eqnarray} \(1 - \rm{P}_{2}\)\rm{P}_{\ell} &=& \frac{3}{2}\(1-\mu^2\)\rm{P}_{\ell} \ &=& b_\ell^+\rm{P}_{\ell+2} + b_\ell^0\rm{P}_{\ell} + b_\ell^-\rm{P}_{\ell-2} \end{eqnarray} so \begin{eqnarray} b_\ell^+ &=& -a_\ell^+ \ b_\ell^0 &=& -3 \frac{\ell^2 + \ell - 1}{\(2\ell+3\)\(2\ell-1\)} \ b_\ell^- &=& -b_\ell^- \end{eqnarray}

### Approximations <a id="app:approx"></a>

#### R and a <a id="sub:r_and_a"></a>

Zaldarriaga defines $R \equiv \frac{3\rho_b}{4\rho_\gamma}$

This means $\frac{\dot{R}}{R} \approxeq \frac{\dot{a}}{a}$, where corrections are of order the momentum of the baryons and potentially also the correct consideration of the neutrinos.

