import discord
from discord.ext import commands
import paramiko
import requests


intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

#Tutorial z jakiego to robiłem https://www.youtube.com/watch?v=afPxQTqlMtg&ab_channel=TheCloudNerd
#https://stackoverflow.com/questions/27535945/how-to-access-ssh-keys-for-a-google-cloud-platform-compute-engine-vm-instance

def start_instance():
    # The API endpoint
    url = "API endpoint"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)

    return

def stop_instance():
    # The API endpoint
    url = "API endpoint"

    # A GET request to the API
    response = requests.get(url)

    # Print the response
    response_json = response.json()
    print(response_json)

    return

 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('!start'):
    # nawiązanie połączenia SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('VM IP', username='ssh user', key_filename='ssh key')

        # uruchomienie skryptu Bash
        stdin, stdout, stderr = ssh.exec_command(f'bash {"mcStart"}')
        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')

        # zamknięcie połączenia SSH
        ssh.close()

        # wysłanie wyniku do bota Discord
        await message.channel.send(f"Output: {output}")
        print(output)
        if errors:
            await  message.channel.send(f"Error: {errors}")
            print(errors)
    
    if message.content.startswith('!stop'):
    # nawiązanie połączenia SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('VM IP', username='ssh user', key_filename='ssh key')

        # uruchomienie skryptu Bash
        stdin, stdout, stderr = ssh.exec_command(f'bash {"mcStop"}')
        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')

        # zamknięcie połączenia SSH
        ssh.close()

        # wysłanie wyniku do bota Discord
        await message.channel.send(f"Output: {output}")
        print(output)
        if errors:
            await  message.channel.send(f"Error: {errors}")
            print(errors)
    
    if message.content.startswith('!restart'):
    # nawiązanie połączenia SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('VM IP', username='ssh user', key_filename='ssh key')

        # uruchomienie skryptu Bash
        stdin, stdout, stderr = ssh.exec_command(f'bash {"mcRestart"}')
        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')

        # zamknięcie połączenia SSH
        ssh.close()
        # wysłanie wyniku do bota Discord
        await message.channel.send(f"Output: {output}")
        print(output)
        if errors:
            await  message.channel.send(f"Error: {errors}")
            print(errors)

    if message.content.startswith('!VMs'):
         stop_instance()
         await message.channel.send("Maszny Została Zatrzymana")

    if message.content.startswith('!VMst'):
         start_instance()
         await message.channel.send("Masznyna Ruszyła I Nic Jej Nie Zatrzyma (Daj jej 1-2 min żeby było GIT :LIKE:)")
client.run("Discord Bot Token")

