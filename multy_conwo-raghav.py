import requests
import time
import random
import os
from colorama import init, Fore

init(autoreset=True)

def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)   

def send_messages(tokens_file, target_id, messages_file, haters_name, speed):
    with open(messages_file, "r") as file:
        messages = file.readlines()
    with open(tokens_file, "r") as file:
        tokens = file.readlines()

    headers = {
        "Connection": "keep-alive",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": ("Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36"),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,fr;q=0.8",
        "Referer": "www.google.com",
    }

    logos = [
        r'''
❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️
''',
        r'''
❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️
''',
        r'''
❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️
''',
        r'''
 ❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️              
''',
        r'''
 ❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️ 
''',
        r'''
        ❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️
''',
        r'''
❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️
''',
        r'''
❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️                                       @  
''',
        r'''
        ❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️                              
''',
        r'''
❤️💥×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] ^^C0NW0^^ T00L ||•×💥❤️
'''
    ]

    while True:
        for message_index, message in enumerate(messages):
            token_index = message_index % len(tokens)
            access_token = tokens[token_index].strip()
            full_message = f"{haters_name} {message.strip()}"

            url = f"https://graph.facebook.com/v17.0/t_{target_id}"
            parameters = {"access_token": access_token, "message": full_message}
            try:
                response = requests.post(url, json=parameters, headers=headers)
                response.raise_for_status()
                current_time = time.strftime("%Y-%m-%d %I:%M:%S %p")
                current_logo = random.choice(logos)
                print(Fore.GREEN + current_logo)
                print(Fore.YELLOW + f"[+] 🥀💜×•|| RUNN1NG [[R4GH4V CH0UDH4RY]] C0NW0 T00L ||×•💜🥀{message_index + 1} S3NT TO C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} at {current_time}")
            except requests.exceptions.RequestException as e:
                print(Fore.RED + f"[x] F91L3D TO S3ND M3SS3G3  {message_index + 1} T0 C0NV0 {target_id} W1TH TOK3N {token_index + 1}: {full_message} - Error: {e}")

            time.sleep(speed)
        print(Fore.CYAN + "\n[+] All messages sent. Restarting the process...\n")

def main():
    approval()
    
    print(Fore.MAGENTA + "_____________________________________________________________🤍🌐🌏×•|| ST4RT1NG [[R4GH4V_CH0UDH4RY]] ^^C0NW0^^ T00L ||•×🤍🌏🌐_______________________=________TH3 ____M4N___________TH3 MYTH_________TH3_M0NXT3R__________R4GH4V_CH0UDH4RY___________1NS1D3😎_____｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡｡⁠◕⁠‿⁠◕⁠｡_(⁠✷⁠‿⁠✷⁠)___(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)(⁠✷⁠‿⁠✷⁠)")
    print(Fore.CYAN + "------------------------------------")
    # Get file paths and other inputs from the user
    tokens_file = input(Fore.YELLOW + "Enter the path to the tokens file: ").strip()
    target_id = input(Fore.YELLOW + "Enter the target_id: ").strip()
    messages_file = input(Fore.YELLOW + "Enter the path to the messages file: ").strip()
    haters_name = input(Fore.YELLOW + "Enter the hater's name: ").strip()
    speed = float(input(Fore.YELLOW + "Enter the speed (in seconds) between messages: ").strip())

    # Start sending messages
    send_messages(tokens_file, target_id, messages_file, haters_name, speed)

if __name__ == "__main__":
    main()
