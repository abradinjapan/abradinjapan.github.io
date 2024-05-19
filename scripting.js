let site_json = {
    pages: [
        {
            name: "empty",
            top_links: "normal",
            left_links: "empty",
            content: [
                {
                    type: "text",
                    data: "Page not found.",
                }
            ]
        },
        {
            name: "about",
            top_links: "normal",
            left_links: "empty",
            content: [
                {
                    type: "header",
                    data: "Hi, I'm Brad",
                },
                {
                    type: "text",
                    data: "I am a developer that is familiar with a wide range of software technologies.",
                },
                {
                    type: "text",
                    data: "I am familiar with OpenGL, C, C++, Lua, Python, C#, Web Development, Linux and more.",
                },
                {
                    type: "header",
                    data: "Experience",
                },
                {
                    type: "text",
                    data: "In my programming career I have worked at Code Ninjas in various locations for about two years total."
                },
                {
                    type: "text",
                    data: "My highest role was as a Lead Sensei (Lead Teacher) who was responsible for creating coding based summer camp activities."
                },
                {
                    type: "text",
                    data: "I have taught Roblox Lua, Python, JavaScript, C#, and more."
                },
                {
                    type: "header",
                    data: "Contact",
                },
                {
                    type: "text",
                    data: "I am always open for a chat, please do not hesitate to contact me."
                },
                {
                    type: "text",
                    data: "abradinjapan@outlook.com",
                },
                {
                    type: "external_link",
                    data: "LinkedIn",
                    link: "https://linkedin.com/in/abradinjapan",
                },
                {
                    type: "external_link",
                    data: "GitHub",
                    link: "https://github.com/abradinjapan",
                }
            ]
        },
        {
            name: "projects",
            top_links: "normal",
            left_links: "empty",
            content: [
                {
                    type: "header",
                    data: "Wave Programming Language",
                },
                {
                    type: "text",
                    data: "Wave is an interpreted programming language that I designed and implemented."
                },
                {
                    type: "text",
                    data: "Here is a hello world function."
                },
                {
                    type: "code_block",
                    data: "main()() = {\n\twave.load.string(\"\'Hello World!\'\")(message.start message.end)\n\tstring.print(message.start message.end)()\n\twave.return_memory(message.start message.end)()\n}"
                },
                {
                    type: "text",
                    data: "The next version named 'dragon' is currently in development.",
                },
                {
                    type: "external_link",
                    data: "Wave GitHub Link",
                    link: "https://github.com/abradinjapan/wave"
                },
                {
                    type: "header",
                    data: "Voxelize",
                },
                {
                    type: "text",
                    data: "Voxelize is a voxel renderer written in straight C & OpenGL. It's basically minecraft."
                },
                {
                    type: "text",
                    data: "Here is a sample and link to an earlier stage of the project.",
                },
                {
                    type: "external_link",
                    data: "Voxelize GitHub Link",
                    link: "https://github.com/abradinjapan/voxelize-drawing"
                },
                {
                    type: "internal_image",
                    link: "./images/voxelize-alpha.png"
                }
            ]
        }
    ],
    top_links: [
        {
            name: "empty",
            content: []
        },
        {
            name: "normal",
            content: [
                {
                    text: "About",
                    page: "about",
                },
                {
                    text: "Projects",
                    page: "projects"
                }
            ]
        }
    ],
    left_links: [
        {
            name: "empty",
            content: []
        },
        {
            name: "tutorials",
            content: [
                {
                    text: "Home",
                    page: "tutorial.home",
                }
            ]
        }
    ]
};

// write header
function generate_header(text) {
    // build code
    return ("<div class=\"page_document_text_header\">" + text + "</div>");
}

// write text
function generate_text(text) {
    // build code
    return ("<div class=\"page_document_text\">" + text + "</div>");
}

// write code block
function generate_code_block(text) {
    // build code
    return ("<div class=\"page_document_code_block\"><pre>" + text + "</pre></div>");
}

// write external link
function generate_external_link(text, link) {
    // build code
    return ("<div class=\"page_document_text\"><a class=\"page_document_link\" href=\"" + link + "\">" + text + "</a></div>");
}

// write side navigation link
function generate_side_link(text, link) {
    // build code
    return ("<div class=\"page_side_navigation_link\" onclick=\"goto_page('" + link + "')\">" + text + "</div>");
}

// write top navigation link
function generate_top_link(text, link) {
    // build code
    return ("<div class=\"page_top_link\" onclick=\"goto_page('" + link + "')\">" + text + "</div>");
}

// write internal image
function generate_internal_image(link) {
    // build code
    return ("<div class=\"page_document_text\"><img class=\"page_document_image\"src=\"" + link + "\"></img></div>");
}

// write internal video
function generate_internal_video(link) {
    // build code
    return ("<div class=\"page_document_text\"><video class=\"page_document_video\"src=\"" + link + "\"controls></video></div>");
}

// generate main document
function generate_document(json) {
    var output = "";
    var current_content;

    // write pieces in order
    for (var i = 0; i < json.content.length; i++) {
        // get content
        current_content = json.content[i];

        // write html
        switch (current_content.type) {
        case "header":
            output += generate_header(current_content.data);

            break;
        case "text":
            output += generate_text(current_content.data);

            break;
        case "code_block":
            output += generate_code_block(current_content.data);

            break;
        case "external_link":
            output += generate_external_link(current_content.data, current_content.link);

            break;
        case "internal_image":
            output += generate_internal_image(current_content.link);

            break;
        case "internal_video":
            output += generate_internal_video(current_content.link);
    
            break;
        }
    }

    return output;
}

// generate top navigation
function generate_top_links(json) {
    var output = "";

    // write pieces in order
    for (var i = 0; i < json.content.length; i++) {
        // get content
        output += generate_top_link(json.content[i].text, json.content[i].page);
    }

    return output;
}

// search for a page by name in the site json
function search_for_page(json, name) {
    // search for page
    for (var i = 0; i < json.pages.length; i++) {
        // check if correct page
        if (json.pages[i].name == name) {
            // return correct page
            return json.pages[i];
        }
    }

    // page not found
    return json.pages[0];
}

// search for a top link set by name in the site json
function search_for_top_link_set(json, name) {
    // search for page
    for (var i = 0; i < json.top_links.length; i++) {
        // check if correct page
        if (json.top_links[i].name == name) {
            // return correct page
            return json.top_links[i];
        }
    }

    // page not found
    return json.top_links[0];
}

// set the page body and navigation to fit the user's request
function goto_page(page_name) {
    var page_document_div = document.getElementById("page_document_container");
    var page_top_links_div = document.getElementById("page_top_links");
    var page_left_links_div = document.getElementById("page_left_links");
    var page_json;
    var page_json_top_links;

    // get page json data
    page_json = search_for_page(site_json, page_name);
    page_json_top_links = search_for_top_link_set(site_json, page_json.top_links);

    // setup page document contents to requested information
    page_document_div.innerHTML = generate_document(page_json);
    page_top_links_div.innerHTML = generate_top_links(page_json_top_links);
    //page_left_links_div.innerHTML = generate_left_links();
    
    return;
}
