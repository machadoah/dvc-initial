import os
import subprocess

def set_dvc_remote():
    # Defina os possíveis caminhos
    path1 = "/home/antoniomachado/Dropbox/dropbox/"
    path2 = "/home/machadoah/Dropbox/dropbox/"

    # Verifique qual caminho existe e use-o para configurar o remoto do DVC
    if os.path.isdir(path1):
        url = path1
    elif os.path.isdir(path2):
        url = path2
    else:
        print("Nenhum dos diretórios foi encontrado.")
        return

    # Execute o comando para modificar o remoto do DVC
    try:
        subprocess.run(["dvc", "remote", "modify", "myremote", "url", url], check=True)
        print(f"Remoto 'myremote' configurado para {url}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao configurar o remoto: {e}")

if __name__ == "__main__":
    set_dvc_remote()
