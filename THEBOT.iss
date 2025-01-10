[Setup]
AppName=THEBOT
AppVersion=1.0
DefaultDirName={pf}\THEBOT
DefaultGroupName=THEBOT
OutputBaseFilename=THEBOT-Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\THEBOT.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\THEBOT"; Filename: "{app}\THEBOT.exe"
Name: "{group}\Uninstall THEBOT"; Filename: "{uninstallexe}"
Name: "{commondesktop}\THEBOT"; Filename: "{app}\THEBOT.exe"
