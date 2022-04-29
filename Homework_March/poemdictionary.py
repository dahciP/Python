poems = {"1. Ba Ba Black Sheep" : "Baa, baa black sheep\nHave you any wool\nYes sir, yes sir\nThree bags full.\n\nOne for my master\nAnd one for my dame\nAnd one for the little boy\nWho lives down the lane.", 
      "2. Humpty Dumpty" : "Humpty Dumpty sat on a wall,\nHumpty Dumpty had a great fall.\nAll the King's horses and all the King's men,\nCouldn't put Humpty together again.", 
      "3. Hickory Dickory Dock" : "Hickory Dickory Dock\nGently bounce your baby to the beat\nThe mouse ran up the clock\nRun your fingers up from your baby's toes to their chin and give them a tickle\nThe clock struck one\nClap your hands together once\nThe mouse ran down\nRun your fingers back down to your baby's toes and tickle them\nHickory Dickory Dock", 
      "4. Twinkle Twinkle Little Star" : "Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\n\nWhen the blazing sun is gone,\nWhen he nothing shines upon,\nWhen you shower your little light,\nTwinkle, twinkle, all the night.\n\nThen the traveller in the dark,\nThanks you for your tiny spark,\nHe could not see which way to go,\nIf you did not twinkle so.",
      "5. Ten Little Indians" : "Ten little Indian boys went out to dine;\nOne choked his little self and then there were nine.\n\nNine little Indian boys sat up very late;\nOne overslept himself and then there were eight.\n\nEight little Indian boys traveling in Devon;\nOne said he’d stay there and then there were seven.\n\nSeven little Indian boys chopping up sticks;\nOne chopped himself in halves and then there were six.\n\nSix little Indian boys playing with a hive;\nA bumblebee stung one and then there were five.\n\nFive little Indian boys going in for law,\nOne got in Chancery and then there were four.\n\nFour little Indian boys going out to sea;\nA red herring swallowed one and then there were three.\n\nThree little Indian boys walking in the Zoo;\nA big bear hugged one and then there were two.\n\nTwo little Indian boys sitting in the sun;\nOn got frizzled up and then there was one.\n\nOne little Indian boy left all alone;\nHe went and hanged himself and then there were none.",
      "6. Rock-a-Bye Baby" : "Rock a bye baby, on the tree top,\nWhen the wind blows the cradle will rock,\nWhen the bough breaks the cradle will fall,\nAnd down will come baby, cradle and all.",
      "7. If you're happy and you know it" : "If you're happy and you know it, clap your hands.\n(clap clap)\nIf you're happy and you know it, clap your hands.\n(clap clap)\nIf you're happy and you know it, then your face will surely show it.\nIf you're happy and you know it, clap your hands.\n(clap clap)",
      "8. Golden Slumbers" : "Golden slumbers kiss your eyes,\nSmiles await you when you rise.\nSleep, pretty baby, do not cry,\nAnd I will sing a lullaby.\n\nCare you know not, therefore sleep\nWhile over you a watch I’ll keep.\nSleep, pretty darling, do not cry,\nAnd I will sing a lullaby.",
      "9. Ding Dong Bell" : "Ding, dong, bell,\nPussy’s in the well.\nWho put her in?\nLittle Johnny Flynn.\nWho pulled her out?\nLittle Tommy Stout.\nWhat a naughty boy was that,\nTo try to drown poor pussy cat,\nWho never did him any harm,\nBut killed all the mice in the farmer's barn.",
      "10. Little Jack Horner" : "Little Jack Horner\nSat in the corner,\nEating a Christmas pie;\nHe put in his thumb,\nAnd pulled out a plum,\nAnd said, 'What a good boy am I!'"
      }

for key in poems:
    print(key)

c = 1
while c==1:
    x = int(input("\nEnter the desired number of poem: \n"))
    if x==1:
        print(poems['1. Ba Ba Black Sheep'])
    elif x==2:
        print(poems['2. Humpty Dumpty'])
    elif x==3:
        print(poems['3. Hickory Dickory Dock'])
    elif x==4:
        print(poems['4. Twinkle Twinkle Little Star"'])
    elif x==5:
        print(poems['5. Ten Little Indians'])
    elif x==6:
        print(poems['Rock-a-Bye Baby'])
    elif x==7:
        print(poems["7. If you're happy and you know it"])
    elif x==8:
        print(poems['8. Golden Slumbers'])
    elif x==9:
        print(poems['9. Ding Dong Bell'])
    elif x==10:
        print(poems['10. Little Jack Horner'])
    else:
        print("Input Error")
    c = int(input("\nIf you wish too continue press 1 else press 0: "))

#Code by Chinmay Pichad