double cfib(int n){
    double a=0.0,b=1.0,tmp;
    for(int i=0;i<n;i++){
        tmp=a;a=a+b;b=tmp;
    }
    return a;
}

