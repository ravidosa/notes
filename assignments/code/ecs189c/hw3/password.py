"""
The password game

https://neal.fun/password-game/

You will implement a series of rules that the
password should satisfy. Each rule is a function

    rule_<number>(password)

that takes a Z3 string variable `password` and returns
a Z3 formula that the password should satisfy.

To run the code, open a terminal and execute

    python3 password.py

The code should print out a solution like this:

    [password = "abc"]

which you can copy and paste into the password game to
see if it satisfies all the rules so far.

=== Additional requirements ===

To simplify the problem, we will assume that the
password is ASCII-only. The rule `rule_0` is written for you,
and it enforces this constraint.

With the exceptions listed below (in rules 5, 6, 8, 9, and 10),
all of the other rules should exactly encode the requirements
given by the password game -- with no additional restrictions.
For example, if the password is at least 5 characters long,
you shouldn't say that it is exactly 10 characters long,
and you shouldn't hard-code a specific string like "password"
to satisfy the rule.
We will be checking your implementation against a correct implementation
of the rule during grading to see if it matches the right set of
strings.

For rules 5 and 9: you may not be able to encode the exact
requirements, but you should come up with a useful stronger
requirement. For example, if the rule is "contains a number",
you could encode that as "contains exactly 1, 2, or 3 numbers."
But you still shouldn't hard code a specific string like "123"
to satisfy the rule.

For rules 6 and 8: the password game online accepts both case-insensitive
and case-sensitive versions of the rule.
For this homework, please instead take one of the following two conventions:
1. All lowercase: Assume the part of the password that is being checked is all lowercase letters.
2. Assume the first letter of the part of the password being checked is uppercase, and the rest is lowercase.

For rule 10: since we do not know all captchas that might appear in the game,
for this rule, please manually encode that the password contains the specific captcha that you got when playing the game. You may need to change your encoding
if you refresh the game and it gives you a new captcha.

Finally, Z3 may start to slow down once all the rules are added!
Be patient -- the code may take a few minutes to run.

=== Grading notes ===

To ensure you get credit, please be sure that:
- python3 password.py runs without errors
- You do not rename or change the signature of any of the functions
      rule_0, rule_1, ..., rule_10.
  During grading, these will be checked against a correct implementation
  to see if they match the right set of strings.
  (You don't have to have the exact same implementation as us, but it should be
  equivalent, aside from rules 5 and 9. See the additional requirements above).
- pytest password_test.py runs with a single non-skipped test (for problem 11)
- problem 11 has one assertion for every redundant rule (make sure it is exhaustive)
- Your answers to problems 12-13 are filled in only in the designated space,
  between the marker lines "Answer Q" and "End of Answer"
- Running time is at most 10 minutes for python3 password.py
- Running time is at most 5 minutes for pytest password_test.py

=== Getting help ===

If you get stuck, take a look at:
- regex_help.md
- ascii_table.txt
- hints.md
- [Z3 python documentation](https://z3prover.github.io/api/html/namespacez3py.html)
"""

import z3

##########################
###  Helper functions  ###
##########################
# These are provided for you -- you may find them useful.

def ReFull():
    """
    Returns a Z3 regex that matches all strings.
    """
    return z3.Full(z3.ReSort(z3.StringSort()))

def ReContaining(r):
    """
    Returns a Z3 regex that matches any string containing a match for regex `r` somewhere in the middle.
    For example,

        ReContaining(z3.Range("a", "z"))

    will match any string containing a lowercase letter.
    """
    return z3.Concat(
        ReFull(),
        r,
        ReFull(),
    )

#########################
###   Password Rules  ###
#########################
"""
Implement the rules for rounds 1 through 10 of the game.
You will need to play the game to figure out what the rules are!

Similarly to rule 0, your rules will refer
to the password variable `password` and return a Z3 formula.
Rule 1 can be done without regular expressions.
For the rest, you can use `z3.InRe(password, R)` to assert that the
password matches a regular expression `R`.
"""

def rule_0(password):
    """
    password: a `z3.String` variable representing the password
    returns: a Z3 formula that the password should satisfy
    """
    # The password consists of only ASCII characters.
    return z3.InRe(password, z3.Star(z3.Range(" ", "~")))

def rule_1(password):
    # The password must be at least 5 characters.
    return z3.Length(password) >= 5

def rule_2(password):
    # The password must include a number.
    return z3.InRe(password, ReContaining(z3.Range("0", "9")))

def rule_3(password):
    # The password must include an uppercase letter.
    return z3.InRe(password, ReContaining(z3.Range("A", "Z")))

def rule_4(password):
    # The password must include a special character.
    return z3.InRe(password, ReContaining(z3.Union(
        z3.Range("{", "~"), z3.Range(" ", "/"), 
        z3.Range("[", "`"), z3.Range(":", "@")
        )))

def rule_5(password):
    # The digits in the password must add up to 25.
    return z3.Sum([z3.If(z3.And(z3.Length(password) > i, z3.CharIsDigit(password[i])), 
                         z3.CharToInt(password[i]) - 48, 0) for i in range(30)]) == 25

def rule_6(password):
    # The password must include a month of the year.
    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    return z3.InRe(password, ReContaining(z3.Union([z3.Re(m) for m in months])))

