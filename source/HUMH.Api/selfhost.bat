dotnet restore
dotnet build -c Release
set ASPNETCORE_URLS=http://0.0.0.0:5107
dotnet run -c Release
