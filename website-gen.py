"""

Helper Classes

"""

def ABOUT_tabs(tab_depth):
    return "\t" * tab_depth

class ABOUT_css_element:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def serialize(self):
        return self.name + ": " + str(self.value) + ";"

class ABOUT_style_data:
    def __init__(self):
        self.elements = []

    def serialize(self):
        output = ""

        for element in self.elements:
            output += element.serialize() + " "
        
        return output

class ABOUT_attribute:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def serialize(self):
        if type(self.value) == ABOUT_style_data:
            return self.name + "=\"" + self.value.serialize() + "\""
        else:
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

class ABOUT_theme:
    def __init__(self):
        self.settings = None
        self.styles = None

"""

Generating Pages

"""

def generate_page_head(page_title):
    # title
    title = ABOUT_tag("title")
    title.inner_tags.append(str(page_title))

    # head
    head = ABOUT_tag("head")
    head.inner_tags.append(title)

    return head

def generate_page_contents_paragraph(msg):
    output = ABOUT_tag("p")

    output.attributes.append(ABOUT_attribute("style", ABOUT_css_element("text-align", "center").serialize()))
    output.inner_tags.append(msg)

    return output

def generate_page_contents_heading(msg):
    output = ABOUT_tag("h2")

    output.attributes.append(ABOUT_attribute("style", ABOUT_css_element("text-align", "center").serialize()))
    output.inner_tags.append(msg)

    return output

def generate_index(theme):
    # break tag
    break_tag = ABOUT_tag("br")
    break_tag.self_closing = True

    # message
    msg = ABOUT_tag("h1")
    msg.attributes.append(ABOUT_attribute("style", theme.styles["welcome_message_style"]))
    msg.inner_tags.append("Welcome!")

    # page contents
    page_contents_div = ABOUT_tag("div")
    page_contents_div.attributes.append(ABOUT_attribute("style", theme.styles["page_contents_div_style"]))
    page_contents_div.inner_tags.append(generate_page_contents_heading("Hi! I'm Bradford Shapleigh!"))
    page_contents_div.inner_tags.append(break_tag)
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("My passion is creating tools for myself and other people to use."))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("I believe that software these days is bloated and inefficient."))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("It is my dream to make software as efficient as possible while still maintaining productivity."))
    page_contents_div.inner_tags.append(break_tag)
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Though, like everyone else, I have to settle for less."))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Which is why I create compilers and other tools to improve the world."))
    page_contents_div.inner_tags.append(break_tag)
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Although I don't upload my compiler designs I do upload some other things."))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Like byte machines and what not that you can find on my new GitHub."))
    page_contents_div.inner_tags.append(break_tag)
    page_contents_div.inner_tags.append(generate_page_contents_heading("Public Projects"))
    page_contents_div.inner_tags.append(break_tag)
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Byte Machine 0"))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Voxelize"))


    # header
    header_div = ABOUT_tag("div")
    header_div.attributes.append(ABOUT_attribute("style", theme.styles["header_div_style"]))
    header_div.inner_tags.append(msg)

    # footer
    footer_div = ABOUT_tag("div")
    footer_div.attributes.append(ABOUT_attribute("style", theme.styles["footer_div_style"]))
    footer_div.inner_tags.append(generate_page_contents_paragraph("This site is a work in progress."))
    footer_div.inner_tags.append(generate_page_contents_paragraph("It's currently generated with python!"))
    footer_div.inner_tags.append(generate_page_contents_paragraph("Working on it!"))

    # main page div
    main_page_div = ABOUT_tag("div")
    main_page_div.attributes.append(ABOUT_attribute("style", theme.styles["main_page_div_style"]))
    main_page_div.inner_tags.append(header_div)
    main_page_div.inner_tags.append(page_contents_div)
    main_page_div.inner_tags.append(footer_div)

    # page body
    body = ABOUT_tag("body")
    body.attributes.append(ABOUT_attribute("style", theme.styles["body_style"]))
    body.inner_tags.append(main_page_div)

    # page html
    html = ABOUT_tag("html")
    html.inner_tags.append(generate_page_head("A Brad in Japan"))
    html.inner_tags.append(body)

    return ABOUT_page(html).serialize()

"""

Saving Changes

"""

def write_string_to_file(destination_file_path, string):
    f = open(destination_file_path, "w")

    f.write(string)

    f.close()

"""

Generating Website

"""

def create_website(destination_file_path):
    # create theme
    theme = ABOUT_theme()

    # create theme data
    theme.settings = {
        "color_1" : "#000000",
        "color_2" : "#ffffff",
        "font_1" : "Courier New",
        "page_header_and_footer_margin" : "2%",
        "main_page_div_width" : "60%",
        "normal_margin" : "0 auto",
        "shadow" : "0 10px 10px rgba(0, 0, 0, .5)",
        "body_text_align" : "center"
    }
    theme.styles = {
        "page_contents_div_style" : ABOUT_style_data(),
        "header_div_style" : ABOUT_style_data(),
        "footer_div_style" : ABOUT_style_data(),
        "main_page_div_style" : ABOUT_style_data(),
        "welcome_message_style" : ABOUT_style_data(),
        "body_style" : ABOUT_style_data()
    }

    # create theme styles
    theme.styles["page_contents_div_style"].elements.append(ABOUT_css_element("color", theme.settings["color_1"]))
    theme.styles["page_contents_div_style"].elements.append(ABOUT_css_element("background-color", theme.settings["color_2"]))
    theme.styles["page_contents_div_style"].elements.append(ABOUT_css_element("padding", theme.settings["page_header_and_footer_margin"])) # welcome_margin_length

    theme.styles["header_div_style"].elements.append(ABOUT_css_element("color", theme.settings["color_2"]))
    theme.styles["header_div_style"].elements.append(ABOUT_css_element("padding", theme.settings["page_header_and_footer_margin"])) # welcome_margin_length

    theme.styles["footer_div_style"].elements.append(ABOUT_css_element("color", theme.settings["color_2"]))
    theme.styles["footer_div_style"].elements.append(ABOUT_css_element("padding", theme.settings["page_header_and_footer_margin"])) # welcome_margin_length

    theme.styles["main_page_div_style"].elements.append(ABOUT_css_element("background-color", theme.settings["color_1"]))
    theme.styles["main_page_div_style"].elements.append(ABOUT_css_element("width", theme.settings["main_page_div_width"]))
    theme.styles["main_page_div_style"].elements.append(ABOUT_css_element("margin", theme.settings["normal_margin"]))
    theme.styles["main_page_div_style"].elements.append(ABOUT_css_element("box-shadow", theme.settings["shadow"]))

    theme.styles["welcome_message_style"].elements.append(ABOUT_css_element("text-align", theme.settings["body_text_align"]))

    theme.styles["body_style"].elements.append(ABOUT_css_element("background-color", theme.settings["color_2"]))
    theme.styles["body_style"].elements.append(ABOUT_css_element("font-family", theme.settings["font_1"]))

    write_string_to_file(destination_file_path + "index.html", generate_index(theme))

"""

Main

"""

create_website("./")
