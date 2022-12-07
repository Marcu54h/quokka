if (-not (Test-Path Env:\FLASK_APP)) { $env:FLASK_APP="quokka" }
if (-not (Test-Path Env:\FLASK_ENV)) { $env:FLASK_ENV="development" }
flask.exe run