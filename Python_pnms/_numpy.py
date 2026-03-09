import numpy as np

print(np.__version__)



# ---------------------------------


#Normal Py
my_list = [ 1, 2, 3, 4]
my_list = my_list *2    #duplicate the elm -> [ 1 2 3 4 1 2 3 4]
print(my_list)


#Num Py

list = np.array( [ 1 , 2, 3, 4] )

list = list * 2    #[elm*2 ,..] -> VECTORIZED Calculation

print(list)

print(type(list))  #np.array  -> not normal arr


# ---------------------------------------------


# Multidimensional Array

arr0 = np.array(1)            # Single point = 0D arr

arr1 = np.array([1 ,2 ,3])    # x   = 1D arr
arr1 = np.array([1])         

#num of dimension = .ndim
print(arr0.ndim,"D"," and " ,  arr1.ndim ,"D")


arr2 = np.array([ ['a' ,'b' ,'c'],   
                  ['e','f' , 'g'],
                  ['e','f' , 'g'] ])   # x,y = 2D arr/matrix

print(arr2.ndim ,"D")       


arr3 = np.array([ [ [1,2,3] ,[1,2,3] ,[1,2,3] ],
                  [ [1,2,3] ,[1,2,3], [1,2,3] ],
                  [ [1,2,3] ,[1,2,3] ,[1,2,3] ]   # x,y,z = 3D arr
                 ])
print(arr3.ndim ,'D')                       # 4d ,  5d ...



print(arr3.size)   # gives tuple -> ( depth x  no_of_rows x no_of_col ) 



arr = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]  
                ])


# CHAIN INDEXING
print("1st letter = " , arr[0][0][0]) # A

#MULTI-D INDEXING
print(arr[0,0,0])      # A
print(arr[0,0,1])      # B
print(arr[0,0,2])      # C

print(arr[1,1,1])    # centre = N

# print(arr[0,0,3])     ->  OUT OF INDEX


#Create 4 letter word by indexing
word = arr[0,0,2] + arr[1,1,2] + arr[1,1,0] + arr[0,1,1]
#         C               O           M            E
print(word)



# -------------------------------------------------------


# SLICING  -  array [ start : end+1 : step ] 
        

array2 = np.array([[1, 2 , 3 , 4], 
                   [5 , 6 , 7 ,8 ], 
                   [9 , 10, 11 ,12] , 
                   [13 , 14, 15 ,16]])

print(  array2[0],      # 1st []
      
        array2[0:4],
        array2[-4:0],     # all

        array2[0:3],
        array2[-4:-1],    # 1st three [ ]

        array2[1:3],
        array2[-3:0],    # last three []

        array2[0: 4 : 2],     
        array2[ : : 2],     #skip 2 , 4 [ ] line = step 2

        array2[ : : -1],    # reverse the print_arr 

        array2[ : : -2]     # reverse arr -> skips the 2nd and 4th [ ] == [9 10 11 12] and [1 2 3 4] skipped
)


print( #    arr[ row , col]
        array2 [ 0:4 , 0 ],  # print all 1st elm of  [ ] = [1] [5] [9] [13]
     #      arr[ :   , 0]

        array2 [ 0:4 , 1 ],  # print all 2nd elm of  [ ] = [2] [6] [10] [14]

        array2 [ 0:4 , 0:3 ],  # print all 1->3rd  elm of  [ ] = [1 2 3  ] [5 6 7  ] [9 10 11  ] [13 14 15  ]

        array2 [ : , 1: ],     # print all 2->4th  elm of  [ ] = [  2 3 4] [  6 7 8] [  10 11 12] [  14 15 16]

        array2 [ : , ::2 ],     # print all 1st and 3rd only elm of  [ ] =[1   3  ] [5   7  ] [9   11  ] [13   15  ]

        array2 [ : , 1::2 ],     # print all 2nd and 4th only elm of  [ ] =[  2   4] [  6   8] [  10    12] [  14   16]

        array2 [ : , ::-1 ],     # print all  the [ ] but in each [] elm be reversed = [4 3 2 1] [8 7 6 5] [12 11 10 9] [16 15 14 13]

        array2 [ ::-1 , ::-1 ],     # print all  [] in reversed and elm in each [] be reversed = [[16 15 14 13] [12 11 10  9] [ 8  7  6  5] [ 4  3  2  1]]

        array2 [ 0:2 , 0:2 ],     # print 1st two [] , in which 1st two elm only = [1 2    ] [5 6    ] [9 10     ] [13 14     ]

        array2 [ 0:2 , 2:4 ],     # print 1st two [] , in which last two elm only = [    3 4] [    7 8]

)


