/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_abs_node.h
 * Author: nickovic
 *
 * Created on August 3, 2019, 5:23 PM
 */

#ifndef STL_ABS_NODE_H
#define STL_ABS_NODE_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlAbsNode : public StlNode {
    private:
        Sample in;
        void addNewInput(int i, Sample msg);
        
        
    public:
        StlAbsNode();
        Sample update();
        void addNewInput(Sample msg);
        void reset();
       
};

} // namespace stl_library

#endif /* STL_ABS_NODE_H */

