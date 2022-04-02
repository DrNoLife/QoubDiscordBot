class Reply:

    def __init__(self, arguments, api_url):
        self.arguments = arguments
        self.url = api_url
        self.possible_arguments = ['-cat', '-pop', '-ord', '-help']
        self.category = None
        self.popularity = None
        self.order = None

    # Used for going through the arguments and finding out what to reply with.
    def get_arguments(self):

        # Go through all the arguments.
        # Split each by a space, and check if the first element is in the possible arguments.
        for argument in self.arguments:

            argument_array = argument.split(' ')

            # Guard clause for if the argument is not in the possible arguments.
            if argument_array[0] not in self.possible_arguments:
                continue

            # If it is, set the property to the second element.
            if argument_array[0] == '-cat':
                self.category = argument_array[1]

            elif argument_array[0] == '-pop':

                # Check if a second element is present.
                if len(argument_array) > 1:
                    self.popularity = argument_array[1]
                else:
                    self.popularity = "1"

            elif argument_array[0] == '-ord':
                self.order = argument_array[1]

            elif argument_array[0] == '-help':
                return '''
                !qoub -cat <category> -pop <nth-popular> -ord <order>
                -cat: Category to search in.
                -pop: Get the nth-most popular to search for.
                -ord: Order to search for.
                '''

    # Get the reply based on the arguments.
    def get_reply(self):
        
        output = ""

        # If no arguments are given, return the default reply.
        if self.arguments == []:
            output = "Returns a random coub from a random category."
            return output

        # If popularity is set, then generate a response based on the arguments.
        if self.popularity is not None:
            output = f"Popular {self.popularity}"
            
            # Now check if category is set.
            if self.category is not None:
                output += f" in {self.category}"

            # Check if ordering is set.
            if self.order is not None:
                output += f" ordered by {self.order}"

            return output

        # If we get to this point, then popularity is not set, and we're just getting a random coub from a specific category.
        output = f"Random coub in {self.category}"
        return output