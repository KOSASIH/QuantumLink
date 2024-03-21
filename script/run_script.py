import subprocess

def run_script(script_path):
    """
    Run a script located at the specified path.
    """
    try:
        subprocess.run(["bash", script_path], check=True)
        print(f"Script '{script_path}' executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script '{script_path}': {e}")

# Example script usage
if __name__ == "__main__":
    script_path = "scripts/deploy_quantumlink.sh"
    run_script(script_path)
