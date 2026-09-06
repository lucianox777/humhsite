@echo off
set ASPNETCORE_URLS=http://localhost:5178
dotnet run --project "%~dp0.."
