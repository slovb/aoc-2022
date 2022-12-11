module Day11.Solution (main) where

import System.IO
    ( hClose, hGetContents, openFile, IOMode(ReadMode) )

data Monkey = Monkey {
    items :: [Int],
    op :: Int -> Int,
    test :: Int -> Int
}

readItems :: String -> [Int]
readItems xs = do
    let (_, _:_:part) = span (/= ':') xs
    let a = words part
    let b = map (fst . span (/= ',')) a
    [read x | x <- b]

readOp :: String -> (Int -> Int)
readOp xs = do
    let (_, _:_:part) = span (/= ':') xs
    -- need sleep

readInput :: [String] -> [Monkey]
readInput [] = []
readInput ("":rest) = readInput rest
readInput _:items:op:test:ifTrue:ifFalse:rest = do
    let monkey = Monkey {
        items=readItems items,
        op=readOp op,
        test=readTest test ifTrue ifFalse
    }
    monkey:readInput rest

-- solve :: [Monkey] -> Int
-- solve ops = sum records
--     where
--         xs = simulate [1] ops
--         extract xs i = (xs !! (i - 1)) * i
--         records = map (extract xs) [20, 60, 100, 140, 180, 220]
    
main :: IO ()
main = do
    let day = "Day11"
    let test = True
    let filename = day ++ if test then "/test.txt" else "/input.txt"
    handler <- openFile filename ReadMode
    contents <- hGetContents handler
    let xs = lines contents
    let monkeys = readInput xs
    print [monkey.items | monkey <- monkeys]
    -- let output = solve ops
    -- print output
    hClose handler
