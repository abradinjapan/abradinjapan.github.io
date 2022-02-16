import string

"""

Helper Classes

"""

def ABOUT_tabs(tab_depth):
    return "\t" * tab_depth

class ABOUT_attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        return self.name + "=\"" + str(self.value) + "\""

class ABOUT_tag:
    def __init__(self, name):
        self.name = name
        self.attributes = []
        self.inner_tags = []
        self.self_closing = False
    
    def serialize(self, tab_depth):
        output = ABOUT_tabs(tab_depth) + "<" + self.name

        for attribute in self.attributes:
            output += " " + attribute.serialize()

        if not self.self_closing:
            output += ">\n"

            for inner_tag in self.inner_tags:
                if type(inner_tag) is str:
                    output += ABOUT_tabs(tab_depth + 1) + inner_tag + "\n"
                elif type(inner_tag) is ABOUT_tag:
                    output += inner_tag.serialize(tab_depth + 1)
            
            output += ABOUT_tabs(tab_depth) + "</" + self.name + ">\n"
        else:
            output += "/>\n"

        return output

class ABOUT_page:
    def __init__(self, tag):
        self.root = tag
    
    def serialize(self):
        return "<!DOCTYPE html>\n" + self.root.serialize(0)

"""

Generating Website

"""

def write_string_to_file(destination_file_path, string):
    f = open(destination_file_path, "w")

    f.write(string)

    f.close()

def generate_index():
    # message
    msg = ABOUT_tag("h1")
    msg.inner_tags.append("Hello!")

    #page body
    body = ABOUT_tag("body")
    body.inner_tags.append(msg)

    # page html
    html = ABOUT_tag("html")
    html.inner_tags.append(body)

    return ABOUT_page(html).serialize()

def create_website(destination_file_path):
    write_string_to_file(destination_file_path + "index.html", generate_index())

create_website("./")
