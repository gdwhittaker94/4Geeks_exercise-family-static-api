# This file is our databse, where we're going to save our family members
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list

NB: we reference these methods from app.py
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
            {'id': 1, 'first_name': 'John', 'last_name': self.last_name, 'age': 33, 'lucky_numbers': [7, 13, 22]},
            {'id': 2, 'first_name': 'Jane', 'last_name': self.last_name, 'age': 35, 'lucky_numbers': [10, 14, 3]},
            {'id': 3, 'first_name': 'Jimmy', 'last_name': self.last_name, 'age': 5, 'lucky_numbers': [1]}
        ]  

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    # receives new member from POST method, here we add them to self._members list 
    def add_member(self, member):
        self._members.append(member)
        pass

    def delete_member(self, id):
        member_id = id 
        if member_id is None: 
            return None  
        
        members_to_remove = []

        for member in self._members: 
            if member['id'] == member_id:
                members_to_remove.append(member)

        for member in members_to_remove:
            self._members.remove(member)
            
        pass

    def get_member(self, id):
        member_id = id 
        for member in self._members: 
            if member['id'] == member_id:
                return member
        return None  
        pass

    # finished method: returns a list with all the family members
    def get_all_members(self):
        return self._members
