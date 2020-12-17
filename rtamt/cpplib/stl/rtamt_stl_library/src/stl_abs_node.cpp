/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_abs_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace std;
using namespace stl_library;

// Initialize previous and current value
StlAbsNode::StlAbsNode() {
}

void StlAbsNode::reset() {
}

void StlAbsNode::addNewInput(int i, double sample) {
    if (i != 0)
        return;
    
    in = sample;
}

void StlAbsNode::addNewInput(double sample) {
    addNewInput(0,sample);
}

double StlAbsNode::update() {
    double out;
    
    out = abs(in);

    return out;
}

