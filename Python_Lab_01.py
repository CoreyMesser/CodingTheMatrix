class CtMLab01(object):

    def test(self):
        pass

    def task_five(self):
        {x**2 for x in {1,2,3,4,5}}

    def task_six(self):
        {x**2**x for x in {0,1,2,3,4,5}}

    def task_exmp_union_intersection(self):
        # | union operator, & intersection operator
        {x*x for x in S | {5,7}}
        {x*x for x in S | {5,7} if x > 2}
        #contional filter
        {x*y for x in {1,2,3} for y in {2,3,4}}

    def task_seven(self):
        # Replace {1,2,3} and {2,3,4} with two other three-element sets so that the value becomes a nine-element set.
        {x * y for x in {1, 3, 5} for y in {2, 4, 6}}

    def task_exmp_dbl_comprehension_filtered(self):
        {x*y for x in {1,2,3} for y in {2,3,4} if x != y}

    def task_eight(self):
        #replace set A & set B with two disjointed 3-element sets so the value becomes a five-element set
        {x * y for x in {2, 4, 6} for y in {1, 3, 5} if x != y}

    def task_nine(self, S, T):
        # Assume that S and T are assigned sets. Without using the intersection operator &, write a compre-hension over S whose value is the intersection of S and T
        {x for x in S if S == T}

    #A list can contain a set or another list.  a set cannot contain a list since lists are mutable.

    def task_ten(self):
        #Write an expression whose value is the average of the elements of the list [20, 10, 15, 75]
        average_list = len(li)/sum(li)

    #You can combine the elements in one list with the elements in another list to form a new list (without changing the original lists) using the + operator.
    #>>> [1,2,3]+["my", "word"]

    #You can use sum() on a collection of lists, obtaining the concatenation of all the lists, by providing [] asthe second argument.
    #>>> sum([ [1,2,3], [4,5,6], [7,8,9] ], [])

    def task_eleven(self):
        # Write a double list comprehension over the lists [A,B,C] and [1,2,3] whose value is the list of all possible two-element lists [letter, number].
        [[x] + [y] for x in ['A','B','C'] for y in [1,2,3]]

    def task_twelve(self):
        #Suppose LofL has been assigned a list whose elements are themselves lists of numbers. Write an expression that evaluates to the sum of all the numbers in all the lists. The expression has the form sum([sum(...
        LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
        [sum(sum([[y] + [x] for y in [x for x in LofL]] for x in LofL))]


if __name__ == '__main__':
    ctm = CtMLab01()
    ctm.test()


#  Set comprehensions
# {2*x for x in {1,2,3}}
