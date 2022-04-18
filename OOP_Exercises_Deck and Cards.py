#!/usr/bin/env python
# coding: utf-8

# 
# # Exercise 2: Deck
# Create `Deck` and `Card` classes. Your requirements are:
# * The `Card` class should have a `suit` (Hearts, Diamonds, Clubs, Spades) and a `value` (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)
# * Add `__str__` method to `Card` class. 
# * Create a Deck class, no parameters needs to be given. But it should have attribute `cards`. You can keep cards in a list.
# * The `Deck` class should have a `deal` method to deal a single card from deck
# * After a card is dealt, it is removed from the deck. If deck is empty raise a ValueError 
# * There should be a `shuffle` method which makes sure the deck of cards has all 52 cards and then rearranges them randomly. If there are not 52 cards raise a ValueError. 
# * Add `__str__` method to Deck class representing cards

# In[1]:


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['A', '2', '3', '4', '5', '6', '7','8' , '9', '10', 'J', 'Q', 'K']
import random

class Card:
    def __init__(self,suit,value):
        self.suit=suit
        self.value=value
        
    def __str__(self):
        return f'{self.suit}-{self.value}'
    
class Deck:
    def __init__(self):
        self.cards=[]
        for suit in suits:
            for value in values:
                card=Card(suit,value)
                self.cards.append(card)
            
    def deal(self):
        if len(self.cards)==0:
            raise ValueError('Deck is empty')
        else:
            return self.cards.pop()
            
    def shuffle(self):
        if len(self.cards)!=52:
            raise ValueError('The Deck is not full')
        else:
            return random.shuffle(self.cards)
            
    def __str__(self):
        return f'there are {len(self.cards)} cards in Deck' 
    
    def printDeck(self):
        for card in self.cards:
            print(card)
    
    


# In[ ]:




