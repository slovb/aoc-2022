module Day11.Input where

import Day11.Monkey
    ( State, Monkey(..) ) 

readIndex :: String -> Int
readIndex index = read (init . last $ words index) :: Int

readItems :: String -> [Int]
readItems xs = do
    let (_, _:_:part) = span (/= ':') xs
    -- let a = words part
    -- let b = map (takeWhile (/= ',')) a
    -- [read x | x <- b]
    read ("[" ++ part ++ "]")

readOp :: String -> (Int -> Int)
readOp xs = do
    let parts = words xs
    let (a, b, c) = (parts !! 3, parts !! 4, parts !! 5)
    let left x = if a == "old" then x else read a
    let op = if b == "*" then (*) else (+)
    let right x = if c == "old" then x else read c
    \x -> op (left x) (right x)

readTest :: String -> String -> String -> (Int -> Int)
readTest test ifTrue ifFalse = do
    let divider = read (last $ words test) :: Int
    let trueN = read (last $ words ifTrue) :: Int
    let falseN = read (last $ words ifFalse) :: Int
    \x -> if mod x divider == 0 then trueN else falseN

readDivider :: String -> Int
readDivider test = read (last $ words test) :: Int

readInput :: [String] -> State
readInput [] = []
readInput ("":rest) = readInput rest
readInput (idText:items:op:test:ifTrue:ifFalse:rest) = do
    let monkey = Monkey {
        index=readIndex idText,
        items=readItems items,
        op=readOp op,
        test=readTest test ifTrue ifFalse,
        divider=readDivider test,
        count=0
    }
    monkey:readInput rest
