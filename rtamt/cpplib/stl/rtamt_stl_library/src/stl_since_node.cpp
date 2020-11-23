/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

#include <rtamt_stl_library/stl_since_node.h>
#include <algorithm>
#include <limits>

using namespace stl_library;

// Initialize previous and current value
StlSinceNode::StlSinceNode() {
    prev_out.seq = 0;
    prev_out.time.sec = 0;
    prev_out.time.msec = 0;
    prev_out.value = - std::numeric_limits<double>::infinity();
}

void StlSinceNode::reset() {
    prev_out.seq = 0;
    prev_out.time.sec = 0;
    prev_out.time.msec = 0;
    prev_out.value = - std::numeric_limits<double>::infinity();
}

void StlSinceNode::addNewInput(int i, Sample sample) {
    if (i < 0 || i > 1)
        return;
    
    in[i].seq = sample.seq;
    in[i].time.sec = sample.time.sec;
    in[i].time.msec = sample.time.msec;
    in[i].value = sample.value;
}

void StlSinceNode::addNewInput(Sample left, Sample right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

Sample StlSinceNode::update() {
    Sample out;
    
    out.value = std::min(in[0].value, prev_out.value);
    out.value = std::max(out.value, in[1].value);
    
    prev_out.seq = out.seq;
    prev_out.time.sec = out.time.sec;
    prev_out.time.msec = out.time.msec;
    prev_out.value = out.value;
    
    return out;
}