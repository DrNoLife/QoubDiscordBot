import requests
import urllib.parse
import urllib.request

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

    # Get the url based on the arguments.
    def get_url(self):
        url = self.url

        # If popularity is set, then generate a response based on the arguments.
        if self.popularity is not None:
            url += f"Popular?NthMostPopular={self.popularity}"

            # Now check if category is set.
            if self.category is not None:
                url += f"&Category={self.category}"

            # Check if ordering is set.
            if self.order is not None:
                if self.order == "views":
                    url += f"&SortByLikes=true"

            return url

        # Check if we need a random coub from a specific category.
        if self.category is not None:
            url += f"Random?Category={self.category}"
            return url
        else:
            return self.url + "Random"

    # Call the api based on URL.
    def call_api(self, url):
        response = requests.get(url)
        return response.json()

    # Removes bad characters from the coub name.
    def handle_coub_name(self, name):
        return name.replace('|', ',').replace('/', '').replace('\\', '').replace(':', '').replace("http", '').replace("https", '').replace('?','').replace('*', '').replace('<', '').replace('>', '').replace('\'', '').replace('"', '')

    # From the coub json, get the title and id of the coub.
    def get_coub_info(self, coub_json):

        base_url = "https://genresearcher.com/Videos/"

        # Get the title, category, and originalCoubId from the coub json.
        title = self.handle_coub_name(coub_json['title'])
        originalCoubId = coub_json['originalCoubId']
        category = coub_json['category']['title']

        # Structure on the website is: 
        # /Videos/CoubName_CoubId/CoubName_OriginalCoubId.mp4
        # Meaning, we have a video folder, containing a coub folder, containing the coub video.
        full_name = f"{title}_{originalCoubId}"

        # URL encode the full_name.
        full_name_encoded = urllib.parse.quote(full_name)

        # Return the full url.
        full_url = f"{base_url}{category}/{full_name_encoded}.mp4"
        #full_url = f"{base_url}{category}/{full_name_encoded}/{full_name_encoded}.mp4"

        return full_url, full_name

    # Get the reply based on the arguments.
    def get_reply(self):

        url = self.get_url()
        response = self.call_api(url)
        coub_info = self.get_coub_info(response)    # Gives us a direct link to the coub.

        # Download the video based on the coub_info.
        urllib.request.urlretrieve(coub_info[0], coub_info[1] + ".mp4") # Params are URL and Name of local file.
        
        return coub_info[1]