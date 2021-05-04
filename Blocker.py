HOST="C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP='127.0.0.1'


def block_website(websites):
    '''Blocks the all the websites which are mentioned in the list'''

    if type(websites) != type([]):
        raise TypeError('Paramerter websites expects a list')

    with open(HOST,'r+') as f:
        content=f.read()

        for website in websites:

            if website not in content:
                f.write("{} {}\n".format(REDIRECT_IP,website))

    f.close()
    print('Given Websites are Blocked !',end='\n\n')

def unblock_website(websites):
    with open(HOST,'r+') as f:
        content=f.readlines()
        f.seek(0)

        for line in content:
            if not any(website in line for website in websites):
                f.write(line)
        f.truncate()
        f.close()
    print('Given Wnsites are Unblocked !',end='\n\n') 


if __name__=='__main__':
    while True:
        for op in ["1.Block Website","2.UnBlock Website","3.Exit"]:
            print(op)
        option=int(input('Enter option number :'))

        if option==1:
            print('You have chosen option 1: To Block Websites')
            print('Please Enter the websites you want to block seperated by a comma (,)',end='\n\n')
            webpages=input('Enter Websites :')
            webpages=webpages.split(',')
            block_website(webpages)

        elif option==2:
            print('You have chosen option 2: To Unblock Websites')
            print('Please Enter the websites you want to unblock seperated by a comma (,)',end='\n\n')
            webpages=input('Enter Websites :')
            webpages=webpages.split(',')
            unblock_website(webpages)

        elif option==3:
            print('Exiting Program')
            break
        else:
            print('Wrong Option')
            break