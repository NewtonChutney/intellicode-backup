# intellicode-backup
VSCode Intellicode models manual backup - "Cache" folder

Steps to manually download and install intellicode models:
  - Go to the extension's folder [ `C:\Users\<USERNAME>\.vscode\extensions\visualstudioexptteam.vscodeintellicode-1.x.x\` ]
  - Create a folder called "cache" if not present
  - Download the models from the releases page, and download the models.json from the repo, and place everything in the cache folder 
  - Change the <username> to your username in the models.json file
    - you're looking for something like "filePath":"`c:\\Users\\<USERNAME>\\.vscode\\extensions\\visualstudioexptteam.vscodeintellicode-1.2.17\\cache\\E61945A9A512ED5E1A3EE3F1A2365B88F8FE_E4E9EADA96734F01970E616FAB2FAC19`"
  - Also don't forget to check the version in the path string:
    - you're looking for the `\\visualstudioexptteam.vscodeintellicode-1.2.17\\cache` part
    - change it, if necessary, to what you find on your machine [from step 1]
  - As a last troubleshootin step, check if extensions are able to update [Settings > Extensions: Auto Update ]
    - I faced an issue when pylance's extension was older and intellicode was a newer one.
