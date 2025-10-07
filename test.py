# import abc 

# # abstract class is a class that cannot be instantiated loool 


# str_var = 10 & 3 

# print(str_var)


# # words = ["hello", "world", "python", "java", "javascript"]
# # list_var = [ 1, 2, 3, 4, 5 ]


# # x = zip(words, list_var)
# # print(x)
# # for word , int_var in zip(words, list_var)  : 
# #     print(word, int_var)
# #     if word == "amine" : 
# #         print("found amine ")

# var = 20 
 
# match (var):
#    case 10: 
#     print("var is 10")
#    case 20 : 
#     print("var is 20")
#    case _ : 
#     print("var is not 10 or 20")

# def addition(a, *args, log = False ): 

#     if log == True : 
#         return "fuck you bitch"
#     else: 
#         return a + sum(args) 


# print (addition(10,20,30,40,50, True))




# def addition2(val_0 , val_1 , **options):
#   print(options)
#   if "power" in options.values(): 
#     return "True ma man"
#   elif "log" in options: 
#     return "False ma man"
#   else: 
#     return "fuck you bitch"



# def main ():
#     print("we are in the main func")

# if __name__ == "__main__":
#     main()



# addition = lambda x,y : x+y 

# list_var = [1,2,3,4,5,6,7,8,9,10]

# print(list(map(lambda x : x+1 , list_var)))

# print( list(filter( lambda x : x%2 == 0 , list_var)))


# try: 
#     print(10/0)
# except Exception as e: 
#     print(e)

from unittest.mock import patch

def get_weather(city):
    response = requests.get(f"https://api.weather.com/{city}")
    if response.status_code == 200:
        return response.json()
    else:
        return None


class TestWeather (unittest.TestCase):
    @patch("requests.get")
    def test_get_weather(self, mock_get):
         # Create a fake response object
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"temp": 25}

        result = get_weather("Paris")

        self.assertEqual(result, {"temp": 25})
        mock_get.assert_called_once_with("https://api.weather.com/Paris")


def has_user_expired(user) -> bool: 

    if user.expiration_date < datetime.now(): 
        return True
    else: 
        return False



        



def test_has_user_expired(): 
    user = Mock()
    user.expiration_date = datetime.now() + timedelta(days=1)
    assert has_user_expired(user)



test_has_user_expired()




















# class Animal(abc.ABC): 
#     @abc.abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")


# dog = Animal()

# dog.make_sound()