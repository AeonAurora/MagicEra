import os
import json

def commandHelp() -> None:
    print("update -> Updata modlist. Output new modlist and deleted modlist.")
    print("serverban + JarFileName -> Add mod which server don't require at Server Blacklist.")
    print("help -> Get help.")
    print("exit -> Exit Console.")

def commandUpdate() -> None:
    # 获取 ./Client/mods 文件夹下的 mod 列表
    nowModList = os.listdir("./Client/mods")
    # 获取 ModList.json 的 mod 列表
    with open("./ModList.json", 'r') as f:
        oldModList = json.load(f)
    # 获取新 mod 列表
    newModList = []
    for mods in nowModList:
        if mods in oldModList:
            continue
        newModList.append(mods)
    # 获取被删除 mod 列表
    deletedModList = []

    for mods in oldModList:
        if mods in nowModList:
            continue
        deletedModList.append(mods)

    print("New mod list:")
    for mods in newModList:
        print(mods)
    print("--------------------------")

    print("Deleted mod list:")
    for mods in deletedModList:
        print(mods)
    print("--------------------------")

    print("The modpack has " + str(len(nowModList)) + " mods.")

    with open("./ModList.json", 'w') as f:
        f.write(json.dumps(nowModList))

def commandServerBan(argList: list) -> None:
    if len(argList) != 2:
        print("Please input the name of the jar file which server don't require!")
        return

    with open("./ServerBlacklist.json", 'r') as f:
        temp = json.load(f)
    temp.append(argList[1])
    with open("./ServerBlacklist.json", 'w') as f:
        f.write(json.dumps(temp))

print("Modpack Management Console")
print("Input 'help' to get help.")

while True:
    # 获得命令
    command = input(">")
    argList = command.split()

    if argList[0] == "updata":
        commandUpdate()
    
    elif argList[0] == "serverban":
        commandServerBan(argList)

    elif argList[0] == "help":
        commandHelp()
    
    elif argList[0] == "exit":
        break

    else:
        print("Unknown command.")