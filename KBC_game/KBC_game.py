questions = [
["1. Who is the current Secretary-General of the United Nations (as of 2024)?","1. António Guterres", "2. Ban Ki-moon", "3. Kofi Annan", "4. Ursula von der Leyen", 1],
["2. Which planet is known as the Red Planet?","1. Earth", "2. Jupiter", "3. Mars", "4. Venus", 3],
["3. What is the capital of Canada?","1. Toronto", "2. Ottawa", "3. Vancouver", "4. Montreal", 2],
["4. Who invented the telephone?", "1. Thomas Edison", "2. Nikola Tesla", "3. Alexander Graham Bell", "4. Guglielmo Marconi", 3],
["5. In which year did World War II end?","A. 1942", "2. 1945", "3. 1939", "4. 1950", 2],
["6. What is the capital city of Australia?", "1 Sydney","2. Melbourne","3. Canberra","4. Brisbane",3],
["7. Who painted the Mona Lisa?","1. Vincent van Gogh","2. Pablo Picasso","3. Michelangelo","4. Leonardo da Vinci",4],
["8. What is the largest planet in our solar system?","1. Earth","2 Saturn","3. Jupiter","4. Mars",3],
["9. Which element has the chemical symbol o?","1. Gold","2. Oxygen","3. Osmium","4. Opal",2],
["10. Who wrote the play Romeo and Juliet?","1. William Shakespeare","2. Charles Dickens","3. George Orwell","4. Jane Austen",1],
["11. What is the currency of Japan?","1. Yuan","2. Dollar","3. Won","4. Yen",4],
["12. In which year did World War II end?","1. 1943","2. 1945","3. 1950","4. 1939",2],
["13. Which gas do plants absorb from the atmosphere?","1. Oxygen","2. Nitrogen","3. Carbon Dioxide","4. Hydrogen",3],
["14. What is the hardest natural substance on Earth?","1. Gold","2. Iron","3. Diamond","4. Quartz",1],
["15. How many continents are there in the world?","1. 5","2. 6","3. 7","4. 8",3],
["16. What is the chemical symbol for water?","1. O2","2. CO2","3. H2O","4. NaCl",3],
["17. Which organ in the human body is responsible for pumping blood?","1. Brain","2. Liver","3. Heart","4. Kidney",3],
]
money = "₹1,000", "₹2,000", "₹3,000", "₹5,000", "₹10,000", "₹20,000", "₹40,000", "₹80,000", "₹160,000", "₹320,000", "₹640,000","₹1,250,000", "₹2,500,000", "₹5,000,000", "₹7,500,000", "₹1 crore", "₹7.5 crore"
for i in range(0,len(questions)):
    option = questions[i]
    print(f"{option[0]}")
    print(f"{option[1]}           {option[2]}")
    print(f"{option[3]}           {option[4]}")    
    ans = int(input("Choose your option: "))
    if ans == option[-1]:
        print("\n")
        print(f"Congrats you won {money[i]}")
        print("\n")
            
    else:
        print(f"Wrong answer, your winning amount is: {money[i-1]}")    
        break
    
    ans = int(input("Do you want to continue ?,\n Enter 0 - Quit \n 1 - continue \n"))
    if ans == 0:
        print("Thank you for playing")
        print("Your winning amount is ",money[i-1])
        break
    