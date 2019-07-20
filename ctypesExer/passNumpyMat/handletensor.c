#include"indexing.h"
#include "somecalc.h"

float* handle_tensor(const float* tensor,float* ret){

    for(int i=0;i<P;i++){
        for(int j=0;j<H;j++){
            for(int k=0;k<W;k++){
                ret[at(i,j,k)]+=twice(tensor[at(i,j,k)]);
            }
        }
    }

    for(int i=0;i<P;i++){
        for(int j=0;j<H;j++){
            for(int k=0;k<W;k++){
                ret[at(P+i,j,k)]+=twice(tensor[at(i,j,k)]);
            }
        }
    }

    return ret;
}
