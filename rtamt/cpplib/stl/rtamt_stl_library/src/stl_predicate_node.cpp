/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_predicate_node.h>
#include <cmath>

using namespace stl_library;

StlPredicateNode::StlPredicateNode(StlComparisonOperator op, double threshold, StlIOType io_type) {
    this->op = op;
    this->threshold = threshold;
    this->io_type = io_type;
}

void StlPredicateNode::addNewInput(int i, Sample msg) {
    if (i!=0) {
        return;
    }
    
    in.seq = msg.seq;
    in.time.msec = msg.time.msec;
    in.time.sec = msg.time.sec;
    in.value = msg.value;
}

void StlPredicateNode::addNewInput(Sample msg) {
    addNewInput(0, msg);
}

Sample StlPredicateNode::update() {
    Sample out;
    
    out.seq = in.seq;
    out.time.msec = out.time.msec;
    out.time.sec = out.time.sec;
    
    switch(op) {
        case EQUAL:
            out.value = -std::abs(in.value - threshold);
            break;
        case NEQ:
            out.value = std::abs(in.value - threshold);
            break;
        case LEQ:
        case LESS:
            out.value = threshold - in.value;
            break;
        case GEQ:
        case GREATER:
            out.value = in.value - threshold;
            break;
    }
    
    return out;
}
