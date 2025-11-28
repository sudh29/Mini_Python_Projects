# def temp(timestamp,sessions):
#     for t in timestamp:
#         res=0
#         for i in sessions:
#             if t in range(i[0],i[1]+1):
#                 res+=1
#         print("TimeStamp: {} / Sessions: {}".format(t,res))


# ses=[[1,4], [2,5], [4,7], [3, 8]]
# print(temp([i for i in range(1,9)],ses))

# def temp(timestamp,sessions):
#     res=0
#     sessions.sort()
#     tmin=sessions[0][0]
#     tmax=0
#     for i in sessions:
#         if tmin<=i[1]:
#             res+=1
#         tmax=max(tmax,i[1])
#         print("TimeStamp: {} / Sessions: {}".format(tmin,res))
#         while tmin<tmax:
#             tmin+=1
#             res+=1
#             print("TimeStamp: {} / Sessions: {}".format(tmin,res))


# ses=[[1,4], [2,5], [4,7], [3, 8]]
# print(temp([i for i in range(1,9)],ses))


# # Write a decorator to calculate time taken by the function on which it is applied?
# import time

# def timedec(fun):
#     def wrapper():
#         val=time.time()
#         f=fun()
#         val2=time.time()
#         print("Time:", val2-val)
#         return f
#     return wrapper

# @timedec
# def time_fn():
#     print("Hello")
#     for i in range(500):
#         for j in range(100000):
#             i*j

# time_fn()


# # Write a generator and an iterator to find all the even numbers from an array till the end [1, 100]?

# def gen(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             yield(i)

# def ite(a,b):
#     temp=[]
#     for i in range(a,b+1):
#         if i%2==0:
#             temp.append(i)
#     return temp

# print(gen(1,10))
# print(ite(1,10))


# # what will be the output of the below code?
# # a)   ------------------- Ans
# # test of B called
# # test of C called
# # test of A called
# # b)
# # test of B called
# # test of A called
# # test of C called
# # c)
# # test of B called
# # test of A called
# # d) Error, all the three classes from which D derives has same method test()

# class A:
#     def test(self):
#         print("test of A called")
# class B(A):
#     def test(self):
#         print("test of B called")
#         super().test()
# class C(A):
#     def test(self):
#         print("test of C called")
#         super().test()
# class D(B, C):
#     def test2(self):
#         print("test of D called")
# obj=D()
# obj.test()

# # what will be the output of the below code?
# # a)
# # test of B called
# # test of C called
# # test of A called
# # b)
# # test of B called
# # test of A called
# # test of C called
# # c) ----------------------Ans
# # test of B called
# # test of A called
# # d) Error, all the three classes from which D derives has same method test()

# class A:
#     def test(self):
#         print("test of A called")
# class B(A):
#     def test(self):
#         print("test of B called")
#         super().test()
# class C:
#     def test(self):
#         print("test of C called")
#         super().test()
# class D(B, C):
#     def test2(self):
#         print("test of D called")
# obj=D()
# obj.test()

# # what will be the output of the below code?
# # a) 0 1
# # b) 0 0
# # c) Error because class B inherits A but variable x isn’t inherited -------------------ans
# # d) Error because when object is created, argument must be passed like Derived_Test(1)

# class Test:
#     def __init__(self):
#         self.x = 0
# class Derived_Test(Test):
#     def __init__(self):
#         self.y = 1
# def main():
#     b = Derived_Test()
#     print(b.x,b.y)
# main()

# # what will be the output of the below code?
# # a) Invalid syntax for inheritance
# # b) Error because when object is created, argument must be passed
# # c) Nothing is printed--------------------Ans
# # d) A disp() ---------correct

# class A():
#     def disp(self):
#         print("A disp()")
# class B(A):
#     pass
# obj = B()
# obj.disp()


# # what will be the output of the below code?
# # a) 2 7
# # b) 1 5
# # c) 1 7---------------------ans
# # d) 2 5

# class A:
#      def __init__(self):
#          self.__i = 1
#          self.j = 5

#      def display(self):
#          print(self.__i, self.j)
# class B(A):
#      def __init__(self):
#          super().__init__()
#          self.__i = 2
#          self.j = 7
# c = B()
# c.display()


# # what will be the output of the below code?
# # a) 1
# # b) 0
# # c) Error, invalid syntax for object declaration
# # d) Error, private class member can’t be accessed in a subclass --------------ans

# class A:
#     def __init__(self):
#         self.__x = 1
# class B(A):
#     def display(self):
#         print(self.__x)
# def main():
#     obj = B()
#     obj.display()
# main()
