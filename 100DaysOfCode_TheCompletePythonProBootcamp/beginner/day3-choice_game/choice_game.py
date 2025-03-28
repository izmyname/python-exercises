print(r'''





                                    _______________________________________
                                   |,--------------_----------------------.|
                                   ||______ __,---'_ |         ||--.   || ||
                                   ||__,--'| _,---' ||         ||   )  || ||
           ______________________  ||__,-: ||       ||         ||--' * || ||
     __,--'                __,--'| ||;-. : ||      __:         || .    || ||
 ,-_'__________________,--'__,-: | ||/ '>: ||    ,%%%%%.       ||   )) || ||
 |'.      .   ______ ,'| -',--.: | ||):' : ||   |%%" o \       ||   (  ||*||
 ||.'.    .  /,----,',|| :<' \/: | || )) : ||   \%|o 7 |       ||__|"|_||_||
 || ||    . //   ,',' || : `;( : | ||'/  : ||    \%`..'(____   ||""|_|"||"||
 || ||    .||    ||   || : (( `: __  :: ,mMMm.    %%,  " )  `. ||__"""_||_||
 || ||    .||:   ||   || :  \` ,%%%%%. |MMMMMm     / `--' _)  \`----------||
 || ||    .||:   ||   || :  ;; %%%%%%%.-"MMMM/    |  | _)   |\ \      =o.,||
 || ||    .||:   ||   || : __,  \%_%%_|   `",      \ \_,_ _,\| |        |o||
 || ||    .||:   ||   || ''      /     `-._/        `._\_)  =o.,o=     _|_||
 || ||    .||:   ||   ||        ;          `-.  ____:|________|o=______)_(||
 || ||    .||::  ||   ||       /  ,           \  ------------_|_ ----------'
 || ||    .||::  ||   ||      |  <;     `.     \ ___________ ) ( ___________
 || ||    .||::  ||   ||    _ `._/;         /  |            (___)      __,--|
 || (|    .||::: ||)  ||_-'______ ;._       |  ; __________________,--'     |
 || ||    .||::: ||   ||`.______, |._`--...-|,' ______,'|`.______,'|        |
 || ||    .||::: ||   || |      | |  `--...-|: |      | | |      | |        |
 || ||    .||::::||   || | :    | ;         || |:     |o|o|:     | |        |
 || ||    ._\\:::||   || |  ::  | |     :   || |::    | | |:::   | |        |
 || ||_,-'   \\__||   || |___::_| :         || |______| | |__::__| |   __,--'
 |'.||________`-_||  ,'|,_______`_|         ||,_______`_|,'______`_|--'
  `. |           ||,','           |  .      :
____`|  ________ |_,'___________  ;      :  |  ______________________________
.*,--.*,--.*,--.*,--.*,--.*,--.* ;__;    :   \ ,--.*,--.*,--.*,--.*,--.*,--.*
'jrei' `--' `--' `--' `--' `--' `  |`'---..__; `--' `--' `--' `--' `--' `--'
,--.*,--.*,--.*,--.*,--.*,--.*,--. '--'  '--' --.*,--.*,--.*,--.*,--.*,--.*,-
''')
print("Welcome to the Night Hunt.")
print("You're a vampire. Your goal is to find a victim and drain their blood.")

# Stage 1-1
choice1 = str(input("You're in a dark, abandoned mansion. There are two doors before you. One is to your left, the other"
                    " is to you right."
                    " Where do you want to go?\n").lower())
if choice1 == "left":
    choice2 = str(input ("You enter a big ballroom. There's a big door on the opposite side. Do you want to run  towards"
                       " the door or walk carefully?\n").lower())
    if choice2 == "walk":
        choice3 = str(input(" You enter a  corridor. In the corridor, there are three doors - silver, golden and wooden"
                            " - which one will you enter?\n").lower())
        if choice3 == "silver":
            print("Once you touched the door - the holy silver metal burned you alive. Game over")
        elif choice3 == "golden":
            print("There was a vampire hunter behind the door. He shoots you with the crossbow. Game over.")
        elif choice3 == "wooden":
            print("There's a shrine with the fountain of blood. You satisfy your urge and ascend as a higher vampire. "
                  "You win!")
        else:
            print("Unsure where to go, you waited long enough for the night to end, and the first rays of sunlight,"
                  " coming through the windows, burned you alive. Game over.")
    else:
        print("While running, you don't notice a stake, laying on the floor. Game over")
else:
    print("You lost within the mansion. While you were wandering around till the night ended and the light, shining "
          "from the windows, burned you. Game over")

