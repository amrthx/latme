@echo off
if %1$==$ (
    rem use the localcomputername if nothing is specified
    set computer=%computername%
    ) else (
    rem user the computername passed as a parameter
    set computer=%1
        )

echo Creating report for %computer%
set htmlfile=%computer%-report.html

rem redirect wmic output to NULL since we don't really need to see it
wmic /node:%computer% /Output:"%htmlfile%" OS get /format:hform >NULL
wmic /node:%computer% /Append:"%htmlfile%" computersystem get /format:hform >NULL
wmic /node:%computer% /Append:"%htmlfile%" service list brief /format:htable >NULL
wmic /node:%computer% /Append:"%htmlfile%" logicaldisk list brief /format:htable >NULL

echo See %htmlfile%
set computer=
set htmlfile=

