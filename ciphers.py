def caesar(message: str, step: int, alpha: str) -> str:
    encrypted_message = ""

    # TODO: add a choice for case sensitive/insensitive encryption
    message = message.lower()
    
    for i, char in enumerate(message):
        if char in alpha:
            idx = alpha.find(char)
            encrypted_message += alpha[(idx + step) % len(alpha)]
        else:
            encrypted_message += message[i]

    return encrypted_message 
