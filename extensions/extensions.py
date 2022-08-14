def main():
    user_ip = input("What is your file name?: ").strip().casefold()
    if user_ip.isalnum():
        print("application/octet-stream")
    else:
        file_name, ext_type = user_ip.rsplit(".", 1)
        file_type(ext_type)

def file_type(ext_type):
    if ext_type == "jpg" or ext_type == "jpeg":
        print("image/jpeg")
    elif ext_type == "gif":
        print("image/gif")
    elif ext_type == "png":
        print("image/png")
    elif ext_type == "pdf":
        print("application/pdf")
    elif ext_type == "txt":
        print("text/plain")
    elif ext_type == "zip":
        print("application/zip")
    else:
        print("application/octet-stream")

main()

