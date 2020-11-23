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

void StlAbsNode::addNewInput(int i, Sample sample) {
    if (i != 0)
        return;
    
    in.seq = sample.seq;
    in.time.sec = sample.time.sec;
    in.time.msec = sample.time.msec;
    in.value = sample.value;
}

void StlAbsNode::addNewInput(Sample sample) {
    addNewInput(0,sample);
}

Sample StlAbsNode::update() {
    Sample out;
    
    out.seq = in.seq;
    out.time.msec = in.time.msec;
    out.time.sec = in.time.sec;
    out.value = abs(in.value);

    return out;
}

