/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_operator_type.h
 * Author: nickovic
 *
 * Created on August 5, 2019, 2:11 PM
 */

#ifndef STL_OPERATOR_TYPE_H
#define STL_OPERATOR_TYPE_H

enum StlOperatorType {
    UNDEFINED,
    PREDICATE,
    NOT,
    OR,
    AND,
    IMPLIES,
    IFF,
    XOR,
    EV,
    ALWAYS,
    UNTIL,
    ONCE,
    HIST,
    SINCE
};

#endif /* STL_OPERATOR_TYPE_H */

