using Formatting

function scratchmax(arr)
    max_value=arr[1]
    for a in arr
        if max_value < a
            max_value=a
        end
    end 
    return max_value

end

function main()
    N=100000000
    arr=[x for x in 0:N-1]
    @time maximum(arr)
    @time max_value=scratchmax(arr)
    printfmt("max value of the array is {}\n", max_value)
end

main()
