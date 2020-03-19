# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   : Sympy Parameters
# AUTHOR  : Nathaniel Starkman
# PROJECT : Cyborg Math Final Project
#
# ----------------------------------------------------------------------------

"""Custom Sympy Parameter definitions.

See init for parameter construction.

Routing Listings
----------------
LgP
HiddenTau
ScaleFunc
RFunc
TauCFunc
KappaFunc
HiddenTauAndOrder
VbFunc
PsiFunc
PhiFunc
DeltaClass
DeltaT
DeltaP
AMFunc
A0Func
APFunc
BMFunc
B0Func
BPFunc

"""

__author__ = "Nathaniel Starkman"

__all__ = [
    "dummyL",
    "dummyO",
    "dummyMinus",
    "dummyZero",
    "dummyPlus",
    "legendre_products_constants",
    "tau",
    "tau0",
    "mu",
    "l",
    "k",
    "lge2",
    "lge3",
    "LgP",
    "DeltaT", "DeltaP"
]


###############################################################################
# IMPORTS

# GENERAL

import sympy as sp
from sympy import Function, Symbol
from sympy import legendre

# CUSTOM

# PROJECT-SPECIFIC


###############################################################################
# PARAMETERS

# Dummy Variables
dummyL = Symbol(r"\mathcal{\ell}")  # Legendre l
dummyO = Symbol(r"\mathcal{O}")  # order

dummyMinus = Symbol(r"\mathcal{-}")
dummyZero = Symbol(r"\mathcal{0}")
dummyPlus = Symbol(r"\mathcal{+}")
legendre_products_constants = {"-": dummyMinus, "0": dummyZero, "+": dummyPlus}

# ------------------------------------------------------------------------

# variables
tau = Symbol(r"\tau")  # conformal time / distance
tau0 = Symbol(r"\tau_0")
mu = Symbol("mu")
l = Symbol(r"\ell")  # Legendre l
k = Symbol("k")

lge2 = Symbol(r"\mathcal{\ell} \geq 2")
lge3 = Symbol(r"\mathcal{\ell} \geq 3")


###############################################################################
# CODE
###############################################################################


class LgP(Function):
    """Legendre Polynomial Wrapper.

    Easier to work with in unexpanded form.

    """

    def __new__(cls, l: Symbol = dummyL, x: Symbol = mu, **options):
        """Make new LgP.

        Parameters
        ----------
        l : Symbol
            the ell argument of a Legendre Polynomial
        x : Symbol
            the argument of the function
        options : dict
            idk

        """
        return super().__new__(cls, l, x, **options)

    # /def

    def _latex(self, printer=None):
        L, X = self.args  # values
        l, x = [printer.doprint(i) for i in self.args]
        d = r"\rm{P}_{" + l + "}"
        if X != mu:
            d += r"\hspace{-2.5pt}\left({" + x + r"}\right)"
        return fr"{d}"

    # /def

    # def my_eval(self):
    #     """deprecated."""
    #     L, X = self.args  # values
    #     return legendre(L, X)

    def doit(self, superdeep: bool = False, **hints):
        """Sympy doit.

        Parameters
        ----------
        superdeep : bool
            whether to substitute LgP for Sympy legendre(l, x)
        hints : dict
            standard hints for doit

        """
        L, X = self.args  # values
        if superdeep:
            return legendre(L, X)
        else:
            return self.__class__(l=L, x=X)

    # /def


# /class


# ------------------------------------------------------------------------


class HiddenTau(Function):
    """HiddenTau.

    Implemented as a function to control whether the argument is shown.

    """

    def __new__(cls, t: Symbol = tau, **options):
        """__new__.

        Parameters
        ----------
        t : Symbol
            the time
        options:
            see Sympy Function arguments

        """
        return super().__new__(cls, t, **options)

    # /def

    def _latex(self, printer=None):
        (T,) = self.args  # values
        (t,) = [printer.doprint(i) for i in self.args]
        d = self._symbol
        if T != tau:
            d += r"\hspace{-2.5pt}\left({" + t + r"}\right)"
        return fr"{d}"

    # /def


class ScaleFunc(HiddenTau):
    """Scale Function.

    Implemented as a function to control whether the argument is shown.

    """

    _symbol = r"\rm{a}"


# /class


class RFunc(HiddenTau):
    r"""Baryon Fraction.

    Implemented as a function to control whether the argument is shown.

    .. math::
        \frac{3\rho_b}{4\rho_\gamma}

    """

    _symbol = r"\rm{R}"


# /class


class TauCFunc(HiddenTau):
    r"""Inverse of Thompson Scattering Rate.

    .. math::
            1 / \dot(\kappa)

    """

    _symbol = r"\tau_C"


# /class


class KappaFunc(HiddenTau):
    """Thompson Scattering."""

    _symbol = r"\kappa"


# /class


# ------------------------------------------------------------------------


