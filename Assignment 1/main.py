
def search_and_replace(path, search, replace):
    """
    Method Name: search_and_replace
    Description: This function is used to read text from a txt file whose path is
                 passed as an argument and search for a piece of text and
                 replace it with another piece of text.
    params: path - path of the relevant text file.
            search - the piece of text to search for.
            replace - the piece of text to replace with.
    returns - None

    """

    try:

        # Opening file in Read Mode
        with open(path, 'r') as f:
            # Reading the text into a variable.
            text = f.read()

            # Splitting the text from the file into words into a list
        text_list = text.split()

        # Checking for the word in the text list
        for i in range(len(text_list)):
            # Checking whether the word to be replaced is present or not.
            if text_list[i] == search:
                # Replacing the concerned word
                text_list[i] = replace

        # Joining the new list of word to a string.
        text_new = " ".join(text_list)

        # Opening file in Read Mode
        with open(path, 'w') as f:
            # Writing the updated text to the same file
            f.write(text_new)

    # Catching any Exception that occur during runtime
    except Exception as e:
        print(f"ERROR: {str(e)}")


# DRIVER CODE

search_and_replace(path="example.txt", search="placement", replace="screening")
