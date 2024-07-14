from db import Library, Book, Author, Member
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


library = Library()

while True:

    print('1_books')
    print('2_authors')
    print('3_members')
    print('4_Exit')
    first_input = input('please choose:')
    clear_screen()
    if first_input == '1':
        print('1_add_book')
        print('2_edit_book')
        print('3_delete_book')
        print('4_show_book')
        book_input = input('please choose:')
        
        if book_input == '1':
            clear_screen()
            book_name = input('enter the name of the book:')
            library.show_authors()
            author_id = input('enter the authors_id:')
            year_of_release = input('enter the  publication year :')
            book = Book(book_name , author_id , year_of_release)
            library.add_books(book)
            clear_screen()

        elif book_input == '2':
            clear_screen()
            new_book_value = input('enter the new name of the book:')
            library.show_authors()
            new_authors_value = input('enter new authors_id:')
            new_year_value = input('enter the new publication year:')
            library.show_id_and_name()
            book_id = input('please enter the book id you want change:')
            book = Book(new_book_value , new_authors_value , new_year_value )
            library.update_book(book , book_id)
            clear_screen()

        elif book_input == '3':
            clear_screen()
            library.show_id_and_name()
            book_id = input('please enter the book id you want delete:')
            ask_again = input('are you sure . you want to delete this book? [y/n]?')
            if ask_again == 'y':
                library.delete_book(book_id)
                clear_screen()
            elif ask_again == 'n':
                print('ok ')
            else:
                print('you cant choose this . try again')
            
        elif book_input == '4':
            clear_screen()
            library.all_books_and_authors()
            end = input('please click any key to end this part:')
            clear_screen()


    elif first_input == '2':
        print('1_add_authors')
        print('2_update_authors')
        print('3_delete_authors')
        print('4_show_all_auhors')
        print('5_show_book_from_authors')
        authors_input = input('please choose:')
        
        if authors_input == '1':
            clear_screen()
            new_authors = input('enter authors name:')
            author = Author(new_authors)
            library.add_authors(author)
            clear_screen()

        elif authors_input == '2':
            clear_screen()
            library.show_authors()
            authors_id = input('please enter author id you want change:')
            edited_aothors = input('enter a new name for aouthors:')
            author = Author(edited_aothors)
            library.update_authors(author , authors_id)
            clear_screen()

        elif authors_input == '3':
            clear_screen()
            library.show_authors()
            authors_id = input('plese enter the author id you want delete:')
            ask_again = input('are you sure . you want to delete this authors? [y/n]?')

            if ask_again == 'y':
                library.delete_authors(authors_id)
                clear_screen()
            elif ask_again == 'n':
                print('ok ')
            else:
                print('you cant choose this . try again')
        elif authors_input == '4':
            clear_screen()
            print('all authors:')
            library.show_authors()
            end = input('please click any key to end this part:')
            clear_screen()

        elif authors_input == '5':
            clear_screen()
            library.show_authors()
            authors_id = input('enter the author id to see all their books:')
            clear_screen()
            library.all_books_from_authors(authors_id)
            end = input('please click any key to end this part:')
            clear_screen()
    

    elif first_input == '3':
        print('1_add_members')
        print('2_update_members')
        print('3_delete_members')
        print('4_show_all_members')
        members_input = input('please choose:')
        
        if members_input == '1':
            clear_screen()
            members_name = input('please enter member name:')
            member = Member(members_name)
            library.add_members(member)
            clear_screen()
        
        elif members_input == '2':
            clear_screen()
            library.show_members()
            members_id = input('please enter member id you want change:')
            new_members = input('please enter new member name:')
            member = Member(new_members)
            library.update_members(member , members_id)
            clear_screen()
        
        elif members_input == '3':
            clear_screen()
            library.show_members()
            member_id = input('please enter member id want delete:')
            ask_again = input('are you sure . you want to delete this member? [y/n]?')
            
            if ask_again == 'y':
                library.delete_members(member_id)
                clear_screen()
            elif ask_again == 'n':
                print('ok ')
            else:
                print('you cant choose this . try again')
        elif members_input == '4':
            clear_screen()
            print('all members')
            library.show_members()
            end = input('please click any key to end this part:')
            clear_screen()

    elif first_input == '4':
        break
