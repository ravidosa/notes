reachable(StartState, FinalState, []) :- StartState == FinalState.
reachable(StartState, FinalState, [Symbol|InputTail]) :- transition(StartState, Symbol, NextStates), member(NextState, NextStates), reachable(NextState, FinalState, InputTail).