class HiddenTauAndOrder(Function):
    """HiddenTau.

    Implemented as a function to control whether the argument is shown.

    """

    def __new__(cls, t: Symbol = tau, O: Symbol = dummyO, **options):
        """__new__.

        Parameters
        ----------
        t : Symbol
            the time
        options:
            see Sympy Function arguments

        """
        return super().__new__(cls, t, O, **options)

    # /def

    def _latex(self, printer=None):
        T, O = self.args  # values
        t, o = [printer.doprint(i) for i in self.args]
        d = self._symbol
        if O != dummyO:
            d += r"^{(" + o + r")}"
        if T != tau:
            d += r"\hspace{-2.5pt}\left({" + t + r"}\right)"
        return fr"{d}"

    # /def


class VbFunc(HiddenTauAndOrder):
    """Baryon Velocity."""

    _symbol = r"\rm{V}_{b}"


# /class


class PsiFunc(HiddenTauAndOrder):
    """Psi Gravity from Bardeen Potential."""

    _symbol = r"\Psi"


# /class


class PhiFunc(HiddenTauAndOrder):
    """Phi Gravity from Bardeen Potential."""

    _symbol = r"\Phi"


# /class


###############################################################################


class DeltaClass(Function):
    def __new__(
        cls, t: Symbol = tau, l: Symbol = dummyL, O: Symbol = dummyO, **options
    ):
        return super().__new__(cls, t, l, O, **options)

    def my_eval(self, l=None, fullsub=False, i=l):
        r"""

        \Delta = \sum_{\ell=0}^{\infty}\left((2*\ell + 1)\Delta_{T\ell}\right)

        Parameters
        ----------
        l: int or tuple or Symbol, optional
            if tuple then takes summation from l[0] to l[1]
        """
        T, L, O = self.args  # values

        if l is None:
            return self.__class__(t=T, l=L, O=O)
        if isinstance(l, tuple):
            if fullsub is True:
                return sp.summation(
                    (2 * i + 1)
                    * self.__class__(t=T, l=i, O=O)
                    * LgP(i, mu).my_eval(),
                    (i, l[0], l[1]),
                )
            else:
                return sp.summation(
                    (2 * i + 1) * self.__class__(t=T, l=i, O=O) * LgP(i, mu),
                    (i, l[0], l[1]),
                )
        else:  # it's an int
            if fullsub is True:
                return (
                    (2 * l + 1)
                    * self.__class__(t=T, l=l, O=O)
                    * LgP(l, mu).my_eval()
                )
            else:
                return (2 * l + 1) * self.__class__(t=T, l=l, O=O) * LgP(l, mu)

    # /def

    def doit(self, i=None, superdeep=False, **hints):
        """doit.

        Parameters
        ----------
        superdeep:
            send deep through
        hints : dict

        """
        T, L, O = self.args  # values

        if i is None:
            return self.__class__(t=T, l=L, O=O)
        else:
            if hints.get("deep", True):
                return sp.summation(
                    (2 * i + 1)
                    * self.__class__(t=T, l=i, O=O)
                    * LgP(l=i, x=mu).doit(superdeep=superdeep, **hints),
                    (i, 0, sp.oo),
                )
            else:
                return self.__class__(t=T, l=i, O=O)

    def _latex(self, printer=None):
        T, L, O = self.args  # values
        t, l, o = [printer.doprint(i) for i in self.args]
        d = self._symbol
        if l == r"\mathcal{\ell}":
            d += r"}"
        else:
            d += r"" + l + r"}"
        if O != dummyO:
            d += r"^{(" + o + r")}"
        if T != tau:
            d += r"\hspace{-2.5pt}\left(" + t + r"\right)"
        return fr"{d}"


class DeltaT(DeltaClass):
    """Temperature Anisotropies."""

    _symbol = r"\Delta_{T"


# /class


class DeltaP(DeltaClass):
    """Polarization Anisotropies."""

    _symbol = r"\Delta_{P"


###############################################################################


class LegendreProductsConstants(Function):
    """LegendreProductsConstants."""

    def __new__(
        cls, t: Symbol = tau, l: Symbol = dummyL, **options,
    ):
        """LegendreProductsConstants.

        Parameters
        ----------
        t : Symbol
        l : Symbol

        """
        return super().__new__(cls, t, l, **options)

    # /def

    def _latex(self, printer=None):
        T, L = self.args  # values
        t, l = [printer.doprint(i) for i in self.args]
        d = self._symbol + "_{" + l + "}"
        if T != tau:
            d += r"\hspace{-2.5pt}\left(" + t + r"\right)"
        return fr"{d}"

    # /def


class AMFunc(LegendreProductsConstants):
    """a minus."""

    _symbol = r"a^{-}"


# /class


class A0Func(LegendreProductsConstants):
    """a not."""

    _symbol = r"a^{0}"


# /class


class APFunc(LegendreProductsConstants):
    """a plus."""

    _symbol = r"a^{+}"


# /class


class BMFunc(LegendreProductsConstants):
    """a minus."""

    _symbol = r"b^{-}"


# /class


class B0Func(LegendreProductsConstants):
    """a not."""

    _symbol = r"b^{0}"


# /class


class BPFunc(LegendreProductsConstants):
    """a plus."""

    _symbol = r"b^{+}"


# /class

# ------------------------------------------------------------------------


###############################################################################
# END
