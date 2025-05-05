**Question:**

Create a class `Team` with the following attributes:

* `int` - `id`
* `String` - `name`
* `String` - `owner`
* `double` - `value`

Create the `__init__` method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.

Create a class `League` with the following attributes:

* `String` - `leagueName`
* `List` - `teamList`

Create the `__init__` method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.

Implement two methods - `findMaximumTeamById` and `sortTeamById` in the `League` class.

**`findMaximumTeamById`:**

Create a method `findMaximumTeamById` in the `League` class. This method will return the `Team` having the maximum value for `id` of all the `Teams` in the `Team List` of the `League` class. If there is no `Team` found in the `Team List` or if the list is empty then return `None` to the main program.

**`sortTeamById`:**

Create a method `sortTeamById` in the `League` class. This method will return the `Team` sorted list for `id` in ascending order of all the `Teams` in the `Team List`. If there is no `Team` in the `Team List` or if the list is empty then return `None` to the main program.

These methods should be called from the main method.

**Instructions for the main section of the code:**

a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the sample input description section mentioned below and to read the data in the same sequence.
c. To create `League` and `Team` objects, take the inputs in below sequence.
d. To create a List of `n` `Team` objects read the value of `n`.
e. To create a List of `n` `Team` objects read values for `owner`, `value`, `id`, `name` and create the `Team` object and add to the `List`. Repeat this step `n` times.
f. Create the `League` object by passing the `leagueName` and the List of `Team` created in the previous step.
g. Call the method `sortTeamById` of the `League` object created in point `#c`. Print the argument read in point `#d`.
h. Call the method `findMaximumTeamById` of the `League` object created in point `#c` by passing the argument read in point `#d`.
i. Print the output of both methods as per given sample output.
j. Don't use any static text or formatting for printing the result. Just invoke the method and print the result.
k. Sequence for specific object will follow same attribute sequence as mentioned in the question. You may refer to the sample Input/output for the display format.




**Sample 1 Input:**

5
Ganguly
395
21
sachin
Ganguly
184
5
virat
Anoop
132
75
rohit
Anoop
904
87
dhoni
Ganguly
849
74
Rahul

**Sample 1 Output:**
Anoop
904.0
87
dhoni
5
21
74
75
87