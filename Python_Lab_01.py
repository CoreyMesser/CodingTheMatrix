class CtMLab01(object):

    def test(self):
        pass

    def task_five(self):
        '''works'''
        {x**2 for x in {1,2,3,4,5}}

    def task_six(self):
        '''works'''
        {x**2**x for x in {0,1,2,3,4,5}}

    def task_exmp_union_intersection(self):
        # | union operator, & intersection operator
        {x*x for x in S | {5,7}}
        {x*x for x in S | {5,7} if x > 2}
        #contional filter
        {x*y for x in {1,2,3} for y in {2,3,4}}

    def task_seven(self):
        '''works'''
        '''
        # Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set.'''

        {x * y for x in {1, 3, 5} for y in {2, 4, 6}}

    def task_exmp_dbl_comprehension_filtered(self):
        '''works'''
        {x*y for x in {1,2,3} for y in {2,3,4} if x != y}

    def task_eight(self):
        '''works but my math is off'''
        '''
        #replace set A & set B with two disjointed 3-element sets so the value becomes a five-element set'''

        {x * y for x in {2, 4, 6} for y in {1, 3, 5} if x != y}

    def task_nine(self, S, T):
        '''works'''
        '''
        # Assume that S and T are assigned sets. Without using the intersection operator &, write a 
        # compre-hension over S whose value is the intersection of S and T'''

        {x for x in S if S == T}

    #A list can contain a set or another list.  a set cannot contain a list since lists are mutable.

    def task_ten(self):
        '''works'''
        '''
        #Write an expression whose value is the average of the elements of the list [20, 10, 15, 75]'''

        average_list = len(li)/sum(li)

    #You can combine the elements in one list with the elements in another list to form a new list (without changing the original lists) using the + operator.
    #>>> [1,2,3]+["my", "word"]

    #You can use sum() on a collection of lists, obtaining the concatenation of all the lists, by providing [] asthe second argument.
    #>>> sum([ [1,2,3], [4,5,6], [7,8,9] ], [])

    def task_eleven(self):
        '''works'''
        '''
        # Write a double list comprehension over the lists [A,B,C] and [1,2,3] whose value is the list of all 
        # possible two-element lists [letter, number].'''

        [[x] + [y] for x in ['A','B','C'] for y in [1,2,3]]

    def task_twelve(self):
        '''Got distracted by sick children and forgot to finish'''

        '''
        #Suppose LofL has been assigned a list whose elements are themselves lists of numbers. Write an expression 
        # that evaluates to the sum of all the numbers in all the lists. The expression has the form sum([sum(...'''

        LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
        [sum(sum([[y] + [x] for y in [x for x in LofL]] for x in LofL))]

    def task_thirteen(self):
        '''This confused me a bit'''

        ''' #Suppose S is a set of integers, e.g. {-4, -2, 1, 2, 5, 0}. Write a triple comprehension whose value is a 
        # list of all three-element tuples (i; j; k) such that i; j; k are elements of S whose sum is zero.'''

        S = {-4, -2, 1, 2, 5, 0}
        (i for (i,j,k) in S if i != 0)

    def task_seventeen(self):
        '''works'''
        list([x for x in range(99) if x %2 != 0])

    def task_eighteen(self):
        '''works'''
        '''
        #Assign to L the list consisting of the rst ve letters ['A','B','C','D','E'] Next, use L in an expression whose
        # value is [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')] Your expression should use a range and a zip,
        # but should not use a comprehension. '''

        list(zip(['A','B','C','D','E'], range(5)))

    def task_nineteen(self):
        '''works'''

        '''Starting from the lists [10, 25, 40] and [1, 15, 20], write a comprehension whose value is the three-element
        list in which the rst element is the sum of 10 and 1, the second is the sum of 25 and 15, and the third is
        the sum of 40 and 20. Your expression should use zip but not list.'''

        [x + y for (x, y) in zip([10, 25, 40], [1, 15, 20])]

    def task_twenty(self):
        ''' should work but doesn't, not sure where i am going wrong.  I can do it outside the
        comprehension but when I put it back in teh comprehension it all goes sideways'''

        '''# Suppose dlist is a list of dictionaries and k is a key that appears in all the dictionaries in dlist. Write a
        # comprehension that evaluates to the list whose ith element is the value corresponding to key
        # k in the ith dictionary in dlist.'''

        dlist = [{'x': 'a', 'y': 'aa'}, {'x': 'b', 'y': 'bb'}, {'x': 'c', 'y': 'cc'}]
        [k['x'] for k in dlist]

        # for k in dlist:
        #     print(k['x'])

    def task_twentyone(self):
        # dlist = [{'x': 'a', 'y': 'aa'}, {'x': 'b', 'y': 'bb'}, {'x': 'c', 'y': 'cc'}]
        # [k['x'] for k in dlist if k in v else 'NOT PRESENT']
        pass




if __name__ == '__main__':
    ctm = CtMLab01()
    ctm.task_twenty()
