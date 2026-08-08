from __future__ import annotations  # the only line of code what suggested IA intelligence 


class User():
    def __init__(self, name: str, description: str):
        self.type: str = "User"
        self.name: str = name
        self.description: str = description
        self.subscriptions: str[Creator] = {} # Nickname -> Creator class
        print("--------------------------------")
        print(f"User with name {self.name}")
        self.showProfile()
        
    def follow(self, creator: Creator):
        if creator.name in self.subscriptions.keys():
            self.unfollow(creator)
            return
            
        creator.addSubscriber(self.name)
        self.subscriptions[creator.name] = creator
        print("--------------------------------")
        print(f"User {self.name} followed to {creator.name}")
    
    def unfollow(self, creator: Creator):
        creator.removeSubscriber(self.name)
        self.subscriptions.pop(creator.name)
        print("--------------------------------")
        print(f"User {self.name} unfollowed from {creator.name}")
        
    def checkNotifications(self):
        for creator in self.subscriptions.values():
            for content in creator.content.values():
                content.show()
        print("--------------------------------")
        print(f"All notifications are checked in {self.name}'s account")
            
    def like(self, twit: Twit):
        twit.likes += 1
        print("--------------------------------")
        print(f"Liked '{twit.title}' now: {twit.likes if twit.likes >= 0 else -1 * twit.likes} {'likes' if twit.likes >= 0 else 'dislikes'}")
         
    def unlike(self, twit: Twit):
        twit.likes -= 1
        print("--------------------------------")
        print(f"Unlike '{twit.title}' now: {twit.likes if twit.likes >= 0 else -1 * twit.likes} {'likes' if twit.likes >= 0 else 'dislikes'}")
    
    def showProfile(self):
        print("--------------------------------")
        print(f"User with name: {self.name} and subscribed on {', '.join(creator for creator in self.subscriptions) if self.subscriptions else 'No one :('}")
        print(f"{self.description}")
        
    def comment(self, twit: Twit, title: str, subject: str):
        twit.comment(self.name, title, subject)
    
    def uncomment(self, twit, title):
        twit.uncomment(title)
    

class Creator(User):
    def __init__(self, name: str, description: str):
        self.type = "Creator"
        self.name: str = name
        self.description: str = description
        self.subscriptions: str[Creator] = {} # Nickname -> Creator class
        self.content: str[Twit] = {} # Title -> twit
        self.followers: set = set()
        self.number_of_followers: int = 0
        self.number_of_twits: int = 0
        print("--------------------------------")
        print(f"Creator {self.name} with {self.number_of_followers} was created")
        print(f"Also have {self.number_of_twits} number of twits")
        
    def makeTwit(self, title: str, subject: str):
        self.content[title] = Twit(self.name, title, subject)
        self.number_of_twits += 1

    def showAllTwits(self):
        for i, content in enumerate(self.content.values()):
            print(f"-----------------{i + 1}---------------")
            content.show()
    
    def addSubscriber(self, subscriber: str):
        self.followers.add(subscriber)
        self.number_of_followers += 1
        
    def removeSubscriber(self, subscriber: User):
        self.followers.remove(subscriber.name)
        self.number_of_followers -= 1
    
    def untwit(self, title: str) -> None:
        self.content.remove(title)
        self.number_of_twits -= 1
        
    def showProfile(self):
        super().show_profile()
        print(f"subscribers: {self.number_of_followers} and twits: {self.number_of_twits}")


class Twit():
    def __init__(self, creator: Creator, title: str, subject: str):
        self.type = "Twit"
        self.creator: Creator = creator
        self.title: str = title
        self.subject: str = subject
        self.likes: int = 0
        self.comments: int = {} # title -> Comment
        
    def show(self, indentation=1):
        print("----------------------------------------")
        print((indentation - 1) * "  " + self.creator)
        print((indentation - 1) * "  " + self.title)
        print(indentation * "  " + self.subject)
        print(f"Likes: {self.likes}" if self.likes >= 0 else f"Dislikes: {abs(self.likes)}")
        print("---------------Comments-----------------")
        
        for comment in self.comments.values():
            comment.show(indentation + 1)
            
    def comment(self, creator: User, title: str, subject: str):
        self.comments[title] = Comment(creator, subject)
        
    def uncomment(self, title: str):
        self.comments.pop(title)
            

class Comment(Twit):
    def __init__(self, creator: User, subject: str):
        self.type = "Comment"
        self.creator: Creator = creator
        self.subject: str = subject
        self.likes: int = 0
        self.comments: int = {} # title -> Comment)
        
    def show(self, indentation: int):
        print("----------------------------------------")
        print((indentation - 1) * "  " + self.creator)
        print(indentation * "  " + self.subject)
        print(f"Likes: {self.likes}" if self.likes >= 0 else f"Dislikes: {abs(self.likes)}")
        print("---------------Comments-----------------") if self.comments else None
        
        for comment in self.comments.values():
            comment.show(indentation + 1)


