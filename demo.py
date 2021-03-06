# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query


# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[0])

def view_heroes(): #DONE
    heroes = execute_query( """
    SELECT * from heroes
    """
    ,None, True)
    for hero in heroes:
        print(hero[1])
    selection = input("View more info? y/n\n> ")
    if selection.lower() == "y":
        name = input("Which hero?\n> ")
        heroes = execute_query( """
        SELECT * from heroes WHERE name = %(name)s
        """,{'name':name}
        , True)
        print('NAME: {}\nABOUT: {}\nBIO: {}'.format(heroes[0][1],heroes[0][2],heroes[0][3]))



def create_hero():
    while True:
        name = input("Enter a Name\n> ")
        if name != '':
            break
    while True:
        about = input("Enter an About\n> ")
        if about != '':
                break
    while True:
        bio = input("Enter a Bio\n> ")
        if bio != '':
                break
    execute_query( """
    insert into heroes(name, about_me, biography) (
        values(%(name)s,%(about)s,%(bio)s)
    )
    """,{'name':name, "about":about, "bio":bio}
)

def update_hero():
    name = input("Enter a Name\n> ")
    selection = input("What would you like to change?\n\n1. Name\n2. About Me\n3. Bio\n4. Abilities\n5. Relationships\n> ")
    if selection == '1':
        oldname = name
        name = input("Enter a New Name\n> ")
        execute_query( """
        UPDATE heroes
        SET name = %(new_name)s
        WHERE name = %(old_name)s;
        """,{'new_name':name, 'old_name':oldname}
        )
    if selection == '2':
        about = input("Enter a New About Me\n> ")
        execute_query( """
        UPDATE heroes
        SET about_me = %(new_about)s
        WHERE name = %(new_name)s;
        """,
        {'new_about': about, 'new_name': name}
        )
    if selection == '3':
        bio = input("Enter a New Bio\n> ")
        execute_query( """
        UPDATE heroes
        SET biography = %(bio)s
        WHERE name = %(name)s;
        """,{'bio':bio, 'name':name}
        )

def delete_hero():
    name = input("Enter a Name\n> ")
    execute_query( """
    DELETE FROM heroes
    WHERE name = %(name)s;
    """,{'name':name}
    )
    print("{} successfully removed".format(name))

while True:
    print("\nWelcome to the Hero Database, what would you like to do?\n")
    selection = input("1. View all Current Heroes\n2. Create a New Hero\n3. Update a Hero\n4. Remove a Hero\n5. Back to Main Menu\n> ")
    while selection:
        if selection == '1':
            # print("You selected View all Current Heroes")
            view_heroes()    
            break
        elif selection == '2':
            # print("You selected Create a New Hero")
            create_hero()
            break
        elif selection == '3':
            # print("You selected Update a Hero")
            update_hero()
            break
        elif selection == '4':
            # print("You selected Remove a Hero")
            delete_hero()
            break
        elif selection == '5':
            break
        else:
            print("Something went wrong... Try again")
            selection = input("Enter a number\n> ")
        
    exit_check = input("\nExit? y/n\n> ")
    if exit_check.lower() == 'y':
        exit()