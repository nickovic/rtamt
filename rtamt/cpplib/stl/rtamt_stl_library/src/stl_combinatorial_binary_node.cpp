#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace stl_library;

// Initialize previous and current value
StlCombinatorialBinaryNode::StlCombinatorialBinaryNode(StlOperatorType type) {
    this->type = type;
    
}

void StlCombinatorialBinaryNode::reset() {
}

void StlCombinatorialBinaryNode::addNewInput(int i, Sample sample) {
    if (i > 1 or i < 0)
        return;
    
    in[i].seq = sample.seq;
    in[i].time.sec = sample.time.sec;
    in[i].time.msec = sample.time.msec;
    in[i].value = sample.value;
}

void StlCombinatorialBinaryNode::addNewInput(Sample left, Sample right) {
    addNewInput(0, left);
    addNewInput(1, right);
}

Sample StlCombinatorialBinaryNode::update() {
    Sample out;
    double val;
    
    switch(type) {
        case AND:
            val = std::min(in[0].value, in[1].value);
            break;
        case OR:
            val = std::max(in[0].value, in[1].value);
            break;
        case IMPLIES:
            val = std::max(-in[0].value, in[1].value);
            break;
        case IFF:
            val = -std::abs(in[0].value - in[1].value);
            break;
        case XOR:
            val = std::abs(in[0].value - in[1].value);
            break;
        default:
            val = nan("");
    }
    
    out.seq = in[0].seq;
    out.value = val;
   
    return out;
}

