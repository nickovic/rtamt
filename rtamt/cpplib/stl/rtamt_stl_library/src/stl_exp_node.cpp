#include <rtamt_stl_library/stl_exp_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace std;
using namespace stl_library;

// Initialize previous and current value
StlExpNode::StlExpNode() {
}

void StlExpNode::reset() {
}

double StlExpNode::update(double sample) {
    double out;
    
    out = exp(sample);

    return out;
}

