# Directories and the number of days after which files will be archived
$directories = @{
    "D:\Project\CSA\Output" = 30
    "D:\ProgramData\Alteryx\Gallery\Logs" = 90
}

# Path where the archived files will be stored
$archivePath = "D:\ArchivedFiles"

# Create archive folder if it doesn't exist
if (!(Test-Path -Path $archivePath)) {
    New-Item -ItemType Directory -Path $archivePath
}

# Function to archive files older than the specified number of days
function Archive-Files {
    param (
        [string]$folderPath,
        [int]$days
    )
    
    $currentDate = Get-Date

    # Get files older than the specified number of days
    $files = Get-ChildItem -Path $folderPath -File | Where-Object { 
        ($currentDate - $_.LastWriteTime).Days -ge $days 
    }

    # Archive each file and then delete it
    foreach ($file in $files) {
        $fileName = $file.Name
        $fileDate = $file.LastWriteTime.ToString("yyyyMMdd")
        
        $zipFilePath = Join-Path $archivePath "$fileName-$fileDate.zip"
        
        Add-Type -AssemblyName 'System.IO.Compression.FileSystem'
        [System.IO.Compression.ZipFile]::CreateFromDirectory($file.FullName, $zipFilePath)
        
        Remove-Item $file.FullName -Force
    }
}

# Process each folder based on the configured days
foreach ($directory in $directories.Keys) {
    Archive-Files -folderPath $directory -days $directories[$directory]
}
