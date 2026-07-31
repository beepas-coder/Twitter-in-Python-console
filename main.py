from __future__ import annotations

class User():
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description
        self.subscriptions: str[Creator] = {} # Nickname -> Creator class
        print("--------------------------------")
        print(f"User with name {self.name}")
        self.show_profile()
        
    def follow(self, creator: Creator):
        if creator.name in self.subscriptions:
            print(f"{self.name} is already subscribed to {creator.name}")
            return
            
        creator.add_subscriber(self.name)
        self.subscriptions[creator.name] = creator
        print("--------------------------------")
        print(f"User {self.name} followed to {creator.name}")
    
    def unfollow(self, creator: Creator):
        creator.remove_subscriber(self.name)
        self.subscriptions.pop(creator.name)
        print("--------------------------------")
        print(f"User {self.name} unfollowed from {creator.name}")
        
    def check_notifications(self):
        for creator in self.subscriptions.values():
            for content in creator.content.values():
                content.show()
        print("--------------------------------")
        print(f"All notifications are checked in {self.name} account")
            
    def like(self, twitte: Twitte):
        twitte.likes += 1
        print("--------------------------------")
        print(f"Liked '{twitte.title}' now: {twitte.likes if twitte.likes >= 0 else -1 * twitte.likes} {'likes' if twitte.likes >= 0 else 'dislikes'}")
         
    def unlike(self, twitte: Twitte):
        twitte.likes -= 1
        print("--------------------------------")
        print(f"Unlike '{twitte.title}' now: {twitte.likes if twitte.likes >= 0 else -1 * twitte.likes} {'likes' if twitte.likes >= 0 else 'dislikes'}")
    
    def show_profile(self):
        print("--------------------------------")
        print(f"User with name: {self.name} and subscribed on {self.subscriptions if self.subscriptions else 'No one :('}")
        print(f"{self.description}")
        
    def comment(self, twitte: Twitte, title: str, subject: str):
        twitte.comment(self.name, title, subject)
    

class Creator(User):
    def __init__(self, name: str, description: str):
        self.name: str = name
        self.description: str = description
        self.subscriptions: str[Creator] = {} # Nickname -> Creator class
        self.content: str[Twitte] = {} # Title -> twitte
        self.followers: set = set()
        self.number_of_followers: int = 0
        self.number_of_twittes: int = 0
        print("--------------------------------")
        print(f"Creator {self.name} with {self.number_of_followers} was created")
        print(f"Also have {self.number_of_twittes} number of twittes")
        
    def twitte(self, title: str, subject: str):
        self.content[title] = Twitte(self.name, title, subject)
        self.number_of_twittes += 1

    def show_all_twittes(self):
        for i, content in enumerate(self.content.values()):
            print(f"-----------------{i + 1}---------------")
            content.show()
    
    def add_subscriber(self, subscriber: User):
        self.followers.add(subscriber.name)
        self.number_of_followers += 1
        
    def remove_subscriber(self, subscriber: User):
        self.followers.remove(subscriber.name)
        self.number_of_followers -= 1
    
    def untwitte(self, title: str):
        self.content.remove(title)
        self.number_of_twittes -= 1
        
    def show_profile(self):
        super().show_profile()
        print(f"subscribers: {self.number_of_followers} and twittes: {self.number_of_twittes}")


class Twitte():
    def __init__(self, creator: Creator, title: str, subject: str):
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
        # print("---------------Comments-----------------")
        
        for comment in self.comments.values():
            comment.show(indentation + 1)
            
    def comment(self, creator: User, title: str, subject: str):
        self.comments[title] = Comment(creator, title, subject)
        
    def uncomment(self, title: str):
        self.comments.pop(title)
            

class Comment(Twitte):
    def __init__(self, creator: User, title: str, subject: str):
        super().__init__(creator, title, subject)
        
    def show(self, indentation: int):
        super().show(indentation + 1)


class Twitter:
    def __init__(self):
        self.users: str[User] = {} # nickname -> User object 
        self.creators: str[Creator] = {} # nickname -> Creator object
    
    def add_user(self, name: str, description: str):
        self.users[name] = User(name, description)
    
    def main(self):
        # This is test case before I public this code to GitHub 
        userIgor = User("Igor228", "Hi, I am new")

        creatorKira = Creator("Kira", "UWU I want to get 10 subscribers")
        userIgor.follow(creatorKira)
        userIgor.follow(creatorKira)

        userIgor.show_profile()
        creatorKira.show_profile()


        creatorKira.twitte("Today, I found out what chairs aren't real!", "I watched Vsauce video about this.")

        creatorKira.twitte("Neal.fun added a new game on his web site!", "The game is kinda similar to draw a perfect circle, password game and so on. I thought it's too hard even in contexts of Neal games.")

        userIgor.like(creatorKira.content["Today, I found out what chairs aren't real!"])
        userIgor.like(creatorKira.content["Today, I found out what chairs aren't real!"])
        userIgor.like(creatorKira.content["Today, I found out what chairs aren't real!"])
        userIgor.like(creatorKira.content["Today, I found out what chairs aren't real!"])
        userIgor.like(creatorKira.content["Today, I found out what chairs aren't real!"])
        userIgor.like(creatorKira.content["Today, I found out what chairs aren't real!"])
        userIgor.unlike(creatorKira.content["Today, I found out what chairs aren't real!"])

        userIgor.unlike(creatorKira.content["Neal.fun added a new game on his web site!"])

        userIgor.comment(creatorKira.content["Today, I found out what chairs aren't real!"], "I am agree", "This is great video, recommend to watch")

        userIgor.comment(creatorKira.content["Today, I found out what chairs aren't real!"].comments["I am agree"], "Coll video", "Cool video BTW")

        creatorKira.show_all_twittes()

        print("The notifications are checked")

        userIgor.check_notifications()

        userIgor.unfollow(creatorKira)
        
        creatorKira.show_profile()
        

twitter = Twitter()


# twitter.add_user("Andrew", "A guy who likes money")

# twitter.users["Andrew"].show_profile()

twitter.main()
