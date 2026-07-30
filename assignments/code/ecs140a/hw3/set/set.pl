isUnion([], Set2, Set2).
isUnion(Set1, [], Set1).
isUnion([Set1Head|Set1Tail], Set2, Union) :- member(Set1Head, Set2), isUnion(Set1Tail, Set2, Union).
isUnion([Set1Head|Set1Tail], Set2, [Set1Head|UnionTail]) :- not(member(Set1Head, Set2)), isUnion(Set1Tail, Set2, UnionTail).

isIntersection([], Set2, []).
isIntersection(Set1, [], []).
isIntersection([Set1Head|Set1Tail], Set2, [Set1Head|IntersectionTail]) :- member(Set1Head, Set2), isIntersection(Set1Tail, Set2, IntersectionTail).
isIntersection([Set1Head|Set1Tail], Set2, Intersection) :- not(member(Set1Head, Set2)), isIntersection(Set1Tail, Set2, Intersection).

isEqual([], []).
isEqual([Set1Head|Set1Tail], Set2) :- select(Set1Head, Set2, XRemoved), isEqual(Set1Tail, XRemoved).
