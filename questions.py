week0 = [
[{"question" : "What is binary?",
  "answer" : "Binary is the base-2 numeral system that forms the foundation of computing. It uses only two digits, 0 and 1, to represent any number and encode data. Each digit in binary is called a 'bit', the smallest unit of data in computing, which can either be off (0) or on (1). This system is used because it directly maps to the on and off states of a computer's transistors."}],

[{"question" : "What is a bit?",
  "answer" : "A bit is a 0 (off) or a 1 (on) on a computer. The term comes from binary digit. Computers are made of transistors that are being turned on and off in huge quantities, which represent all types of data."}],

[{"question" : "What is a byte?",
  "answer" : "A byte is 8 bits."}],

[{"question" : "What is ASCII?",
  "answer" : "ASCII (American Standard Code for Information Interchange) is a character encoding standard that was created to map specific letters to specific numbers, so they could be represented on computers. Each character is represented by a number between 0 and 127. For example 'A' is 65 and 'a' is 97."}],

[{"question" : "What is Unicode?",
  "answer" : "Unicode is a computing industry standard designed to encode characters used in written languages around the world. It allows for the use of over a million unique characters (far beyond ASCII's 128). Unicode includes emoji, symbols, and most languages. Unicode is maintained by the Unicode Consortium non-profit organization."}],

[{"question" : "What is RGB?",
  "answer" : "RGB stands for red, green, blue. It is a combination of three numbers used to represent color in computers. RGB values typically range from 0 to 255, and these numbers determine the intensity of the colors red, green, and blue that mix to create a broad spectrum of colors."}],

[{"question" : "What is pseudocode?",
  "answer" : "Pseudocode is human-readable version of your code. It is often written before coding to help you think through the logic of the problems you'll be solving."}],

[{"question" : "What is Scratch?",
  "answer" : "A visual programming language developed by MIT. Aimed at younger audiences or beginners, Scratch aims to help them learn programming concepts through interactive and visual blocks."}],

[{"question" : "What is a conditional?",
  "answer" : "Conditionals are an essential building block of programming, where the program looks to see if a specific condition has been met. If a condition is met, the program does something."}],

[{"question" : "What is an algorithm?",
  "answer" : "An algorithm in computer science is a set of step-by-step instructions or rules to solve a particular problem or accomplish a specific task. It's like a recipe in cooking, providing a detailed guide to reach the desired outcome. Algorithms can be expressed in many forms, including natural languages, pseudocode, flowcharts, and programming languages."}],

[{"question" : "What is the difference between a high-level language and a low-level language?",
  "answer" : "High-level languages are programming languages that are more user-friendly, easier to write, and provide higher abstraction from machine language. They are designed to be more understandable by humans and are closer to natural language.\n\nLow-level languages are closer to the hardware and provide less abstraction from the machine code. They are harder to read and write as they involve more detailed instructions."}]
]

week1 = [
[{"question" : "What is a compiler?",
  "answer" : "A compiler is a piece of software that takes a particular programming language's program code (source code) and turns it into object code (aka machine language, machine code) that a computer's processor uses."}],

[{"question" : "What are 3 axes that code can be evaluated on?",
  "answer" : "1) Correctness - does the code run as intended?\n2) Design - how well is the code designed?\n3) Style - how aesthetically pleasing and consistent is the code?"}],

[{"question" : "How do you run a program in C?",
  "answer" : "1) 'make filename' compiles the code\n2) './filename' runs the code\n[You do not need to include the file extension '.c']"}],

[{"question" : "[C] - What is the syntax for telling your complier you are using something from another file?",
  "answer" : "Put '#include <headerfile.h>' at the top of your file.\nEx: #include <stdio.h>"}],

[{"question" : "[C] - What are 3 basic loop types?",
    "answer" : "1) while\n2) for\n3) do ... while"}],

[{"question" : "[C] - What are 3 different ways I can increment/decrement a variable by 1?",
    "answer" : "1) variable = variable + 1\n2) variable += 1\n3) variable++\n[Replace + with - for decrement]"}], 

[{"question" : "[C] - How do you print the main types of variables in CS50x?",
  "answer" : "Using a the printf function and a placeholder known as a format code.\nEx: printf('%s\\n', string_variable)\nString: %s\nInteger: %d\nLong Integer: %li\nFloat: %f\nDouble: %lf\nChar: %c"}],

[{"question" : "[C] - What is a char?",
  "answer" : "A char is a variable that contains a single character. A char occupies 1 byte of memory. Char can be signed or unsigned, which means it can either range from -128 to 127 (signed char) or from 0 to 255 (unsigned char). When using char with letters, make sure to use single quotes around single letters."}],

[{"question" : "[C] - How do you create and/or initialize a variable?",
  "answer" : "You must first write what data type of variable, and then name it.\nEx: int number;    or    int number, sum;\nThe above examples would create an int variable name number, or two int variables names number and sum.\nYou can create and initialize a variable at the same time.\nEx: int number = 0;"}],

[{"question" : "What is abstraction?",
  "answer" : "Abstraction is the art of simplifying our code such that it deals with smaller and smaller problems. This helps in reducing complexity by hiding details."}],

[{"question" : "What is truncation?",
  "answer" : "Truncation refers to reducing the number digits right of the decimal point. One way this occurs is when you divide integers and the result is not a whole number. Integers cannot have decimals, so whatever would follow the whole number gets cut off (aka truncated) instead of being rounded up or down."}],

[{"question" : "What are 7 common command line commands (aka shell commands) and what do they do?",
  "answer" : "cd: changes our current directory\ncp: copies files and directories\nls: listing files in a directory\nmkdir: make a directory\nmv: move (or rename) files and directories\nrm: remove (delete) files\nrmdir: remove (delete) directories"}],

[{"question" : "[C] - Explain the syntax and convention around comments.",
  "answer" : "The syntax is to write // before your comment.\nConventions in C would be to always leave a space after //, start your comment with a capital letter, leave comments above each function explaining what they do, leave a comment at the start of your file (above any #include) that explains what your program does."}],

[{"question" : "[C] - What are the common data types used in this course?",
  "answer" : "bool: a Boolean expression of either true or false\nchar: a single character like a or 2\nfloat: a floating-point value, or real number with a decimal value\ndouble: a floating-point value with more digits than a float\nint: integers up to a certain size (4,294,967,295) or number of bits\nlong: integers with more bits, so they can count higher than an int\nstring: a string of characters"}],

[{"question" : "What is integer overflow?",
  "answer" : "Integer overflow is a condition that occurs when the result of an arithmetic operation, such as addition or multiplication, exceeds the maximum size that can be stored by the data type of the integer. For example, if you're using an 8-bit unsigned integer, the maximum value it can hold is 255. If you try to store 256 in it, it will overflow and wrap around to 0. This can lead to unexpected behavior in programs if not properly handled."}],

[{"question" : "What is floating point imprecision?",
  "answer" : "Floating point imprecision refers to the fact that some numbers cannot be represented exactly in binary floating point, which is the format computers use to handle decimal numbers. This can lead to small rounding errors. For example, the decimal number 0.1 cannot be represented exactly as a base 2 fraction, resulting in a small error when it's stored as a floating point number. This is why you might see strange results when comparing floating point numbers for equality."}],

[{"question" : "[C] - How much memory is available to an integer?",
  "answer" : "A integer is typically 4 bytes aka 32 bits. A 4-byte integer can store values from -2,147,483,648 to 2,147,483,647 or from 0 to 4,292,967,295."}],

[{"question" : "[C] - What does the main function represent?",
  "answer" : "The main function is the entry point of the program; when you run a C program, execution starts from the main function. The main function must return an int and take either no arguments or two arguments representing the number and values of command-line arguments."}],

[{"question" : "[C] - What is the difference between a for loop and a while loop?",
  "answer" : "A while loop runs until a set condition changes; it has only one part: the condition. A for loop has 3 parts: initialization, condition, and increment/decrement. You typically would use a for loop when you know how many times you want the loop to run."}],

[{"question" : "[C] - By style convention, where should your main function be located?",
  "answer" : "At the top of your file, below any #include and function prototypes."}],

[{"question" : "[C] - What is a double? How much memory can it use?",
  "answer" : "A double in C is a data type that is used to store decimal numbers (real numbers), where the precision is typically double that of a float. It can represent very large (or very small) numbers. The exact amount of memory a double uses can vary, but in most systems, it's 8 bytes (64 bits). This allows it to have a larger range and greater precision than a float."}],

[{"question" : "[C] - What do you need to do if you define a function but your main function calls it before the definition appears in your code?",
  "answer" : "You need to copy the first line of your function (the output + name + arguments) and paste it at the top of your file, below any #include but above the main function. These are called function prototypes or function declarations.\n\nThis is necessary because in C the file is read top to bottom, and the compiler will try to run your function before it knows what it is."}],

[{"question" : "[C] - If you have a switch statement conditional, what happens if you don't 'break;' at the end of a case?",
  "answer" : "You will continue ('fall through') to the next case side-effect. This can be useful in some cases, but can lead to unexpected behavior if not used intentionally."}],

[{"question" : "What is a ternary operator?",
  "answer" : "A conditional format used for writing trivially small conditionals. Also known as '?:'.\nEx: int x = (expression) ? 5 : 6;\nThe above conditional is a shorter way to write\nint x;\nif (expression)\n{\nx = 5;\n}\nelse\n{\nx = 6;\n}"}]
]