# ====================================================

# Scalar Arithematic - Scalar means single value term , and arithematic applied by single value term is 

array = np.array([1,2,3])

print(
  
   array + 1 ,  # add 1 in each elm of  [ ] = [2,3,4]
   array - 2 ,  # minus 2 from each elm of  [ ] = [-1  0  1]
   array * 3,   # [ 1x3 , 2x3, 3x3]
   array / 4 ,   # divide each elm in [ ] by 4
   array ** 5,    # a^5 for each a elm in [ ]
   array // 6    # int remainder of a/6 for each a in [ ]
  )
  
  # --------------------------------------------------------------
  
  
  # Vectorized math func
  
array = np.array([1.32,2.43,3.94])

print(
  
     np.sqrt(array), # make the elm [ a x a , b x b ,  cx c]
     np.round(array),  # rond off the elm in [ ]
     np.floor(array),   # round down the elm
     np.ceil(array),     # round up the elm
     np.pi,             # return pi value 3.14...
  )
  
  
#Exsercise - find the area arr from the ridias array given
  
radii = np.array([1 ,2 ,3])
  
area = np.pi * np.sqrt(radii)  # or np.pi* array**2 -> Scalar way

roundoff_area = np.floor(area)

print(roundoff_area)


# --------------------------------------------------------------

# Element-wise arithematic - where we have 2 array , and Each operation is applied by elm btw 2 arrays
#                          -  Similarly like Matrix operation

array1 = np.array([1 ,2 ,3])
array2 = np.array([4,5,6])

print(
        array1 + array2,  #[ 1+4 ,2+5, 3+6]
        array1 - array2,  #[ 4-1 ,5-2, 6-3]
        array1 * array2,  #[ 1x4 ,2x5, 3x6]
        array1 / array2,  #[ 1/4 ,2/5, 3/6]
        array1 ** array2,  #[ 1^4 ,2^5, 3^6]
  )


# ----------------------------------------------------------------

# Comparison operator - gives an Boolean array according to the condition given done by elment wise on each elm of array

score = np.array([54 , 67 ,86 ,55 , 100])

print( 
       score == 100,  # [ F F F F T ]
       score > 60  ,  # [F T T F T]
       score >= 60 ,  # [F T T F T ]
)


score[ score < 60 ] = 0  # anyone who score below 60 , thier score given as 0 as final
print( score )           # [ 0 , 67 ,86 ,0 ,100]


# ========================================================================


# Broadcasting

# Broadcasting allows Numpy to perform operation on arrays 
# with different shapes by virtually expanding dimensions
# so they match the larger arrays shape.

# Condition - for broadcasting operation allowed

# 1. The boths dimensions in shape have same size like - (2 , 2) & (2 , 2) 
# OR 
# 2. One of the dimensions of any2 has a size of 1 like - ( 1 , 4) & (3 , 1) 



# 1. not work for when (2 , 3) ; (2 , 4) - 3 != 4 not applicable for broadcasting

arr1 = np.array([[1,2] , [3,4] ])      # ( 2 ,2)   
                                     #     |  |
arr2 = np.array([[1 ,2 ], [4,5]])  #     ( 2 ,2)

print( arr1.shape , arr2.shape) 

print( arr1 * arr2 ) #( 2 , 2)


#2.  not work if (1 , 2) ; (3 , 3) -> both should have 1 in each resp dimensions

arr1 = np.array([[1,2,3,4]])              #( 1, 4)

arr2 = np.array([[1] ,[2] , [3] , [4]])  # (4 , 1)  -> in bothe the dimension we have 1 allowe

print( arr1.shape , arr2.shape )

print(arr1 * arr2 )   # (4 ,4 )



# Both 1 , 2 => ( 1 ,4 ) * (4 , 4) = ( 4 ,4)

arr1 = np.array([ [1 ,2 ,3, 4 ] ])   # ( 1 ,4)

arr2 = np.array([[1 ,2 ,3, 4] , 
                 [1 ,2 ,3, 4] ,
                 [1 ,2 ,3, 4] ,
                 [1 ,2 ,3, 4] ])   # ( 4 ,4)

print(arr1.shape , arr2.shape) # allowed broadcasting

print( arr1 * arr2 )  # (4 ,4)



#Exercise - create a Multiplication table from 1 to 5

arr1 = np.array([[1,2,3,4,5]])    #(1,5)

arr2 = np.array([[1] , [2] , [3] ,[4] ,[5]])  # (5 ,1)

