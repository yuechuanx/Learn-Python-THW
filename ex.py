# ex-1 print()语句
"""
You should have spent a good amount of time in Exercise 0 learning how to install a text editor, run the text editor, run the terminal, and work with both of them. If you haven't done that, then do not go on. You will not have a good time. This is the only time I'll start an exercise with a warning that you should not skip or get ahead of yourself.

Type the following text into a single file named ex1.py. Python works best with files ending in .py.
"""
print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
print("I'd much rather you 'not'.")
print('I "said" do not touch this.')
# Hello World!
# Hello Again
# I like typing this.
# This is fun.
# Yay! Printing.
# I'd much rather you 'not'.
# I "said" do not touch this.
#---------------------------------------------------------------------_


# ex-2  comment的使用
# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.
print("I could have code like this.") # and the comment after is ignored
# You can also use a comment to "disable" or comment out a piece of code:
# print("This won't run.")
print("This will run.")
#---------------------------------------------------------------------_

# ex-3 数据类型
print("I will now count my chickens:")
# 整型的四则运算
print("Hens", 25 + 30 / 6)              # Hens 30.0
print("Roosters", 100 - 25 * 3 % 4)     # Roosters 97
print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)    # 6.75
# bool型 >, <, >=, <=判断
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)            # False
print("What is 3 + 2?", 3 + 2)    # What is 3 + 2? 5
print("What is 5 - 7?", 5 - 7)      # What is 5 - 7? -2
print("Oh, that's why it's False.")
print("How about some more.")
print("Is it greater?", 5 > -2)     # Is it greater? True
print("Is it greater or equal?", 5 >= -2) # Is it greater or equal? True
print("Is it less or equal?", 5 <= -2) # Is it less or equal? False
#---------------------------------------------------------------------_


# ex-4 变量运算
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
# There are 100 cars available.
# There are only 30 drivers available.
# There will be 70 empty cars today.
# We can transport 120.0 people today.
# We have 90 to carpool today.
# We need to put about 3.0 in each car.
#---------------------------------------------------------------------_

# ex-5 More Variables and Printing
"""
Now we'll do even more typing of variables and printing them out.
This time we'll use something called a "format string." Every time you put " (double-quotes) around a piece of text you have been making a string. A string is how you make something that your program might give to a human. You print strings, save strings to files, send strings to web servers, and many other things.

Strings are really handy, so in this exercise you will learn how to make strings that have variables embedded in them.You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters. You also must start the string with the letter f for "format", as in f"Hello {somevar}".
This little f before the " (double-quote) and the {} characters tell Python 3, "Hey, this string needs to be formatted. Put these variables in there."
"""
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")
# Let's talk about Zed A. Shaw.
# He's 74 inches tall.
# He's 180 pounds heavy.
# Actually that's not too heavy.
# He's got Blue eyes and Brown hair.
# His teeth are usually White depending on the coffee.

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
# If I add 35, 74, and 180 I get 289.
#---------------------------------------------------------------------_



# ex-6 Strings and Text - 字符串与文本
"""
当你一直在写字符串，你仍然不知道他们在做什么。在这个练习中，我们用复杂的字符串创建了一堆变量，这样你就可以看到它们的作用了。首先是字符串的解释。

字符串通常是一些你想要显示给某人的文本，或者是从你正在编写的程序中“导出”出来。Python知道你想要的东西是当你把一个字符串“（双引号）或者'（单引号）中的文本。您与您使用的看到这个多次打印，当你把文字要进去打印后打印字符串的“或”后面的字符串。

字符串可以包含任何数量的Python脚本中的变量。请记住，一个变量是你设置一个名字=（等于）一个值的任何代码行。在本练习的代码中，types_of_people = 10会创建一个名为types_of_people的变量，并将其设置为=（等于）10。你可以用{types_of_people}把它放在任何字符串中。你也看到我必须使用特殊类型的字符串来“格式”; 它被称为“f-字符串”，看起来像这样：

f“这里有些东西{avariable}”
f“其他东西{anothervar}”
Python 也有另一种使用在第17行上看到的.format（）语法的格式。当我想要将格式应用于已经创建的字符串时，例如在循环中，您会看到我使用该格式。我们稍后再介绍。

现在我们将输入大量的字符串，变量和格式，并打印出来。您还将练习使用简短的缩写变量名称。程序员喜欢使用烦人的简短和晦涩的变量名称来节省时间，所以让我们开始阅读并尽早写出它们。
"""
# left out assignment for types_of_people mentioned in intro
types_of_people = 10
# change variable from 10 to types_of_people
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

# left out f in front of string and omit extra period
print(f"I said: {x}")
# left out f in front of string and omit extra period
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# change "What You Should See" snapshot to reflect changes



# ex-7
"""

"""
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end.  try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
# Mary had a little lamb.
# Its fleece was white as snow.
# And everywhere that Mary went.
# ..........
# Cheese Burger



# ex-8
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
# 1 2 3 4
# one two three four
# True False False True
# {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {}
# I had this thing. That you could type up right. But it didn't sing. So I said goodnight.




# ex-9
# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
# Here are the days:  Mon Tue Wed Thu Fri Sat Sun
# Here are the months:  Jan
# Feb
# Mar
# Apr
# May
# Jun
# Jul
# Aug
#
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.



# ex-10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
# 	I'm tabbed in.
# I'm split
# on a line.
# I'm \ a \ cat.
#
# I'll do a list:
# 	* Cat food
# 	* Fishies
# 	* Catnip
# 	* Grass



# ex-11
