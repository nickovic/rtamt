<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-generate-toc again -->
**Table of Contents**

- [Introduction](#intro)
- [Semantic Extension](#semantic)
- [Syntactic Extension](#syntactic)

<!-- markdown-toc end -->


# Introduction

This document gives several examples of how RTAMT library 
can be extended in a way that maximizes reuse of existing code.

# Semantic Extension

In this scenario, we show how to extend classical STL robustness semantic 
to the Interface-Aware STL (IA-STL). We first start by recalling the theory 
behind the IA-STL extension. 

We assume that both STL and IA-STL 
share the same syntax. A formula `phi` is defined over some set of 
variables `X`, where a subset `I` of `X` is declared as input, and 
a subset `O` of `X` are declared as output variables.

Let `phi` be an STL formula defined over `X` and `U` and `V` be disjoint 
(and possibly empty) subsets of `X`. We define relative robustness 
`rho_U_V(phi, w, t)` as a robustness measure that is dependent on 
the sets of variables `U` and `V`. It is defined in the same way 
as the classical robustness `rho(phi, w, t)`, except for the case 
of a predicate:
```
rho_U_V(f(R) > 0, w, t) = 0 if R is not a subset of U union V
                          f(w_R(t)) else if R is not a subset of V
                          sign(f(w_R(t))*inf otherwise
```   

Let `phi` be an STL formula defined over `X`, and `I` and `O` subsets of 
input and output variables. There are four interesting IA-STL interpretations:
- Output robustness - `rho_X\O_O(phi, w, t)`
- Input vacuity - `rho_{}_I(phi, w, t)` 
- Input robustness - `rho_X\I_I(phi, w, t)`
- Output vacuity - `rho_{}_O(phi, w, t)`

It follows that in order to extend STL to IA-STL, one needs in essence to 
extend the way how the predicate is evaluated. We recall that RTAMT implements 
four flavors of RTAMT monitors:
- Discrete-time online
- Discrete-time offline
- Dense-time online, and
- Dense-time offine


The IA-STL extension is orthogonal to these four flavors. We show how 
discrete-time online STL monitors are extended to IA-STL and le