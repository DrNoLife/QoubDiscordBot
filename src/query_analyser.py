class Analyser:

    # Constructor, gets a query and saves it in a property.
    def __init__(self, query):
        self.query = query

    def find_arguments(self):
        query_array = self.query.split(' ')

        arguments = []
        for i in range(len(query_array)):

            # If current element starts with !qoub, skip it.
            if query_array[i].startswith('!qoub'):
                continue

            # Check if current element starts with a -
            # If it does, add it and the next element to a string, and add it to the arguments array.
            if query_array[i].startswith('-'):

                # If we are working with the -pop argument.
                # Check if the next element is an argument or if the next element is out of bounds.
                if query_array[i] == '-pop' and (i + 1 >= len(query_array) or query_array[i + 1].startswith('-')):
                    arguments.append(query_array[i] + ' 1')
                    continue

                if query_array[i] == "-help":
                    arguments.append(query_array[i] + ' help')
                    continue

                # Add current and next element to list.
                arguments.append(query_array[i] + ' ' + query_array[i + 1])

        # Return the arguments.
        return arguments