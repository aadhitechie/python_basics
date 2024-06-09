#Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25
calc = (5**2 * 5)/1 - 25 + .25
# print(calc)
# print(4 + 6 * 5 )
f = 3 + 1.5 + 4
# print(type(f))

#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
s = 'hello'
# print(s[1])
# #Reverse the string 'hello' using slicing:
# print(s[::-1])
#Given the string hello, give two methods of producing the letter 'o' using indexing

#method 1 :
# print(s[4])
# print(s[-1])
# print(s[4:])
#Build this list [0,0,0] two separate ways.
new_list = []
listt = new_list + [0,0,0]
randoml=[ 0] *3
# print(listt)
# print(randoml)

list3 = [1,2,[3,4,'hello']]
list3[2][2]='good bye'
# print(list3)
list4 = [5,3,4,6,1]
list4.sort()
# print(list4)


#grab the hello
d = {'simple_key':'hello'}
e = {'k1':{'k2':'hello'}}
f = {'k1':[{'nest_key':['this is deep',['hello']]}]}
g = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(g['k1'][2]['k2'][1]['tough'][2])
# print(f['k1'][0]['nest_key'][1])

#set
list5 = 4**0.5 != 2
# print(list5)

l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
res = l_one[2][0] >= l_two[2]['k1']
a = 59
# print(a[1])

