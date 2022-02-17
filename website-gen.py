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

def generate_index():
    # colors
    color_1 = "#00ffbf"
    color_2 = "#eeeeee"
    color_3 = "#000000"
    color_4 = "#cccccc"
    welcome_margin_length = "2%"
    main_page_div_width = "60%"
    font_1 = "Courier New"
    
    # style
    page_contents_div_style = ABOUT_style_data()
    page_contents_div_style.elements.append(ABOUT_css_element("color", color_3))
    page_contents_div_style.elements.append(ABOUT_css_element("background-color", color_2))
    page_contents_div_style.elements.append(ABOUT_css_element("padding", welcome_margin_length))
    header_div_style = ABOUT_style_data()
    header_div_style.elements.append(ABOUT_css_element("margin-top", "0 auto"))
    main_page_div_style = ABOUT_style_data()
    main_page_div_style.elements.append(ABOUT_css_element("background-color", color_1))
    main_page_div_style.elements.append(ABOUT_css_element("width", main_page_div_width))
    main_page_div_style.elements.append(ABOUT_css_element("margin", "0 auto"))
    main_page_div_style.elements.append(ABOUT_css_element("box-shadow", "0 10px 10px rgba(0, 0, 0, .5)"))
    welcome_message_style = ABOUT_style_data()
    welcome_message_style.elements.append(ABOUT_css_element("color", color_2))
    welcome_message_style.elements.append(ABOUT_css_element("text-align", "center"))
    welcome_message_style.elements.append(ABOUT_css_element("padding", welcome_margin_length))
    body_style = ABOUT_style_data()
    body_style.elements.append(ABOUT_css_element("background-color", color_2))
    body_style.elements.append(ABOUT_css_element("font-family", font_1))

    # message
    msg = ABOUT_tag("h1")
    msg.attributes.append(ABOUT_attribute("style", welcome_message_style))
    msg.inner_tags.append("Welcome!")

    # page contents
    page_contents_div = ABOUT_tag("div")
    page_contents_div.attributes.append(ABOUT_attribute("style", page_contents_div_style))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("This site is a work in progress."))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph("Working on it!"))
    page_contents_div.inner_tags.append(generate_page_contents_paragraph(":)"))

    # header
    header_div = ABOUT_tag("div")
    header_div.attributes.append(ABOUT_attribute("style", header_div_style))
    header_div.inner_tags.append(msg)

    # main page div
    main_page_div = ABOUT_tag("div")
    main_page_div.attributes.append(ABOUT_attribute("style", main_page_div_style))
    main_page_div.inner_tags.append(header_div)
    main_page_div.inner_tags.append(page_contents_div)

    # page body
    body = ABOUT_tag("body")
    body.attributes.append(ABOUT_attribute("style", body_style))
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
    write_string_to_file(destination_file_path + "index.html", generate_index())

"""

Main

"""

create_website("./")
