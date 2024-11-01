import numpy
import numpy as np
from numpy.linalg import norm
x = np.a r ra y ( [ 2 , 2 , 4 , 3 ] , f l o a t )
alpha = 0. 5
A = np . a r ra y ([[2 , −2 ,8 ,0] ,[ −6 , −1 ,0 , −1]] , f l o a t )
c = np . a r ra y ([ −2 , 3 , 0 , 0 ] , f l o a t )
i = 1
while True :
v = x
D = np . diag ( x )
AA = np . dot (A,D)
cc = np . dot (D, c )
I = np . eye ( 4 )
F = np . dot (AA, np . t r a n s p o s e (AA) )
FI = np . l i n a l g . in v (F)
H = np . dot ( np . t r a n s p o s e (AA) , FI )
P = np . s u b t r a c t ( I , np . dot (H, AA) )
cp = np . dot (P, cc )
nu = np . a b s ol u t e ( np . min ( cp ) )
y = np . add ( np . one s ( 4 , f l o a t ) , ( alpha /nu ) ∗ cp )
yy = np . dot (D, y )
x = yy
i f i==1 or i == 2 or i == 3 or i == 4 :
pr int ( " In ␣ i t e r a t i o n ␣␣" , i , "␣we␣ have ␣x␣=␣" , x , "\n" )
i = i + 1
i f norm ( np . s u b t r a c t ( yy , v ) , ord = 2)< 0. 0 0 0 0 1 :
break
pr int ( " In ␣ the ␣ l a s t ␣ i t e r a t i o n ␣␣" , i , "␣␣we␣ have ␣x=␣␣\n" , x )
If we consider minimization problem we will have