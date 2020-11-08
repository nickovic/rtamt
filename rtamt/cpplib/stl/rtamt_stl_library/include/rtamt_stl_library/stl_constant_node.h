/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_constant.h
 * Author: nickovic
 *
 * Created on August 3, 2019, 5:23 PM
 */

#ifndef STL_CONSTANT_H
#define STL_CONSTANT_H

#include <rtamt_stl_library/stl_sample.h>
#include <rtamt_stl_library/stl_node.h>

namespace stl_library {

class StlConstantNode : public StlNode {
    private:
        double val;
        long time;
        void addNewInput(int i, Sample msg);

        
    public:
        StlConstantNode(double val);
        Sample update();
        void reset();
};

} // namespace stl_library

#endif /* STL_NOT_H */

