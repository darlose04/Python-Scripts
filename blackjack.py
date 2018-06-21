'''
This is a blackjack game between one player and a dealer. 
It does not take in any bets(yet)
'''

import random

deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,
              10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,11,11,11,11]*5
random.shuffle(deck)

#creates lists for the player and dealer hands
player_hand = []
dealer_hand = []
#creates empty string used later when asking player to hit or stay
player_choice = ''

def dealing_cards():
    print('Dealing cards...')
    #adds cards to the player and dealer hands
    #player hand is printed while only one of the dealer's cards is printed
    player_hand.append(deck.pop())
    
    dealer_hand.append(deck.pop())
    
    player_hand.append(deck.pop())
    print('Player cards: {}'.format(player_hand))
    print(sum(player_hand))
    
    dealer_hand.append(deck.pop())
    print('Dealer card showing: {}'.format(dealer_hand[1]))

def player_turn():
    #this determines whether or not the player will add more cards to their hand based on the sum of their hand
    while sum(player_hand) <= 21:

        player_choice = input('You have %s: Would you like to hit or stay? Enter hit or stay: ' %(sum(player_hand))).lower()
        
        if player_choice == 'hit':
            player_hand.append(deck.pop())
            print('Player cards: {}'.format(player_hand))
            #if there is an 11 in the hand, it can be counted as 1 if the sum of the hand is greater than 21
            if 11 in player_hand and sum(player_hand) >= 21:
                new_player_hand = (sum(player_hand) - 10)
                print(new_player_hand)
            else:
                print(sum(player_hand))
            
        elif player_choice == 'stay':
            return sum(player_hand)
        

def dealer_turn():
    
    print('Dealer hand: {}'.format(dealer_hand))
    print(sum(dealer_hand))
    #if the sum of the dealer's hand is less than 17, they have to hit until reaching 17 or higher
    while sum(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print('Dealer hand: {}'.format(dealer_hand))
        #same as with 11 being in the player's hand
        if 11 in dealer_hand and sum(dealer_hand) >= 21:
            new_dealer_hand = sum(dealer_hand) - 10
            print(new_dealer_hand)
        else:
            print(sum(dealer_hand))
    #if the sum of the dealer's hand is between 16 and 22, the dealer will stay
    if sum(dealer_hand) >= 17 and sum(dealer_hand) <= 21:
        print(sum(dealer_hand)) 

def win_or_lose():
    #this function deetermines the different winning and losing scenarios for the player and dealer
    if 11 in player_hand and sum(player_hand) > 21:
        player_turn()
    elif sum(player_hand) > 21:
        print('PLAYER BUSTS, DEALER WINS')
    elif sum(player_hand) > sum(dealer_hand):
        print('PLAYER WINS')
    elif 11 in dealer_hand and sum(dealer_hand) > 21:
        dealer_turn()
    elif sum(dealer_hand) > 21:
        print('DEALER BUSTS, PLAYER WINS')   
    elif sum(dealer_hand) > sum(player_hand):
        print('DEALER WINS')
    elif sum(player_hand) == sum(dealer_hand):
        print('PUSH')
        
def replay():
    #this function asks the player if they want to play again
    return input('Do you want to play again? Enter yes or no: ').lower().startswith('y')

    
while True:
    
    print('Welcome to blackjack!')
    
    play_game = input('Are you ready to play blackjack? Enter yes or no: ')
    #determines if the player is ready to play the game or nota
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        player_hand = []
        dealer_hand = []
        #calls the functions defined above in order to play the game
        dealing_cards()
        player_turn()
        dealer_turn()
        win_or_lose()
        break
        
    if replay():
        #if the player wants to play again, this resets the hands for the next game
        del player_hand[:]
        del dealer_hand[:]
    else:
        break



