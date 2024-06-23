import json

def pure_maths1_completion(section, subsection):
    
    # Define the structure of the textbook
    pure_maths1_structure = {
        "1": 6, "2": 6, "3": 7, "4": 7, "5": 5, "6": 5,
        "7": 5, "8": 5, "9": 6, "10": 6, "11": 6, "12": 11,
        "13": 7, "14": 8
    }

    # Calculate the total number of subsections
    total_subsections = sum(pure_maths1_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(pure_maths1_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def applied_maths1_completion(section, subsection):
    
    # Define the structure of the textbook
    applied_maths1_structure = {
        "1": 5, "2": 5, "3": 5, "4": 2, "5": 4, "6": 3,
        "7": 4, "8": 4, "9": 5, "10": 6, "11": 5
    }

    # Calculate the total number of subsections
    total_subsections = sum(applied_maths1_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(applied_maths1_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def further_maths1_completion(section, subsection):
    
    # Define the structure of the textbook
    further_maths1_structure = {
        "1": 5, "2": 5, "3": 2, "4": 5, "5": 4, "6": 6,
        "7": 6, "8": 3, "9": 6
    }

    # Calculate the total number of subsections
    total_subsections = sum(further_maths1_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(further_maths1_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def further_stats1_completion(section, subsection):
    
    # Define the structure of the textbook
    further_stats1_structure = {
        "1": 4, "2": 6, "3": 4, "4": 4, "5": 2, "6": 6,
        "7": 4, "8": 4
    }

    # Calculate the total number of subsections
    total_subsections = sum(further_stats1_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(further_stats1_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def pure_maths2_completion(section, subsection):
    
    # Define the structure of the textbook
    pure_maths2_structure = {
        "1": 5, "2": 7, "3": 8, "4": 3, "5": 5, "6": 5,
        "7": 7, "8": 5, "9": 10, "10": 4, "11": 11, "12": 4
    }

    # Calculate the total number of subsections
    total_subsections = sum(pure_maths2_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(pure_maths2_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def applied_maths2_completion(section, subsection):
    
    # Define the structure of the textbook
    applied_maths2_structure = {
        "1": 3, "2": 5, "3": 7, "4": 5, "5": 3, "6": 4,
        "7": 6, "8": 5
    }

    # Calculate the total number of subsections
    total_subsections = sum(applied_maths2_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(applied_maths2_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def further_maths2_completion(section, subsection):
    
    # Define the structure of the textbook
    further_maths2_structure = {
        "1": 7, "2": 4, "3": 5, "4": 4, "5": 4, "6": 5,
        "7": 4, "8": 4
    }

    # Calculate the total number of subsections
    total_subsections = sum(further_maths2_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(further_maths2_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage

def further_stats2_completion(section, subsection):
    
    # Define the structure of the textbook
    further_stats2_structure = {
        "1": 2, "2": 3, "3": 6, "4": 1, "5": 4, "6": 4,
        "7": 5
    }

    # Calculate the total number of subsections
    total_subsections = sum(further_stats2_structure.values())
    
    # Convert inputs to integers
    section = int(section)
    subsection = int(subsection)
    
    # Calculate the number of subsections before the current section
    subsections_before = sum(further_stats2_structure[str(i)] for i in range(1, section))
    
    # Add the current subsection to the count
    current_position = subsections_before + subsection
    
    # Calculate the percentage of completion
    completion_percentage = (current_position / total_subsections) * 100
    
    return completion_percentage


def view_textbook_completion(textbook_choice):
    
    with open(f"{textbook_choice}.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        
    if textbook_choice == 'pm1':
        completion_percentage = pure_maths1_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'a1':
        completion_percentage = applied_maths1_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'fm1':
        completion_percentage = further_maths1_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'fs1':
        completion_percentage = further_stats1_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'pm2':
        completion_percentage = pure_maths2_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'a2':
        completion_percentage = applied_maths2_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'fm2':
        completion_percentage = further_maths2_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")
    elif textbook_choice == 'fs2':
        completion_percentage = further_stats2_completion(section, subsection)
        print(f"\n\n\nYou have completed {completion_percentage:.2f}% of the {(textbook_choice).upper()} textbook")
        print(f"Your last completed section is {section}.{subsection}\n")

def view_all_completion():
    
    with open(f"pm1.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage1 = pure_maths1_completion(section, subsection)
        
    with open(f"a1.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage2 = applied_maths1_completion(section, subsection)
    
    with open(f"fm1.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage3 = further_maths1_completion(section, subsection)
    
    with open(f"fs1.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage4 = further_stats1_completion(section, subsection)
    
    with open(f"pm2.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage5 = pure_maths2_completion(section, subsection)
    
    with open(f"a2.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage6 = applied_maths2_completion(section, subsection)
    
    with open(f"fm2.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage7 = further_maths2_completion(section, subsection)
    
    with open(f"fs2.json", 'r') as json_file:
        completion_percentage = json.load(json_file)
        section, subsection = completion_percentage.split(".")
        completion_percentage8 = further_stats2_completion(section, subsection)

        percentages  = [
            completion_percentage1, 
            completion_percentage2, 
            completion_percentage3, 
            completion_percentage4, 
            completion_percentage5, 
            completion_percentage6, 
            completion_percentage7, 
            completion_percentage8,
        ]
        
        year1_percentages = [
            completion_percentage1, 
            completion_percentage2, 
            completion_percentage3, 
            completion_percentage4,
        ]
        
        year2_percentages = [
            completion_percentage5, 
            completion_percentage6, 
            completion_percentage7, 
            completion_percentage8,
        ]
        
        
        
        total_percentage = 0
        year1_percentage = 0
        year2_percentage = 0
        
        for num in percentages:
            total_percentage += num
        for num in year1_percentages:
            year1_percentage += num
        for num in year2_percentages:
            year2_percentage += num
        
        all_mean_completion = (total_percentage / 8)
        year1_mean_completion = (year1_percentage / 4)
        year2_mean_completion = (year2_percentage / 4)
        
        print(f"Total A-Level completion = {all_mean_completion:.2f}%")
        print(f"Total Year 1 completion = {year1_mean_completion:.2f}%")
        print(f"Total Year 2 completion = {year2_mean_completion:.2f}%\n\n")


textbooks = ['pm1', 'a1', 'fm1', 'fs1', 'pm2', 'a2', 'fm2', 'fs2']   
         
active = True 
  
while active:
    view_or_update = input("View progress ('v') or Update progress ('u') or Exit ('e'): ").lower()
# Calculate the completion percentage for specific book
    if view_or_update == 'u':
        while True:
            
            while True:
                textbook_choice = input("Choose textbook: PM1, A1, FM1, FS1, PM2, A2, FM2, FS2: ").lower()
                if textbook_choice in textbooks:
                    break
                else:
                    print("invalid choice")
                    continue
                
            # Input: point you are up to (e.g., "4.3")
            
            input_point = input("What point are you up to: ")
            section, subsection = input_point.split(".")
            
            
            if textbook_choice == 'pm1':
                with open('pm1.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)
                completion_percentage = pure_maths1_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'a1':
                with open('a1.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = applied_maths1_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'fm1':
                with open('fm1.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = further_maths1_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'fs1':
                with open('fs1.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = further_stats1_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'pm2':
                with open('pm2.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = pure_maths2_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'a2':
                with open('a2.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = applied_maths2_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'fm2':
                with open('fm2.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = further_maths2_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            elif textbook_choice == 'fs2':
                with open('fs2.json', 'w') as json_file:
                    json.dump(input_point, json_file, indent=4)            
                completion_percentage = further_stats2_completion(section, subsection)
                print(f"You have completed {completion_percentage:.2f}% of the textbook.")
                break
            else:
                print("invalid choice)")
                continue
            
    elif view_or_update == 'v':
        
        # check if textbook choice is valid

        while True:
            textbook_choice = input("Choose textbook: PM1, A1, FM1, FS1, PM2, A2, FM2, FS2: ").lower()
            if textbook_choice in textbooks:
                break
            else:
                print("invalid choice")
                continue
                
        view_textbook_completion(textbook_choice)
        
        view_all_completion()
        
    elif view_or_update == 'e':
        active = False
        break
    else:
        print("invalid choice")
        continue