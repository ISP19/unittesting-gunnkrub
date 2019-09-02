## Unit Testing Assignment

by Gunn Torcheep.


## Test Cases for unique

Write a table describing your test cases.

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item many times    |  list with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| list of empty list  | list of empty list        |
| list in list that have same integer but not same order  |  list of item in list with same order       |
| extremely large list  |   extremely large list      |

## Test Cases for Fraction
test str

| Test case              |  Expected Result    |
|------------------------|---------------------|
| integer                 |  string of integer  |
| proper form fraction    |  string of fraction in proper form|
| improper form fraction  |  string of fraction in proper form|
| zero                    |  string of zero     |
| fraction without denominator |  string of fraction with denominator equal one|
| number that denominator equal zero |  string of infinity|
| negative number that denominator equal zero |  string of negative infinity|
| zero over zero (suppose that equal zero) |  string of zero|

test add

| Test case              |  Expected Result    |
|------------------------|---------------------|
| a / b  +  c / d        |  (ad + bc) / bd     |
| -n + n                 |  0                  |
| 0 + 0                  |  0                  |
| -a / b   +  (-c / d)   |  (-ad + (-bc)) / bd |
| large integer  +  large integer  |  large integer|
| infinity + integer     |  infinity           |
| infinity - infinity    | 0 (supposed)                  |
| -infinity - infinity   | -infinity           |

test eq

| Test case              |  Expected Result    |
|------------------------|---------------------|
| same fraction in proper form |  true         |
| not same fraction in proper form | false     |
| zero and zero with denominator  |  true      |
| infinity and infinity           |  true      |
| infinity and negative infinity  |  false     |

test mul

| Test case              |  Expected Result    |
|------------------------|---------------------|
| (a / b) * 1            |  a / b              |
| (a / b) * 0            |  0                  |
| 0 * 1                  |  0                  |
| integer * (-infinity)  |  -infinity          |
|(-infinity) * (-infinity) |  infinity         |
| infinity * 0           |  0 (supposed)       |
| (-infinity) * 0        |  0 (supposed)       |

test init

| Test case              |  Expected Result    |
|------------------------|---------------------|
| numerator              |  numerator of proper form |
| denominator            |  denominator of proper form |
| negative denominator   |  positive denominator of proper form |
| gcd                    | gcd of numerator and denominator |
| numerator of infinity in fraction form |  infinity     |
| numerator of negative infinity in fraction form |  negative infinity |
| denominator of infinity in fraction form |  1  |
