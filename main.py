# Copyleft 🄯 2025, Germano Castanho;
# Software livre licenciado sob a GPL-3.0;
# Cada linha, um manifesto pela liberdade!


import os
import time

import pandas as pd
import vt
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())


API_KEY = os.getenv("VT_API_KEY")


def get_file_path():
    print("Bem-vindo ao Virus Scanner! 🦠")
    time.sleep(1)

    file_path = input("Digite o caminho do arquivo: ")
    return file_path


def scan_susp_file(file_path):
    try:
        with vt.Client(API_KEY) as client:
            with open(file_path, "rb") as f:
                analysis = client.scan_file(f, wait_for_completion=True)
                antivirus = analysis.to_dict()["attributes"]["results"]

                scanners = []
                results = []
                for i in antivirus:
                    scanners.append(i)
                    results.append(antivirus[i]["category"])

            df = pd.DataFrame({"SCANNERS": scanners, "RESULTS": results})
            print(df.to_string(index=False))

    except Exception as e:
        print(f"ERRO: {e}")
    return None


def main():
    file_path = get_file_path()
    scan_susp_file(file_path)
    return None


if __name__ == "__main__":
    main()