week2 = [
[{"question" : "[C] - Beyond allowing you to run your program with './filename' what does the terminal command 'make' do?",
  "answer" : "'make' is running a compiler named clang (or c-lang) for you. By default, using clang will output your compiled code as './a.out' instead of './filename'. What 'make filename' does is run 'clang -o output_filename filename.c' for you. However, if you are including/using a third party library (like <cs50.h>), the terminal command clang needs to be given an additional command line argument to tell the compiled you are using that library. For '#include <cs50.h>' in your file, you would add '-lcs50' (the l is for link or library, then the name of the library). Ex: 'clang -o output_filename filename.c -lcs50'. The 'make' command does all that for you."}],

[{"question" : "[C] - Compiling (with clang) is just one of 4 steps in turning source code in to machine code; what are the 4 steps, in order?",
  "answer" : "1) preprocessing: looks at all the '#include' lines (and a few others), and 'converts' them into all the needed function prototypes referenced in your file\n2) compiling: used as a catch-all phrase for this entire process, but specifically means it takes your code and 'compiles' it in to assembly language\n3) assembling: takes the assembly code and converts it in to machine language (aka binary: 0s and 1s)\n4) linking: takes all the machine language from all files involved (your file + the files referenced as headers) and combines them together in an intelligent way"}],

[{"question" : "What is reverse engineering?",
  "answer" : "Taking machine code (0s and 1s), and de-compiling it to understand what the assembly code or source code was. This is generally a process of interpretation and analysis, not just a straight conversion."}],

[{"question" : "What does it mean to debug? What is a debugger?",
  "answer" : "To debug is to eliminate mistakes in a computers code (bugs). A debugger is a tool (program) that allows you to 'step through' and 'step in' your program to understand what your program is doing exactly at each line. In C, the debugger needs your code to be compiled in order use - it will not help with syntax errors, but it will help with programmatic/logical errors once your code is running."}],

[{"question" : "What is a breakpoint?",
  "answer" : "Used by debuggers, a breakpoint is a (or multiple) location/line in your code that you've picked for the debugger to break/pause while executing your file. Set your breakpoint in your IDE by clicking just to the left of the line number; a mark will appear there. "}],

[{"question" : "[C] - What is an array?",
  "answer" : "An array is a data structure that is made if a sequence of values, back to back to back in memory. A chunk of memory with no gaps, no fragmentation. In C, the length of the array must be set at compile time, or managed dynamically with pointers."}],

[{"question" : "[C] - What is a string?",
  "answer" : "An array of chars. They are 'null terminated', which means they have a char of '\\0' set as the last index of the array, which is a byte of all 0s (aka eight 0 bits, aka NUL), and signals to the computer that that is the end of the string."}],

[{"question" : "[C] - What happens if you are trying to printf a char thats a letter, but you use the %i format code/specifier instead of %c?",
  "answer" : "The printf function will interpret the characters byte value as an integer, putting the ASCII number value of the char instead of the letter into the format code/specifier placeholder. For example, if the character is 'A' and you used %i instead of %c, printf would replace %i with '65', the ASCII value of 'A'."}],

[{"question" : "[C] - How do you access individual elements of an array?",
  "answer" : "Use the syntax 'array[index_number]' where array is the name of the array, and index_number is the zero-based location (index) in the array you'd like to get the value of. For example, if you have an array declared as 'char array[] = {'A', 'B', 'C'}', to access 'B' you would write 'array[1]'.}"}],

[{"question" : "[C] - What is the difference between a string and a character array?",
  "answer" : "A string is always null terminated, while a char array may or may not be. Both are a sequence of chars that are stored consecutively in memory. Without the null termination, functions that process strings may not work on a char array as the function will not know where the array ends."}],

[{"question" : "[C] - How do you declare and initialize an array?",
  "answer" : "datatype array_name[array_size]\nFor example: int grades[3] = {88, 73, 95}; would declare an array named grades which will hold integers and have a length of 3. It has been initialized to have values at 88, 73, and 95 at grades[0], grades[1], and grades[2]."}],

[{"question" : "[C] - What is the difference between a 1D and a 2D array?",
  "answer" : "A 1D (aka one-dimensional) array is an array that has a collection of element accessed by a single index (array_name[n]). A 2D (aka two-dimensional) array is an array of arrays (or a matrix), and requires two indices to access an element (array_name[n][i])."}],

[{"question" : "[C] - How do you declare and initialize a 2D array?",
  "answer" : "To create a 2D array, declare the data type and name, and put the size for both dimensions in square brackets. To initialize a 2D array, follow the definition with initial values for each element enclosed in nested curly braces.\nFor example: int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}}"}],

[{"question" : "What's a helper function?",
  "answer" : "A small function designed to do a specific task and be used by other functions. Using helper functions helps break your problem down in to smaller, manageable pieces, and enhances readability and maintainability of your code."}],

[{"question" : "[C] - How can I convert a string to all uppercase, or all lowercase?",
  "answer" : "By including the <ctype.h> library, and using the toupper(string[index]) or tolower(string[index]) function on each character of the string, while looping through it. You cannot use toupper() or tolower() to convert the entire string at once. Alternatively, for English letters you could take the character you'd like to convert and either subtract 32 to go from lower to upper, or add 32 for upper to lower. This method is using the ASCII values of the characters."}],

[{"question" : "[C] - How does C handle array out-of-bounds access?",
  "answer" : "In C, array out of bound access is not checked or handled automatically. If you try to access or modify an element outside the designated bounds of the array, it results in undefined behavior. This could lead to runtime errors, data corruption, program crashes, or other unpredictable issues."}],

[{"question" : "[C] - What is a command-line argument?",
  "answer" : "Command-line arguments are parameters provided to the program when it is invoked from the command line. These arguments are accessible in the program through argc and argv in the main function, allowing the program to react based on user input from the terminal."}],

[{"question" : "[C] - In your main function, what can you replace void with in 'int main(void)'?",
  "answer" : "'int argc, string argv[]' can be used instead of void.\n'argc' stands for argument count - how many strings does the human type at the prompt. This allows you to do error checks, for example: 'if argc == 2' { do something; } else { handle error; }'. 'argv' stands for argument vector, which is another name for an array. 'string argv[]' means an array of strings. String comes with the <cs50.h> library and is not inherently part of standard C. If not using <cs50.h> or some other library that defines 'string', you would use 'char *argv[]', which mean an array of character pointers, each pointing to a string."}],

[{"question" : "[C] - What happens if you try to access an index of argv that doesn't exist?",
  "answer" : "Trying to access an index of argv that doesn't exist will lead to undefined behavior. In some cases you will get a value of '(null)' (but this is not something you should rely on happening), some cases you will get an unpredictable result, and in other cases your program may crash."}],

[{"question" : "[C] - When accessing the index of an array, can you use negative values? As in array_name[-1], perhaps attempting to get the last value in the array.",
  "answer" : "In C, using negative index numbers is not valid and leads to undefined behavior."}],

[{"question" : "What is a magic number?",
  "answer" : " A magic number refers to hardcoded numbers in source code that may not have an immediately clear meaning on context. They appear arbitrary, can lead to mistakes, and can make your code hard to understand, modify, and maintain, especially if used in multiple places. It's generally considered good practice to avoid magic numbers by using constants or variables with descriptive names instead."}],

[{"question" : "[C] - What is casting and how do you do it?",
  "answer" : "Casting is when you convert a variable or array from one data type in to another. In order to do this, you would define your target variable with the desired new data type, and then initialize it to the value you want to cast, but prepend it with the data type you want to cast it to, surrounded by parenthesis.\nFor example:\nfloat number = (float) my_int"}],

[{"question" : "[C] - Can a function in C return multiple values?",
  "answer" : "A function in C can only return one value directly. You can work around this by using structs or pointers."}],

[{"question" : "What is scope?",
  "answer" : "Scope is the characteristic of a variable that determines where a variable can be accessed within a program. Variables with local scope can only be accessed within the block of code or function in which they were declared. Variables with global scope are declared outside of all functions and can be accessed by any function in the program."}],

[{"question" : "[C] - How are variables passed to functions in C, and what impact does this have on the variables' original values?",
  "answer" : "For the most part, local variables in C are passed by value in function calls. This means the callee receives a copy of the variable, not the variable itself. Therefore the variable in the caller remains unchanged."}],

[{"question" : "What's a garbage value?",
  "answer" : "Garbage values in programming refer to uninitialized variables. When a variable is declared but not assigned a value, it contains random data from memory, which we call a 'garbage value'. Its important to always initialize your variables to avoid unpredictable behavior in your programs."}],
]