class Twitter:
    def __init__(self):
        self.signed: User | Creator = None 
        self.users: str[User] = {}  # Nickname -> User
        self.creators: str[Creator] = {}  # Nickname -> Creator
        self.twits: str[Twit] = {}  # Title -> Twit
        print("Welcome to Twitter in python!!!")
        
    def main(self):
        while True:
            print("-------------------------------\n")    
            print("Enter -1 to exit")
            print("Enter 0 to unsign")
            
            if not self.signed:
                print("-------------------------------")    
                print("You are not signed")
                print("(1) Select existing User or Creator")
                print("(2) Create new User")
                print("(3) Make User to a Creator")
                answer: str = input()
                if answer == "-1":
                    break
                if answer == "1":
                    candidate = input("Users (1) or Creators (2): ")
                    match candidate:
                        case "-1":
                            break
                        case "0":
                            self.signed = None
                        case "1":
                            self.select("User")
                        case "2":
                            self.select("Creator")
                elif answer == "2":
                    self.createUser()
                elif answer == "3":
                    name = input(f"Which User to transform for [{', '.join(self.users.keys())}]: ")
                    self.transformUserToCreator(name)
                else:
                    print("Invalid answer")
                continue
            
            print("-------------------------------")    
            print(f"You are signed as {self.signed.name}! It is a {self.signed.type}")
                
            if self.signed.type == "Creator":
                print("------------Creator commands------------")
                print("User commands are also useable\n")
                print("(6) Make a twit")
                print("(7) Delete a twit")
                print("(8) Show all twits\n")
            
            print("------------User commands------------\n")
            print("(1) Check notifications")
            print("(2) Follow / Unfollow a Creator")
            print("(3) Like / Unlike a Twit")
            print("(4) Live a comment / delete a comment")
            print("(5) show profile")
            
            answer = input()
            
            match answer:
                case "-1":
                    break
                case "0":
                    self.signed = None
                    
            self.actionsForUser(answer) if answer <= "5" else self.actionsForCreator(answer)
                    
                
            
        print("Exiting...")
        
    def actionsForUser(self, answer):
        match(answer):
            case "1":
                self.signed.checkNotifications()
            case "2":
                name = input(f"Creator name [{', '.join(self.creators.keys())}]: ")
                creator = self.creators[name]
                self.signed.follow(creator)
            case "3":
                title = input("Twit title: ")
                self.signed.like(self.twits[title])
            case "4":
                title = input("Twit title: ")
                if title in self.twits[title].comments:
                    self.signed.uncomment(title)
                else:
                    commentTitle = input("Comment Title: ")
                    commentDescription = input("Comment Description: ")
                    self.signed.comment(self.twits[title], commentTitle, commentDescription)
            case "5":
                self.signed.showProfile()
            case _:
                print("invalid input")
    
    def actionsForCreator(self, answer):
        match(answer):
                    case "6":
                        title = input("Title for the Twit: ")
                        subject = input("Subject for the Twit: ")
                        self.signed.makeTwit(title, subject)
                        self.twits[title] = self.signed.content[title]
                    case "7":
                        print("7")
                    case "8":
                        print("8")
                    case "9":
                        print("9")
                    case _:
                        print("Invalid input")
        
    def select(self, prototype: str):
        answer: str = input(f"Which {prototype} to select [{ ', '.join(self.users.keys()) if prototype == 'User' else ', '.join(self.creators.keys()) }]: ")
        if (prototype == "User" and answer in self.users.keys()):
            self.signed = self.users[answer]
            return
        elif (prototype == "Creator" and answer in self.creators.keys()):
            self.signed = self.creators[answer]
        else:
            print("invalid nickname")
            
    def createUser(self):
        print("To create an User, you need a name and description")
        name: str = input("name: ")
        description: str = input("description (can be short): ")
        
        self.people[name] = User(name, description)
        
    def transformUserToCreator(self, user: str):
        if user not in self.users:
            print(f"{user} isn't in list or already a Creator")
        candidate = self.users.pop(user)
        self.creators[user] = Creator(candidate.name, candidate.description)
        print(f"{user} successfully transformed to Creator")
      
          
            
            
        
        

twitter = Twitter()
twitter.users["Mike"] = User("Mike", "Then the light is running low...")
twitter.users["Lilly"] = User("Lilly", "The blind one")
twitter.creators["John"] = Creator("John", "I have thoughts to share...")

twitter.main()




