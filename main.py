# TODO:

# User class:
# user id, name $
# follow to $
# unfollow to $
# check notifications $
# like a twitte $
# dislike a twitte $
# live a comment (comment object) $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# delete a comment $$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Creator class (is a child of User class):
# add and remove followers $
# content variable $
# statistics: number of followers and followers, number of twittes $
# make a twitte (twitte class) $
# check statistics of a twitte ???????????????????????????????/
# delete a twitte $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Twitte class:
# Creator
# statistics: likes(negative = dislike | positive = like), comments, title, subject
# notify followers (automatic when object is made)
# to show content (view)
# check comments

# Comment class (is a child of Twitte class):

# Twitter class (aka The scene | main class):
# show history 
class Twitte():
    def __init__(self, creator, title, subject):
        self.creator = creator
        self.title = title
        self.subject = subject
        self.likes = 0
        self.comments = {} # title -> Comment
        
    def show(self):
        print("--------------------------------")
        print(self.creator)
        print(self.title)
        print(self.subject)
        print(f"Likes: {self.likes}" if self.likes >= 0 else f"Dislikes: {abs(self.likes)}")
        for comment in self.comments.values():
            comment.show()
            
    def comment(self, creator, title, subject):
        self.comments[title] = Comment(creator, title, subject)
        
    def uncomment(self, title):
        self.comments.pop(title)
            

class Comment(Twitte):
    def __init__(self, creator, title, subject):
        super().__init__(creator, title, subject)
        
    def show(self):
        super().show()


class User():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.subscriptions = set()
        print("--------------------------------")
        print(f"User with name {self.name}")
        self.show_profile()
        
    def follow(self, channel):
        channel.add_subscriber(self.name)
        self.subscriptions.add(channel.name)
        print("--------------------------------")
        print(f"User {self.name} followed to {channel.name}")
    
    def unfollow(self, channel):
        channel.remove_subscriber(self.name)
        self.subscriptions.remove(channel.name)
        print("--------------------------------")
        print(f"User {self.name} unfollowed from {channel.name}")
        
    def check_notifications(self):
        for channel in self.subscriptions:
            for content in channel:
                content.show()
        print("--------------------------------")
        print(f"All notifications are checked in {self.name} account")
            
    def like(self, twitte):
        twitte.likes += 1
        print("--------------------------------")
        print(f"Liked '{twitte.title}' now: {twitte.likes}")
         
    def unlike(self, twitte):
        twitte.likes -= 1
        print("--------------------------------")
        print(f"Unlike '{twitte.title}' now: {twitte.likes}")
    
    def show_profile(self):
        print("--------------------------------")
        print(f"User with name: {self.name} and subscribed on {self.subscriptions if self.subscriptions else 'No one :('}")
        print(f"{self.description}")
        
    def comment(self, twitte, title, subject):
        twitte.comment(self.name, title, subject)
    

class Creator(User):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.subscriptions = set()
        self.content = {} # Title -> twitte
        self.followers = set()
        self.number_of_followers = 0
        self.number_of_twittes = 0
        print("--------------------------------")
        print(f"Creator {self.name} with {self.number_of_followers} was created")
        print(f"Also have {self.number_of_twittes} number of twittes")
        
    def twitte(self, title, subject):
        self.content[title] = Twitte(self.name, title, subject)
        self.number_of_twittes += 1

    def show_all_twittes(self):
        for i, content in enumerate(self.content.values()):
            print(f"-----------------{i + 1}---------------")
            content.show()
    
    def add_subscriber(self, subscriber):
        self.followers.add(subscriber)
        self.number_of_followers += 1
        
    def remove_subscriber(self, subscriber):
        self.followers.remove(subscriber)
        self.number_of_followers -= 1
    
    def untwitte(self, title):
        self.content.remove(title)
        self.number_of_twittes -= 1
        
    def show_profile(self):
        super().show_profile()
        print(f"subscribers: {self.number_of_followers} and twittes: {self.number_of_twittes}")
        
        

    
    

# This is test case before I public this code to GitHub 
userIgor = User("Igor228", "Hi, I am new")

creatorKira = Creator("Kira", "UWU I want to get 10 subscribers")
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

creatorKira.show_all_twittes()






        
    
        
