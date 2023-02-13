let about_page = {
    page_contents: [
        {
            type: "header",
            string: "Hi, I'm Brad",
        },
        {
            type: "paragraph",
            string: "I enjoy writing software.",
        }
    ]
};

let about_contact_page = {
    page_contents: [
        {
            type: "header",
            string: "Contact",
        },
        {
            type: "paragraph",
            string: "abradinjapan@outlook.com",
        },
        {
            type: "link",
            address: "https://linkedin.com/in/abradinjapan",
            string: "LinkedIn",
        },
        {
            type: "link",
            address: "https://github.com/abradinjapan",
            string: "GitHub",
        }
    ]
};

let about_side_navigation = {
    navigation_links: [
        {
            display_name: "About",
            internal_name_of_link: "about",
        },
        {
            display_name: "Contact",
            internal_name_of_link: "about_contact",
        }
    ]
};

// generate html for document information that takes up the page
function generate_html_from_page_body_json(json) {
    var inner_html = "";
    var type;

    // write all tags to the inside of the destination html tag
    for (var i = 0; i < json.page_contents.length; i++) {
        // get the type of display and information
        type = json.page_contents[i].type;
        
        // append html tag based on information type
        switch (type) {
        case "header":
            inner_html += ("<div class=\"page_document_text_header\">" + json.page_contents[i].string + "</div>");

            break;
        case "paragraph_boldened":
            inner_html += ("<div class=\"page_document_text_bold\">" + json.page_contents[i].string + "</div>");

            break;
        case "paragraph":
            inner_html += ("<div class=\"page_document_text\">" + json.page_contents[i].string + "</div>");

            break;
        case "link":
            inner_html += ("<div class=\"page_document_text\"><a class=\"page_document_link\" href=\"" + json.page_contents[i].address + "\">" + json.page_contents[i].string + "</a></div>");

            break;
        default:
            inner_html += "ERROR";

            break;
        }
    }

    // return html string
    return inner_html;
}

let top_navigation_links = {
    top_navigation_links: [
        {
            display_name: "About",
            internal_name_of_link: "about",
        },
        {
            display_name: "Contact",
            internal_name_of_link: "about_contact",
        }
    ]
}

// generate html for the side navigation of the specific page
function generate_html_for_side_navigation_json(json) {
    var inner_html = "";

    // write all links in order
    for (var i = 0; i < json.navigation_links.length; i++) {
        // write link html
        inner_html += "<div class=\"page_side_navigation_link\" onclick=\"set_page_as('" + json.navigation_links[i].internal_name_of_link + "')\">" + json.navigation_links[i].display_name + "</div>";
    }

    return inner_html;
}

// generate html for the top navigation
function generate_html_for_top_navigation_json(json) {
    var inner_html = "";

    // write all links in order
    for (var i = 0; i < json.top_navigation_links.length; i++) {
        // write link html
        inner_html += "<div class=\"page_top_link\" onclick=\"set_page_as('" + json.top_navigation_links[i].internal_name_of_link + "')\">" + json.top_navigation_links[i].display_name + "</div>";
    }

    return inner_html;
}

// set the page body and navigation to fit the user's request
function set_page_as(internal_name) {
    var page_document_div = document.getElementById("page_document_container");
    var page_body_json_contents;

    // get appropriate json contents
    switch (internal_name) {
    case "about":
        page_body_json_contents = about_page;

        break;
    case "about_contact":
        page_body_json_contents = about_contact_page;

        break;
    }

    // setup page document contents to requested information
    page_top_links.innerHTML = generate_html_for_top_navigation_json(top_navigation_links);
    page_document_div.innerHTML = generate_html_from_page_body_json(page_body_json_contents);
    
    return;
}
