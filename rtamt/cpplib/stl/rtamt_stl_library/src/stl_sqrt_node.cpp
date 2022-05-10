#include <rtamt_stl_library/stl_sqrt_node.h>
#include <algorithm>
#include <limits>
#include <cmath>

using namespace std;
using namespace stl_library;

// Initialize previous and current value
StlSqrtNode::StlSqrtNode() {
}

void StlSqrtNode::reset() {
}

double StlSqrtNode::update(double sample) {
    double out;
    
    out = sqrt(sample);

    return out;
}

