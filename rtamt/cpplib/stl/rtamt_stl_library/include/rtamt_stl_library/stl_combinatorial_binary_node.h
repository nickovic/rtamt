/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_combinatorial_binary_node.h
 * Author: nickovic
 *
 * Created on August 5, 2019, 11:31 AM
 */

#ifndef STL_COMBINATORIAL_BINARY_NODE_H
#define STL_COMBINATORIAL_BINARY_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlCombinatorialBinaryNode : public StlNode {
    protected:
        StlOperatorType type;
        Sample in[2];
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlCombinatorialBinaryNode(StlOperatorType type);
        Sample update();
        void addNewInput(Sample left, Sample right);
        void reset();
};

} // namespace stl_library

#endif /* STL_COMBINATORIAL_BINARY_NODE_H */

