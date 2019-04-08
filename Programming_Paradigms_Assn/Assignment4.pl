% Description: Complete the requirements set forth in the assignment description.
% Author: Michael Krakovsky  
% Date: March 27, 2019
% Version: 1.0

% Part 1: Structure and Sample Facts

% Sample Facts For Question 1 -- Please Ignore

%-------%
% Users %
%-------%
user(harry).
user(ron).
user(herminone).
user(petunia).
user(molly).
user(dumbledore).
user(testbirthday).
user(mike).

%-------------------------%
% Date: day, month & year %
%-------------------------%
today(20,3,2019).

birthday(harry, date(31,7,1980)).
birthday(ron, date(1,3,1980)).
birthday(herminone, date(19,11,1979)).
birthday(petunia, date(6,9,1953)).
birthday(molly, date(27,2,1954)).
birthday(dumbledore, date(14,8,1881)).
birthday(mike, date(20,3,1996)).
birthday(testbirthday, date(20,3,1972)).

%------------------------------------------------------%
% Connections: first user, second user, relationship   %
% A connection is *not* symmetric and the relationship %
% is defined by the first user for the second.         %
%------------------------------------------------------%
connection(harry, ron, strong).
connection(harry, herminone, strong).
connection(harry, dumbledore, professional).

connection(ron, harry, strong).
connection(ron, herminone, strong).
connection(ron, molly, familial).
connection(ron, dumbledore, professional).

connection(herminone, harry, strong).
connection(herminone, ron, strong).
connection(herminone, dumbledore, professional).

connection(molly, ron, familial).


%------------------------------------------------%
% Posts: user, date, relationship level, content %
%------------------------------------------------%
post(harry, date(5,24,1997), strong, 'I\'m presently safe in the Burrow.').
post(harry, date(9,8,2020), public, 'I\'m honoured to accept the post as Head of the Department of Magical Law Enforcement.').

post(ron, date(18,12,1993), public, 'Looking forward to the holidays!').
post(ron, date(15,1,1994), professional, 'I\'m really enjoying Care of Magical Creatures this year.').
post(ron, date(21,2,1994), strong, 'I didn\'t get enough sleep last night - better skip Care of Magical Creatures.').
post(ron, date(21,2,1994), familial, 'I hope my family doesnt see this.').


post(herminone, date(1,8,2019), public, 'I\'m honoured to accept the post as Minister of Magic.').

%-------------------------------%
% Part 2: Basic Rules & Queries %
%-------------------------------%

% Question 2.1: has_birthday_today
% Create a predicate that determines the user has a birthday today.

has_birthday_today(User) :-             
    today(Day, Month, _),                               % Compare todays date with the Users birthday.
    birthday(User, date(Day, Month, _)).

% Question 2.2: level_appropriate
% Contains three identifiers: user viewing posts, user with posts, relationship
% Determine if the user viewing content can see something posted by the second user with the given relationship level.

level_appropriate(_, _, public).                                % Every public acception is acceptable.

level_appropriate(Poster, Viewer, Priviledge) :-                % Establish a connection and ensure the Priveldge is in the acceptable range.
    connection(Viewer, Poster, professional),
    member(Priviledge, [professional]).

level_appropriate(Poster, Viewer, Priviledge) :-
    connection(Viewer, Poster, familial),
    member(Priviledge, [professional, familial]).

level_appropriate(Poster, Viewer, Priviledge) :-
    connection(Viewer, Poster, strong),
    member(Priviledge, [professional, familial, strong]).


% Question 2.3: view_posts
% Contains four identifiers: identifier for a user viewing posts, an identifier for a user with posts, a date for the posts, the content of the post
% Determine which post content the user viewing posts can see by the second user.

view_posts(Viewer, Poster, Date, Content) :-
    post(Poster, Date, A, Content), 
    level_appropriate(Poster, Viewer, A).


% Question 3.1: connected
% Contains two arguments: identifier for a first user, identifier for a second user
% Determine whether there is a connection, either directly or through other people, between the first user and the second user.

findConnection(FirstUser, SecondUser, Acc) :-
    connection(FirstUser, SecondUser, _), 
    not(member(SecondUser, Acc)).

findConnection(FirstUser, SecondUser, Accumulator) :-
    connection(FirstUser, Mutual, _),
    not(member(Mutual, Accumulator)),
    findConnection(Mutual, SecondUser, [FirstUser|Accumulator]).

connected(A, B) :-   
    findConnection(A, B, [A]).

% Question 3.2: remove_duplicates
% Contains two list arguments: the first must be bound, the second must be unbound.
% Create a second list which contains every unique element from the first list in no particular order.

remove_duplicates(A, B) :-              % Handle empty list case.
    rd_helper(A, [], B).

rd_helper([], A, A).            % Base Case

rd_helper([H|T], NT, Final) :-
    member(H, NT),                          % If the int exists, do not append anything to the new list
    rd_helper(T, NT, Final).

rd_helper([H|T], NT, Final) :-              % Append if the value is unique.
    not(member(H, NT)),
    rd_helper(T, [H|NT], Final).

% Question 3.3: network
% Contains two arguments: a bound user's identifier, a bound or unbound list of users' identifiers.
% Ensure the list contains the identifiers of all users that the first user is connected to, either directly or indirectly.

network(Name, Connections) :-
    findall(Z, connected(Name, Z), R), 
    remove_duplicates(R, Connections).          % Ensure uniqueness
    