# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------------
#
# TITLE   : Sympy Parameters
# AUTHOR  : Nathaniel Starkman
# PROJECT : Cyborg Math Final Project
#
# ----------------------------------------------------------------------------

"""initialization file for cyborg math final project.

description

Routine Listings
----------------
module

"""

__author__ = "Nathaniel Starkman"

# __all__ = [
#     ""
# ]

##############################################################################
# IMPORTS

# GENERAL

import pickle

import sympy as sp
from sympy import pprint, Symbol, init_printing

from IPython.core.interactiveshell import InteractiveShell


# PROJECT-SPECIFIC

from .parameters import (
    # dummy's
    dummyL,
    dummyO,
    dummyMinus,
    dummyZero,
    dummyPlus,
    legendre_products_constants,
    # variables
    tau,
    tau0,
    mu,
    l,
    k,
    lge2,
    lge3,
)

from .parameters import (
    LgP,
    ScaleFunc,
    RFunc,
    TauCFunc,
    KappaFunc,
    VbFunc,
    PsiFunc,
    PhiFunc,
    DeltaT,
    DeltaP,
    AMFunc,
    APFunc,
    A0Func,
    BMFunc,
    BPFunc,
    B0Func,
)


##############################################################################
# PARAMETERS

i = sp.Symbol("i")  # index

# Legendre
Pl = LgP(l=l)

# scale factor
a = ScaleFunc(tau)

Rt = RFunc(tau)

tauc = TauCFunc(tau)  # 1 / dot(kappa)
tex_tauc = sp.latex(tauc)

kappa = KappaFunc(tau)
dkappa = kappa.diff(tau)


# Vb
Vb = VbFunc(tau)
Vb0 = Vb.subs(dummyO, 0)
Vb1 = Vb.subs(dummyO, 1)
Vb2 = Vb.subs(dummyO, 2)
dVb = Vb.diff(tau)
dVb0 = dVb.subs(dummyO, 0)
dVb1 = dVb.subs(dummyO, 1)
dVb2 = dVb.subs(dummyO, 2)

# Psi
Psi = PsiFunc()
dPsi = Psi.diff(tau)

# Phi
Phi = PhiFunc()
Phi_0 = Phi.subs(dummyO, 0)
Phi_1 = Phi.subs(dummyO, 1)

dPhi = Phi.diff(tau)
dPhi_0 = dPhi.subs(dummyO, 0)
dPhi_1 = dPhi.subs(dummyO, 1)

# ------------------------------------------------------------------------
# DeltaT

DT = DeltaT()
DT_a_0 = DeltaT(l=0)
DT_a_1 = DeltaT(l=1)
DT_a_2 = DeltaT(l=2)
# 0th order
DT_0 = DeltaT(O=0)
DT_0_0 = DeltaT(l=0, O=0)
DT_0_1 = DeltaT(l=1, O=0)
DT_0_2 = DeltaT(l=2, O=0)
DT_0_3 = DeltaT(l=3, O=0)
DT_0_ge3 = DeltaT(l=lge3, O=0)
# 1st order
DT_1 = DeltaT(O=1)
DT_1_0 = DeltaT(l=0, O=1)
DT_1_1 = DeltaT(l=1, O=1)
DT_1_2 = DeltaT(l=2, O=1)
# derivatives
dDT = DT.diff(tau)

tex_DT = sp.latex(DeltaT())
tex_DT_a_0 = sp.latex(DeltaT(l=0))
tex_DT_a_1 = sp.latex(DeltaT(l=1))
tex_DT_a_2 = sp.latex(DeltaT(l=2))
# 0th order
tex_DT_0 = sp.latex(DeltaT(O=0))
tex_DT_0_0 = sp.latex(DeltaT(l=0, O=0))
tex_DT_0_1 = sp.latex(DeltaT(l=1, O=0))
tex_DT_0_2 = sp.latex(DeltaT(l=2, O=0))
# 1st order
tex_DT_1 = sp.latex(DeltaT(O=1))
tex_DT_1_0 = sp.latex(DeltaT(l=0, O=1))
tex_DT_1_1 = sp.latex(DeltaT(l=1, O=1))
tex_DT_1_2 = sp.latex(DeltaT(l=2, O=1))
# derivatives
tex_dDT = sp.latex(DT.diff(tau))

# ------------------------------------------------------------------------
# DeltaP

DP = DeltaP()
DP_a_0 = DeltaP(l=0)
DP_a_1 = DeltaP(l=1)
DP_a_2 = DeltaP(l=2)
# 0th order
DP_0 = DeltaP(O=0)
DP_0_0 = DeltaP(l=0, O=0)
DP_0_1 = DeltaP(l=1, O=0)
DP_0_2 = DeltaP(l=2, O=0)
DP_0_3 = DeltaP(l=3, O=0)
DP_0_ge3 = DeltaP(l=lge3, O=0)
# 1st order
DP_1 = DeltaP(O=1)
DP_1_0 = DeltaP(l=0, O=1)
DP_1_1 = DeltaP(l=1, O=1)
DP_1_2 = DeltaP(l=2, O=1)
# derivatives
dDP = DP.diff(tau)

tex_DP = sp.latex(DeltaP())
tex_DP_a_0 = sp.latex(DeltaP(l=0))
tex_DP_a_1 = sp.latex(DeltaP(l=1))
tex_DP_a_2 = sp.latex(DeltaP(l=2))
# 0th order
tex_DP_0 = sp.latex(DeltaP(O=0))
tex_DP_0_0 = sp.latex(DeltaP(l=0, O=0))
tex_DP_0_1 = sp.latex(DeltaP(l=1, O=0))
tex_DP_0_2 = sp.latex(DeltaP(l=2, O=0))
# 1st order
tex_DP_1 = sp.latex(DeltaP(O=1))
tex_DP_1_0 = sp.latex(DeltaP(l=0, O=1))
tex_DP_1_1 = sp.latex(DeltaP(l=1, O=1))
tex_DP_1_2 = sp.latex(DeltaP(l=2, O=1))
# derivatives
tex_dDP = sp.latex(DP.diff(tau))
# /class


# ------------------------------------------------------------------------

aM = AMFunc()
a0 = A0Func()
aP = APFunc()
bM = BMFunc()
b0 = B0Func()
bP = BPFunc()

# ------------------------------------------------------------------------

Sx = Symbol("S_{TP}")  # DT2 + DP2 - DP0
rels = {Sx: DT_a_2 + DP_a_2 - DP_a_0, tauc: 1 / dkappa}


###############################################################################
# CODE
###############################################################################

init_printing()


##############################################################################
# END
