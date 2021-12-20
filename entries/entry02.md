# Entry 2
##### 12/19/2021

## Content
Right now me and my partner are going through the official cs50 website watching the video of different weeks. We follow along and tinkered with the codes. We decided that each of us will be tasked a specific week. She focused on doing [<i> Week 7: SQL </i>](https://cs50.harvard.edu/college/2021/fall/weeks/7/) while I focus on [<i> Week 6: Python </i>](https://cs50.harvard.edu/college/2021/fall/weeks/6/). To learn Python more easier, I would often compare it with Java since right now I would say is the coding language that I am most used to now. 

### Some [Python Synatx](https://video.cs50.io/mgBpcQRDtl0?start=39) Notes 
#### Variables: 
- have no specifier
- declare with initilization
- ex: `int x = 54 ;` → `x = 54`
- ex 2: `string s = "hello, world";` →  `s = "hello, world"`

#### Conditionals
- In python, when you want to use <b>and</b> or <b>or</b>, instead of using the symbols && or ||, you just use the actual word. The `!` is also replaced by the actual word <b>not</b>.
- ex: `if (y < 43 || z == 15){ // code}` → `if y < 43 or z == 15: #code`
- ex 2: ` if (y < 43 && z == 15){ // code} else { // code}` → `if y < 43 and z == 15: #code else: #code `
- the `else if` in Java is replaced by `elif`

#### Loops
- use `+= 1` for `++`
- like Java it has a WHILE and FOR loop
- While loops looks pretty similar to Java while loops: ` while x < 100: print (counter) counter +=1`
- For loops, you have to add <b> in range</b> : `for x in range (100): print (x)`. Another for loop exmaple is: `for x in range (0, 100, 2): print (x)` which has a increment by 2

#### Arrays / List
- not fix in size
- can add, splice, remove thing easily
- declare a list with [] : `nums = []`
- list comprehension - using for loops inside a list to generate the list: `nums = [x for x in range(500)]` → the nums list has 500 elements from 0 - 499
- `.append()` add to the list
- ex: `nums = [1, 2, 3, 4] nums.append(5)` attach 5 to the end of the list
- `.insert (x, y)` where x is the index and y is what we put into that index
- ex: `nums.insert(4,5)` is the same as `nums.append(5)`

#### Tuples (a new data type)
- are ordered, immutable set of data
- great with associating collections of data
- fast to navigate
- ex: ` ("December", 12)`
- ex 2: List of tuples 
``` 
presidents = [
  ("George Washington", 1789),
  ("John Adams", 1797),
  ("George Washington", 1801),
  ("George Washington", 1809)
]
```
#### Dictionaries (also new)
- allow user to specify list indices or phrases
- python has built in support for dictionaries
- ex: 
``` 
pizzas = {
"cheese" : 9,
"pepperoni" : 10.
"vegetable" : 11,
"buffalo chicken" : 12
}
```
- set a new integer: `pizzas ["cheese" = 8]`
- use in conditions: `if pizza ["vegetables"] < 12: #code`
- add new keys: `pizza ["bacons"] = 14`
- To iterate through dictionaries use for loops: `for pie in pizzas: print (pie)` or `for pie, price in pizzas.items(): pizza (price)` list might not be in the same order but it still has correct assoiations between keys and value

#### Functions
- do not need to specify the return type nor the data type of any parameters
- introduced with `def` keyword
- ex: `def square (x): return x * x`

#### Objects
- use `class` keyword to define the type of object
- requires intilization funcation thats ets starting avles of properities of the object
- in each method `self` should be the first parameter
- ex: 
```
class Student ():
def __int__(self, name, id):
  self:name = name
  self.id = id
def changeID(self, id):
  self.id = id
def print(self):
  print ("{} - {}".format(self.name, self.id))
```
#### Important things to remember for Python
- style is important
- tabs and indentation matters here
- no semicolons

#### files
- import cs50: allows is to call useful cs50 functions like: `cs50.get_int()` or `cs50.get_string()` 

To help me understand python, I just focus of making small changes. For example using the calculator.py example provided I learn how python program would react if user input wrong data type. Also unlike Java, when you divide two number that has remainder, it does not truncates. Instead it just gives us the actual number without doing casting. 

Using the easier version of [problem set 6](https://cs50.harvard.edu/college/2021/fall/psets/6/mario/less/) helped me grasp a better understanding python's for  loops how to control the loop with different values in the parenthesis in python and also the printing since it is somewhat different from Java. 
In this problem, the result shown look like this :
```
   #
  ##
 ###
####
```
This pyramid could be larger or smaller depending on the user's input. My code look like this 
```
from cs50 import get_int

height = get_int("Height: ")
for i in range(0, height, 1):
    for j in range(height-1, height, -1):
        print(" ", end = '')
    for k in range(-1, i, 1):  
        print("#", end = '')
    print ();
```
My code was on the right track since my results were:
```
Height: 4
 #
 ##
 ###
 ####
```
Seeing this, I knew I need to focus on spacing so I decided to tinkered with the -1 in `for j in range(height-1, height, -1):` However no matter if I change it to 1, the sturcture would always look similar the pyramid above. Then I switch to change the height-1 in `for j in range(height-1, height, -1):` but it would awlays result in the same pyramid structure. The only part left to tinker was the middle so  I decided to tinker with the height in `for j in range(height-1, height, -1):`. I switch it to `i`` and it work. My final code looks like:
```
from cs50 import get_int

height = get_int("Height: ")
for i in range(0, height, 1):
    for j in range(height-1,i, -1):
        print(" ", end = '')
    for k in range(-1, i, 1):  
        print("#", end = '')
    print ();
    
```

## Engineering Design Process
I would say I am currently at step 4 of the Engineering Design Process -- <b>Plan the most promising solution</b>. Having decided to make my project using python, I needed to learn the coding language which the cs50 course helped. In the beginning I want to use python because it is way simpler to comprehend than other coding languages and that there were no semicolon which means less syntax errors. However, one con I notice was how much more important indenatation has become. If you did not ident right, it would cause a indentation error. But these are usually easier to solve. 

My next step would be to exchange the info with my partner. During the upcoming winter break, I want to solve problem set 6, the [harder version](https://cs50.harvard.edu/college/2021/fall/psets/6/mario/more/). I think this will further my understanding of python. 

## Skills
The skills I used so far is <b>Logical Reasoning</b> and <b>How to learn</b>.

I used my  <b>Logical Reasoning</b> skills during the mario coding activity. As I learn more languaged, I realized the important of Pseudocode: writing the code in english first and then turning into coding language. To made sure, that I get the spaces and when to put the # correctly, I have to logically find a pattern and follow it. If it was not spaces then it would be the #. Turning the solution to the problem  in english help me better logically comprehend my solution.

I used my  <b>How to learn</b> skills when learning the actual python language. Since I am the most versed in Java, I would often compare python to Java so I have a way to connect what I am learning to what I already know. For the new data types, I made sure to know what they are used for and how. I also made sure to watch video of python syntax where I learn the importance of style and indentation is to when compiling python.

[Previous](entry01.md) | [Next](entry03.md)

[Home](../README.md)
