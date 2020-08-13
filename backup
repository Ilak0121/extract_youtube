param([switch]$Elevated)

    function Test-Admin {
        $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
            $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
    }

$x = Test-Path -Path "./Inited"
if($x -eq $false){
    if ((Test-Admin) -eq $false)  {
        if ($elevated) 
        {
            # tried to elevate, did not work, aborting
        } 
        else {
            Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
        }

        exit
    }
    Set-ExecutionPolicy Bypass -Scope Process -Force; `
        iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

        choco install ffmpeg -y
        choco install python3 -y
        New-Item -Name Inited -ItemType File
        exit
}

python3 main.py
