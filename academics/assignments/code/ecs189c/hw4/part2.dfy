/*
    Part 2: Classes and class invariants

    This part is an introduction to classes and class invariants
    in Dafny, through implementing a simple stopwatch class.

    ===== What is a class invariant? =====

    A class invariant is a condition that should always be true
    - after the constructor is called, and
    - at every *entry* and *exit* point of every method or function of a class.

    In other words, it is the same thing as a precondition and postcondition
    on every method of the class.

    ===== How do classes work in Dafny? =====

    Most of the syntax here should be familiar from the lectures and part 1.
    The new syntax is as follows:
    - the "reads" clause indicates that a function reads the state of the object
        in a particular variable. (e.g. `reads x` to read the variable x.)
    - the "modifies" clause indicates that a method modifies the state of the object.
        You can just say "modifies this" to indicate that the object itself is modified.
    - You can use the "this" keyword to refer to the object, however, this is not
        usually necessary as just referring to the field name will also work.

    Note: "reads" is only used for functions, and "modifies" is only used for methods.

    Also:
    - the old(value) function is useful in postconditions! It allows you to refer
        to the value of a variable before the method was called. For example, to say
        that seconds is not modified by a method, you would say
            `ensures seconds == old(seconds)`
        However this is only necessary if the method `modifies` the variable, it should
        not be necessary if the method only `reads` the variable.

    ===== Your Task =====

    The stopwatch consists of four fields: seconds, minutes, hours, and days.
    You will first implement a class invariant that should ensure that the time is always
    valid (the meaning of "valid" is described above the class invariant).
    Then you will implement all of the methods below.
    The constructor is written for you, but it needs a postcondition.

    To check that your implementation is working, there is a Tests() method at the end
    of the file.

    ===== Just for fun =====

    There's an excellent list called "falsehoods programmers believe about time":
    https://gist.github.com/timvisee/fcda9bbdff88d45cc9061606b4b923ca

    Since our stopwatch is not concerned with things like leap seconds
    and time zones, fortunately, we can ignore these falsehoods for
    the purpose of this exercise.
    But it might be fun (as a larger project) to write a real time module in
    a verified language like Dafny and try to prove or disprove some of these falsehoods
    given a sufficiently detailed model of time.

    ===== Grading notes =====

    - Your file should pass the Dafny verifier with no errors or warnings.
        Look for the green bars on the left or
        (if you have the command line): `dafny verify part2.dfy` should output
        ```
        Dafny program verifier finished with <n> verified, 0 errors
        ```

    - Your test cases in Tests() should cover at least one case for each method.

    - The implementation of all methods should
        match the description given above the method.
        (This is most important for `class_invariant` and `as_seconds`.)

    - Ensure that you implement *both* the preconditions and postconditions for
        each methods, and that the class invariant is mentioned
        in the pre and postconditions of each method.
*/

class Stopwatch
    {

    var seconds: int
    var minutes: int
    var hours: int
    var days: int

    /*
        1. Class invariant

        The stopwatch should ensure that the time is always valid,
        i.e., when seconds gets to 60, it should wrap over to 0 and minutes should
        go up by 1, and similarly for minutes or hours. "days" is just a counter that
        can be arbitrarily large.

        Additionally, none of the time values should ever be negative.
    */
    
    function class_invariant(): bool
        reads this
    {
        0 <= seconds < 60 &&
        0 <= minutes < 60 &&
        0 <= hours < 24 &&
        0 <= days
    }

    /*
        2. Convert the stopwatch to a total number of seconds.

        This is a function as it does not modify the state of the object,
        so it doesn't need a pre or postcondition.
    */
    
    function as_seconds(): int
        reads this
    {
        seconds + 60 * (minutes + 60 * (hours + 24 * days))
    }

    /*
        3. Constructor

        Initializes the stopwatch to 0.
    */
    constructor ()
        ensures class_invariant()
        ensures as_seconds() == 0
    {
        seconds := 0;
        minutes := 0;
        hours := 0;
        days := 0;
    }

    /*
        4. Add 1 second to the stopwatch.
    */
    method Tick()
        modifies this
        requires class_invariant()
        ensures class_invariant()
        ensures as_seconds() == old(as_seconds()) + 1
    {
        seconds := seconds + 1;
        if seconds == 60 {
            seconds := 0;
            minutes := minutes + 1;
            if minutes == 60 {
                minutes := 0;
                hours := hours + 1;
                if hours == 24 {
                    hours := 0;
                    days := days + 1;
                }
            }
        }
    }

    /*
        5. Reset the stopwatch to 0 (for all counters).
    */
    method Reset()
        modifies this
        requires class_invariant()
        ensures class_invariant()
        ensures as_seconds() == 0
    {
        seconds := 0;
        minutes := 0;
        hours := 0;
        days := 0;
    }

    /*
        6. Advance the stopwatch by an arbitrary number of seconds.
        The number to advance by should be nonnegative!

        This should be equivalent to calling Tick() repeatedly
        `inc` times.
        You may implement it however you like, but if you want a challenge,
        try calling Tick() in a loop and coming up with the loop invariant.
    */
    method AdvanceBy(inc: int)
        modifies this
        requires class_invariant()
        requires inc >= 0
        ensures class_invariant()
        ensures as_seconds() == old(as_seconds()) + inc
    {
        var i := 0;
        while i < inc
            invariant 0 <= i <= inc
            invariant class_invariant()
            invariant as_seconds() == old(as_seconds()) + i
        {
            Tick();
            i := i + 1;
        }
    }
}

/*
    7. Test your stopwatch here.

    Add at least one test case for each method.
*/
method Tests()
{
    // Test the constructor
    var sw := new Stopwatch();

    // Test the class_invariant() function
    assert sw.class_invariant();

    // Test the as_seconds() function
    assert sw.as_seconds() == 0;

    // Test the Tick() method
    sw.Tick();
    assert sw.as_seconds() == 1;
    assert sw.seconds == 1;
    assert sw.class_invariant();

    // Test the Reset() method
    sw.Reset();
    assert sw.as_seconds() == 0;
    assert sw.class_invariant();

    // Test the AdvanceBy() method
    sw.AdvanceBy(59);
    assert sw.seconds == 59;
    sw.Tick();
    assert sw.seconds == 0;
    assert sw.minutes == 1;
    sw.AdvanceBy(59 * 60 - 1);
    assert sw.seconds == 59;
    assert sw.minutes == 59;
    sw.Tick();
    assert sw.seconds == 0;
    assert sw.minutes == 0;
    assert sw.hours == 1;
    sw.AdvanceBy(23 * 60 * 60 - 1);
    assert sw.seconds == 59;
    assert sw.minutes == 59;
    assert sw.hours == 23;
    sw.Tick();
    assert sw.seconds == 0;
    assert sw.minutes == 0;
    assert sw.hours == 0;
    assert sw.days == 1;
}

/*
    8. Comment on the following questions:

    Does abstracting pre/postconditions in
    a class invariant help make verification
    easier, harder, or equally as difficult
    as if classes (objects) were not available?

    Are classes and object-oriented programming necessary
    for a practical, real-world verification language?

    ===== ANSWER Q8 BELOW =====
    Class invariants make verification easier since you only need to define the invariant once and can apply it to all class methods. Classes and OOP are not necessary for a practical verification language, but the presence of those features makes it easier to model and verify complex systems.
    ===== END OF Q8 ANSWER =====
*/
