/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_predicate_node.h>
#include <cmath>

using namespace stl_library;

StlPredicateNode::StlPredicateNode(StlComparisonOperator op) {
    this->op = op;
}

void StlPredicateNode::reset() {
}

void StlPredicateNode::addNewInput(int i, double msg) {
    in[i] = msg;
}

void StlPredicateNode::addNewInput(double left, double right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

double StlPredicateNode::update() {
    double out;
    
    switch(op) {
        case EQUAL:
            out = -std::abs(in[0] - in[1]);
            break;
        case NEQ:
            out = std::abs(in[0] - in[1]);
            break;
        case LEQ:
        case LESS:
            out = in[1] - in[0];
            break;
        case GEQ:
        case GREATER:
            out = in[0] - in[1];
            break;
    }
    
    return out;
}
