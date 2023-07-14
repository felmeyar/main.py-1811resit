class SocialNetwork:
    def __init__(self, file_name):
        self.file_name = file_name
        self.network = self.read_social_network_file()

    def read_social_network_file(self):
        network = {}
        with open(self.file_name, 'r') as file:
            for line in file:
                data = line.strip().split()
                if len(data) == 1:  # Person with no friends
                    person = data[0]
                    network[person] = []
                elif len(data) == 2:  # Person with friends
                    person, friend = data[0], data[1]
                    if person not in network:
                        network[person] = []
                    network[person].append(friend)
        return network

    def pretty_print(self):
        for person, friends in self.network.items():
            if friends:
                print(f"{person} is friends with {', '.join(friends)}")
            else:
                print(f"{person} is friends with none")

    def delete_member(self, member):
        # Delete the member from the network
        if member in self.network:
            del self.network[member]

        # Delete the member from the friends list of all other members
        for friends in self.network.values():
            if member in friends:
                friends.remove(member)


class SocialNetworkFile:
    @staticmethod
    def open_social_network_file():
        while True:
            file_name = input("Enter the file name (or 'done' to exit): ")
            if file_name.lower() == "done":
                return None

            try:
                file = open(file_name, "r")
                return file
            except FileNotFoundError:
                print("Error: File not found. Please enter a valid file name.")
            except IOError:
                print("Error: Unable to open the file. Please enter a valid file name.")

    @staticmethod
    def validate_input(file_name):
        try:
            with open(file_name, "r") as file:
                lines = file.readlines()
                num_members = int(lines[0].strip())  # Number of members is on the first line

                unique_names = set()
                for line in lines[1:]:  # Start from the second line
                    for name in line.strip().split():
                        unique_names.add(name)

                if len(unique_names) < num_members:
                    raise Exception(f"The number of unique names ({len(unique_names)}) is fewer than the number of members given ({num_members}).")
                elif len(unique_names) > num_members:
                    raise Exception(f"The number of unique names ({len(unique_names)}) is more than the number of members given ({num_members}).")
                else:
                    print("Social network data is valid.")
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == "__main__":
    file = SocialNetworkFile.open_social_network_file()
    while file is not None:
        # Process the opened file
        print("File opened successfully!")
        file_name = file.name
        file.close()

        SocialNetworkFile.validate_input(file_name)

        social_network = SocialNetwork(file_name)

        print_network = input("Do you want to print the social network? (y/n): ")
        if print_network.lower() == 'y':
            social_network.pretty_print()

        delete_member_choice = input("Do you want to delete a member from the social network? (y/n): ")
        if delete_member_choice.lower() == 'y':
            member_to_delete = input("Enter the name of the member to delete: ")
            social_network.delete_member(member_to_delete)
            print(f"{member_to_delete} has been deleted from the network.")

            print_network = input("Do you want to print the updated social network? (y/n): ")
            if print_network.lower() == 'y':
                social_network.pretty_print()

        file = SocialNetworkFile.open_social_network_file()


