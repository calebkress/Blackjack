data Card = Card { suit :: String, value :: Int }

data Deck = Deck [Card]

data Player = Player { name :: String, hand :: [Card] }

-- print a Player's hand
instance Show Card where
    show (Card suit value) = "Card { suit = " ++ suit ++ ", value = " ++ show value ++ " }"

-- take list of Cards and return value of hand
handValue :: [Card] -> Int
handValue cards = sum [value | Card {value = value} <- cards]

-- take Deck and Player, remove Card from Deck and add to Player
draw :: Deck -> Player -> (Deck, Player)
draw (Deck deck) player@(Player {hand = hand})
    | null deck = (Deck deck, player)
    | otherwise =
        let card = head deck
            newDeck = tail deck
            newHand = card : hand
        in (Deck newDeck, player {hand = newHand})

-- take Deck and Player, ask Player to draw until stay or bust
playHuman :: Deck -> Player -> IO (Deck, Player)
playHuman deck player = do
    putStrLn $ "Your hand is: " ++ show (hand player)
    putStrLn "Do you want to hit or stay? (h/s)"
    input <- getLine
    if input == "s" then
        return (deck, player)
    else
        let (newDeck, newPlayer) = draw deck player
        in
            if handValue (hand newPlayer) > 21 then
                return (newDeck, newPlayer)
            else
                playHuman newDeck newPlayer

-- take Deck and Player, implement basic logic for Dealer
playDealer :: Deck -> Player -> IO (Deck, Player)
playDealer deck player@(Player {hand = hand}) =
    if handValue hand >= 17 then
        return (deck, player)
    else
        playDealer newDeck newPlayer
    where
        (newDeck, newPlayer) = draw deck player

main :: IO ()
main = do
    let deck = Deck [Card "Spades" 2, Card "Spades" 3, Card "Spades" 4, Card "Spades" 5, Card "Spades" 6, Card "Spades" 7, Card "Spades" 8, Card "Spades" 9, Card "Spades" 10, Card "Spades" 11,
                     Card "Hearts" 2, Card "Hearts" 3, Card "Hearts" 4, Card "Hearts" 5, Card "Hearts" 6, Card "Hearts" 7, Card "Hearts" 8, Card "Hearts" 9, Card "Hearts" 10, Card "Hearts" 11,
                     Card "Diamonds" 2, Card "Diamonds" 3, Card "Diamonds" 4, Card "Diamonds" 5, Card "Diamonds" 6, Card "Diamonds" 7, Card "Diamonds" 8, Card "Diamonds" 9, Card "Diamonds" 10, Card "Diamonds" 11,
                     Card "Clubs" 2, Card "Clubs" 3, Card "Clubs" 4, Card "Clubs" 5, Card "Clubs" 6, Card "Clubs" 7, Card "Clubs" 8, Card "Clubs" 9, Card "Clubs" 10, Card "Clubs" 11]

    let (deck1, player1) = draw deck (Player "Player 1" [])
    let (deck2, player2) = draw deck1 (Player "Player 2" [])

    -- ask player 1 to play
    (finalDeck1, finalPlayer1) <- playHuman deck2 player1

    if handValue (hand finalPlayer1) > 21 then do
        putStrLn "You busted"
        putStrLn "Dealer wins"
    else do
        -- ask player 2 to play
        (finalDeck2, finalPlayer2) <- playDealer finalDeck1 player2
        if handValue (hand finalPlayer2) > 21 then do
            putStrLn "Dealer busts"
            putStrLn "You win"
        else do
            -- compare hands and determine winner
            let player1Score = handValue (hand finalPlayer1)
            let player2Score = handValue (hand finalPlayer2)
            if player1Score > player2Score then do
                putStrLn "You win"
            else if player2Score > player1Score then do
                putStrLn "Dealer wins"
            else do
                putStrLn "It's a tie"