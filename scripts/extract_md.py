import json
import sys


def extract_markdown(notebook_path, output_path=None):
    """
    Extracts only the Markdown cell content from a Jupyter notebook.

    Parameters
    ----------
    notebook_path : str
        The path to the input .ipynb file.
    output_path : str, optional
        The path to save the extracted Markdown. If None, prints to console.

    Returns
    -------
    None
        Writes the extracted Markdown to a file or prints to console.

    Raises
    ------
    FileNotFoundError
        If the notebook file is not found.
    json.JSONDecodeError
        If the notebook file contains invalid JSON.
    IOError
        If there is an error writing to the output file.
    """
    try:
        with open(notebook_path, "r", encoding="utf-8") as f:
            notebook_content = json.load(f)
    except FileNotFoundError:
        print(f"Error: Notebook '{notebook_path}' not found.", file=sys.stderr)
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in notebook '{notebook_path}'.", file=sys.stderr)
        return

    markdown_cells = []
    for cell in notebook_content.get("cells", []):
        if cell.get("cell_type") == "markdown":
            # Join the list of strings that make up the Markdown source
            markdown_cells.append("".join(cell.get("source", [])))

    extracted_markdown = "\n\n---\n\n".join(
        markdown_cells
    )  # Add a separator between cells

    if output_path:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(extracted_markdown)
            print(f"Markdown successfully extracted to '{output_path}'.")
        except IOError as e:
            print(f"Error writing to output file '{output_path}': {e}", file=sys.stderr)
    else:
        print(extracted_markdown)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python your_script_name.py <notebook_file.ipynb> [output_file.md]"
        )
        sys.exit(1)

    input_notebook = sys.argv[1]
    output_markdown = sys.argv[2] if len(sys.argv) > 2 else None

    extract_markdown(input_notebook, output_markdown)
