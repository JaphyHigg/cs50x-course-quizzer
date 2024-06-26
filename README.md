# cs50x-course-quizzer
**Harvard CS50x Course Quizzer**  
A self quiz program to help reinforce what i'm learning.

## To-Do:
- Fill out questions and answers  
- Explore how to not use global variables in this program

## Questions currently included:
#### Week 0 - General + Scratch
1) What is binary?
2) What is a bit?
3) What is a byte?
4) What is ASCII?
5) What is Unicode?
6) What is RGB?
7) What is pseudocode?
8) What is Scratch?
9) What is a conditional?
10) What is an algorithm?
11) What is the difference between a high-level language and a low-level language?

#### Week 1 - C
1) What is a compiler?
2) What are 3 axes that code can be evaluated on?
3) How do you run a program in C?
4) What is the syntax for telling your complier you are using something from another file?
5) What are 3 basic loop types?
6) What are 3 different ways I can increment/decrement a variable by 1?
7) How do you print the main types of variables in CS50x?
8) What is a char?
9) How do you create and/or initialize a variable?
10) What is abstraction?
11) What is truncation?
12) What are 7 common command line commands (aka shell commands) and what do they do?
13) Explain the syntax and convention around comments.
14) What are the common data types used in this course?
15) What is integer overflow?
16) What is floating point imprecision?
17) How much memory is available to an integer?
18) What does the main function represent?
19) What is the difference between a for loop and a while loop?
20) By style convention, where should your main function be located?
21) What is a double? How much memory can it use?
22) What do you need to do if you define a function but your main function calls it before the definition appears in your code?
23) If you have a switch statement conditional, what happens if you don't 'break;' at the end of a case?
24) What is a ternary operator?

#### Week 2 - Arrays
1) Beyond allowing you to run your program with './filename' what does the terminal command 'make' do?
2) Compiling (with clang) is just one of 4 steps in turning source code in to machine code; what are the 4 steps, in order?
3) What is reverse engineering?
4) What does it mean to debug? What is a debugger?
5) What is a breakpoint?
6) What is an array?
7) What is a string?
8) What happens if you are trying to printf a char thats a letter, but you use the %i format code/specifier instead of %c?
9) How do you access individual elements of an array?
10) What is the difference between a string and a character array?
11) How do you declare and initialize an array?
12) What is the difference between a 1D and a 2D array?
13) How do you declare and initialize a 2D array?
14) What's a helper function?
15) How can I convert a string to all uppercase, or all lowercase?
16) How does C handle array out-of-bounds access?
17) What is a command-line argument?
18) In your main function, what can you replace void with in 'int main(void)'?
19) What happens if you try to access an index of argv that doesn't exist?
20) When accessing the index of an array, can you use negative values? As in array_name[-1], perhaps attempting to get the last value in the array.
21) What is a magic number?
22) What is casting and how do you do it?
23) Can a function in C return multiple values?
24) What is scope?
25) How are variables passed to functions in C, and what impact does this have on the variables' original values?
26) What are garbage values?

#### Week 3 - Algorithms
1) What is an algorithm?
2) What is linear search? How does it work? What time complexity does it have?
3) What is binary search? How does it work? What time complexity does it have?
4) What is the difference between linear search and binary search in terms of efficiency?
5) What is an algorithms' time complexity?
6) What is the difference between O(n) and O(n^2) in terms of time complexity?
7) What is the concept of space complexity?
8) How can you compare if two strings are the same?
9) How does the bubble sort algorithm work? What time complexity does it have?
10) How does the selection sort algorithm work? What time complexity does it have?
11) How does the insertion sort algorithm work? What time complexity does it have?
12) What is the difference between bubble sort, selection sort, and insertion sort in terms of efficiency?
13) What is the concept of a base case in a recursive algorithm?
14) What is a divide and conquer algorithm?
15) How does a merge sort algorithm work? What time complexity does it have?
16) What is a quicksort algorithm? How does it work? What time complexity does it have?
17) What is a struct?
18) What does asymptotically mean?
19) What is recursion?
20) What is runtime?

