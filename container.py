import os
import re


class Container:
    users = {}
    curr_user = ""
    values = set()

    def __init__(self):
        self.users = {}
        self.curr_user = ""
        self.values = set()

    def add_user(self, name):
        path = os.getcwd() + '/' + name + ".txt"
        if name not in self.users:
            self.users.update({name: path})
            if os.path.exists(path) and os.path.getsize(path) > 0:
                self.load_from_file(name + ".txt")
            else:
                f = open(path, "w")
                f.close()
            if self.curr_user == "":
                self.curr_user = name


    def add_key(self, keys):
        if type(keys) == str:
            try:
                self.values.add(float(keys))
            except ValueError:
                self.values.add(keys)
        else:
            for key in keys:
                try:
                    self.values.add(float(key))
                except ValueError:
                    self.values.add(key)

    def remove_key(self, key):
        try:
            self.values.discard(float(key))
        except ValueError:
            self.values.discard(key)

    def write_to_file(self):
        if self.curr_user in self.users.keys():
            f = open(self.users[self.curr_user], "w")
            temp = ""
            for value in self.values:
                temp = temp + str(value) + " "
            temp = temp[:len(temp)-1]
            f.write(temp)
            f.close()

    def load_user(self):
        f = open(self.users[self.curr_user], "r")
        file_values = " ".join(f.readlines())
        f.close()
        self.values.clear()
        for value in file_values.split(" "):
            self.add_key(value)

    def load_from_file(self, path):
        p = path
        f = open(path, "r")
        file_values = " ".join(f.readlines())
        f.close()
        self.values.clear()
        for value in file_values.split(" "):
            self.add_key(value)

    def find_key(self, keys):
        if type(keys) == str:
            try:
                if float(keys) in self.values:
                    print(keys + " ")
                else:
                    print("No such elements")
            except ValueError:
                if keys in self.values:
                    print(keys + " ")
                else:
                    print("No such elements")
        else:
            found = False
            for key in keys:
                try:
                    if float(key) in self.values:
                        print(key + " ")
                        found = True
                except ValueError:
                    if key in self.values:
                        print(key + " ")
                        found = True
            if not found:
                print("No such elements")

    def list(self):
        for value in self.values:
            print(value, end=" ")
        print()

    def switch(self, name, need_save, need_load):
        if need_save:
            self.write_to_file()
        self.add_user(name)
        self.curr_user = name
        if need_load:
            self.load_user()
        else:
            self.values.clear()

    def reg_find(self, reg):
        result_list = []
        for value in self.values:
            if re.match(reg, str(value)):
                result_list.append(str(value))
        if result_list:
            print(result_list)
        else:
            print("No such elements")


def choices():
    temp = []
    print("username:", end=" ")
    container = Container()
    container.add_user(input())
    while True:
        print("Choose action(write exit to stop program)")
        choice = input()
        if choice.find("exit") != -1:
            break
        elif choice.find("list") != -1:
            container.list()
        elif choice.find("add") != -1:
            temp = choice.split(" ")[1:]
            container.add_key(temp)
        elif choice.find("remove") != -1:
            temp = choice.split(" ")[1]
            container.remove_key(temp)
        elif choice.find("find") != -1:
            temp = choice[choice.find("find") + 5:].split(" ")
            container.find_key(temp)
        elif choice.find("grep") != -1:
            temp = choice.split(" ")[1]
            container.reg_find(temp)
        elif choice.find("save") != -1:
            container.write_to_file()
        elif choice.find("load") != -1:
            temp = choice.split(" ")
            if len(temp) == 1:
                container.load_user()
            else:
                container.load_from_file(temp[1])
        elif choice.find("switch") != -1:
            temp = choice.split(" ")[1]
            sbool = input("Save? y/n") == "y"
            lbool = input("Load? y/n") == "y"
            container.switch(temp, sbool, lbool)

choices()

