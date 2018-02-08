class CtMLab02(object):

    def problem_one(self, u, v):
        '''For vectors v = [-1; 3] and u = [0; 4], nd the vectors v + u, v - u, and 3v - 2u.'''
        [[b+a, b-a, b**3-a**2] for a in u for b in v]

    def problem_two(self, u, v):
        '''Given the vectors v = [2;-1; 5] and u = [-1; 1; 1], nd the vectors v + u, v - u, 2v - u,
        and v + 2u.'''
        [[b+a, b-a, b**2-a, b+a**2] for a in u for b in v]

    def problem_three(self, u, v):
        pass



if __name__ == '__main__':
    ctm = CtMLab02()
    ctm.problem_one(u, v)
