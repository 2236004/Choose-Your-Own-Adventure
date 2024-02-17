from symbol import while_stmt
from textwrap import fill as raptext
import textwrap


tryagain = "y"
while tryagain.lower() == "y":
    
        
        
        player_is_dead = None
        player_friend_dead = None
        Outlaw = None
        print("\n")
        print(raptext("Welcome! I'm thrilled to share an exciting story with you. But before we dive in, I'd like to ask you a few questions. After typing your answers, remember to press the enter key to proceed. Let's embark on this journey together!"))
        print("\n")

        while True:
            try:
                name = input("What is your character's name?:  ")
            except ValueError:
                print("I don't understand")
                continue
            if name.isdigit():
                print ("That is a number")
                continue
            if name and not name.isdigit():
                break
            else: 
                print("Answer cannot be blank!")
                continue
     

        while True:
            try:
                friend = input("What the name of your best freind?:  ")
            except ValueError:
                print("I don't understand.")
                continue
            if friend.isdigit():
                print ("That is a number")
                continue
            if friend and not friend.isdigit():
                break
            else: 
                print("Answer cannot be blank!")
                continue
    

        while True:
            try:
                location = input("Where does our adventure take place?:  ")
            except ValueError:
                print("I don't understand.")
                continue
            if location.isdigit():
                print ("That is a number")
                continue
            if location and not location.isdigit():
                break
            else: 
                print("Answer cannot be blank!")
                continue
        

        while True:
            try:
                years = int(input("Choose a number from 1 to 100:  "))
            except ValueError:
                print("You must enter a number greater then 0")
                continue
            if years >= 1: 
                break
            print ("You must enter a number greater then 0")
            continue
    
        while True:
            try:
                dream = input("What is your character's dream?:  ")
            except ValueError:
                print("I don't understand.")
                continue
            if dream:
                break
            else: 
                print("Answer cannot be blank!")
                continue
    
        print("\n")
        print(raptext(f"{name} awakens to a world of shadows and secrets within the dimly lit confines of a high-security prison. The air hangs heavy with the weight of despair, and the constant clanking of metal against metal reverberates through the narrow corridors, a continual reminder of captivity. Amidst the bleakness, {name} finds themselves alongside their friend {friend}, both unjustly imprisoned for a crime they did not commit. Their pasts are shrouded in mystery, their presents confined within the unforgiving walls of the prison. Sentenced to {years} year(s) of imprisonment, they are victims of circumstance, pawns in a game of power and corruption. Despite their innocence, they have accepted their fate with stoic resignation, determined to survive the ordeal with dignity intact. As they navigate the harsh realities of prison life, {name} and {friend} cling to the hope of eventual redemption, their unwavering bond serving as a beacon of light in the darkness of their shared confinement."))
        print("\n")    
        
        while True:
            try:
                rules = input("Do you follow the rules or break them? Follow or Break:  ").lower()
                print("\n")
            except ValueError:
                print("I don't understand.")
                continue
            if rules == "follow" or rules == "break":
                break
            else: 
                print("Please answer with 'Follow' or 'Break'!")
                print("\n")
                continue

        while rules == 'break':
            try:
                print(raptext(f"As {name} walks through the dimly lit corridors of the prison, they feel a strong sense of injustice weighing heavily on their shoulders. The unfairness of their situation gnaws at them relentlessly. Seeking solace, {name} turns to {friend} and asks to challenge the unjust system. Together, they vow to fight for their rights and seek redemption amidst the darkness of captivity."))
                print("\n")
                plans = input(f"{friend} asks you to pick from two plans. Tunnal or Disguise:   ").lower()
                print("\n")
            except ValueError:
                print("I don't understand.")
                continue
            if plans == "tunnal" and years >= 5:
                player_is_dead = True
                player_friend_dead = True
                Outlaw = None
                break
            elif plans == "tunnal" and years >= 1:
                print(raptext(f"In their confinement, {friend} and {name} conceived a daring plan a tunnel to freedom, a passage out of incarceration. Fuelled by the allure of imminent release, they labored tirelessly, chiseling away at the earth with fiery determination. Yet, in their zeal, they overlooked a crucial truth: the length of their sentence paled compared to the time it took to excavate their subterranean route to liberty. As the days stretched into weeks and the tunnel's end remained elusive, the folly of their endeavor became painfully apparent. What good is the promise of legal release when one's impatience closes their eyes to the passage of time? Their tunnel, a symbol of misguided hope, now serves as a stark reminder of the limits of human ambition and the folly of chasing shadows in the pursuit of freedom. {friend} gets released back out into {location}"))
                print("\n")
                player_is_dead = False
                player_friend_dead = None
                Outlaw = None
                break 
            elif plans == "disguise":
                print(raptext(f"In their confinement, {friend} and {name} devised a daring scheme to acquire disguises, the key to their swift escape from the confines of their imprisonment. With careful planning and steely resolve, they orchestrated a daring heist, seizing the necessary attire from unsuspecting guards and fellow inmates alike. Cloaked in their newfound identities, they slipped through the shadows of the prison undetected, their hearts pounding with anticipation as they navigated the labyrinthine corridors to freedom. In less than a week, they emerged from the prison gates, their disguises serving as a shield against scrutiny and suspicion. As they stepped out into the city's bustling streets, a sense of exhilaration washed over them, mingled with the thrill of their audacious escape. For {friend} and {name}, the journey to liberty was a testament to their cunning and resourcefulness and a triumph of the human spirit in the face of adversity. With every step forward, they embraced the promise of a new beginning, their spirits unbroken by the trials of their past into {location}."))
                print("\n")
                player_is_dead = False
                player_friend_dead = None
                Outlaw = True
                break
            else:
                print("Please answer with 'Tunnal' or 'Disguise'!")
                print("\n")
                continue
    
        while rules == 'follow':
            try:
                print(raptext(f"As {name} walks through the dimly lit corridors of the prison, they feel a strong sense of injustice weighing heavily on their shoulders. The unfairness of their situation gnaws at them relentlessly. Seeking solace, they turn to their friend {friend} and ask if they want to join in challenging the unjust system. While {friend} is determined to escape and seek freedom, {name} believes in the system's ability to uncover the truth and grant them justice. Despite the temptation to break free, {name} chooses to abide by the rules and await the day when their innocence will be recognized, and they will be released legally."))
                print("\n")
                plans = input(f"Do you convince {friend} to wait out his sentence or refuse to help? Wait or Refuse:   ").lower()
                print("\n")
            except ValueError:
                print("I don't understand.")
                continue
            if plans == "wait" and years >= 40:
                print(raptext(f"In the shadowed corridors of the prison, {friend} and {name} spent their days confined by the unforgiving bars and the relentless passage of time. Despite dreams of escape, they found themselves bound by the harsh reality of their sentences. As the years stretched into decades, their youthful vigor waned, replaced by the weary weight of age. Each day became a testament to the inevitability of mortality as the echoes of their forgotten ambitions faded into the silence of forgotten dreams. And when the final curtain fell, they left behind not tales of daring escape but the quiet resignation of lives lived within the confines of their own making, their hopes and aspirations lost to the relentless march of time never to step foot into {location}."))
                print("\n")
                player_is_dead = True
                player_friend_dead = None
                Outlaw = None
                break
            elif plans == "wait" and years <= 39:
                print(raptext(f"In the confines of their prison cell, {friend} and {name} chose a different path one of patience and compliance with the system's rules. Despite the longing for freedom gnawing at their spirits, they remained steadfast, understanding that liberation would eventually come through legal channels. With each passing day, they found solace in the routine of prison life, forging bonds with fellow inmates and seeking redemption through self-reflection. And when the day of their scheduled release finally arrived, it brought the sweet taste of freedom and the satisfaction of knowing that they had abided by the law, their patience rewarded with the promise of a new beginning beyond the prison walls of {location}."))
                print("\n")
                player_is_dead = False
                player_friend_dead = None
                Outlaw = None
                break 
            elif plans == "refuse":
                print(raptext(f"Despite {friend}'s plea, {name} refuses to aid in the escape, believing that justice will prevail in due time. In a desperate attempt to break free, {friend} executes a daring escape plan, hoping to find freedom beyond the prison walls. However, his efforts end in tragedy as he meets his demise during the escape attempt, leaving {name} grief stricken and guilt ridden. Despite the loss of his friend, a strange twist of fate unfolds as new evidence comes to light, revealing {name}'s innocence and overturning his unjust conviction. Freed from the shackles of false accusations, {name} emerges from the shadows of captivity back into {location}, carrying the memory of his friend's sacrifice and the hope for a brighter future."))
                print("\n")
                player_friend_dead = True
                player_is_dead = False
                Outlaw = None
                break
            else:
                print("Please answer with 'Wait' or 'Refuse'!")
                print("\n")
                continue
    
        if player_is_dead == False and player_friend_dead == True:
            print("\n")
            print(raptext(f"As {name} tries to cope with the unfairness of the situation gnawing at them relentlessly, especially after the tragic demise of their friend {friend}. Seeking solace, {name} reflects on their shared memories and dreams they once held dear. Despite the pain of loss, {name} emerges from the shadows of captivity, carrying the memory of their friend's sacrifice and the hope for a brighter future. With newfound determination, {name} sets out to honor their friend's memory and fulfill the dreams they once cherished together. Through perseverance and resilience, {name} embarks on a journey toward achieving {dream}, turning adversity into opportunity and embracing the promise of a new beginning beyond the prison walls."))
  
        elif player_is_dead == True and player_friend_dead == True:
            print("\n")
            print(raptext(f"Tragically, after years of tireless effort, the tunnel became their tomb, collapsing under the weight of their aspirations and sealing their fate in the cold embrace of the earth under {location}. Their dreams of {dream}, their voices silenced beneath the rubble, {friend} and {name} found their final refuge in the darkness they sought to escape. In death, they remain bound together, their legacy etched into the walls that once confined them, a testament to the indomitable spirit of those who dare defy the chains of oppression. Though cut short, their story serves as a sad reminder of the perils of resistance and the fragility of human aspirations in the face of impossible odds. As the world above continues to turn, their memory lives on, a poignant echo of lost hope and unfulfilled dreams in the shadowed corridors of history."))
   
        elif player_is_dead == False and Outlaw == True:
            print("\n")
            print(raptext(f"After their daring escape from prison, {friend} and {name} slipped into the shadows, determined to seek vengeance against those who wronged them. Living in the clandestine depths of the city, they meticulously planned their retribution, biding their time until the moment was ripe for justice. Operating in the shadows, they struck swiftly and decisively, leaving no trace of their presence as they exacted their revenge upon their enemies. With each act of retribution, they felt a sense of satisfaction and closure, knowing they were reclaiming what was rightfully theirs. As fugitives on the run, they lived each day with caution and vigilance, always one step ahead of those who sought to capture them. Despite the dangers lurking in the shadows, {friend} and {name} found solace in their newfound freedom, embracing the thrill of living on the edge. Together, they forged a bond in the crucible of adversity, their shared determination serving as a beacon of hope in the darkness. As they disappeared into the annals of history, their legend grew, a testament to the indomitable spirit of those who refused to be shackled by the chains of injustice. They found peace in the quiet moments of reflection, knowing they had forged their own path in a world that once sought to crush their spirits. And so, they lived out their days in the shadows, forever free, vigilant, and bound by the unbreakable bond of friendship and shared destiny. Sacrificing their old {dream} to take vengeance into their own hands never able to return to {location} again"))        
    
        elif player_is_dead == False:
            print("\n") 
            print(raptext(f"As time passed, the memories of their wrongful imprisonment faded into the background, replaced by the simple joys of everyday life. Despite the injustices they endured, [friend] and [name] refused to be defined by their past, focusing instead on their {dream}, leaving behind their past in {location}."))       
        
        elif player_is_dead == True:
            print("\n") 
            print(raptext(f"{name} and {friend} met their tragic end within the cold confines of the prison walls, their dreams of {dream} forever out of reach. Despite their fervent efforts to break free, fate had other plans. As they lay side by side, their spirits intertwined in an eternal embrace, their aspirations shattered by the unforgiving hand of destiny. Their journey, a somber reminder of the fleeting nature of hope and the relentless march of time. In the end, they departed, leaving behind the echoes of their shattered dreams, forever lost in the abyss of despair."))
        
        print("\n")
        tryagain = input("GAME OVER, do you wish to try again? Enter y/n:").lower()

        
 
