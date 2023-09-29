filename = input("Filename: ").upper()

if filename.endswith(".GIF"):
    print("image/gif")
elif filename.endswith(".JPG"):
    print("image/jpg")
elif filename.endswith(".JPEG"):
    print("image/jpeg")
elif filename.endswith(".PNG"):
    print("image/png")
elif filename.endswith(".PDF"):
    print("application/pdf")
elif filename.endswith(".TXT"):
    print("text/txt")
elif filename.endswith(".ZIP"):
    print("compressed file/zip")