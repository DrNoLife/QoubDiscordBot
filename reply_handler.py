class Reply:

    def __init__(self, arguments):
        self.arguments = arguments
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

        # Check if category is set.
        if self.category is not None:
            output = output + 'Category: ' + self.category + ' '

        # Check if popularity is set.
        if self.popularity is not None:
            output = output + 'Popularity: ' + self.popularity + ' '
        
        # Check if order is set.
        if self.order is not None:
            output = output + 'Order: ' + self.order + ' '

        return "You searched for " + output.strip()