def rule_7(password):
    # The password must include a roman numeral.
    numerals = ["I", "V", "X", "L", "C", "D", "M"]
    return z3.InRe(password, ReContaining(z3.Union([z3.Re(n) for n in numerals])))

def rule_8(password):
    # The password must include one of our sponsors:
    sponsors = ["pepsi", "starbucks", "shell"]
    return z3.InRe(password, ReContaining(z3.Union([z3.Re(s) for s in sponsors])))

def rule_9(password):
    # The roman numerals in the password should multiply to 35.
    numerals = ["I", "V", "X", "L", "C", "D", "M"]
    numerals = z3.Union([z3.Re(n) for n in numerals])
    non_numerals = z3.Complement(numerals)
    non_I = z3.Concat(z3.Star(non_numerals), z3.Star(z3.Concat(z3.Re("I"), z3.Plus(non_numerals))))
    I_non = z3.Concat(z3.Star(z3.Concat(z3.Plus(non_numerals), z3.Re("I"))), z3.Star(non_numerals))
    non_I_non = z3.Concat(z3.Star(z3.Concat(z3.Plus(non_numerals), z3.Re("I"))), z3.Plus(non_numerals))

    return z3.InRe(password, z3.Union(z3.Concat(non_I, z3.Re("XXXV"), I_non),
                                      z3.Concat(non_I, z3.Re("V"), non_I_non, z3.Re("VII"), I_non),
                                      z3.Concat(non_I, z3.Re("VII"), non_I_non, z3.Re("V"), I_non)))

def rule_10(password):
    # The password must include this CAPTCHA:
    captcha = "ecd4w"
    return z3.InRe(password, ReContaining(z3.Re(captcha)))

########################
###    Entrypoint    ###
########################
"""
You shouldn't need to modify this part.
It combines all the rules to solve the game.
To run, run `python3 password.py` in the terminal.

If you have any unimplemented rules, it
will skip after the first rule that is not implemented.
"""

def main():
    solver = z3.Solver()

    password = z3.String("password")

    rules = [rule_0, rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9, rule_10]
    try:
        for (i, rule) in enumerate(rules):
            solver.add(rule(password))
            print(f"Rule {i}: added")

    except NotImplementedError:
        print(f"Rule {i}: not implemented (additional rules skipped)")

    print("Solving...")
    print("")
    result = solver.check()
    if result == z3.sat:
        print(f"[password = {solver.model()[password]}]")
    elif result == z3.unsat:
        print("No solution found")
    elif result == z3.unknown:
        print("Unknown")
    else:
        assert False, "Unreachable"

    # Uncomment for debugging:
    # print(solver.assertions())

if __name__ == "__main__":
    main()

########################
###    Discussion    ###
########################
"""
Complete the last three questions after you have finished rules 1-10.

11. How many of your rules are redundant?
By "redundant", we mean that the rule is implied by one of the
other rules.

For each rule that is redundant, use Z3 to prove it:
show that the redundant rule
is implied by one of the others.
Many of these implications are intractable. So, it is enough to show it
for a certain bound on the password length, e.g., 20 characters.
If that's still intractable, you can comment out the case and add
a comment that it's true, but Z3 is not able to prove it.

Fill in the test below; it should have one assertion
for each redundant rule.
Remember to unskip the test to get credit!

Time bound: the test should run in under 5 minutes.
"""

import pytest

SAT = z3.sat
UNSAT = z3.unsat
UNKNOWN = z3.unknown
PROVED = UNSAT
COUNTEREXAMPLE = SAT

def prove(spec):
    solver = z3.Solver()
    solver.add(z3.Not(spec))
    result = solver.check()
    if result == PROVED:
        print("proved")
    elif result == COUNTEREXAMPLE:
        print("counterexample")
        print(solver.model())
    else:
        # result == UNKNOWN
        print("failed to prove or find counterexample")
    return result

def test_redundant_rules():
    password = z3.String("password")
    for r1, r2 in [(rule_5, rule_2), (rule_7, rule_3), (rule_8, rule_1), (rule_9, rule_3), (rule_9, rule_7), (rule_10, rule_1), (rule_10, rule_2)]:
        assert prove(z3.Implies(z3.And(r1(password), z3.Length(password) <= 20), r2(password))) == PROVED

"""
12. Which of the rules was hardest to encode?
Why do you think it was difficult?
(Give your best guess -- there is no specific right answer.)

# Do not remove this line:
===== ANSWER Q12 BELOW =====
Rule 9 was the hardest since, unlike Rule 5, it considered the number as a whole and not just the digits, and since there is no built in function in Z3 like z3.Sum but for multiplication. However, since 35 has only four factors, I wrote the regex using casework (either 5/V and 7/VII are both present, or 35/XXXV is present, in addition to some 1/I's).
===== END OF Q12 ANSWER =====

13. Which of the rules was hardest for Z3 to solve?
Why do you think it was difficult?
(Give your best guess -- there is no specific right answer.)

# Do not remove this line:
===== ANSWER Q13 BELOW =====
Rule 5 was the hardest since we weren't able to specify it exactly, but instead had to bound the search space, since there could be an arbitrarily large number of digits.
===== END OF Q13 ANSWER =====
"""
