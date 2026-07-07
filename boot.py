import os
import sys
import subprocess
import time
import webbrowser

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def install_requirements():
    print("📦 Installing required software dependencies (this may take a moment)...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"])
    except Exception as e:
        print(f"⚠️ Failed to install dependencies: {e}")

def launch_web_ui():
    print("🌐 Starting OmniMind OS Premium Web Interface...")
    try:
        # Start the Flask web server in a subprocess
        env = os.environ.copy()
        env["FLASK_APP"] = "src.ui.web.app"
        server_process = subprocess.Popen(
            [sys.executable, "-m", "flask", "run", "--port", "5000", "--host", "127.0.0.1"],
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        
        # Give the server a moment to boot
        time.sleep(2)
        
        # Check if process crashed immediately
        if server_process.poll() is not None:
            raise Exception("Web server process crashed immediately upon startup.")
            
        print("🔗 Launching browser at http://127.0.0.1:5000")
        webbrowser.open("http://127.0.0.1:5000")
        
        print("\nPress Ctrl+C to terminate the web server and exit.")
        server_process.wait()
    except KeyboardInterrupt:
        print("\nTerminating web server...")
        if 'server_process' in locals() and server_process.poll() is None:
            server_process.terminate()
        return True
    except Exception as e:
        print(f"\n⚠️ Web Interface failed to launch: {e}")
        if 'server_process' in locals() and server_process.poll() is None:
            server_process.terminate()
        return False
    return True

if __name__ == "__main__":
    install_requirements()
    success = launch_web_ui()
    
    if not success:
        print("\n💻 Gracefully falling back to the Terminal CLI...\n")
        time.sleep(1)
        import src.main
        src.main.run_demo()