week3 = [
[{"question" : "What is an algorithm?",
  "answer" : "An algorithm is a set of well-defined, precise steps designed to accomplish a specific task. Each step in an algorithm must be clear and unambiguous to ensure that it can be systematically followed and applied to a range of similar problems."}],

[{"question" : "What is linear search? How does it work? What time complexity does it have?",
  "answer" : "= Linear search is an algorithm used to find a specific element in an array. It starts at one end of a data set and steps through it one index at a time, examining the element. If the desired element is found, the search stops early. This method can be slow, with a worst case time complexity of O(n). However, its best-case time complexity, Omega, is 1. This means in the worst case scenario it has to look through every element in the array, best case scenario the target element is the first element of the array."}],

[{"question" : "What is binary search? How does it work? What time complexity does it have?",
  "answer" : "Binary search is an algorithm used to find a specific element within a sorted array. It operates by repeatedly dividing the search interval in half. You start with the middle element of the array. If the middle element is equal to the target value, the search is complete. If the target value is less or greater, the half of the array in which the target cannot reside is eliminated, and the search continues on the remaining half, again starting with the middle element. This process repeats until the element is found or the sub-array is reduced to zero size. Binary search cannot be used unless the array is sorted.\n\nBinary search is more efficient than linear search, particularly for large datasets. The best-case time complexity of binary search is Omega(1), which occurs when the target element is found in the middle of the array on the first try. Both the average-case and worst-case time complexities are O(log n), where the search might require logarithmically dividing the array several times until the target is found or until it can be confirmed that the target is not present."}],

[{"question" : "What is the difference between linear search and binary search in terms of efficiency?",
  "answer" : "Binary search is much more efficient than linear search, especially as the data set size increases. You can get equally 'lucky' with linear search or binary search when the target element is the first one checked (giving them both a best case time complexity of Omega(1)), but binary will generally be much faster. Linear search has a worst case time complexity of O(N), requiring on the order of N steps, while binary has a worst case time complexity of O(log(N)), with the process logarithmically reducing the number of elements to check, which dramatically speeds up the search in large datasets."}],

[{"question" : "What is an algorithms' time complexity?",
  "answer" : "Time complexity refers to the computational complexity that describes the amount of time it takes to run an algorithm as a function of the length of the input. It is often expressed as an upper bound, 'O' (Big O notation), representing the maximum steps the algorithm could take in the worst-case scenario. However, time complexity can also be described by the best-case scenario, known as 'Omega' (Big Omega), and the average-case, often described by 'Theta' (Big Theta). This complexity helps in understanding the efficiency of an algorithm, particularly as the size of the input data scales."}],

[{"question" : "What is the difference between O(n) and O(n^2) in terms of time complexity?",
  "answer" : "O(n) time complexity indicates that the performance of an algorithm scales linearly with the size of the input, meaning the execution time increases proportionally as the input size grows. In contrast, O(n^2) time complexity suggests that the execution time increases quadratically, making the algorithm significantly slower for large datasets as the input size doubles, the processing time quadruples."}],

[{"question" : "What is the concept of space complexity?",
  "answer" : "Space complexity measures the total amount of memory an algorithm needs to run relative to the size of its input. It accounts for both the temporary space required during execution and any additional space used for storing input data."}],

[{"question" : "[C] - How can you compare if two strings are the same?",
  "answer" : "In C, you can use the strcmp(string0, string1) function to compare two strings. It returns 0 if the strings are identical and a non-zero value if they differ."}],

[{"question" : "How does the bubble sort algorithm work? What time complexity does it have?",
  "answer" : "Bubble sort steps through an array, comparing pairs of adjacent values one at a time and swapping them if they are in the incorrect order. This continues until the list is sorted. This algorithm is straightforward but can be slow for large datasets. In terms of time complexity, the worst case (Big O) is O(n^2), which can be quite slow. In the best case (Big Omega), where the data is sorted or nearly sorted already, Bubble sort operates faster, with a time complexity on the order of Omega(n)."}],

[{"question" : "How does the selection sort algorithm work? What time complexity does it have?",
  "answer" : "Search the unsorted array (or unsorted part of an array) for the smallest element, then swap that element with the first element of the unsorted part of the array. This repeats, and the sorted part of the array will increase by 1 and the unsorted part of the array will decrease by 1, each pass through until the entire array is sorted. In terms of time complexity, the worst case, best case, and average case would all be O(n^2)."}],

[{"question" : "How does the insertion sort algorithm work? What time complexity does it have?",
  "answer" : "Insertion sort builds the final sorted array gradually, inserting each new element into its proper position among the previously sorted elements. This method is efficient for small or partially sorted datasets with a worst-case time complexity of O(n^2) and a best-case of Omega(n)."}],

[{"question" : "What is the difference between bubble sort, selection sort, and insertion sort in terms of efficiency?",
  "answer" : "All three have O(n^2) as their worst-case time complexity, but insertion sort generally performs better, especially for small or nearly sorted arrays due to fewer required comparisons and shifts."}],

[{"question" : "What is the concept of a base case in a recursive algorithm?",
  "answer" : "A base case is a condition within a recursive function that stops the recursion when met, ensuring the function does not call itself indefinitely."}],

[{"question" : "What is a divide and conquer algorithm?",
  "answer" : "Divide and conquer algorithms split a problem into simpler sub-problems, solve them independently, and combine their solutions. The time complexity varies; for example, mergesort has a consistent O(n log n)."}],

[{"question" : "How does a merge sort algorithm work? What time complexity does it have?",
  "answer" : "Merge sort is implemented using a divide-and-conquer strategy. The algorithm starts by recursively dividing the array into two halves until each segment contains a single element. Once it reaches this level, merge sort begins to combine these segments back together in a sorted order. This merging step is crucial, as it ensures that the smaller sorted arrays are combined into larger sorted arrays until the entire array is sorted. The time complexity of merge sort remains consistent at O(n log n) for all cases—whether worst, average, or best. "}],

[{"question" : "What is a quicksort algorithm? How does it work? What time complexity does it have?",
  "answer" : "Quicksort uses a pivot to partition the array into two sub-arrays, then sorts each recursively. Typically efficient with an average and best-case time complexity of O(n log n), but can degrade to O(n^2) in the worst case."}],

[{"question" : "[C] - What is a struct?",
  "answer" : "A struct is short for structure, and is somewhat like creating your own custom data type to use in your program. It's not a full data type, but it is a way to encapsulate information so you can refer to it with only one name. This new 'type' will hold a collection of other basic types, known as the structure's 'members'."}],

[{"question" : "What does asymptotically mean?",
  "answer" : "Asymptotically refers to the behavior of functions as the input size approaches infinity, commonly used to describe how an algorithm performs under large input sizes. It helps in understanding the limiting behavior of algorithms, especially in terms of their efficiency and scalability."}],

[{"question" : "What is recursion?",
  "answer" : "Recursion is a programming technique where a function calls itself in order to solve a problem. Each time the function calls itself, it attempts to solve a smaller part of the problem, until it reaches a base case which is solvable without further recursion. This base case is crucial because it provides the condition under which the recursive calls can stop, preventing an infinite loop."}],

[{"question" : "What is runtime?",
  "answer" : "In C programming, 'runtime' refers to the period when a program is executing, starting from when it's launched to when it exits. It involves the runtime environment, which includes the operating system, memory management, and runtime libraries that support the program's operation. Runtime also encompasses any errors that occur during execution, such as memory allocation failures or division by zero, which were not detected at compile-time."}]
]

