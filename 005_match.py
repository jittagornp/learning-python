status = int(input("Please input the status: "))

message = ""
match status:
    case 400:
        message = "Bad request"
    case 401:
        message = "Unauthorized"
    case 404:
        message = "Not found"
    case 418:
        message = "I'm a teapot"
    case _:
        message = "Something's wrong with the internet"

print("Error: " + message)
