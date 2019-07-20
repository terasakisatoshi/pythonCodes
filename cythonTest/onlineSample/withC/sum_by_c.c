#include "sum_by_c.h"

unsigned long long sum_combi(int *xs, int *ys, int lenxs, int lenys){
    unsigned long long total=0;
    for(int i=0;i<lenxs;++i){
        for(int j=0;j<lenys;j++){
            total+=xs[i]+ys[j];
        }
    }
    return total;
}