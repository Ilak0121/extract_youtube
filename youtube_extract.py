import extract_module as ym
import sys

def main():
    ym_class = ym.extracter()

    ym_class.print_menu()

    try:
        choice=input(" Input the number :")
    except KeyboardInterrupt:
        sys.exit(1)
    except EOFError:
        sys.exit(1)

    if choice == "1": #mp3 single
        ym_class.extract_single("")
        '''
    elif choice == "2": #mp4 single
        ym_class.
    elif choice == "3": #mp3 naming
        '''
    elif choice == "4": #mp3 list-up
        ym_class.extract_list()
    #elif choice == "5": #mp4 list-up
    #elif choice == "6":



   
while(1):
    main()
