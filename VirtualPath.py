import os
import subprocess
import ctypes
import logging

# Configure logging
logging.basicConfig(filename='VirtualPath.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def is_admin():
    """Check if the script is running with administrative privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        logging.error(f"Failed to check admin status: {e}")
        return False

def restart_windows_search():
    """Restart the Windows Search service."""
    try:
        subprocess.run(["net", "stop", "wsearch"], check=True)
        subprocess.run(["net", "start", "wsearch"], check=True)
        logging.info("Successfully restarted Windows Search service.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to restart Windows Search service: {e}")
        print("Error: Could not restart Windows Search service. Please run as administrator.")

def rebuild_search_index():
    """Rebuild the Windows Search index."""
    try:
        subprocess.run("IndexerVolumeGuid", shell=True, check=True)
        logging.info("Successfully initiated search index rebuild.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to rebuild search index: {e}")
        print("Error: Could not rebuild search index.")

def check_search_path():
    """Ensure important directories are included in the search path."""
    try:
        search_paths = [
            os.getenv('USERPROFILE'),  # User's home directory
            "C:\\Program Files",
            "C:\\Program Files (x86)",
            "C:\\Windows"
        ]
        for path in search_paths:
            if not os.path.exists(path):
                logging.warning(f"Search path does not exist: {path}")
                print(f"Warning: Search path does not exist: {path}")
            else:
                logging.info(f"Search path verified: {path}")
    except Exception as e:
        logging.error(f"Failed to check search paths: {e}")

def main():
    if not is_admin():
        print("Please run this script as an administrator.")
        return

    print("Repairing Windows Search...")
    restart_windows_search()
    rebuild_search_index()
    check_search_path()
    print("Windows Search repair completed.")

if __name__ == "__main__":
    main()