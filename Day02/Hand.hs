module Day02.Hand where

data Hand = Rock | Paper | Scissors deriving (Show, Eq)

instance Ord Hand where
    compare Rock Rock = EQ
    compare Paper Paper = EQ
    compare Scissors Scissors = EQ
    compare Rock Paper = LT
    compare Paper Scissors = LT
    compare Scissors Rock = LT
    compare _ _ = GT

handScore :: Hand -> Integer
handScore Rock = 1
handScore Paper = 2
handScore Scissors = 3

vsScore :: Hand -> Hand -> Integer
vsScore left right
    | left < right = 6
    | left == right = 3
    | otherwise = 0

stronger :: Hand -> Hand
stronger Rock = Paper
stronger Paper = Scissors
stronger Scissors = Rock

weaker :: Hand -> Hand
weaker Rock = Scissors
weaker Paper = Rock
weaker Scissors = Paper
