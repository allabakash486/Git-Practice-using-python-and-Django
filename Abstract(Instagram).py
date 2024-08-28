from abc import ABC,abstractmethod
class InstagramFrontEnd(ABC):
    def story(self):
        pass 
    def profile_pic(self):
        pass 
    def post(self):
        pass
    def Messenger(self):
        pass       
class InstagramBackend(InstagramFrontEnd):
    @abstractmethod
    def story(self):
        print("Story is available")        
    @abstractmethod
    def profile_pic(self):
        print("Profile pic is available")        
    @abstractmethod
    def post(self):
        print("Post iis available ")        
    @abstractmethod
    def Messenger(self):
         print("Messenger is Available")        
user1 = InstagramFrontEnd()
user1.story()

    