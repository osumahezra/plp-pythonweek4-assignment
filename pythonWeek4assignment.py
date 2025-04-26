import os
with open ("input.txt", "w") as file:
    file.write("my name is osilama osumah\n")
    file.write("I am a Civil Engineer\n")
    file.write("I am a young Adult\n")
    file.write("I am a Nigerian\n")
    file.write("I love programming\n")


    while True:
        try:
            filename = input("Enter the name of the input file (e.g., input.txt): ")


            with open (filename, "r", encoding="utf-8") as file:
                content = file.read()
            wordcount = len(content.split())
            upperContent = content.upper()
            output = f"{upperContent}\nWord Count: {wordcount}"
            with open ("output.txt", "w") as file:
                file.write(output)
    
            print("File processed successfully. Output written to output.txt.")
            exit()

        except FileNotFoundError:
            print(f"Error: '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: You do not have permission to read '{filename}'. Try a different file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.") 
    
            
       
   




