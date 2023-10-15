@echo off

REM Directory paths where files should be moved
set "directories=object-storage dbaas paas mail dns"

REM Loop through directories and move specified files
for %%d in (%directories%) do (
    REM Move README.md file if it exists
    if exist "%%d\README.md" (
        move "%%d\README.md" ".\doc\%%d"
    )

    REM Move all mark down files except README.md file in the doc directory
    if exist "%%d\docs\*.md" (
        move /Y "%%d\docs\*.md" ".\doc\%%d\docs"
        rmdir /S /Q "%%d\docs"
    )
)