# This is why you'll execute a series of SQL statements during demo day.
from connection import execute_query4


# select_heroes = """
#     SELECT * FROM heroes
#     ORDER BY id DESC 
# """

# heroes = execute_query(select_heroes).fetchall()
# for hero in heroes:
#     print(hero[0])

def view_heroes(): #DONE
    heroes = execute_query( """
    SELECT name from heroes
    """
    , True)
    for hero in heroes:
        print(hero[0])

def create_hero():
    name = input("Enter a Name: ")
    about = input("Enter an About: ")
    bio = input("Enter a Bio: ")
    execute_query( """
    insert into heroes(name, about_me, biography) (
        values('{}','{}','{}')
    )
    """.format(name, about, bio)
)

def Update_hero():
    name = input("Enter a Name: ")
    about = input("Enter an About: ")
    bio = input("Enter a Bio: ")
    execute_query( """
    insert into heroes(name, about_me, biography) (
        values('{}','{}','{}')
    )
    """.format(name, about, bio)
    )

def delete_hero():
    name = input("Enter a Name: ")
    execute_query( """
    DELETE FROM heroes
    WHERE name = '{}';
    """.format(name)
    )

while True:
    clear()
    print("\nWelcome to the Hero Database, what would you like to do?\n")
    print('1. View all Current Heroes\n2. Create a New Hero\n3. Update a Hero\n4. Remove a Hero')
    selection = input("Enter a number: ")
    while selection:
        if selection == '1':
            print("You selected View all Current Heroes")
            view_heroes()    
            break
        elif selection == '2':
            print("You selected Create a New Hero")
            create_hero()
            break
        elif selection == '3':
            print("You selected Update a Hero")
            break
        elif selection == '4':
            print("You selected Remove a Hero")
            delete_hero()
            break
        else:
            print("Something went wrong... Try again")
            selection = input("Enter a number: ")
    
    exit_check = input("Are you done? y/n: ")
    if exit_check == 'y':
        break