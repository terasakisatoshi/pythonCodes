import random 
import linalg 
from math import ln,sqrt,exp
import times 

const N = 100
const beta:float64 = ln(1+sqrt(2.0))/2

randomize() 

proc makePmOne(i,j:int):float64=
  if random(max=1.0)<0.5:
    return -1
  else:
    return 1

proc ising2dSumOfAdjacentSpins(s:Matrix64[N,N],m,n,i,j:int):int=
    var i_bottom,i_top:int
    var j_right,j_left:int 
    if i+1 < m:
      i_bottom=i+1
    else:
      i_bottom=0
    if i-1 >= 0:
      i_top=i-1
    else:
      i_top=m-1
    if j+1<n:
      j_right=j+1
    else:
      j_right=0
    if j-1>=0:
      j_left=j-1
    else:
      j_left=n-1
    return (s[i_bottom,j]+s[i_top,j]+s[i,j_right]+s[i,j_left]).int

proc ising2dSweep(beta:float64,niters:int):Matrix64[N,N]=
  var s:Matrix64[N,N]=makeMatrix(N,N,makePmOne)
  let m=s.M
  let n=s.N
  var s1:float64
  var k:int
  var start = cpuTime()
  let prob=[exp(-2*beta*(-4)),exp(-2*beta*(-3)),exp(-2*beta*(-2)),exp(-2*beta*(-1)),1,
            exp(-2*beta*(1)),exp(-2*beta*(2)),exp(-2*beta*(3)),exp(-2*beta*(4))]
  for _ in 0..<niters:
    for i in 0..<m:
      for j in 0..<n:
        s1=s[i,j]
        k=s1.int*ising2dSumOfAdjacentSpins(s,m,n,i,j)
        if random(max=1.0)<prob[k+4]:
          s[i,j] = -s1
        else:
          s[i,j] = s1
  var endtime=cpuTime()
  echo "elapsed=",endtime-start
  return s


const niters=1e5.int
if isMainModule:
  discard ising2dSweep(beta,niters)
