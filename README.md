<div align="center">
  <h1>Such Much AI Coding Test</h1>
  <br />
  <br />
</div>

<details open="open">
<summary>Table of Contents</summary>

- [About](#about)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
    - [Manual setup](#manual-setup)
    - [System Design](#system-design)
    - [Environment variables](#environment-variables)
- [License](#license)

</details>

---

## About

<table>
<tr>
<td>

This is a coding exercise for Such Much AI. The front-end part was not implemented due to time constraints.
The app has a single API endpoint, that returns either product recomendations or the price of the products, depending on the input.

I've using Chat GPT 4o mini model for prompt engineering (to categorize user input, extract product description from input, extract product price).

I've also using text-embedding-ada-002 for the embeddings.

Some cleanup for the products.csv was done:
* removed HTML;
* removed new lines;
* used the first sentence (100 chars) for the embeddings.

I'm storing product_embeddings inside a Pandas dataframe (database -> in_memory.db.py).

</td>
</tr>
</table>

### Built With

- BAML
- Python 3.12
- FastAPI
- OpenAI
- Pydantic
- Pandas
- Numpy
- Swagger

## Getting Started

### Prerequisites

1. The easiest way to install Cookiecutter is by running:

    ```sh
    pip install --user cookiecutter
    ```

### Usage

#### Manual setup

Please follow these steps for manual setup:
1. Download this GitHub repository.
2. Create a virtual environment.

    ```
    python3 -m venv <myenvname>
    ```

3. Activate virtual environment.

    ```
    cd venv
    Scripts\Activate.ps1
    ```
    Or different Activate script, if you are not working from Visual Code.

4. Install packages from requirements.txt

    ```
    pip install -r /path/to/requirements.txt
    ```

5. Download [VS Code extension for BAML](https://marketplace.visualstudio.com/items?itemName=Boundary.baml-extension)

6. Go to any .baml file and click Save (CTRL + S). This will generate python code from .BAML.

7. If the baml_client got generated in the root directory, move it inside app/backend.

8. Inside baml_src > clients.baml, replace your api_key for GPT4oMini model.
   Also do this for the .env file's ```OPENAI_API_KEY``` key.

9. Run the app:

    ```
    python main.py
    ```

#### System Design

You can find System Design notes in [Miro](https://miro.com/app/board/uXjVLZLm9gc=/?share_link_id=867179278993).


#### Environment variables

in the .env file, replace these environment variables with your own values.

| Name                       | Default value      | Description                                                                 |
| -------------------------- | ------------------ | --------------------------------------------------------------------------- |
| OPENAI_API_KEY               |  | OpenAI API KEY                                                            |

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
