
def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as file:
                return True, file.read()

        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
            return True, "Content successfully written to file"

        else:
            return False, "Invalid action"

    except Exception as e:
        return False, str(e)


print("=== Cyber Archives Security ===")

print("Using 'secure_archive' to read from a nonexistent file:")
print(secure_archive("/not/existing/file"))

print("Using 'secure_archive' to read from an inaccessible file:")
print(secure_archive("/etc/master.passwd"))

print("Using 'secure_archive' to read from a regular file:")
print(secure_archive("archive.txt"))

print("Using 'secure_archive' to write previous content to a new file:")
print(secure_archive("new_archive.txt", "write", "Hello World"))
