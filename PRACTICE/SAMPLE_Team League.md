**Question:**

Create a class `Team` with the following attributes:

* `String` - `owner`
* `double` - `value`
* `int` - `id`
* `String` - `name`

Create the `__init__` method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.

Create a class `League` with the following attributes:

* `String` - `leagueName`
* `List` - `teamList`

Create the `__init__` method which takes all parameters in the above sequence. The method should set the value of attributes to parameter values inside the method.

Implement a method `findMinimumTeamById` in the `League` class.

**`findMinimumTeamById`:**

Create a method `findMinimumTeamById` in the `League` class. This method will return the `Team` object having the minimum value for the `id` of all the `Teams` in the `Team List` of the `League` class. If there is no `Team` found in the `Team List` or if the list is empty then return `NONE` to the main program.

**Instructions for the main section of the code:**

a. You would require to write the main section completely, hence please follow the below instructions for the same.
b. You would require to write the main program which is inline to the sample input description section mentioned below and to read the data in the same sequence.
c. To create a `League` and `Team` objects, take the inputs in the below sequence.
d. To create a List of `n` Team objects read the value of `n`.
e. To create a List of `n` Team objects read values for `owner`, `value`, `id`, `name` (in this order) and create the `Team` object and add to the `List` of `Team` objects. Repeat this step `n` times.
f. Create the `League` object by passing the `leagueName` (this can be any random string) and the `List` of `Team` objects created in the previous step.
g. Call the method `findMinimumTeamById` using the `League` object created in point `#f`.
h. Print the output of both methods as per given sample output.
i. If there is `NONE` returned from any method print "No Data Found".





**Sample Input:**

3
Owner1
100.5
3
Team A
Owner2
150.2
1
Team B
Owner3
95.7
2
Team C



**Expected Output:**
Minimum ID Team:
Owner: Owner2
Value: 150.2
ID: 1
Name: Team B