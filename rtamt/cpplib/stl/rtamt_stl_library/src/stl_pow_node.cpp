#include <rtamt_stl_library/stl_pow_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace std;
using namespace stl_library;

// Initialize previous and current value
StlPowNode::StlPowNode() {
}

void StlPowNode::reset() {
}

double StlPowNode::update(double base, double exponent) {
    double out;
    
    out = pow(base, exponent);

    return out;
}

