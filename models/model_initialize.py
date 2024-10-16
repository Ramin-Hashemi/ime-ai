#########################
# File model_initialize #
#########################


import subprocess
import sys


def create_base_model():
    base_model()
    ime_model()


def base_model():
    # Update package lists
    subprocess.run(["sudo", "apt-get", "update", "-y"])
    
    # Install snap package manager
    subprocess.run(["sudo", "snap", "install", "ollama"])
    
    # Install Python packages using pip
    subprocess.run(["sudo", "pip", "install", "ollama"])
    subprocess.run(["sudo", "pip", "install", "ollama-haystack"])
    
    # Pull the llama3.2 model
    subprocess.run(["sudo", "ollama", "pull", "llama3.2"])


def ime_model():
    # Create the iME model using ollama
    subprocess.run(["sudo", "ollama", "create", "iME", "-f", "/home/one-user/ime-ai/Modelfile"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        func_name = sys.argv[1]
        if func_name == "make_server_ready":
            create_base_model()
        else:
            print(f"No function named {func_name} found.")
    else:
        print("Please provide a function name to run.")