print(arr1.shape , arr2.shape) # allowed broadcasting by 2 rule

print(arr1 * arr2 )  #( 5 ,5)


# ===========================================================





# Aggregate function = summarize data and typically
#                      return a single value


array = np.array([[1,2,3,4,5],
                 [6,7,8,9,10] ])

print( np.sum(array) ) # summ of elm in array

# in Statictics
print( np.mean(array),  # mean of elm in array , 
       np.std(array),   # standard deviation 
       np.var(array)    # variance = std^2
)

print( np.min(array),   # min elm in array
       np.max(array),   #max elm in array
       
       np.argmin(array),  #gives index/position of min elm
       np.argmax(array),  #gives index/position of max elm
)


print( 
        np.sum(array , axis=0),   # sum elm according to column(X axis / 0 axis)   
        np.sum(array , axis=1),   # sum elm according to rows(Y axis / 1 axis)      

)


#=========================================================================



# Filtering - Refers to the process of selecting elements 
#             from an array that match a given condition


ages = np.array([[21 , 13 ,43 , 18 ,10 ,44 ,87 , 24]
                ,[17  ,29 ,11 ,13 ,15 , 88 , 32 ,44]])

teenagers = ages[ages < 18]
adults = ages [ ages >= 18 ]
seniors = ages[ ages >= 65 ]

print(teenagers ,  adults ,  seniors)

print(ages)  # without changes og data we create sub data teenager,eyc



betw_18_to_65 = ages[ (ages >= 18) & (ages <65)]  # and wont work numpy = c ,use &

above65_below18 = ages[ (ages<18) | (ages >= 65)] # or (no) , | (yes)

print(betw_18_to_65 , above65_below18)



even_ages = ages[ages % 2 == 0]
odd_ages = ages[ ages % 2 != 0]

print(even_ages , odd_ages)


# WHERE( , , ) -> very slow as compared ages[ages >=18]

# If u need to preserve the shape of filered_array as og_array -> WHERE function
# where( CONDITION , ARRAY , replacing_value )  -->  for dont match condition, repace with that value(0/-1/np.NaN)

adults = np.where( ages >= 18 , ages , 0)

print(adults)  # some num replace by 0 , bcz dont fullfill codition
 
print(ages.shape ,"==" ,adults.shape)  #(2, 8) == (2, 8)
#not same shape if we do -> adults = ages[ ages >= 18 ] -> shape = 1D arr != og_arr_shape (2D)


# ====================================================================


# Random Number in numpy



# 1.  INTEGERS :-

rng = np.random.default_rng()   #object files 

# __.default_rng( seed = 1) => get same ans

print(
  
  rng.integers(low = 1 , high = 7 , size = 3),  # give any int from 1-> (7-1) ; if (low , high+1) range is
                                               # size = no_of_random ans u want
                                               
                                               
                                               
  rng.integers( 1 , 7 , size =( 3 , 2) )  # gives arr.shape(3 ,2) => [[1 6], [1 1] ,[4 1]]
  )




# 2. FLOAT :-

# np.random.seed( seed= 1)  => for getting constant anwser

rng_f = np.random.uniform( low =0 ,high =1 ) # random floationg number btw 0 -> 1

rng_f1 = np.random.uniform( low= -1 , high = 1 , size= 2) # gives 2 random_float( size = 2) no from -1 -> 1 any

rng_f2 = np.random.uniform( low =-1 , high = 1 , size =(3 ,2)) # arr = [ [a ,b] ,[c ,d] ,[e ,f]] -> shape(3,2)

print(rng_f , rng_f1 , rng_f2 )  



# =====================================================

# SHUFFLE array  By  Random_INT


array = np.array ( [ 1 , 2 ,3 ,4,5])
print(array)

rng = np.random.default_rng()  # we use int ka random object

rng.shuffle(array)             # and its shuffle function here

print(array)


# ---------------------------

# CHOICE By Random_INT

rng = np.random.default_rng()  # we use int ka random object

abc = np.array([ "a" , "b" , "c" , "d" ,"e"])

abc_random = rng.choice(abc)             # give 1 random letter

abc_random3 = rng.choice(abc , size =3 ) # give 3 random letter

abc_random3x3 = rng.choice(abc , size = (3,3) ) # give arr of shape (3,3) with random letter
                                                # [['a' 'a' 'c'] ,['e' 'b' 'e'],['e' 'b' 'e']]

print(abc_random   , abc_random3  , abc_random3x3)



# ===========================================================

