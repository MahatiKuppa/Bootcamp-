lizard = """
   _.-~~-.__
 _-~ _-=-_   ''-,,
('___ ~~~   0     ~''-_,,,,,,,,,,,,,,,,
 \~~~~~~--'                            '''''''--,,,,
  ~`-,_      ()                                     '''',,,
       '-,_      \                           /             '', _~/|
  ,.       \||/~--\ \_________              / /______...---.  ;  /
  \ ~~~~~~~~~~~~~  \ )~~------~`~~~~~~~~~~~( /----         /,'/ /
   |   -           / /                      \ \           /;/  /
  / -             / /                        / \         /;/  / -.
 /         __.---/  \__                     /, /|       |:|    \  
/_.~`-----~      \.  \ ~~~~~~~~~~~~~---~`--- \---__ \:\    /  /
                  `\`                     ' ' '    --\, /  /
                                               '\,        ~-_'''"
"""

spock = '''
                         .ss$$$$$$$$$$$$$$$ss.
                       .s$$$$$$$$$$$$$$$$$$$$$$$$$$ss.
                   .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                 .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.
               .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
             .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s.
            $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        .$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$                                  $$
        $$$$$$$$$$$$$$$$$$     .
       s$$$$$$$$$$$$$$$$$     sssss.                           s
      ss $$$$$$$$$$$$$$$          ssss                      ss$s
     sss   $$$$$$$$$$$            ssss$$$$ss              $$$$s.
    sssss   $$$$$$$$   s.      .sss$$$$$$$$sss      sss$$$$$$s
    ss$ssss  $$$$$$$  sss.  .ss$$$$$$ss$ss     .         s$$$$s.
    ss$s   s  $$$$$$ ss.ss           ..        ss           .sss
     ss   s $s $$$$$ ss..s.                   ss
      s ss$$$$s $$$$ ssssss.                 .ss
    ss     s$$$s $$$ ssssssssss..           ssss.              .
    ss      $$  s $$ ss..ss$$$$sss        .sssss              ..
     s      s$$ss  $ ssss.sss$$$sss       .sssss.     ss..
      s.     $     $ .sss . .ss$sss        .  sssssss...   ss$
        ss   sssss$$ ..ss   ...sssss            .sss.       s
          ss    $$ $ .ss..s .sssssss
            ss$$  $$  .ssssss .sssss              ..       $
                $$$$  .ss$$ssss...s.s        ..sss$$ssss.
               $$.$$$  .ss$$sss.. sss.    .ssss$$s..s$ss. s
               ss ssss  .sssssss...sss.      .ssss$$ss..  .
               ss  ssss   .ssssssss.sss.        .sss.
               ss    .ssss    .sssssssss.               s
               ss      .sssss.  .sssssss.s .. ..ss$s. .s
              ss         sssssss.  .sssssssssssss$$s. .ss
            $ss           ssssssss.   ..sssssssssss  .ss.
          $$$$.            .sssssssss.     ssssss ssss.$s
      s$$$$$$$$s.             ..ssssssssss......ssss. s$$$s
    .s$$$$$$$$$$$s.              .ssssssssssssssss. s$$$$$ss.
       s$$$$$$$$$$$$$$ss..          .ssssssssss. .s$$$$$$$$s
         s$$$$$$$$$$$$$$$$$$$ssss...   ...ss.. s$$$$$$$$$s
           s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
              .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                    .s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$s
                          .s$$$$$$$$$$$$$$$$$$$$s
                                ..s$$$$$$$$$$s
'''

scissors = '''
    ______
___'  ____)______
        _________)
      _________)
      (____)
---.__(___)
'''

rock = '''
    ______
---' ________)
    (_________)
    (_________)
    (________)
--__(____)
'''

paper = '''
     _______
____'   ____)____
        _________)__
        ____________)
        ___________)
-----.__________)
'''

list = [rock, paper, scissors, spock, lizard]

import random

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors, 3 for lizard, 4 for spock."))
computer_choice = random.randint(0,4)

# if user_choice == computer_choice:
#     print("It's a draw")
# else:
#     if user_choice == rock:
#         if computer_choice == paper:
#             print("You win")
#         else:
#             print("You lose")
#     elif user_choice == paper:
#         if computer_choice == rock:
#             print("You win")
#         else:
#             print("You lose")
#     else:
#         if computer_choice == rock:
#             print("You lose")
#         else:
#             print("You win")

# if user_choice == 2 and computer_choice == 0:
#     print("You lose")
# elif user_choice == 0 and computer_choice == 2:
#     print("You win")
# elif user_choice > computer_choice:
#     print("You win")
# elif user_choice == computer_choice:
#     print("It's a draw")
# else:
#     print("you lose")

print(f"You chose:\n {list[user_choice]}")
print(f"Computer chose:\n {list[computer_choice]}")

if user_choice > computer_choice:
    if (user_choice - computer_choice)%2 == 0:
        print("You lose")
    else:
        print("You win!")
elif user_choice < computer_choice:
    if (user_choice - computer_choice)%2 == 0:
        print("You win!")
    else:
        print("You lose")
elif computer_choice == user_choice:
    print("It's a draw")
elif user_choice>=4:
    print("Invalid number")

