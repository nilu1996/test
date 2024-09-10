# Directories and the number of days after which files will be archived
$directories = @{
    "D:\Project\CSA\Output" = 30
    "D:\ProgramData\Alteryx\Gallery\Logs" = 90
}

# Path where the archived zip files will be stored
$archivePath = "D:\ArchivedFiles"

# Create archive folder if it doesn't exist
if (!(Test-Path -Path $archivePath)) {
    New-Item -ItemType Directory -Path $archivePath
}

# Function to archive files older than the specified number of days into a single zip file per folder
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

    # Check if there are files to archive
    if ($files.Count -eq 0) {
        Write-Host "No files older than $days days found in $folderPath."
        return
    }

    # Create zip file name based on folder name and date
    $folderName = (Get-Item $folderPath).Name
    $zipFileName = "$folderName-$($currentDate.ToString('yyyyMMdd')).zip"
    $zipFilePath = Join-Path $archivePath $zipFileName

    # Create a new zip archive
    Add-Type -AssemblyName 'System.IO.Compression.FileSystem'
    $zipArchive = [System.IO.Compression.ZipFile]::Open($zipFilePath, 'Create')

    # Archive each file into the zip and retain folder structure
    foreach ($file in $files) {
        $relativePath = $file.FullName.Substring($folderPath.Length + 1)  # Maintain relative folder structure in zip
        [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zipArchive, $file.FullName, $relativePath)

        # Optionally: Delete the original file after it's added to the zip
        Remove-Item $file.FullName -Force
    }

    # Close the zip archive
    $zipArchive.Dispose()

    Write-Host "Archived $($files.Count) files from $folderPath to $zipFilePath."
}

# Process each folder based on the configured days
foreach ($directory in $directories.Keys) {
    Archive-Files -folderPath $directory -days $directories[$directory]
}
