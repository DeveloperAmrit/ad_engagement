import os
import subprocess
import time

def process_notebooks():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    notebooks_dir = os.path.join(base_dir, 'notebooks')
    reports_dir = os.path.join(base_dir, 'reports')
    data_file = os.path.join(base_dir, 'data', 'comments_cleaned.csv')

    print("=" * 60)
    print("Semester 4 Project: Ad Engagement Analysis Pipeline")
    print("=" * 60)
    
    if not os.path.exists(data_file):
        print(f"Error: Required dataset not found at:\n{data_file}")
        print("Please place 'comments_cleaned.csv' into the 'data' directory and try again.")
        return
    else:
        print("Kaggle Dataset verified in data/ folder.")

    os.makedirs(reports_dir, exist_ok=True)
    print(f"Output directory initialized at: {reports_dir}")

    notebooks = sorted([nb for nb in os.listdir(notebooks_dir) if nb.endswith('.ipynb')])

    print("\nBeginning execution of analysis modules...")
    print("-" * 60)

    for i, nb in enumerate(notebooks, start=1):
        nb_path = os.path.join(notebooks_dir, nb)
        report_output = os.path.join(reports_dir, nb.replace('.ipynb', '.html'))
        
        print(f"[{i}/{len(notebooks)}] Executing: {nb}...")
        
        start_time = time.time()
        command = [
            "jupyter", "nbconvert", 
            "--execute", 
            "--to", "html", 
            "--output-dir", reports_dir,
            nb_path
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        elapsed = time.time() - start_time
        
        if result.returncode == 0:
            print(f"  Success in {elapsed:.1f}s: Report saved -> reports/{os.path.basename(report_output)}")
        else:
            print(f"  Execution Failed for {nb}. See error trace:")
            print(result.stderr)
            print("Aborting pipeline to preserve order integrity.")
            return

    print("-" * 60)
    print("All analysis modules executed perfectly!")
    print(f"You can now view the compiled HTML reports located inside the /reports directory.")

if __name__ == "__main__":
    process_notebooks()