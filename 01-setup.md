# 01-setup

## Imports and Setup

\`\`\`{r include=FALSE} knitr::opts\_chunk$set\(echo = TRUE\)

Each chapter includes the following code block, which is used to set the python environment. This should be changed to \*your\* python path to be run.

```text
```{r python_setup, echo=TRUE}
library(reticulate)
library(knitr)
opts_chunk$set(engine.path='/Users/nathanielstarkman/miniconda3/bin/python3.7')
```

The following imports and definitions may be found in the `src` folder of this project. They are included here for easy perusal, but are imported in each chapter with the following code block \(hidden in chapters\)

\`\`\`{python, echo=TRUE, eval=TRUE} from src import \*

```text
## Imports

These are the important imports from `src`

```{python example_imports, echo=T, eval=F}
import pickle

import sympy as sp
from sympy import pprint, Symbol, init_printing

init_printing()

from src.parameters import (  # Parameters
    # dummy's
    dummyL, dummyO, dummyMinus, dummyZero, dummyPlus,
    legendre_products_constants,
    # variables
    tau, tau0, mu, l, k, lge2, lge3,
)

from .parameters import (LgP, DeltaT, DeltaP)  # Functions to Make Parameters
```

### Symbols and Sympy Functions <a id="symbols"></a>

There are many variables. Here is a table, in alphabetical order.

| Variable | Symbol | Explanation |
| :--- | :---: | ---: |
| `tau` | $\tau$ | conformal time / distance |
| `tau0` | $\tau\_0$ | current conformal time |
| `mu` | $\mu$ | angle |
| `l` | $\ell$ | Legendre $\ell$ |
| `k` | $k$ | vector |
| `dummyL` | $\ell$ | dummy Legendre $\ell$ |
| `dummyO` | $\mathcal{O}$ | dummy Taylor expansion order |
| `tauc` | $\tau\_C\(\tau\)$ | inverse of Thompson scatter rate |
| `kappa` | $\kappa\(\tau\)$ | Thompson scattering |
| `dkappa` | $\dot{\kappa}\(\tau\)$ | Thompson scattering rate |
| `a` | $a\(\tau\)$ | scale factor |
| `R` | $R\(\tau\)$ | $\frac{3\rho_b}{4\rho_\gamma}$ |
| `Psi`, `Phi` | $\Psi$, $\Phi$ | Bardeen potential |
| `DT` | $\Delta\_T$ | temperature fluctuation |
| `DP` | $\Delta\_P$ | Polarization fluctuation |
| `Sx` | $S\_{TP}\(\tau\)$ | $\Delta_{T2} + \Delta_{P2} - \Delta\_{P0}$ |

#### Variable Details

Many of the variables have both order expansions in powers of `tauc` as well as multipole expansions in `l`. Additionally, many variables are implicitly functions of `tau`. In order to make reading these variables easier, they have been implemented using a custom Sympy function class that overloads the base LaTeX functionality. As example, `a` is $a\(\tau\)$, but will appear as $a$ unless its argument is substituted to another variable \($a\(x\)$ would appear as is\). Similarly, `DT` is $\Delta\_{T,\rm{multipole}}^{\(\rm{order}\)}\(\tau\)$ but shows as $\Delta\_T$ unless the order, multipole or argument are changed. When the order or multipole do NOT appear, it means `DT` for ALL orders and/or multipoles.

Besides overloading the LaTeX functionality, some functions, such as `LgP` and `DP` have custom `.doit()` methods and arguments to prevent their being expanded by their definitions \(see next section\).

#### Dummy Variables

Dummy variables are used in function construction as a stand-in for unspecified values. This is done to protect variables from improper substitutions.

Some of the dummy variables used in this paper are:

* Legendre degree $l$:

  ```text
  dummyL = Symbol(r"\mathcal{\ell}")  # Legendre l
  ```

* Taylor expansion order $\mathcal{O}$:

  ```text
  dummyO = Symbol(r"\mathcal{O}")  # order
  ```

### Relations <a id="relations"></a>

Sympy has powerful symbolic substutitution capabilities. We store relations and particular solutions in dictionaries for fast access and Sympy compatibilty.

\`\`\`{python relations}

rels = { Sx : DT\_a\_2 + DP\_a\_2 - DP\_a\_0, tauc: 1/dkappa

## R :

}

sols = {} \# general solutions

sols\_0 = {} \# 0th order solution sols\_1 = {} \# 1st order solution

## 

```text
## Passing Variables

Storing variables and relations for later chapters.

```{python, echo=T}
vars = {}

# save variables
vars['rels'] = rels
vars['sols'] = sols
vars['sols_0'] = sols_0
vars['sols_1'] = sols_1

with open('src/pickled/01.pkl', 'wb') as file:
    pickle.dump(vars, file)
```

