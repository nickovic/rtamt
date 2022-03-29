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

double StlAbsNode::update(double sample) {
    double out;
    
    out = abs(sample);

    return out;
}