week4 = [
[{"question" : "What number system is typically used for computer memory?",
  "answer" : "Binary (base-2) is the number system that is typically used for computer memory, but hexadecimal (base-16) is often used in programming and debugging to represent memory addresses or binary data because it's a more concise way to interpret binary numbers."}],

[{"question" : "[C] -  What is the convention for signaling that a number is in hexadecimal?",
  "answer" : "Prepend the number with 0x.\nFor example:\n0x500000FA4"}],

[{"question" : "[C] - What is the 'address of' operator? What does it do?",
  "answer" : "The 'address of' operator in C is &, and it returns the memory address of a variable. For example, if int a = 5;, then &a gives the address of a."}],

[{"question" : "[C] - What is the 'dereference' operator? What does it do?",
  "answer" : "Using the * symbol prepended to the front of the variable name being pointed at. This allows the pointer to get the value at the memory address it is pointing to. For example, if you have a pointer 'p' pointing to an integer 'calls', you can use '*p' to get the value of 'calls'."}],

[{"question" : "[C] - What is the format code for printing addresses in memory?",
  "answer" : "The format code for printf-ing addresses in memory is: %p"}],

[{"question" : "[C] - What is a pointer? What is the syntax for making one?",
  "answer" : "A pointer is an address. It is a type of variable (an address/named location in memory) that contains a different address in memory, which it is 'pointing' to. The data type of a pointer matches the data type of the variable it id pointing to. Creating a pointer is similar to creating a regular variable but you need to include a * prepended to the start of the variable name. \nFor example:\nint a = 5;\nint *p = &a;"}],

[{"question" : "[C] - What is the difference * being used during the creation of a pointer, and * being use outside of the creation of a pointer?",
  "answer" : "During the creation of a pointer, the * is used to denote that the variable being declared is a pointer. For example, int *p; declares a pointer p to an integer. Outside of the declaration, * is used as a dereference operator, which accesses the value at the address the pointer is pointing to. For example, if p points to an integer, *p gives you the value of that integer."}],

[{"question" : "[C] - How much memory does a pointer typically use?",
  "answer" : "A pointer typically uses the same amount of memory as the size of an address on a computer, which would be 4 bytes on a 32-bit system, and 8 bytes on a 64-bit system.    "}],

[{"question" : "[C] - What is the relationship between a string and a pointer? Why is the null character, \0, important?",
  "answer" : "In C, a string is essentially represented as a pointer to the first character of an array of characters terminated by a null character (\0). This pointer can be used to access and manipulate elements of the string. For example, if char *str = 'hello';, str points to the 'h' of 'hello', and using pointer arithmetic (e.g., str + 1), we can access subsequent characters."}],

[{"question" : "[C] - In the context of pointers and memory, what are strings actually?",
  "answer" : "Strings in C are arrays of characters stored in contiguous memory locations, terminated by a null character (\0). This null character is crucial as it signifies the end of the string, which helps in operations like printing or copying the string. A pointer to the string points to the first character of this array."}],

[{"question" : "[C] - What is malloc? How do you use it?",
  "answer" : "malloc() is a memory allocator, standard library function in C. It allow you to dynamically get memory. You pass to it a parameter of how many bytes of memory you want, and it will return to you a pointer to that memory. If malloc() can't give you memory (because you've run out), it will return NULL. Instead of pasing a number of bytes, you can pass sizeof(datatype), for example: int *px = malloc(sizeof(int)). When using malloc(), alway remember to free() the memory when you're done so you don't suffer a memory leak. Pass the variable you're no longer using to the free() function, for example: free(px)"}],

[{"question" : "[C] - What is Valgrind? How do you use it?",
  "answer" : "Valgrind is a tool that checks your usage of memory and alert you to any issues it finds. To use valgrind, in your command line type 'valgrind ./filename'"}],

[{"question" : "[C] - What does 'free()' do and when do you use it?",
  "answer" : "It 'frees up' or 'gives back' or de-allocates any memory that was reserved/allocated by 'malloc', 'calloc' or 'realloc'. You need to pass to it what variable you are freeing, as an argument.\nFor example:\nfree(p)."}],

[{"question" : "What are garbage values?",
  "answer" : "Values of variables that you did not actively set yourself as intended. They are default values before a variable has been initialized. They are usually random values and can lead to unpredictable behavior if they are used/"}],

[{"question" : "What does it mean to pass by value (aka pass by copy) and pass by reference? What is the difference?",
  "answer" : "Passing variables to functions by value/copy means you are making a copy of the value held in that variable, which the function will them use. This means the original variable outside the function will remain unchanged. Passing by reference (using pointers) means you are passing in the address in memory of the value. This allows you to access and change (in memory) the original variable's value."}],

[{"question" : "What is the relationship between the stack and the heap?",
  "answer" : "Dynamically allocated memory comes from a pool of memory known as the heap. Generally, anytime you give a variable a name, the memory is coming from a pool of memory know as the stack, and generally anytime you don't give a variable a name, the memory is coming from the heap. The heap and the stack actually are one shared pool of memory, but live in different locations. You can run out of memory if your stack gets too tall, or your heap gets too deep, or if the heap and stack run into each other."}],

[{"question" : "[C] - What is heap overflow and stack overflow? Buffer overflow?",
  "answer" : "Heap overflow occurs when data exceeds the space allocated in the heap, potentially overwriting other important data. Stack overflow happens when too much stack memory is used, typically due to deep or infinite recursion or large allocations. Buffer overflow is when data exceeds the buffer's storage capacity, leading to adjacent memory being overwritten. All these can lead to program crashes or vulnerabilities."}],

[{"question" : "[C] - How can you get user input without using the cs50.h built-in get_... functions?",
  "answer" : "Without using cs50.h functions, you can use standard C functions such as scanf, fgets, or getchar to read user input. For example, fgets(buffer, size, stdin) reads a line from the standard input into the buffer, while scanf('%s', buffer) can be used to read formatted input into the buffer."}],

[{"question" : "[C] - What is a segmentation fault error?",
  "answer" : "A segmentation fault (segfault) error occurs when you 'touch'/access memory that you should not have. This can happen for several reasons, including: when you try accessing the index of an array that is outside its bounds (length), when trying to modify memory that has been marked as 'read-only', or dereferencing a null pointer.  "}],

[{"question" : "[C] - Why is scanf dangerous to use with strings?",
  "answer" : "scanf is dangerous to use with strings because it does not check the bounds of the input, which can lead to buffer overflow if the input exceeds the expected length. This can corrupt memory and lead to security vulnerabilities. For safer input, functions like fgets or specifying maximum field widths in scanf (e.g., scanf('%10s', buffer)) are recommended."}],

[{"question" : "[C] - What are some of the common file I/O functions and what do they do?",
  "answer" : "fopen(<filename>, <mode/operation>): Opens a file for reading/writing. The first argument is the name of the file you want to open, in quotes. The second argument is which mode you are opening the file in, such as 'r' for read, 'w' for write, 'a' for append, or others.\nFor example:\nFILE* ptr = fopen('file.txt', 'r'); \n\nfclose(<file pointer>): Closes a file that the pointer you pass as an argument is located at.\n\nfread(<buffer>, <size (in bytes)>, <qty>, <file pointer>): Reads (copies) data from a file into a buffer, in a set block/chunk size (measured in bytes), for a particular number of blocks. Can look like fread(buffer, 1, 4, f)\n\nfwrite(<buffer>, <size>, <qty>, <file pointer>): Writes data from a buffer to a file.\n\nfgetc(<file pointer>): Gets and returns the next character from the file pointed to.\nFor example:\nchar ch = fgetc(ptr);. The operator/mode of the file pointer passed to fgetc() must be 'r' (read) or an error will occur.\n\nfputc(<char>, <file pointer>): Writes or appends the specified char to the pointed-to file. File pointer must have been fopen()-ed with 'w' (write) or 'a' (append) or an error will occur."}],

[{"question" : "What is a buffer?",
  "answer" : "A buffer is a chunk of memory used to temporarily store some data from a file."}],

[{"question" : "[C] - Why is NULL important when using pointers?",
  "answer" : "A NULL pointer is the simplest pointer- it points to nothing. It is valuable when using pointers, in that you can check if a pointer == NULL, and if it does but you don't expect it to, then that can signal something is wrong. Whenever you create a pointer and don't set it's value immediately, you should set it to NULL. If you try to dereference a NULL pointer, you get a segfault."}],

[{"question" : "Why is hexadecimal (base-16) useful?",
  "answer" : "Hexadecimal allows us to count up to really high numbers using less digits than decimal (base-10). It is also easier to covert between hexadecimal and binary, than it is to convert between decimal and binary. Each hexadecimal digit represents 4 binary digits, making conversions straightforward. Hexadecimal counts like: 1 2 3 4 5 6 7 8 9 A B C D E F 10 11, where, in decimal, a = 10, = 11, c = 12, d = 13, e = 14, f = 15, 10 = 16, 11 = 17. Capitalization does not matter."}],

[{"question" : "[C] - Why use pointers?",
  "answer" : "Pointers allow us to pass by reference in to functions instead of passing by copy. This allows for cleaner code. Pointers also allow the dynamic use of memory; this means instead if deciding on a static amount of memory to use, Programs can scale by 'asking for'/using more memory as needed. This is particularly useful when not knowing in advance how much memory will be needed."}],

[{"question" : "[C] - Explain the call stack.",
  "answer" : "When you call a function, the system sets aside space in memory for that function to do its necessary work. We call such chunks of memory stack frames or function frames. More than one function's stack frame may exist in memory at a given time, and they are arranged in a stack. In general, only the most recent function, the 'active frame', is running at a time. This means the most recently called function is always on top of the stack. When a new frame is called, it is 'pushed' to the top of the stack and becomes the active frame. When a function finishes its work, it 'pops off' of the stack, and the frame immediately below it becomes the new active function and picks up where it left off.."}],

[{"question" : "[C] - What is EOF?",
  "answer" : "EOF is a special value defined in <stdio.h> which is the end of file character. This is useful when using fgetc(), as you can make a conditional that checks if a character you got was the EOF char."}]  
]

