import hashlib

def hash_file(fileName):
    h = hashlib.sha1()
    with open(fileName, "rb") as file:
        while True:
            chunk = file.read(1024)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

msg1 = hash_file("transcript final.docx")
msg2 = hash_file("resume_alizadangi.pdf")

if msg1 != msg2:
    print("These files are not identical")
else:
    print("These files are identical")
