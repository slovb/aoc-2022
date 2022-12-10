module Day10.Op ( Op, State, readOp, step, simulate ) where

type Op = (String, Int -> Int)
type State = [Int]

readOp :: String -> Op
readOp "noop" = ("noop", id)
readOp input = ("addx", (+y))
    where
        (_, _:part) = span (/= ' ') input
        y = read part

step :: State -> Op -> State
step xs ("noop", op) = xs ++ [last xs]
step xs ("addx", op) = xs ++ [last xs, op $ last xs]

simulate :: State -> [Op] -> State
simulate xs [] = xs
simulate state (op:ops) = simulate (step state op) ops