week5 = [
[{"question" : "How are stacks and queues different?",
  "answer" : "Queues are first in, first out (FIFO), and items are enqueued or dequeued. Stacks are last in, first out (LIFO), and items are pushed or popped."}],

[{"question" : "What is a linked list and how are they structured?",
  "answer" : "A linked list is a list of nodes, with each node containing data and a pointer. It is a dynamic data structure that can grow or shrink as needed, and unlike arrays the data in a linked list does not need to be stored in contiguous locations in memory. A linked list starts at a pointer that is pointing at the first node. The first node contains a pointer to the second node, and so on. The final node has a pointer that points to NULL, indicating the end of the list. In C, the most common way to build these nodes would be to create a node struct which contains the data and the pointer."}],

[{"question" : "What is metadata?",
  "answer" : "Metadata is data about data. It provides additional context and details about a piece of data or file."}],

[{"question" : "Why can't you use binary search on a linked list?",
  "answer" : "Items in a linked list are not contiguous in memory, so you do not know where the middle of the list is. You cannot use indexing to find the middle."}],

[{"question" : "What is the time complexity of adding to a linked list? How about searching a linked list?",
  "answer" : "Adding to the beginning (prepending) of a linked list has a time complexity of O(1) (constant time), but adding to the end of a linked list (appending) has a time complexity of O(n). Searching a linked list has a time complexity of O(n)."}],

[{"question" : "What does a hash map function do?",
  "answer" : "A hash map function takes some input (key), performs some computation on it, and outputs a number (the hash value) which becomes the inputs location (index) in the array of a hash table. The purpose of this is for efficient retrieval of a value, if given the key associated with it."}],

[{"question" : "What is a hash table?",
  "answer" : "A hash table is populated by data that has been fed to a hash (mapping) function, and been output as a value (a non-negative integer, known as a hash code) that determines its location (index) in the hash table. The hash function maps keys to their associated values. One way to implement a hash table is an array that is populated by pointers which are each the start of a linked list. Insertion, deletion, and lookup, in a well constructed hash table, trend toward Theta(1), but a poorly constructed hash table can degrade to O(n) time complexity in the worst case. The downsides of using a hash table is that they are bad at ordering or sorting data."}],

[{"question" : "What are tries, in the context of data structures?",
  "answer" : "A trie is a tree-like data structure that stores keys, typically strings, in a way that the links between nodes represent parts of the keys. Nodes are typically arrays that contain pointers to additional children. Tries are especially efficient for operations such as search, insert, and delete, where the time complexity is O(m), with m being the length of the key. This makes operations in a trie relatively fast and not directly dependent on the number of keys stored within it. The downside to using a trie instead of a hash map is that tries use a lot more memory, and much of that memory is unused (NULL)."}],

[{"question" : "[C] - Explain the arrow operator.",
  "answer" : "The arrow operator, ->, is a shorter way to access the field of a struct via its pointer. It does two things, back to back: first it dereferences the pointer on the left side of the arrow, and then second it accesses the field on the right of the arrow. For example: mycar->year 2006; is equivalent to (*mycar).year = 2006;"}],

[{"question" : "What are the differences between singly linked lists and doubly linked lists?",
  "answer" : "In a singly linked list, for the most part you can only move one direction: further into the list. This is because at your current node, you only have the location of the next node. With a doubly linked list, you can traverse both directions because you have the location of the next node as well as the previous node. Using a doubly linked list adds flexibility at the cost of using more memory, and having more complexity with insertion and deletion operations."}],

[{"question" : "Why is keeping track of the head of a linked list important? Relating to this point, how do you add a new node to the beginning of a linked list? Why would you want to prepend instead of append to a linked list?",
  "answer" : "If you lose track of the head of a linked list, you will lose track of the rest of the nodes in the list; it serves as the entry point to your list. When you add a new node to the beginning of a linked list, first point your new node to the current head, then update your head to be the new node, this way you dont orphan your other nodes. Prepending is constant time, but appending has a time complexity of O(n)."}],

[{"question" : "What makes a good hash function?",
  "answer" : "A good hash function:\n- Uses only the data being hashed\n- Uses all of the data being hashed\n- Is deterministic (every time you pass the same data into the hash function, the same hash code is output)\n- Uniformly distributes data (spreads the data close to evenly throughout the table)\n- Generates very different hash codes for very similar data"}],

[{"question" : "What is a hash function collision? How do you work around it?",
  "answer" : "A collision occurs when two pieces of data, when run through a hash function, yield the same hash code. This is an issue because we generally would not want to overwrite the data in the hash table that already uses that hash code. We want to insert that additional data into the array while preserving quick insertion and lookup. There are multiple ways to handle this:\n\n- Linear probing: Try to place the data in the next consecutive element in the array (wrapping around to the beginning if necessary) until we find a vacancy. That way if we dont find what were looking for in the first location, at least hopefully it is somewhere nearby.\n\n- Chaining: Each index (hash code) that is being used in the array, contains a pointer to the head of a linked list. If a new piece of data has a collision with something already in the table, it will just get added to the linked list at that location."}]
]

