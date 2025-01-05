import os
import sys
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")


list_of_files = [
    "configs/project_config.yml",
    "configs/tools_config.yml",
    "data/unstructed_docs/stories",
    "data/unstructed_docs/swiss_airline_policy",
    "Notebooks/Tools/RAG_tool/rag_tool.ipynb",
    "Notebooks/Tools/sql_agents/sql_agent_chain_for_large_db.ipynb",
    "Notebooks/Tools/sql_agents/sql_agent_chain_steps.ipynb",
    "Notebooks/Tools/sql_agents/sql_agent_steps.ipynb",
    "Notebooks/Tools/tavily/tavily_search.ipynb",
    
    "Notebooks/custom_agent/openai_function_calling.ipynb",
    
    "Notebooks/explore_databases/explore_chinook.ipynb",
    "Notebooks/explore_databases/explore_traveldb.ipynb",

    "Notebooks/python_tip_automatic_docstring/automatic_docstring.ipynb",
    
    "Notebooks/test_gpt_models/gpt-4o.ipynb",
    "Notebooks/test_gpt_models/gpt.ipynb",

    "Notebooks/full_graph.ipynb",

    'images',
    'memory',
    'src/agent_graph',
    'src/chatbot',
    'src/utils',
    'src/app.py',
    'src/prepare_vector_db.py',
    "requirements.txt",
    

]

def is_file_path(path):
    """Check if the path represents a file by looking for a file extension."""
    return bool(Path(path).suffix)

def create_project_structure():
    for filepath in list_of_files:
        # Convert to Path object for cross-platform compatibility
        path = Path(filepath)
        
        ## First create the Directry or Parent Directry and then checck for File, else Error will come, as filepath dont exist
        filedir , filename  = os.path.split( path )

        if filedir and filedir != '.':  # Ensure filedir is not empty or just '.'
            if not os.path.exists(filedir):  # Check if directory doesn't already exist
                os.makedirs(filedir, exist_ok=True)
                logging.info(f"Created directory: {filedir}")
            else:
                logging.info(f"Directory {filedir} already exists.")


        # If path represents a file (has extension), create it if doesn't exist
        if is_file_path(path):
            if not path.exists() or path.stat().st_size != 0:
                path.touch()
                logging.info(f"Created empty file: {path}")
            else:
                logging.info(f"File already exists: {path}")
        else:
            # It's a directory path
            os.makedirs(path, exist_ok=True)
            logging.info(f"Created directory: {path}")

if __name__ == "__main__":
    try:
        create_project_structure()
        logging.info("Project structure creation completed successfully!")
    except Exception as e:
        logging.error(f"Error creating project structure: {str(e)}")
        sys.exit(1)
