#solve linear equation

#Example1
a=float([0 4 5 2
         1 0 2 -6;
         4 1 0 -2;
         1 7 1 0])::Array{Float64,2}
b=float([9,-3, 1, -3])::Array{Float64,1}
x=float([0, 0, 0, 0])::Array{Float64,1}

function main(a,b,x)
    ori_a=a
    a=hcat(a,b)
    row,col=size(a)
    for j in 1:row
        #search pivot
        maxidx=j-1+indmax(abs.(a[j:end,j]))
        #swap
        a[j,:],a[maxidx,:]=a[maxidx,:],a[j,:]
        #push foward
        for i in j+1:row
            p=-a[i,j]/a[j,j]
            a[i,:]+=p*a[j,:]
        end
    end
    #back foward
    for i in row:-1:1
        x[i]=(a[i,col]-dot(a[i,i+1:row],x[i+1:row]))/a[i,i]
    end
    println("answer=",x)
    println("check ax-b=",ori_a*x-b)
end 

main(a,b,x)