#Problem: Change word bad to good and Remove nextline
#Source: https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

#Importing FileInput from fileinput module 
from fileinput import FileInput 
  
# Creating a function to replace the text 
def replacetext(search_text, replace_text): 
  
    # Opening file using FileInput 
    with FileInput("3littlepigs_story.txt", inplace=True, 
                   backup='.bak') as f: 
  
        # Iterating over every and changing the search_text with replace_text  using the replace function and Remove newlines
        for line in f:
                print(line.strip().replace(search_text, 
                                replace_text), end='')
                
    # Return "Text replaced" string 
    return "Text replaced"
  
  
# Creating a variable and storing the text that we want to search 
search_text = "bad"
  
# Creating a variable and storing the text that we want to update 
replace_text = "good"
  
# Calling the replacetext function and printing the returned statement 
print(replacetext(search_text, replace_text)) 