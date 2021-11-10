###QN 4
"""
Write a programme that takes as input a finite set or list (you may decide) A and a list R where
R is of the form (written mathematically):

R = {(x1, y1),(x2, y2), ...,(xn, yn)}.

Your code should first check if R is a relation on A (that is, if R is a set and if R ⊆ A × A).
If R is not a relation on A, your programme should output a statement to this effect.
If R is a relation on A then your programme should output which of the following properties
the relation satisfies:
a) reflexive,
b) transitive, and/or
c) symmetric.
"""
#Having the user enter list A
#Takes input from user,converts the string into a list
A = input("Enter a list of numbers for A with spaces to differentiate them:")
list_A = A.split()
print("This is your list_A:", list_A)

#-------------------------------------------------------------------------------

# Having the user enter the relation R = {(x1, y1),(x2, y2), ...,(xn, yn)}

list_R = []#Stores the pairs input by the user
print("""Next, enter the relation R, one paired set at a time. 
         After entering a pair, choose Y to add another ordered pair 
         and N if there are no other ordered pairs """)

def accept_paired_items():
 """Function that accepts list_R from the user one pair at a time"""
 global list_R
 pair_item_1 = input("Enter the first value in the pair"
                     "(only enter the first value without any other character eg comma):")
 pair_item_2 = input("Enter your second value in the pair"
                     "(only enter the first value without any other character eg comma):")
 paired_item = [pair_item_1, pair_item_2]
 list_R.append(paired_item)

accept_paired_items()

while True:
 response = input("Do you have another paired item? Y or N?").lower().strip()
 if response == 'y':
   accept_paired_items()
 elif response == 'n':
   print("This is your List_R:", list_R)
   break
 else:
   print("Enter a valid response (Y or N)")
#-------------------------------------------------------------------------------

###Code to check if R is a set, to do cartesian product and check if the list R is a relation on A

# checking if R is a set

off_pairs = []#Stores paired items that make R not be a set
for a in list_R:
 if list_R.count(a) > 1:
   off_pairs.append(a)

if len(off_pairs) == 0:
 print("R is a set")
else:
 print("R is not a set. Ensure there are no repeating pairs.")
 exit()




# checking if the list R is a relation on A
# Cartesian product of A
cartesian_product_A = []
for a in list_A:
 for b in list_A:
     x = [a,b]
     cartesian_product_A.append(x)

#Checking if R is a subset of cartesian product
not_in_CA = []
for pair in list_R:
 if pair not in cartesian_product_A:
   not_in_CA.append(pair)
# print(not_in_CA)

if len(not_in_CA) == 0:
 print("R is a subset of AxA")
 print("R is a relation on A")
else:
 print(f"R is not a subset of AxA because these pairs: {not_in_CA} aren't in AxA.")
 print("R is thus is not a relation on A. The program cannot continue")
 exit()
#----------------------------------------------------------------------------------------------------------------------
####Checking if list_R is reflexive
#have a list of the reflexive pairs based on definition:
# (a, a) ∈ R for every element a ∈ A
reflexive_pairs = []
for a in list_A:
 for b in list_A:
   if a==b:
     reflexive_pairs.append([a,b])
# print(reflexive_pairs)

#Check the reflexive pairs present in R
reflexive_pairs_in_R = []
for pair in list_R:
 if pair[0] == pair[1]:
   reflexive_pairs_in_R.append(pair)
# print(reflexive_pairs_in_R)

#Checking whether R has all the reflexive pairs to determine whether it is reflexive
not_present =[]
failing_factor = []
for pair in reflexive_pairs:
 if pair not in reflexive_pairs_in_R:
   not_present.append(pair)
   failing_factor.append(pair[0])
#Printing out the statement to the user by che
if len(not_present) == 0:
 print("R is Reflexive")
else:
 print(f"R is not Reflexive because the pair(s){not_present} is/are missing")
 print("The value(s) in A that disqualify it is/are",failing_factor,"\n")

#----------------------------------------------------------------------------------------------------------------------
##Checking if R is transive as per the definition whenever (a, b) ∈ R and (b, c) ∈ R,then (a, c) ∈ R, for all a, b, c ∈ A
transitive_elements = []#Stores the corresponding transitive elements
transitive_constructors = []# The two paired elements that give a corresponding transitive element
transitive_constructors_2 = []# The two paired elements plus its corresponding transitive element
for pair in list_R:
   for item in list_R:
       if pair[1] == item[0]: #Checking if the second element in one pair is equal to the first in another so as to create the corresponding transitive element that arises for the two pairs
          a = [pair[0], item[1]]
          transitive_elements.append(a)#Adds them to a list of the corresponding transitive elements
          x = [pair, item]
          transitive_constructors.append(x)
          y = [x,a]
          transitive_constructors_2.append(y)

transitive_elements_not_in_R = [] #Stores those transitive values that ought to be in R but aren't
for x in transitive_elements:
   if x not in list_R:
       transitive_elements_not_in_R.append(x)

transitive_failing_values = []#Holds the values that are making R not be transitive. Stores them as [[a,b],[b,c]]
for a in transitive_elements_not_in_R:
   for b in transitive_constructors_2:
       if a == b[1]:
           transitive_failing_values.append(b[0])


if len(transitive_elements_not_in_R) == 0 and len(transitive_elements) > 0:#if there is no transitive element missing in R, then R is transitive
   print("R is transitive")
elif len(transitive_elements_not_in_R) ==0 and len(transitive_failing_values)==0:
       print("R is not transitive since there are no transitive elements at all.")
else:
    print(f"R is not transitive because paired element(s) {transitive_elements_not_in_R} is/are missing")
    print("The value pairs in A making it not transitive are:",transitive_failing_values)
print("\n")
#----------------------------------------------------------------------------------------------------------------------
#Checking if R is symmetric as per the definition if (b, a) ∈ R whenever (a, b) ∈ R, for all (a, b) ∈ A
symmetric_pairs = []#Stores the corresponding symmetric pair

for item in list_R:
   if item not in reflexive_pairs:#Makes sure that we only look for through pairs that are not reflexive
       p = [item[1], item[0]]
       symmetric_pairs.append(p)
# print(symmetric_pairs)
sym_not_in_R = [] #stores the corresponding symmetric pairs that aren't in R
failing = [] #Stores the specific pairs in R that cause it not to be symmetric
for x in symmetric_pairs:
   if x not in list_R:
     m = [x[1],x[0]]
     sym_not_in_R.append(x)
     failing.append(m)

if len(sym_not_in_R) == 0: #Checks if there is any element that added to the list sym_not_in_R
   print("R is symmetric")
else:
   print("R is not symmetric. The following symmetric pair(s) is/are missing.", sym_not_in_R)
   print("Thus The pair(s) in A that disqualify it is/are", failing)


