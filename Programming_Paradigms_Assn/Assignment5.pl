% Description: Complete the requirements set forth in the assignment description.
% Author: Michael Krakovsky  
% Date: April 6, 2019
% Version: 1.0

% Sample Facts Please Ignore:

mmyws(ium+titan/2010/300/224507).
mmyws(ium+titan/2011/300/262391).
mmyws(ium+titan/2012/400/267041).
mmyws(ium+titan/2013/500/268842).
mmyws(ium+titan/2014/500/263528).

mmyws(ium+pluton/2010/300/99356).
mmyws(ium+pluton/2011/300/76184).
mmyws(ium+pluton/2012/300/65830).

mmyws(ium+zircon/2010/400/326624).
mmyws(ium+zircon/2011/400/337295).
mmyws(ium+zircon/2012/500/332653).
mmyws(ium+zircon/2013/500/330106).
mmyws(ium+zircon/2014/500/335865).

mmyws(cosmos+dyne/2010/400/145522).
mmyws(cosmos+dyne/2011/500/149490).
mmyws(cosmos+dyne/2012/500/151870).
mmyws(cosmos+dyne/2013/500/149911).
mmyws(cosmos+dyne/2014/500/149405).

mmyws(cosmos+flux/2010/300/106221).
mmyws(cosmos+flux/2011/300/105672).
mmyws(cosmos+flux/2012/300/105079).
mmyws(cosmos+flux/2013/300/110415).

mmyws(cosmos+orbit/2010/400/85164).
mmyws(cosmos+orbit/2011/400/82390).

% --------------------------------------------------------- %

% Question 1.1: currency_round
% Contains two identifiers: a numeric value (bound), a numeric value (bound or unbound)
% The predicate must round the first argument to two decimal places and bind or compare the value to the second argument.

currency_round(FloatingPoint, PossibleBinder) :- 
    Temp is FloatingPoint * 10^2, 
    round(Temp, NewTemp), 
    PossibleBinder is NewTemp / 10^2, 
    !.                                      % If we make it here, we do not want to call the next function.

currency_round(FloatingPoint, PossibleBinder) :-            % If both variables are bound, we round them and compare them.
    currency_round(FloatingPoint, Number1),
    currency_round(PossibleBinder, Number2),
    Number1 =:= Number2.

% --------------------------------------------------------- %

% Question 2.2: recall_information
% Define two arguments: a unbound variable to contain list of structures of the form Make-Model-Year (unbound),
% a numeric value (bound or unbound).
% The predicate must determine which vehicles are involved in the recall and the total cost of the recall rounded to two decimal places.

print_list([]).

print_list([Head|Tail]) :-
  format('~w~n', Head),
  print_list(Tail).


recall_information(StructList, TC) :-
    findall(Get, mmyws(Get), List),                 % Get all the model information to traverse through.
    recall_information_helper(List, StructList, FindCost), 
    currency_round(FindCost, TC),                   % Round the final currency.
    !.

recall_information_helper([], [], 0).

recall_information_helper([Make+Model/Year/Type/NumCars|Tail], [Make-Model-Year | NewTail], FindCost) :-
    Type =:= 300,
    recall_information_helper(Tail, NewTail, NextCost), 
    FindCost is NextCost + (NumCars*728.63).

recall_information_helper([Make+Model/Year/Type/NumCars|Tail], [Make-Model-Year | NewTail], FindCost) :-
    Type =:= 400,
    recall_information_helper(Tail, NewTail, NextCost), 
    FindCost is NextCost + (NumCars*439.52).            

recall_information_helper([_Make+_Model/_Year/_Type/_NumCars|Tail], NewTail, FindCost) :-
    recall_information_helper(Tail, NewTail, FindCost).             % Propogate further

% Question 2.1: foldl1
% Three arguments: a predicate (bound), a list of values (bound), a numeric value (bound or unbound)
% Calculate the result of folding the values in the list in the same manner as foldl1 in Haskell and bind or compare the value to the third argument.

% Used For Testing... Please Ignore %
subtract(X, Y, Z) :-
    Z is X - Y.
% --------------------------------- %

foldl1_helper(_, [Head], Binder) :-
    Binder = Head, 
    !.                                  % Reached the end, do not continue further.
    
foldl1_helper(Function, [Head, Second | Tail], Binder) :-
    call(Function, Head, Second, X),
    foldl1_helper(Function, [X | Tail], Binder).

foldl1(Function, List, Binder) :-
    foldl1_helper(Function, List, Z),
    Binder = Z.                                 % Compare the Bound variable or assign it a new value.

% Question 2.2: foldr1
% Three arguments: a predicate (bound), a list of values (bound), a numeric value (bound or unbound)
% Calculate the result of folding the values in the list in the same manner as foldr1 in Haskell and bind or compare the value to the third argument.

foldr1(_, [Last], Last).                                % Reached the end, start binding variables

foldr1(Function, [Head | Tail], Binder) :-
    foldr1(Function, Tail, NewBinder),                  % Traverse to the list end, provide a fresh variable to bind to.
    call(Function, Head, NewBinder, Binder), 
    !.
