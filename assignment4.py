#Qu1.What exactly is[]?
Ans:The empty list value ,which is a list value that contains no items .It is empty.

#Qu2.In a list of values stored in a variable called spam,how would you assign the value "hello" as the third value?
(Assume [2,4,6,8,10]are in spam.)
Ans:   spam=[2,4,6,8,10]
       spam[3]='hello'
       spam
       [2,4,'hello',6,8,10]

#Qu3.What is the value of spam[int(int('3'*2)/11]?
Ans: spam['a','b','c','d']
     spam[int(int('3'*2)/11]
      'd'

#Qu4.What is the value of spam[-1]?
Ans: spam[:2]
      'd'

#Qu5.What is the value of spam[:2]?
Ans: spam[:2]
     ['a', 'b']

#lets pretend bacon has the list [3.14,'cat',11,'cat',True] for the next three questions.
Qu6.What is the valueof bacon.index('cat')?
Ans: bacon.index('cat')
      1

#Qu7.How does bacon.append(99) change the look of the list value in bacon?
Ans: bacon.append(99)
     bacon
     [3.14,'cat',11,'cat',True,99]

#Qu8.How does bacon.remove('cat') change the look of the list in bacon?
Ans: bacon.remove('cat')
     bacon
     [3.14,'cat',11,True,99]

#QU9.What are the list concentration and list replication operators?
Ans: The operator for list concatenation is +,while the operator for replication is *.

#Qu10.What is the difference between the list methods append() and insert()?
Ans:             append()                                                 insert()
    1.append() will add values only to the        1.insert() can add them anywhere in the list.
      end of a list.

#Qu11.What are two methods for removing items from a list?
Ans: The del statement and the remove() list method are two ways to remove values from a list.

#Qu12.Describe how list values and string values are identical.
Ans:Both lists and strings can be passed to len(),have indexes and slices,be used in for loops ,be concatenated or
       replicated ,and be used with the in and not in operators.

#Qu13.Whats the difference between tuples and list.
Ans:                           tuples                                          list
    1.tuple are immutable .                                     1. lists are mutable .
    2.they cannot be changed at all.                            2.they can have values added ,removed,or changed.
    3.list are written using square pattern []                  3.tuples are written using parenthesis()

#Qu14.How do you type a tuple value that only contains the integer value?
Ans:(42)

#Qu15.How do you get a list values tuple form?How do you get a tuple values list form?
Ans:The tuple() and list() functions,respectively.

#Qu16.Variables that "contain" list values are not necessarily lists themselves.Instead,what do they contain?
Ans: They contain references to list values.

#Qu17.How do you distinguish between copy.copy() and copy.deepcopy()?
Ans:The copy.copy() function will do a shallow copy of a list,while the copy.deepcopy() function will do a deep copy
    of a list.That is ,only copy.deepcopy() will duplicate any list inside list.
