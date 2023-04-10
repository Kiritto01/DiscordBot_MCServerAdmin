import discord
from discord import app_commands
import paramiko
import requests
import re
import random
import asyncio

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
tree = app_commands.CommandTree(client)

instanceStatus = ""
gameStatus = ""

games = [instanceStatus, gameStatus]

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

def start_mc():
    # nawiązanie połączenia SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('VM IP', username='ssh user', key_filename='ssh key')

        # uruchomienie skryptu Bash
        stdin, stdout, stderr = ssh.exec_command(f'bash {"mcStart"}')
        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')
        new_text = re.sub(r"[^A-Za-z0-9]", "", output)
        # zamknięcie połączenia SSH
        ssh.close()

        # wysłanie wyniku do bota Discord
        print(output)
        if errors:
            print(errors)
        return 

def stop_mc():
    # nawiązanie połączenia SSH
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('VM IP', username='ssh user', key_filename='ssh key')

        # uruchomienie skryptu Bash
        stdin, stdout, stderr = ssh.exec_command(f'bash {"mcStop"}')
        output = stdout.read().decode('utf-8')
        errors = stderr.read().decode('utf-8')
        new_text = re.sub(r"[^A-Za-z0-9]", "", output)
        # zamknięcie połączenia SSH
        ssh.close()

        # wysłanie wyniku do bota Discord
        print(output)
        if errors:
            print(errors)
        return 

def restart_mc():
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
        print(output)
        if errors:
            print(errors)
        return


async def update_status():
    while True:
        game = random.choice(games)
        await client.change_presence(activity=discord.Game(name=game))
        await asyncio.sleep(2)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await tree.sync(guild=discord.Object(id="IDserwera"))
    client.loop.create_task(update_status())

@tree.command(name = "start_maszyny_wirtualnej", description = "Ta komedna startuje maszyne wirtualna", guild=discord.Object(id="IDserwera"))
async def start_maszyny_wirtualnej(interaction):
    await interaction.response.send_message("Masznyna Ruszyła I Nic Jej Nie Zatrzyma (Daj jej 1-2 min żeby było GIT :LIKE:)")
    start_instance()

@tree.command(name = "stop_maszyny_wirtualnej", description = "Ta komendta zatrzymuje maszyne wirtualna", guild=discord.Object(id="IDserwera"))
async def stop_maszyny_wirtualnej(interaction):
    await interaction.response.send_message("Maszny Została Zatrzymana")
    stop_instance()

@tree.command(name = "start_serwera_minecraft", description = "Ta komendta startuje serwer Minecfrat", guild=discord.Object(id="IDserwera"))
async def start_serwera_minecraft(interaction):
    await interaction.response.send_message("Serwer Został Urchomiony")
    start_mc()

@tree.command(name = "stop_serwera_minecraft", description = "Ta komendta zatrzymuje serwer Minecfrat", guild=discord.Object(id="IDserwera"))
async def stop_serwera_minecraft(interaction):
    await interaction.response.send_message("Serwer Został Zatrzymany")
    stop_mc()

@tree.command(name = "restart_serwera_minecraft", description = "Ta komendta restartuje serwer Minecfrat", guild=discord.Object(id="IDserwera"))
async def restart_serwera_minecraft(interaction):
    await interaction.response.send_message("Serwer Został Zrestartowany")
    restart_mc()

client.run('Discord Bot Token')

