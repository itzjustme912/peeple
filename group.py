from account import Account


class Group:
    def __init__(
        self, group_name: str, members: list[Account], admins: list[Account]
    ) -> None:
        self._group_name = group_name
        self._members = members
        self._admins = admins

    def get_name(self):
        return self._group_name

    def get_members(self) -> list[Account]:
        return self._members

    def get_admins(self) -> list[Account]:
        return self._admins

    def get_member_names(self) -> list[str]:
        member_names = []
        for i in range(len(self._members)):
            member = self._members[i]
            member.append(member_names)
        return member_names

    def get_admin_names(self) -> list[str]:
        admin_names = []
        for i in range(len(self._admins)):
            admin = self._admins[i]
            admin.append(admin_names)
        return admin_names

    def set_name(self, group_name):
        self._group_name = group_name

    def set_group_members(self, group_members: list[Account]):
        self._members = group_members

    def set_admin_members(self, admin_members: list[Account]):
        self._admins = admin_members

    def is_admin(self, name):
        for i in range(len(self._admins)):
            if self._admins[i] == name:
                return True
        return False

    def add_member(self, new_account: Account):
        for curr_member in self._members:
            name = curr_member.get_full_name()
            new_name = new_account.get_full_name()
            if name == new_name:
                return False
        self._members.append(new_account)
        return True

    def remove_member(self, removed_member: Account):
        for curr_member in self._members:
        #     name = curr_member.get_full_name()
        #     removed_name = removed_member.get_full_name()
        #     if removed_name == name:
        #         self._members.remove(removed_member)
        #         return True
            if removed_member == self._admins[curr_member]:
                member_index = curr_member
        self._members.remove(self._members[member_index])
        return True
            
    def add_admin(self, new_admin: Account):
        for curr_admin in self._admins:
            admin = curr_admin.get_full_name()
            new_ad = new_admin.get_full_name()
            if new_ad == admin:
                return False
        self._admins.append(new_admin)
        return True
    
    def remove_admin(self, removed_admin: Account):
        for curr_admin in range(len(self._admins)):
            # admin = curr_admin.get_full_name()
            # removed_ad = removed_admin.get_full_name()
            # if removed_ad == admin:
            #     self._admins.remove(removed_admin)
            #     return True
            if removed_admin == self._admins[curr_admin]:
                admin_index = curr_admin
        self._admins.remove(self._admins[admin_index])
        return True