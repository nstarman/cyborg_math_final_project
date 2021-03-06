# index

title: "Cyborg Math Final Project" author: "Nathaniel Starkman" date: "`r Sys.Date()`" output: pdf\_document description: We work through the tight-coupling approximation of the early universe. documentclass: book link-citations: yes bibliography:

* book.bib
* packages.bib

  site: bookdown::bookdown\_site

  biblio-style: apalike

## Introduction

This final project focuses on a rederivation of the analytic 0th and 1st order temperature and linear polarization results of @Zaldarriaga1995 in the Tight Coupling Approximation of the Cosmic Microwave Backgrounds.

The Cosmic Microwave Background \(CMB\) can be described many ways but all essentially reduce to tracking the time evolution of small perturbations on a homogenous and isotropic background. Given the scale of the perturbations we can very well approximate the interactions using linear theory. This simplification only breaks down in the later universe when gravitationally bound systems start to form significant structure, such as clusters, galaxies, etc -- all the way down to our very non-linear planet. There is a rich body of literature on the basic $\Lambda$CDM model, knowledge of which will be assumed. For instance, it is assumed that fluctuations are adiabatic, not isothermal; the background is a Gaussian random field; that there are negligible intermediate velocity species which have a distinct equation of state from radiation or cold matter; that there are negligible thermal source terms such as decaying dark matter, etc.

For the purposes of this project we track the temperature anisotropies of the CMB and observe how anisotropic Thompson scattering before and during the epoch of recombination induces polarization in the CMB on a wide range of angular scales.

As a demonstration of Thompson-induced polarization, see the following graphic.

![Image Credit: \[Wayne Hu\]\(http://background.uchicago.edu/~whu/intermediate/Polarization/polar1.html\)](.gitbook/assets/thompson_polarization.gif)

\`\`\`{r setup, echo=FALSE}

knitr::opts\_chunk$set\(echo = TRUE\)

library\(reticulate\) library\(knitr\) opts\_chunk$set\(engine.path = '/Users/nathanielstarkman/miniconda3/bin/python3.7'\)

```text
```{r bib-database, echo=FALSE, include=FALSE}
# automatically create a bib database for R packages
knitr::write_bib(c(
  .packages(), 'bookdown', 'knitr', 'rmarkdown'
), 'packages.bib')
```

