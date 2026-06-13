# remove_env.ps1

$envs = @(
    "devbase",
    "build",
    "live",
    "video",
    "clip",
    "final",
    "nethelper",
    "adlr",
    "plugins",
    "p39",
    "p310",
    "p311",
    "p312",
    "p313",
    "p314"
)

foreach ($env in $envs) {
    $exists = conda info --envs | ForEach-Object { $_.Split() } | Where-Object { $_ -eq $env }

    if ($exists) {
        Write-Host "Removing environment: $env" -ForegroundColor Red
        conda env remove --name $env -y
    } else {
        Write-Host "Environment not found: $env" -ForegroundColor Yellow
    }
}