week6 = [
[{"question" : "How does Python differ from C in terms of syntax and usage?",
  "answer" : "Python is significantly more human-readable, and requires much less cryptic syntax to complete similar tasks in C. Unlike C, indentation is part of the syntax. In Python, variable types do not need to be declared, lists (arrays) do not need to have predetermined sizes, and memory management is handled for the user instead of manually."}],

[{"question" : "What are Python's data types and how do they compare to C's data types?",
  "answer" : "Python does not have the data types of 'double' or 'long', as the C functionality of those data types are built into float and int in Python. Python has string as an actual data type (no more char *), but no char data type. Python has dynamic typing, unlike C's static typing."}],

[{"question" : "How do you define a function in Python?",
  "answer" : "The syntax is:\ndef function_name():\n    # function code goes here"}],

[{"question" : "What is an interpreter? How is this different from a compiler?",
  "answer" : "An interpreter executes code line by line, translating each line into machine code on the fly. This allows for immediate execution but can be slower. A compiler, on the other hand, translates the entire program into machine code before execution, resulting in faster runtime performance but requiring a compilation step before execution."}],

[{"question" : "What are Python modules and how do you import them?",
  "answer" : "Python modules are single files that are imported under one import and used. They can define functions, variables, and classes to be used in other files. A library is a collection of modules. It's a way of packaging and reusing code. In practice, the terms module and library are used interchangeably.  Some modules/libraries are built in to Python, others need to be installed (with something like pip). If you import the entire module/library, you access the module's methods using dot notation (method.function_name()), but if you import a specific functions/classes/variables, you can access them directly (function_name()). To import them, at the top of your file you would write:\nimport module_name\n\nIf you want to import a particular function or multiple functions, you would write:\nfrom module_name import func0_name, func1_name"}],

[{"question" : "[Python] - What is a method?",
  "answer" : "A method is a function that is associated with the object that contains it. You use the method via dot notation.\nFor example:\nmy_string.upper()\n\n.upper() is a method that is part of the string object (in this case called my_string) which converts the string to uppercase letters."}],

[{"question" : "What is object oriented programming?",
  "answer" : "Object-oriented programming (OOP) is a programming paradigm based on the concept of objects. Objects are instances of classes, which can contain both data (attributes) and functions (methods) that operate on the data. OOP helps to structure programs in a way that models real-world entities and relationships, promoting code reuse and modularity."}],

[{"question" : "What does Pythonic mean?",
  "answer" : "Pythonic refers to a way of writing Python code that follows popular conventions in the Python community."}],

[{"question" : "What is the Pythonic convention for naming a variable (for a loop) you will not need to use?",
  "answer" : "Instead of using 'i' or some other name, you would use an underscore ('_'). This signals to yourself, and other people viewing your code, that the variable will not be referenced or used anywhere else."}],

[{"question" : "[Python] - What is a named parameter?",
  "answer" : "A named parameter is an additional parameter appended to the arguments passed to a function.\nFor example:\nprint('hello, world', end='')\n\nAdding the end='' will overwrite the default newline at the end of print, and replace it with nothing, therefore staying on the same line."}],

[{"question" : "[Python] - What is an exception? What is the syntax for using them?",
  "answer" : "An exception is an error that occurs during the execution of a program. To handle exceptions, you use the try-except block. The syntax is:\ntry:\n    # code that may cause an exception\nexcept ExceptionType:\n    # code that runs if the exception occurs\n\nFor example:\ntry:\n    result = 10 / 0\nexcept ZeroDivisionError:\n    print('Cannot divide by zero')"}],

[{"question" : "What is a list? What is the difference between a list in Python and an array in C?",
  "answer" : "A list in Python is a collection of items that can be of different data types and is dynamically resizable. Unlike arrays in C, Python lists do not need to have a predetermined size, and they can store elements of different data types. Lists are created using square brackets:\nmy_list = [1, 2, 3, 'a', 'b', 'c']"}],

[{"question" : "[Python] - How does a for-else loop work?",
  "answer" : "If 'break' doesn't happen during the for loop, the else condition is run. If 'break' happens during the for loop, else is ignored."}],

[{"question" : "What is a dictionary in Python? How do you make and use one?",
  "answer" : "A dictionary in Python is essentially a hash table; there are keys with associated values. To make a dictionary, create a key:value pair surrounded with curly braces. The keys and values can be variables or any datatype.\nFor example:\nmy_dict = {'name' : 'Carter'}\n\nYou can also make a list that is populated by dictionaries:\nmy_dicts = [{'name' : 'Carter', 'grade' : 'A'}, {'name' : 'John', 'grade' : grade[1]}]"}],

[{"question" : "How do you use list comprehensions in Python?",
  "answer" : "= List comprehensions provide a concise way to create lists. The syntax is:\n[<expression> for <item> in <iterable> if <condition>]\n\nFor example:\ndoubled = [x * 2 for x in range(1, 6) if x % 2 == 0]"}],

[{"question" : "What is the purpose of Python's None keyword?",
  "answer" : "None is a special constant in Python that represents the absence of a value or a null value. It is commonly used to signify that a variable has no value or to indicate the end of a list."}],

[{"question" : "How do you read and write files in Python?",
  "answer" : "The syntax to open a file and read it into a variable named text is:\nwith open(filename) as variable_name:\n    text = variable_name.read()\n    ...\n\nTo write:\nwith open('filename.txt', 'w') as file:\n    file.write('Hello, world!')"}],

[{"question" : "What are Python classes and how do you define them?",
  "answer" : "Python classes are blueprints for creating objects. A class defines attributes and methods that the objects created from the class can have. The syntax to define a class is:\nclass ClassName:\n    def __init__(self, attribute1, attribute2):\n        self.attribute1 = attribute1\n        self.attribute2 = attribute2\n\n    def method_name(self):\n        # method code"}],

[{"question" : "What is an f-string and how do you use them?",
  "answer" : "An f-string, or formatted string literal, is a way to embed expressions inside string literals using curly braces {}. The syntax is:\nprint(f'some text {expression}')"}],

[{"question" : "What is a tuple?",
  "answer" : "A tuple is a data type that is an ordered, immutable set of data. They are useful associating collections of data that wont be changed. They are written like a list, but instead of being surrounded by square brackets they are surrounded by parentheses.\nFor example:\nmy_tuple = ('may', 4)"}]
]

