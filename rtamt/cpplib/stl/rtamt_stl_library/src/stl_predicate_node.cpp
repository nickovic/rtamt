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

void StlPredicateNode::addNewInput(int i, Sample msg) {
    in[i].seq = msg.seq;
    in[i].time.msec = msg.time.msec;
    in[i].time.sec = msg.time.sec;
    in[i].value = msg.value;
}

void StlPredicateNode::addNewInput(Sample left, Sample right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

Sample StlPredicateNode::update() {
    Sample out;
    
    out.seq = in[0].seq;

    switch(op) {
        case EQUAL:
            out.value = -std::abs(in[0].value - in[1].value);
            break;
        case NEQ:
            out.value = std::abs(in[0].value - in[1].value);
            break;
        case LEQ:
        case LESS:
            out.value = in[1].value - in[0].value;
            break;
        case GEQ:
        case GREATER:
            out.value = in[0].value - in[1].value;
            break;
    }
    
    return out;
}
