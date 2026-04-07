# startswith() endswith()

url = "http://www.google.com"

if url.startswith("http://") or url.startswith("https://"):
    if url.endswith(".com") or url.endswith(".in") or url.endswith(".co"):
        print("Valid URL")
    else:
        print("Endpoint is Not Valid")
else:
    print("Url is Not contain Valid Protocol.") 
