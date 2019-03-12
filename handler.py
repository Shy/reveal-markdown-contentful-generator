import contentful

client = contentful.Client(
    "jokk403r56yp",  # This is the space ID. A space is like a project folder in Contentful terms
    "8b9ddca4bfaa8e3f68520e1211700c6b0fbee29459e7d5b5c776626a3230e8d0",  # This is the access token for this space. Normally you get both ID and the token in the Contentful web app
)


def main(event, context):
    entry = client.entry("3hPCvDC6URrqtst7zNMkqI")
    slides = entry.slides
    markdown = ""
    for slide in slides:
        if markdown != "":
            markdown += "\n\n\n"

        try:
            markdown += "".join(["# ", slide.title, "\n"])
        except AttributeError:
            print("Empty Title")

        try:
            markdown += "".join(["## ", slide.subtitle, "\n"])
        except AttributeError:
            print("Empty Subtitle")

        try:
            markdown += "".join([slide.body, "\n"])
        except AttributeError:
            print("Empty Body")

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/markdown",
            "Access-Control-Allow-Origin": "*",
        },
        "body": markdown,
    }
    return response


if __name__ == "__main__":
    main("", "")
