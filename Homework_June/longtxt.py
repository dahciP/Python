string_words = '''In a bid to contain Shivaji, Adil Shah sent Afzal Khan, an experienced veteran general along with an army of 40,000 men to destroy Shivaji. 
Upon weighing his options carefully as to what action must be taken, Shivaji decided to meet Afzal Khan on his home turf at the base of the Pratapgarh fort insisting that the meeting be an informal one. 
He sent a letter to Afzal Khan stating that he was eager for it. 
Afzal agreed.
At the meeting, Afzal Khan stabbed Shivaji in the back when the two embraced each other. 
Shivaji was well prepared for this and survived the attack, protected by a chain mail armour he was wearing and counter-attacked by slaying Afzal Khan with the wagh nakh (tiger-claws glove). 
Afzals army who were prepared to attack had no idea that their leader had been slain when Shivaji walked out with the decapacitated head of Afzal Khan on his sword. 
On seeing this the the army surrendered.'''


word_list = string_words.split()
word_freq = [word_list.count(n) for n in word_list]
print("String: \n {} \n".format(string_words))
print("List: \n {} \n".format(str(word_list)))
print("Pairs: \n {} \n".format(str(list(zip(word_list,word_freq)))))