week7 = [
[{"question" : "What is SQL?",
  "answer" : "SQL (pronounced 'sequel' or 'S-Q-L'), Structured Query Language, is a language specific to databases that is a declarative language. It is used to describe the data you want back or describe the question you have for your data. It is a relatively small language with few keywords. SQL follows the CRUD paradigm -  Create, Read (SELECT), Update, Delete"}],

[{"question" : "What is a flat-file database?",
  "answer" : "A flat-file database is a type of database that stores data in a plain text file. Each line in the file represents a single record, and fields are separated by delimiters such as commas or tabs. Flat-file databases are simple and easy to use but lack the advanced features and performance of relational databases."}],

[{"question" : "What is CRUD?",
  "answer" : "CRUD is the acronym for the four basic functions of persistent storage in a database. It stands for:\n\nCreate\nRead\nUpdate\nDelete"}],

[{"question" : "What is SQLite?",
  "answer" : "SQLite is a lightweight, file-based relational database management system. It is self-contained, serverless, and requires minimal setup, making it ideal for embedded applications, small-scale projects, and as a database for development and testing."}],

[{"question" : "[SQL] - What is schema and how do you use it?",
  "answer" : "A schema in SQL defines the structure of a database. It includes the tables, columns, data types, and constraints such as primary keys and foreign keys. To view the schema of a database in SQLite, you can use the .schema command alone or followed by the table name: .schema table_name\nFor example:\n.schema writers\nCREATE TABLE writers (\n    show_id INTEGER NOT NULL,\n    person_id INTEGER NOT NULL,\n    FOREIGN KEY(show_id) REFERENCES show(id),\n    FOREIGN KEY(person_id) REFERENCES people(id)\n); "}],

[{"question" : "[SQL] - In a schema call, what does FOREIGN KEY(...) and PRIMARY KEY(...) mean?",
  "answer" : "A primary key is used within one table to uniquely identify its rows. It ensures that each record in the table is unique and not null. In a relational database, a foreign key is the primary key of another table that is used to create a relationship between the two tables, ensuring that the data remains consistent and referential integrity is maintained."}],

[{"question" : "What are relational databases?",
  "answer" : "Relational databases are databases structured to recognize relations among stored items of information. They use tables to store data, and relationships between tables are defined by foreign keys."}],

[{"question" : "In relational databases, what are one-to-one, one-to-many, and many-to-many relationships?",
  "answer" : "One-to-One: Each row in Table A is linked to one and only one row in Table B, and vice versa.\nOne-to-Many: Each row in Table A can be linked to multiple rows in Table B, but each row in Table B is linked to only one row in Table A.\nMany-to-Many: Rows in Table A can be linked to multiple rows in Table B, and rows in Table B can be linked to multiple rows in Table A. This is typically implemented using a junction table."}],

[{"question" : "[SQL] - How do you create a table?",
  "answer" : "To create a table in SQL, you use the CREATE TABLE statement. This statement defines the table's name and the columns it will contain, along with their data types and any constraints. For example, to create a table named employees with columns for id, name, position, and salary, you would use the following SQL statement:\nCREATE TABLE employees (\n    id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL,\n    position TEXT,\n    salary REAL,\n);"}],

[{"question" : "[SQL] - When JOINing tables with one-to-many relationships, why is duplication/repetition of cells ok?",
  "answer" : "The JOINed table is only a temporary table for us to view or work with; the data doesn't exist in duplicate in the databases. "}],

[{"question" : "[SQL] - What are indexes?",
  "answer" : "In SQL, indexes are data structures that make it faster to use queries like SELECT and others. If you know in advance you will be making queries on particular columns of a database repeatedly, you can prepare the database in advance by building data structures in memory using an index to speed things up. This is a trade-off of more memory used for less time spent on queries."}],

[{"question" : "What is a B-tree?",
  "answer" : "A B-tree is a self-balancing tree data structure that maintains sorted data and allows for efficient insertion, deletion, and search operations. It's commonly used in databases and file systems. Each node in a B-tree contains a certain number of keys and pointers to its child nodes. The keys act as separation values which divide its subtrees. "}],

[{"question" : "What is a race condition and how can it be addressed?",
  "answer" : "A race condition occurs when two or more operations must execute in the proper sequence but the program has no way to enforce that sequence. In databases, race conditions can occur during concurrent transactions. They can be addressed using techniques such as locking, transactions, and proper isolation levels."}],

[{"question" : "What is a SQL injection attack?",
  "answer" : "A SQL injection attack occurs when an attacker inserts malicious SQL code into a query through user inputs. If the input is not properly sanitized or validated, the attacker can manipulate the query to execute unintended commands, potentially gaining unauthorized access to the database. Using placeholders and prepared statements can help prevent SQL injection attacks."}],

[{"question" : "What are Database Management Systems and what are some examples of them?",
  "answer" : "Database Management Systems (DBMS) are software systems that enable users to define, create, maintain, and control access to databases. Examples of DBMS include MySQL, Oracle, PostgreSQL, and SQLite."}],

[{"question" : "[SQL] - What is an aggregate function?",
  "answer" : "An aggregate function is a keyword that calculates data from multiple rows and returns a single value. They take in a range of data and provide a summary statistic such as a total or average. Some examples are COUNT(column), AVG(column), MIN(column), and MAX(column). You use these functions in conjunction with the SELECT statement.\nFor example:\nSELECT AVG(rating) FROM reviews;"}],

[{"question" : "[SQL] - What are the two ways you can combine tables?",
  "answer" : "Sub-queries and JOINs.\n\nSub-queries: A sub-query is a query nested within another query. It is used to reference and retrieve data from a different relational table. Unlike JOINs, sub-queries do not create a combined result set that you can see directly. Instead, they provide data to the main query.\nFor example:\nSELECT rating\nFROM ratings\nWHERE movie_id = (\n    SELECT id\n    FROM movies\n    WHERE title = 'The Matrix'\n);\n\nJOINs: JOINs allow you to combine data from multiple relational tables and visualize that combined data in a new, temporary, table.\nFor example:\nSELECT rating, title\nFROM ratings\nJOIN movies ON movies.id = ratings.movie_id\nWHERE title = 'The Matrix';"}],

[{"question" : "[SQL] - How does the LIKE keyword work?",
  "answer" : "The LIKE keyword is used in a WHERE clause to search for a specified pattern in a column. It allows you to perform pattern matching within the specified column. The patterns can include wildcard characters:\n% represents zero, one, or multiple characters.\n_ represents a single character.\nFor example, to find all records where a name starts with 'J':\nSELECT * FROM users\nWHERE name LIKE 'J%';"}]
]

week8 = week8 = [
[{"question" : "What are access points? What are some examples of them?",
  "answer" : "Access points are devices that allow wireless devices to connect to a wired network using Wi-Fi. They serve as a bridge between wired and wireless networks. Examples of access points include wireless routers, Wi-Fi hotspots, and wireless range extenders."}],

[{"question" : "What is a packet?",
  "answer" : "A packet is a small segment of data transmitted over a network. Packets are the fundamental units of communication in network systems, containing both the data being sent and metadata such as source and destination addresses. They are used to efficiently transfer data between devices."}],

[{"question" : "What is TCP/IP?",
  "answer" : "IP stands for Internet Protocol, and it is the way that packets (small, broken up pieces of data) are transferred to each other. Machines have IP addresses, and packets are sent through a network of routers in the direction of the destination IP address. Each router moves the data a little closer to its destination. IP does not know if all the packets were successfully transmitted, so it needs to be paired with TCP.\n\nTCP is the Transmission Control Protocol, which directs packets to the correct program/service on the receiving machine. TCP does this by using a port number that is coupled with the IP address. TCP transmits, along with the data, information about how many packets the receiver should expect to get, and in what order they fit together. When a machine receives a packet, TCP looks in the packets header and checks what program/service it belongs to. Since packets are received out of order, TCP presents the data to the receiving machine in proper order. If packets are missing (dropped), TCP knows which ones they are, and sends a request to get them."}],

[{"question" : "What are port numbers?",
  "answer" : "Port numbers are numerical identifiers used in TCP/IP networking to specify particular services or applications on a device. They help direct network traffic to the correct application or service. For example, port 80 is commonly used for HTTP traffic, and port 443 is used for HTTPS traffic."}],

[{"question" : "What is DNS? DHCP?",
  "answer" : "DNS, Domain Name System, exists to help translate IP addresses into domain names for human readability/use. There is no DNS server that has a record of the entire internet; instead, large DNS servers are more like aggregators, collecting smaller sets of DNS records and updating frequently.\n\nDHCP stands for Dynamic Host Configuration Protocol. DHCP servers assign IP addresses to internet accessible devices."}],

[{"question" : "What is HTTP?",
  "answer" : "HTTP stands for Hyper Text Transfer Protocol. HTTP is an application layer protocol, and it dictates the format by which clients request web pages from a server, and the format via which servers return information to clients."}],

[{"question" : "What is curl?",
  "answer" : "curl is a command-line tool used to transfer data to or from a server using various protocols, including HTTP, HTTPS, FTP, and more. It is commonly used for testing API endpoints, downloading files, and interacting with web services. The basic syntax is: curl <url>."}],

[{"question" : "What is HTML?",
  "answer" : "HTML stands for Hypertext Markup Language, and it is used to build the structure and content of web pages. It is not a programming language, as it does not have variables, functions, logic, etc. Instead, HTML is a markup language which uses tags around plain text, which allows web browsers to interpret the text in different ways. HTML is the foundation of a web page and you cannot build one without it."}],

[{"question" : "[HTML] - What are tags and attributes?",
  "answer" : "Tags are the fundamental building blocks of HTML. They are used to define elements within an HTML document and are surrounded by angle brackets. Most tags come in pairs: an opening tag <tag> and a closing tag </tag>. Attributes provide additional information about HTML elements and are included within the opening tag. They come in name-value pairs, like class=\"classname\" or id=\"idname\"."}],

[{"question" : "[HTML] - What are meta tags?",
  "answer" : "Meta tags are HTML tags that provide metadata about the HTML document. They are placed inside the <head> section and can include information such as character set, page description, keywords, author, and viewport settings. Examples include <meta charset=\"UTF-8\"> and <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">."}],

[{"question" : "What is an HTML entity? How are they used?",
  "answer" : "An HTML entity is a special character built into HTML that you can use on your web page. They can be inserted into your HTML using the code associated with the character you'd like. These codes start with & and end with ;. For example, &lt; would insert a less than sign (<) into your page."}],

[{"question" : "[HTML] - What are some things that are generally located in the <head> of an HTML file?",
  "answer" : "Generally located in the <head> of an HTML file are the title of the page, meta tags (containing character encoding, viewport, X-UA-Compatible), CSS, and JavaScript (in the form of <style> and <script> tags, or links to separate files containing them)."}],

[{"question" : "What is CSS?",
  "answer" : "CSS stands for Cascading Style Sheets. CSS is a styling language that describes to the browser how certain HTML elements should be modified. It is not a programming language, as it does not have variables, functions, etc. CSS is used by first indicating a selector, which selects what HTML element to modify, and following that with key:value pairs with the desired modifications."}],

[{"question" : "What are three different ways CSS can be added to a webpage?",
  "answer" : "1) Linked to in the <head> via a <link> tag that is pointed at a separate .css file.\n2) Inserted into the <head>, surrounded by <style> tags\n3) Added as attributes directly inside the HTML tag."}],

[{"question" : "[CSS] - What is a class? What is an id? How are they used? How are they different?",
  "answer" : "A class is a way in CSS to group multiple HTML elements in order to modify them as a batch. An id is a way in CSS to modify a particular single HTML element. An element can have both a class and an id at the same time.\n\nTo add a class to an element, in the HTML tag add 'class=classname' and then in the CSS a '.' is put before the class name selector (.classname).\n\nTo add an id to an HTML element, 'id=idname' is added inside the tag, and the CSS selector for that id is prepended with a # (#idname)."}],

[{"question" : "What is Bootstrap?",
  "answer" : "Bootstrap is a CSS framework which has packaged together many CSS style shortcuts which developers can use to more quickly build nicely styled web pages. To use Bootstrap, you would link to it in your <head> and then use the tags specified in the Bootstrap documentation as you need."}],

[{"question" : "What is Javascript?",
  "answer" : "Javascript (JS) is a programming language used to add functionality to webpages. Javascript is generally run client-side, not server-side. Javascript often is used to respond to events - a response to a user interaction with the web page. JS can behave like an object-oriented programming language, and was derived from C syntax. It was first released in 1995."}],

[{"question" : "What are two different ways Javascript can be added to a webpage?",
  "answer" : "1) Linked to in the <head> by adding a .js file in a <script> tag.\n2) Added directly to the HTML, contained within <script> tags."}],

[{"question" : "What is an anonymous function?",
  "answer" : "An anonymous function is a function that is not given a name. This is useful when you want to write a function you will just use once."}],

[{"question" : "In a broad sense, what are the roles/relationships between HTML, CSS, and Javascript?",
  "answer" : "HTML is the structure and content of the web page, CSS gives it style, and Javascript adds functionality."}],

[{"question" : "What is the DOM?",
  "answer" : "The DOM is the Document Object Model, which is essentially a tree representation of a webpage, containing all the page's tags/elements as its branches and leaves. Navigating and making changes to the document object is the main use of JavaScript. Properties can be changed, and methods can be called, changing the web page without needing the user to refresh."}],

[{"question" : "What is jQuery?",
  "answer" : "jQuery is a popular open-source Javascript library, released in 2006, that is designed to simplify client-side scripting (such as DOM manipulation)."}]
]