#### Week 4 - Memory
1) What number system is typically used for computer memory?
2) What is the convention for signaling that a number is in hexadecimal?
3) What is the 'address of' operator? What does it do?
4) What is the 'dereference' operator? What does it do?
5) What is the format code for printing addresses in memory?
6) What is a pointer? What is the syntax for making one?
7) What is the difference * being used during the creation of a pointer, and * being use outside of the creation of a pointer?
8) How much memory does a pointer typically use, traditionally and in modern computers?
9) What is the relationship between a string and a pointer? Why is the null character, \0, important?
10) In the context of pointers and memory, what are strings actually? 
11) What is malloc? How do you use it?
12) What is Valgrind? How do you use it?
13) What does 'free' do and when do you use it?
14) What are garbage values?
15) What does it mean to pass by value (aka pass by copy) and pass by reference? What is the difference?
16) What is the relationship between the stack and the heap?
17) What is heap overflow and stack overflow? Buffer overflow?
18) How can you get user input without using the cs50.h built-in get_... functions?
19) What is a segmentation fault error?
20) Why is scanf dangerous to use with strings?
21) What are some of the common file I/O functions and what do they do?
22) What is a buffer?
23) Why is NULL important when using pointers?
24) Why is hexadecimal (base-16) useful?
25) Why use pointers?
26) Explain the call stack.
27) What is EOF?

#### Week 5 - Data Structures
1) How are stacks and queues different?
2) What is a linked list and how are they structured?
3) What is metadata?
4) Why can't you use binary search on a linked list?
5) What is the time complexity of adding to a linked list? How about searching a linked list?
6) What does a hash map function do?
7) What is a hash table?
8) What are tries, in the context of data structures?
9) Explain the arrow operator.
10) What are the differences between singly linked lists and doubly linked lists?
11) Why is keeping track of the head of a linked list important? Relating to this point, how do you add a new node to the beginning of a linked list? Why would you want to prepend instead of append to a linked list?
12) What makes a good hash function?
13) What is a hash function collision? How do you work around it?

#### Week 6 - Python
1) How does Python differ from C in terms of syntax and usage?
2) What are Python's data types and how do they compare to C's data types?
3) How do you define a function in Python?
4) What is an interpreter? How is this different from a compiler?
5) What are Python modules and how do you import them?
6) What is a method?
7) What is object oriented programming?
8) What does Pythonic mean?
9) What is the Pythonic convention for naming a variable (for a loop) you will not need to use? 
10) What is a named parameter?
11) What is an exception? What is the syntax for using them?
12) What is a list? What is the difference between a list in Python and an array in C?
13) How does a for-else loop work?
14) What is a dictionary in python? How do you make and use one?
15) How do you use list comprehensions in Python?
16) What is the purpose of Python's None keyword?
17) How do you read and write files in Python?
18) What are Python classes and how do you define them?

#### Week 7 - SQL
1) What is SQL?
2) What is a flat-file database?
3) What is CRUD?
4) What is SQLite?
5) What is schema and how do you use it?
6) In a schema call, what does FOREIGN KEY(...) and PRIMARY KEY(...) mean?
7) What are relational databases?
8) In relational databases, what are one-to-one, one-to-many, and many-to-many relationships?
9) How do you create a table?
10) When JOINing tables with one-to-many relationships, why is duplication/repetition of cells ok?
11) What are indexes?
12) What is a B-tree?
13) What is a race condition and how can it be addressed?
14) What is a SQL injection attack?
15) What are Database Management Systems and what are some examples of them?
16) What is an aggregate function?
17) What are the two ways you can combine tables?
18) How does the LIKE keyword work?

#### Week 8 - HTML, CSS, Javascript, and the Internet
1) What are access points? What are some examples of them?
2) What is a packet?
3) What is TCP/IP?
4) What are port numbers?
5) What is DNS? DHCP?
6) What is HTTP?
7) What is curl?
8) What is HTML?
9) [HTML] - What are tags and attributes?
10) [HTML] - What are meta tags?
11) What is an HTML entity? How are they used?
12) [HTML] - What are some things that are generally located in the <head> of an HTML file?
13) What is CSS?
14) What are three different ways CSS can be added to a webpage?
15) [CSS] - What is a class? What is an id? How are they used? How are they different?
16) What is Bootstrap?
17) What is Javascript?
18) What are two different ways Javascript can be added to a webpage?
19) What is an anonymous function?
20) In a broad sense, what are the roles/relationships between HTML, CSS, and Javascript?
21) What is the DOM?
22) What is jQuery?