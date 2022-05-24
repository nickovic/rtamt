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
(and possibly empty) subsets of `X`. Relative robustness `rho_U_V(phi, w, t)` 
is defined inductively    