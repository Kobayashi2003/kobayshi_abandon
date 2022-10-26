$My_Script_Path = 'C:\Users\KOBAYASHI\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'

# Start or Kill a Process
function Start_and_Kill($app_path, $state="start") {

    $app_name = ($app_path.Split("\")[-1]).Split(".")[-2]
    if ($state -eq "start") { # Start Process
        echo "$app_name Run"
        # Start-Process 
        start $app_path
    } elseif ($state.startswith("k")) { # Kill Process
        echo "$app_name Kill"
        kill -ProcessName $app_name
    }
}

# A function for editing this Sctipt
function Edit_My_Script {
    powershell_ise $My_Script_Path
}

# A function for showing all current Paths
function Show_Path() {
    # echo $My_Script_Path
    echo "===================="
    (Get-Content -Path $My_Script_Path -Raw).Split(";")[-1] | echo
    echo "===================="
}

# A funtion for deleting Paths
function Delete_Path($app_name="") {
    # clc -Path C:\Users\KOBAYASHI\Desktop\test.ps1 -Include "function"
    if ($app_name -eq "") {
        echo "You have to enter an app name"
        return
    }
    $pattern = "# $app_name"
    $content = Select-String -Path $My_Script_Path -Pattern $pattern
    $line = $content.ToString().Split(":")[-2] - 1
    # echo $line
    $old_content = Get-Content -Path $My_Script_Path -ReadCount 0
    $new_content = @()
    for($i = 0; $i -lt $old_content.Length; $i += 1) {
        if ($i -gt $line-1 -and $i -lt $line+6 ) {
            # echo $old_content[$i]
        } else {
            $new_content += $old_content[$i]
        }
    }
    # echo $new_content
    Set-Content -Path $My_Script_Path -Value $new_content
    echo "Path Deleted"
}

# A function for adding new Paths
function Add_Path($app_name="", $app_path="") {
    
    if ($app_name -eq "") {
        echo "You have to enter an app name"
        return
    }
    if($app_path -eq "") {
        echo "You have to enter the path of app"
        return
    }

    $content = Get-Content $My_Script_Path
    if ("# $app_name" -in $content) {
        echo "This path already exists. Do you want to overwrite it? [Y/N]"
        $judge = Read-Host
        if ($judge -eq "Y") {
            Delete_Path $app_name
        } else {
            return
        }
    }
    Add-Content $My_Script_Path "`n# $app_name`nfunction $app_name(`$state`=`"start`") {`n    `$app_path = $app_path`n    Start_and_Kill `$app_path `$state`n}" 
    echo "New Path Added"
}

;
### User's Paths ###

# Clash for Windows
function Clash($state="start") {
    $app_path = 'D:\Item\Clash for Windows\Clash for Windows.exe'
    Start_and_Kill $app_path $state
}

# Free Download Manager
function FDM($state="start") {
    $app_path = 'D:\Item\Free Download Manager\fdm.exe'
    Start_and_Kill $app_path $state
}

# Everything
function Everything($state="start") {
    $app_path = 'D:\Item\Everything\Everything.exe'
    Start_and_Kill $app_path $state
}
