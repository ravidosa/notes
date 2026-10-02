/* All novels published during the year 1953 or 1996*/
year_1953_1996_novels(Book) :-
    novel(Book, 1953); novel(Book, 1996).

/* List of all novels published during the period 1800 to 1900*/
period_1800_1900_novels(Book) :-
    novel(Book, Year), Year >= 1800, Year =< 1900.

/* Characters who are fans of LOTR */
lotr_fans(Fan) :-
    fan(Fan, Collection), member(the_lord_of_the_rings, Collection).

/* Authors of the novels owned by Chris */
author_names(Author) :-
    fan(chris, Collection), member(Book, Collection), author(Author, Bibliography), member(Book, Bibliography).

/* Characters who are fans of Brandon Sanderson's novels */
fans_names(Fan) :-
    fan(Fan, Collection), member(Book, Collection), author(brandon_sanderson, Bibliography), member(Book, Bibliography).

/* Novels common between either of Alex, Logan, and Charlotte */
mutual_novels(Book) :-
    fan(alex, CollectionAlex), fan(logan, CollectionLogan), member(Book, CollectionAlex), member(Book, CollectionLogan); fan(alex, CollectionAlex), fan(charlotte, CollectionCharlotte), member(Book, CollectionAlex), member(Book, CollectionCharlotte); fan(logan, CollectionLogan), fan(charlotte, CollectionCharlotte), member(Book, CollectionLogan), member(Book, CollectionCharlotte).
