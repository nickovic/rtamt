/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_constant_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlConstantNode::StlConstantNode(double val) {
    this->val = val;
    this->time = 0;
}

void StlConstantNode::reset() {
    this->time = 0;
}

void StlConstantNode::addNewInput(int i, Sample sample) {
        return;
}


Sample StlConstantNode::update() {
    Sample out;
    
    out.seq = this->time;
    out.value = this->val;
    this->time = this->time + 1;
    
    return out;
}

