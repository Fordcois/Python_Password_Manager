from datetime import datetime

class service():
    def __init__(self,name,password):
            self.name = name
            self.password = password
            self.last_updated = datetime.now()

    def update_password(self,new_password):
        self.password=new_password
        self.last_updated=datetime.now()
        
class PasswordManager():
        def __init__(self):
            self.vault={}

        def add(self,service_name,service_password):
            if (self.servicename_is_unique(service_name)) and (self.password_is_valid(service_password)):
                    self.vault[service_name]=service(service_name,service_password)
        
        def list_services(self):
            return [service.name for service in self.vault.values()]
        
        def remove(self,name_to_be_removed):
            self.vault.pop(name_to_be_removed)

        def update(self,name_to_be_updated,new_password):
            selected_service = self.vault[name_to_be_updated]
            if self.password_is_valid(new_password):
                selected_service.update_password(new_password)

        def get_for_service(self,searched_name):
            if searched_name in self.vault.keys():
                return self.vault[searched_name].password
        
        def sort_services_by(self,searchCriteria,reverse = False):
            filters = {'service':lambda x: x.name,'added_on':lambda x: x.last_updated}
            reversed_search = (reverse=='reverse')
            sorted_list = sorted(self.vault.values(), key=filters[searchCriteria], reverse=reversed_search)
            return [x.name for x in sorted_list]
        
        def password_atleast_8_characters(self,password):
            return len(password) >= 8
        
        def password_contains_specialcharacter(self, password):
            special_characters = {'!', '@', '$', '%', '&'}
            return any(char in special_characters for char in password)

        def password_is_valid(self,password):
            return self.password_atleast_8_characters(password) and self.password_contains_specialcharacter(password) and self.password_is_unique(password)

        def password_is_unique(self,password):
            currentpasswords = [service.password for service in self.vault.values()]
            return password not in currentpasswords
        
        def servicename_is_unique (self,service_name):
            currentservices = [service.name for service in self.vault.values()]
            return service_name not in currentservices
        
        def password_is_unique (self,password):
            currentpasswords = [service.password for service in self.vault.values()]
            return password not in currentpasswords


            


        
