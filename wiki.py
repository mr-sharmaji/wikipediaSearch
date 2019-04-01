import wikipedia


def enquiry(lis1):
    if not lis1:
        return 1
    else:
        return 0


n = input("Enter The Item You Want To Search In Wikipedia\n")
if wikipedia.suggest(n) is not 0:
    suggestion = wikipedia.suggest(n)
    print('Do You Mean:', suggestion)
    ch = input("Enter (Y/N)")
    if ch is 'N' or ch is 'n':
        print("You Entered", ch, "\n Do You wish to search for the item form our search list\n")
        ch1 = input("Enter (Y/N)\n")
        if ch1 is 'Y' or ch1 is 'y':
            search = wikipedia.search(n)
            #if enquiry(search) is 1:
            print("Search your item form given list\n")
            print(wikipedia.search(n))
            #else:
             #   print("Search List Not Created Please try again\n")
            print("Is Your Search item present in the list?\n")
            ch2 = input("Enter (Y/N)")
            if ch2 is 'Y' or ch2 is 'y':
                ch3 = input("Enter The item from the list or it's position\n")
                if ch3 in search or search[ch3-1] in search:
                    try:
                        summary = wikipedia.summary(search[ch3-1])
                        print("summary")
                    except:
                        print("An Unexpected Error Has Occurred Please try again")
                else:
                    print("We Are Sorry But we are not Able to find Your item in the wikipedia")
    elif ch is 'Y' or ch is 'y':
        n = suggestion
        try:
            summary = wikipedia.summary(n)
            print(summary)
        except:
            print("An Unexpected Error Has Occurred Please try again")
    else:
        print("Wrong Input")
else:
    try:
        summary = wikipedia.summary(n)
        print(summary)
    except:
        print("An Unexpected Error Has Occurred Please try again")






#summary = wikipedia.summary(n)
#search = wikipedia.search(n)
#images = wikipedia.images(n)
#page = wikipedia.page(n)
#page_url = page.url
#page_tittle = page.tittle













#try:
 #   print(wikipedia.summary(n))
  #  print(wikipedia.content(n))
   # print(wiki_search)
#except:
 #   print("No Data Found On wikipedia for your search item\n")