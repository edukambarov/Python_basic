import view
import text
from model import PhoneBook

pb = PhoneBook() # вынес сюда, чтобы search_block тоже работал с экземпляром класса PhoneBook

def search_block(msg: str):
    request = view.input_request(msg)
    result = pb.search(request)
    view.show_book(result, text.not_search(request))
    if result:
        return True
    
def start():
    while True:
        choice =view.menu()
        match choice:
            case 1:
                pb.open_file()
                view.print_message(text.file_load_successful)
            case 2:
                pb.save_file()
                view.print_message(text.file_save_successful)
            case 3:
                book = pb.phone_book
                view.show_book(book, text.empty_phone_book)
            case 4:
                contact = view.input_contact(text.new_contact)
                pb.add_contact(contact)
                view.print_message(text.contact_save_successful(contact[0], text.contact_operation[0]))
            case 5:
                search_block(text.for_search)
            case 6:
                if search_block(text.for_edit):
                    edit_id = int(view.input_request(text.input_edit_id))
                    new_contact = view.input_contact(text.input_edit_contact)
                    name = pb.edit(edit_id, new_contact)
                    view.print_message(text.contact_save_successful(name, text.contact_operation[1]))
            case 7:
                if search_block(text.for_delete): 
                    del_id = int(view.input_request(text.input_delete_id))
                    name = pb.del_contact(del_id)[0]
                    view.print_message(text.contact_save_successful(name, text.contact_operation[2]))
            case 8:
                if pb.phone_book != pb.original_book:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        pb.save_file()
                        view.print_message(text.file_save_successful) 
                view.print_message(text.end_program)
                break
