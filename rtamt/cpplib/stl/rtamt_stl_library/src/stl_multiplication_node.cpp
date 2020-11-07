#include <rtamt_stl_library/stl_multiplication_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

StlMultiplicationNode::StlMultiplicationNode() {
}

void StlMultiplicationNode::reset() {
}

void StlMultiplicationNode::addNewInput(int i, Sample sample) {
    if (i > 1 or i < 0)
        return;
    
    in[i].seq = sample.seq;
    in[i].time.sec = sample.time.sec;
    in[i].time.msec = sample.time.msec;
    in[i].value = sample.value;
}

void StlMultiplicationNode::addNewInput(Sample left, Sample right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

Sample StlMultiplicationNode::update() {
    Sample out;
    double val;
    
    val = in[0].value * in[1].value;
 
    out.seq = in[0].seq;
    out.value = val;
   
    return out;
}

