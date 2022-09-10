email = input("Enter your email:")
k,j = 0,0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email )and (email.count("@")==1):
            if (email[-4]==".")^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                if k==1 or j==1:
                    print("wrong email. fifth condition not met.")
                else:
                    print("Correct Email")
            else:
                print("Wrong Email.Fourth condition not met.")
        else:
             print("Wrong Email.Third condition not met.")
    else:
        print("Wrong Email. Second condition not met.")
else:
    print("Wrong Email. First codition not met.")