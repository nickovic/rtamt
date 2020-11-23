/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stl_node.h
 * Author: nickovic
 *
 * Created on July 8, 2019, 3:20 PM
 */

#ifndef STL_NODE_H
#define STL_NODE_H

#include <rtamt_stl_library/stl_sample.h>

namespace stl_library {

class StlNode {
    public:
        ~StlNode() {}
        // We update the monitor and compute the next outcome
        virtual Sample update()=0;
    private:
        // We add the new ith input msg
        virtual void addNewInput(int i, Sample msg)=0;

};

} // namespace stl_library


#endif /* STL_NODE_H */

