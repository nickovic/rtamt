/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_iff_node.h
 * Author: nickovic
 *
 * Created on August 5, 2019, 3:09 PM
 */

#ifndef STL_IFF_NODE_H
#define STL_IFF_NODE_H

#include <rtamt_stl_library/stl_combinatorial_binary_node.h>
#include <rtamt_stl_library/stl_operator_type.h>

namespace stl_library {

class StlIffNode : public StlCombinatorialBinaryNode {
    public:
        StlIffNode() : StlCombinatorialBinaryNode(IFF) {}      
};

} // namespace stl_library

#endif /* STL_IFF_NODE_H */

