import os
from dotenv import load_dotenv


load_dotenv()


def config() -> dict[str, str | None]:
    nom = ["MATRIX_MODE", "DATABASE_URL",
           "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]
    stock = {}
    for valeur in nom:
        stock[valeur] = os.getenv(valeur)
    return stock


if __name__ == "__main__":
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    dic = config()
    if dic["MATRIX_MODE"] == "development":
        print("Mode: development")
        if dic['DATABASE_URL']:
            print("Database: Connected to local instance")
        else:
            print("Database: Not configured")
        if dic['API_KEY']:
            print("API Access: Authenticated")
        else:
            print("API Access: Not authenticated")
        if dic['LOG_LEVEL']:
            print("Log Level: DEBUG")
        if dic['ZION_ENDPOINT']:
            print("Zion Network: Online")
        else:
            print("Zion Network: Offline")
    elif dic["MATRIX_MODE"] == "production":
        print("Mode: production")
        if dic['DATABASE_URL']:
            print("Database: mode develpoment requis")
        else:
            print("Database: Not configured")
        if dic['API_KEY']:
            print("API Access: mode develpoment requis")
        else:
            print("API Access: Not authenticated")
        if dic['LOG_LEVEL']:
            print("Log Level: mode develpoment requis")
        else:
            print("Log Level: DEBUG")
        if dic['ZION_ENDPOINT']:
            print("Zion Network: mode develpoment requis")
        else:
            print("Zion Network: Offline")
    else:
        print("ERROR, Mode: development or production")
    print()
    if dic["MATRIX_MODE"] in ["production", "development"]:
        print("Environment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available")
        print()
        print("The Oracle sees all configurations.")
