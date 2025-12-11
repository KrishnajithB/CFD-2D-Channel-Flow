import os
import pandas as pd
import matplotlib.pyplot as plt


def list_columns(df: pd.DataFrame):
    print("\nAvailable columns in the CSV:\n")
    for col in df.columns:
        print(f" - {col}")
    print()


def sanitize_name(name: str) -> str:
    for ch in [' ', ':', '/', '\\', '(', ')', '[', ']', '{', '}', ',']:
        name = name.replace(ch, '_')
    return name


def main():

    # Ask file name (file should be in project folder)
    file_name = input("Enter CSV file name (with .csv extension): ").strip()
    
    if not os.path.exists(file_name):
        print("File not found in current directory. Make sure it is placed here.")
        return
    
    print(f"Loading file: {file_name}")
    df = pd.read_csv(file_name)
    
    if df.empty:
        print("CSV is empty. Nothing to plot.")
        return

    list_columns(df)

    # Create output folder
    output_dir = "plots"
    os.makedirs(output_dir, exist_ok=True)

    while True:
        # Select X
        x_col = input("\nEnter column name for X-axis: ").strip()
        if x_col not in df.columns:
            print("Invalid column. Check list and try again.")
            continue

        # Select Y columns
        y_input = input("Enter Y column(s) separated by commas: ").strip()
        y_cols = [c.strip() for c in y_input.split(",") if c.strip()]
        y_cols = [c for c in y_cols if c in df.columns]

        if not y_cols:
            print("No valid Y columns selected.")
            continue

        # Scaling option
        scale_str = input("Enter scale factor for Y (Enter for 1.0): ").strip()
        try:
            y_scale = float(scale_str) if scale_str else 1.0
        except:
            y_scale = 1.0

        # Plot
        plt.figure()
        for y in y_cols:
            plt.plot(df[x_col], df[y] * y_scale, label=y)

        plt.xlabel(x_col)
        plt.ylabel(f"Y values (scaled x{y_scale})")
        plt.title(f"{', '.join(y_cols)} vs {x_col}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Save image
        base = os.path.splitext(file_name)[0]
        img_name = f"{base}_{sanitize_name('_'.join(y_cols))}_vs_{sanitize_name(x_col)}.png"
        img_path = os.path.join(output_dir, img_name)

        plt.savefig(img_path, dpi=200)
        print(f"\nGraph saved as: {img_path}\n")

        show_plot = input("Show plot? (y/N): ").lower()
        plt.show() if show_plot == "y" else plt.close()

        again = input("Generate another plot? (Y/n): ").lower()
        if again == "n":
            break

    print("Finished.")


if __name__ == "__main__":
    main()