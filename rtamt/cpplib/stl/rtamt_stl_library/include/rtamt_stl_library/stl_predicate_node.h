/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_predicate_node.h
 * Author: nickovic
 *
 * Created on July 8, 2019, 3:27 PM
 */

#ifndef STL_PREDICATE_NODE_H
#define STL_PREDICATE_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>
#include <rtamt_stl_library/stl_comp_op.h>
#include <rtamt_stl_library/stl_io_type.h>

namespace stl_library {

class StlPredicateNode : public StlNode {
    private:
        StlComparisonOperator op;
        double threshold;
        StlIOType io_type;
        
        Sample in;
        
        void addNewInput(int i, Sample msg);
        
        
        
    public:
        StlPredicateNode(StlComparisonOperator op, double threshold, StlIOType io_type);
        Sample update();
        void addNewInput(Sample msg);
};

} // namespace stl_library

#endif /* STL_PREDICATE_NODE_H */

