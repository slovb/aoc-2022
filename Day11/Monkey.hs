module Day11.Monkey where

data Monkey = Monkey {
    index :: Int,
    items :: [Int],
    op :: Int -> Int,
    test :: Int -> Int,
    divider :: Int,
    count :: Int
}

type State = [Monkey]

getIndex :: Monkey -> Int
getIndex (Monkey index _ _ _ _ _) = index

incrementCount :: Monkey -> Monkey
incrementCount (Monkey index items op test divider count) = Monkey index items op test divider (count + 1)

getItems :: Monkey -> [Int]
getItems (Monkey _ items _ _ _ _) = items

addItem :: Int -> Monkey -> Monkey
addItem item (Monkey index items op test divider count) = Monkey index (items ++ [item]) op test divider count

composeOp :: (Int -> Int) -> Monkey -> Monkey
composeOp f (Monkey index items op test divider count) = Monkey index items (f . op) test divider count

getDivider :: Monkey -> Int
getDivider (Monkey _ _ _ _ divider _) = divider

getCount :: Monkey -> Int
getCount (Monkey _ _ _ _ _ count) = count

dispatch :: Monkey -> State -> State
dispatch (Monkey _ [] _ _ _ _) monkeys = monkeys
dispatch (Monkey index (item:items) op test divider count) monkeys = dispatch newMonkey newMonkeys
    where
        val = op item
        to = test val
        newMonkey = Monkey index items op test divider (count + 1)
        g monkey
            | getIndex monkey == index = newMonkey
            | getIndex monkey == to = addItem val monkey
            | otherwise = monkey
        newMonkeys = map g monkeys

simulate :: Int -> State -> State
simulate index monkeys
    | index == length monkeys = monkeys
    | otherwise = simulate (index + 1) newMonkeys
    where
        monkey = monkeys !! index
        newMonkeys = dispatch monkey monkeys
